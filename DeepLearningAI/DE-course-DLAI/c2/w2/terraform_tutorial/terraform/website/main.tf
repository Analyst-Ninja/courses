# data source 
data "aws_subnet" "selected_subnet" {
  id = "subnet-0f91451cf97ca5544"
}

data "aws_ami" "latest_amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
  filter {
    name   = "name"
    values = ["al202*-ami-202*"]
  }
}

# resources 
resource "aws_instance" "webserver" {
  // resource type | resource name
  // webserver can also be called as aws_instance.webserver
  # ami           = "ami-0ddfba243cbee3768"
  ami           = data.aws_ami.latest_amazon_linux.id
  instance_type = "t2.micro"
  subnet_id     = data.aws_subnet.selected_subnet.id
  tags = {
    Name = var.server_name
  }
}

// You should make seperate tf file for 
# output --> outputs.tf
# input_variable --> variables.tf 
# resource --> main.tf [You can also make different tf files for different resources]
# providers --> providers.tf

# Terroform will Automatically concatenate all the tf files behind the scenes 
# You can call any variable or resource in any file @ any place
# It will be like one giant concatenated tf file which will have all the tf configurations
