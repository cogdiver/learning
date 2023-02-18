variable "region" {
    description = "Region to deploy"
    default = "us-east-1"
}

locals {
    numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = sum([for x in local.numList : 10 * x if x % 2 == 0])
}
