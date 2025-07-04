// Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

output "primary_bucket_arn" {

  description = "The ARN of the primary bucket"
  value       = aws_s3_bucket.primary.arn
}

output "primary_bucket_id" {

  description = "The ID of the primary bucket"
  value       = aws_s3_bucket.primary.id
}

output "primary_bucket_regional_domain_name" {

  description = "The primary bucket regional domain name"
  value       = aws_s3_bucket.primary.bucket_regional_domain_name
}

output "secondary_bucket_arn" {

  description = "The ARN of the secondary bucket"
  value       = aws_s3_bucket.secondary.arn
}

output "secondary_bucket_id" {

  description = "The ID of the secondary bucket"
  value       = aws_s3_bucket.secondary.id
}

output "secondary_bucket_regional_domain_name" {

  description = "The secondary bucket regional domain name"
  value       = aws_s3_bucket.secondary.bucket_regional_domain_name
}

output "primary_bucket_name" {

  description = "name of the bucket in te primary region"
  value       = aws_s3_bucket.primary.bucket
}
