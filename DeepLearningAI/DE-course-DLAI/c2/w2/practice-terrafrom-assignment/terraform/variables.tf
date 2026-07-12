variable "vpc_id" {
  description = "vpc for db"
  type        = string
}

variable "db_username" {
  description = "db user"
  type        = string
  default     = "admin_user"
}

variable "db_password" {
  description = "db password"
  type        = string
}
