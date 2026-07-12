# data source 
# Getting the subnet Ids
data "aws_subnets" "subnet_ids" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }
}

# Setting the subnet for DB
resource "aws_db_subnet_group" "aws_db_subnet_group" {
  name       = "main_subnet"
  subnet_ids = data.aws_subnets.subnet_ids.ids
  tags = {
    name = "My DB Subnet Group"
  }
}

# resource
resource "aws_db_instance" "my_database" {
  allocated_storage    = 10
  db_name              = "my_database"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
  db_subnet_group_name = aws_db_subnet_group.aws_db_subnet_group.id
}
