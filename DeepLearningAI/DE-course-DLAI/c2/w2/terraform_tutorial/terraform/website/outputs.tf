
# output
output "server_id" {
  value = aws_instance.webserver.id

}
output "server_arn" {
  value = aws_instance.webserver.arn
}
