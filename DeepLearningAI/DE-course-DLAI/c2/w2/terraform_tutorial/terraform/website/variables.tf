
# input 
variable "region" {
  description = "region for AWS resources"
  type        = string
  default     = "ap-south-1"
  // If you don't add default value it will ask its value at the terraform apply step 
}

variable "server_name" {
  description = "name of the server running the website"
  type        = string
  // To give the variable value @ the terraform apply step
  // terraform apply -var server_name=example-server 
  // Or terraform variables can be stored in a separate file -- `terraform.tfvars` 
}
