// Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

module "inventory_data_source_bucket" {

  source = "../../../templates/modules/bucket"

  providers = {
    aws.primary   = aws.primary
    aws.secondary = aws.secondary
  }

  RESOURCE_PREFIX              = "${var.APP}-${var.ENV}-inventory-data-source"
  BUCKET_NAME_PRIMARY_REGION   = "primary"
  BUCKET_NAME_SECONDARY_REGION = "secondary"
  PRIMARY_CMK_ARN              = data.aws_kms_key.s3_primary_key.arn
  SECONDARY_CMK_ARN            = data.aws_kms_key.s3_secondary_key.arn
  APP                          = var.APP
  ENV                          = var.ENV
  USAGE                        = "inventory"
}

module "inventory_data_destination_bucket" {

  source = "../../../templates/modules/bucket"

  providers = {
    aws.primary   = aws.primary
    aws.secondary = aws.secondary
  }

  RESOURCE_PREFIX              = "${var.APP}-${var.ENV}-inventory-data-destination"
  BUCKET_NAME_PRIMARY_REGION   = "primary"
  BUCKET_NAME_SECONDARY_REGION = "secondary"
  PRIMARY_CMK_ARN              = data.aws_kms_key.s3_primary_key.arn
  SECONDARY_CMK_ARN            = data.aws_kms_key.s3_secondary_key.arn
  APP                          = var.APP
  ENV                          = var.ENV
  USAGE                        = "inventory"
}

module "inventory_iceberg_bucket" {

  source = "../../../templates/modules/bucket"

  providers = {
    aws.primary   = aws.primary
    aws.secondary = aws.secondary
  }

  RESOURCE_PREFIX              = "${var.APP}-${var.ENV}-inventory-iceberg"
  BUCKET_NAME_PRIMARY_REGION   = "primary"
  BUCKET_NAME_SECONDARY_REGION = "secondary"
  PRIMARY_CMK_ARN              = data.aws_kms_key.s3_primary_key.arn
  SECONDARY_CMK_ARN            = data.aws_kms_key.s3_secondary_key.arn
  APP                          = var.APP
  ENV                          = var.ENV
  USAGE                        = "inventory"
}

module "inventory_hive_bucket" {

  source = "../../../templates/modules/bucket"

  providers = {
    aws.primary   = aws.primary
    aws.secondary = aws.secondary
  }

  RESOURCE_PREFIX              = "${var.APP}-${var.ENV}-inventory-hive"
  BUCKET_NAME_PRIMARY_REGION   = "primary"
  BUCKET_NAME_SECONDARY_REGION = "secondary"
  PRIMARY_CMK_ARN              = data.aws_kms_key.s3_primary_key.arn
  SECONDARY_CMK_ARN            = data.aws_kms_key.s3_secondary_key.arn
  APP                          = var.APP
  ENV                          = var.ENV
  USAGE                        = "inventory"
}

resource "aws_s3_bucket_notification" "inventory_s3_notification" {

  bucket = module.inventory_data_destination_bucket.primary_bucket_id

  lambda_function {
    lambda_function_arn = aws_lambda_function.inventory_workflow_trigger.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "${var.APP}-${var.ENV}-inventory-data-source-primary/InventoryConfig/data/"
    filter_suffix       = ".gz"
  }

  depends_on = [aws_lambda_permission.allow_s3_invoke]
}

resource "aws_s3_object" "destination_inventory_files" {

  for_each     = fileset("${path.module}/../../../../data/inventory/static/", "*.gz")
  bucket       = module.inventory_data_destination_bucket.primary_bucket_id
  key          = each.value
  source       = "${path.module}/../../../../data/inventory/static/${each.value}"
  content_type = "gz"
  kms_key_id   = data.aws_kms_key.s3_primary_key.arn
}

resource "aws_lakeformation_resource" "hive_s3_location" {

  arn       = "arn:aws:s3:::${var.APP}-${var.ENV}-inventory-hive-primary"
  role_arn  = data.aws_iam_role.glue_role.arn

  use_service_linked_role     = false
  hybrid_access_enabled       = false

  depends_on = [ module.inventory_hive_bucket ]
}

resource "aws_lakeformation_permissions" "hive_deployer_role" {

  principal   = local.role_arn
  permissions = ["DATA_LOCATION_ACCESS"]

  data_location {
    arn = aws_lakeformation_resource.hive_s3_location.arn
  }
}

resource "aws_lakeformation_permissions" "hive_glue_role" {

  principal   = data.aws_iam_role.glue_role.arn
  permissions = ["DATA_LOCATION_ACCESS"]

  data_location {
    arn = aws_lakeformation_resource.hive_s3_location.arn
  }
}

resource "aws_lakeformation_resource" "iceberg_s3_location" {

  arn       = "arn:aws:s3:::${var.APP}-${var.ENV}-inventory-iceberg-primary"
  role_arn  = data.aws_iam_role.glue_role.arn

  use_service_linked_role     = false
  hybrid_access_enabled       = false

  depends_on = [ module.inventory_iceberg_bucket ]
}

resource "aws_lakeformation_permissions" "iceberg_deployer_role" {

  principal   = local.role_arn
  permissions = ["DATA_LOCATION_ACCESS"]

  data_location {
    arn = aws_lakeformation_resource.iceberg_s3_location.arn
  }
}

resource "aws_lakeformation_permissions" "iceberg_glue_role" {

  principal   = data.aws_iam_role.glue_role.arn
  permissions = ["DATA_LOCATION_ACCESS"]

  data_location {
    arn = aws_lakeformation_resource.iceberg_s3_location.arn
  }
}