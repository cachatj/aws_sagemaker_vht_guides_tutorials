// Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

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

variable "QUICKSIGHT_ROLE" {
  type = string
}

variable "USER_NAME" {
  type = string
}

variable "ACCOUNT_NAME" {
  type = string
}

variable "EMAIL" {
  type = string
}

variable "ATHENA_KMS_KEY_ALIAS" {

  type = string
}

variable "ATHENA_OUTPUT_BUCKET" {

  type = string
}

variable "WORKGROUP_NAME" {

  type = string
}
