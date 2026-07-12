# terraform settings 
terraform {
  required_providers {
    aws = {                     // Local Name
      source  = "hashicorp/aws" // Source Location
      version = ">= 4.16"       // Version Constraint
    }
  }
  required_version = ">= 1.2.0"
}

# providers
# A provider is plugin or a binary file that Terraform will use to create your resources

provider "aws" { // aws here is Local Name
  region = var.region
}
