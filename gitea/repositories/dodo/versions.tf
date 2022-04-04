terraform {
  required_version = ">= 0.12.26"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "< 4.0"
    }
  }

  backend "local" {
    path = "../terraform.tfstate"
  }
}