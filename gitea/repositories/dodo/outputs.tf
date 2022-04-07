output "bucket_domain_name" {
  value       = aws_s3_bucket.dodo.bucket_domain_name
  description = "FQDN of bucket"
}

output "bucket_regional_domain_name" {
  value       = aws_s3_bucket.dodo.bucket_regional_domain_name
  description = "The bucket region-specific domain name"
}

output "bucket_id" {
  value       = aws_s3_bucket.dodo.id
  description = "Bucket Name (aka ID)"
}

output "bucket_arn" {
  value       = aws_s3_bucket.dodo.arn
  description = "Bucket ARN"
}