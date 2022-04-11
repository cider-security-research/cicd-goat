variable "bucket_name" {
  type        = string
  description = "Bucket name"
  default     = "dodo"
}

variable "sse_algorithm" {
  type        = string
  default     = "aws:kms"
  description = "The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`"
}

