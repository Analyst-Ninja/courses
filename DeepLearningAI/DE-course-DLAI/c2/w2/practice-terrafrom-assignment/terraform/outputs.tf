output "database_hostname" {
  value = aws_db_instance.my_database.address
}

output "database_username" {
  value = aws_db_instance.my_database.username
}

output "database_password" {
  value     = aws_db_instance.my_database.password
  sensitive = true
}

output "database_port" {
  value = aws_db_instance.my_database.port
}
