// Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

variable "AWS_ACCOUNT_ID" {

  type = string
}

variable "APP" {

  type = string
}

variable "ENV" {

  type = string
}

variable "AWS_PRIMARY_REGION" {

  type = string
}

variable "AWS_SECONDARY_REGION" {

  type = string
}

variable "S3_PRIMARY_KMS_KEY_ALIAS" {

  type = string
}

variable "S3_SECONDARY_KMS_KEY_ALIAS" {

  type = string
}

variable "BILLING_DATA_BUCKET" {

  type = string
}

variable "GLUE_SCRIPTS_BUCKET_NAME" {

  type = string
}

variable "GLUE_ROLE_NAME" {

  type = string
}

variable "BILLING_DATA_FILE" {

  type = string
}

variable "BILLING_ICEBERG_BUCKET" {

  type = string
}

variable "GLUE_SPARK_LOGS_BUCKET" {

  type = string
}

variable "GLUE_TEMP_BUCKET" {

  type = string
}

variable "GLUE_KMS_KEY_ALIAS" {

  type = string
}

variable "CLOUDWATCH_KMS_KEY_ALIAS" {

  type = string
}

variable "EVENTBRIDGE_ROLE_NAME" {

  type = string
}
