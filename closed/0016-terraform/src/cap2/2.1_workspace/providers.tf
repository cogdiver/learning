terraform {
    backend "s3" {
        bucket = "bucket-jikko-personal"
        key = "terraform-study/terraform.tfstate"
        region = "us-east-1"
    }

    required_version = ">= 0.15"

    required_providers {
        local = {
            source = "hashicorp/local"
            version = "~> 2.0"
        }

        aws = {
            source = "hashicorp/aws"
        }
    }
}

provider "aws" {
    region = var.region
}
