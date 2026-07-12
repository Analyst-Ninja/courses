terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region     = "ap-south-1"
  access_key = "YOUR_ACCESS_KEY"
  secret_key = "YOUR_SECRET_KEY"
}

# Practice Project

# Steps:-
# 1. Create a VPC
resource "aws_vpc" "prod_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" : "production"
  }
}

# 2. Create internet gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.prod_vpc.id
}

# 3. Create a custom route table
resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.prod_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = aws_internet_gateway.gw.id
  }

  tags = {
    "Name" : "prod-route-table"
  }
}

# 4. Create a subnet
resource "aws_subnet" "subnet-1" {
  vpc_id            = aws_vpc.prod_vpc.id
  cidr_block        = "10.0.0.0/24"
  availability_zone = "ap-south-1a"

  tags = {
    "Name" = "prod-subnet"
  }
}

# 5. Associate the subnet with route table
resource "aws_route_table_association" "prod-rt-association" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.prod-route-table.id
}

# 6. Create a security group to allow port - 22, 80, 443
resource "aws_security_group" "allow-web" {
  name        = "allow-web-traffic"
  description = "Allow Web traffic and SSH"
  vpc_id      = aws_vpc.prod_vpc.id

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    "Name" = "allow-web-traffic"
  }
}

# 7. Create a network interface with an IP in subnet that was created in step 4
resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.0.50"]
  security_groups = [aws_security_group.allow-web.id]
}

# 8. Assign an elastic IP to the network interface created in step 7
resource "aws_eip" "public-ip" {
  network_interface         = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.0.50"
  domain                    = "vpc"
  depends_on                = [aws_internet_gateway.gw]
}

# 9. Create an EC2 with Ubuntu and install and enable apache2 server
resource "aws_instance" "web-server-instance" {
  ami               = "ami-02d26659fd82cf299"
  instance_type     = "t2.micro"
  availability_zone = "ap-south-1a"
  key_name          = "prod-webserver-using-terraform"

  network_interface {
    device_index         = 0
    network_interface_id = aws_network_interface.web-server-nic.id
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install apache2 -y
              sudo systemctl start apache2
              sudo bash -c "echo my very first webserver deployed using Terraform" > /var/www/html/index.html
              EOF
  tags = {
    "Name" : "web-server"
  }
}

output "webserver-public-ip" {
  value = aws_instance.web-server-instance.public_ip
}
