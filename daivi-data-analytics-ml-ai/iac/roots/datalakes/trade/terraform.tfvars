// Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

APP                         = "###APP_NAME###"
ENV                         = "###ENV_NAME###"
AWS_PRIMARY_REGION          = "###AWS_PRIMARY_REGION###"
AWS_SECONDARY_REGION        = "###AWS_SECONDARY_REGION###"
S3_PRIMARY_KMS_KEY_ALIAS    = "###APP_NAME###-###ENV_NAME###-s3-secret-key"
S3_SECONDARY_KMS_KEY_ALIAS  = "###APP_NAME###-###ENV_NAME###-s3-secret-key"
TRADE_TOPIC                 = "trade-topic"
GLUE_ROLE_NAME              = "###APP_NAME###-###ENV_NAME###-glue-role"
TRADE_HIVE_BUCKET           = "s3://###APP_NAME###-###ENV_NAME###-trade-hive-primary/"
TRADE_ICEBERG_BUCKET        = "s3://###APP_NAME###-###ENV_NAME###-trade-iceberg-primary/"
GLUE_SPARK_LOGS_BUCKET      = "s3://###APP_NAME###-###ENV_NAME###-glue-spark-logs-primary/"
GLUE_TEMP_BUCKET            = "s3://###APP_NAME###-###ENV_NAME###-glue-temp-primary/"
GLUE_SCRIPTS_BUCKET_NAME    = "###APP_NAME###-###ENV_NAME###-glue-scripts-primary"
GLUE_KMS_KEY_ALIAS          = "###APP_NAME###-###ENV_NAME###-glue-secret-key"
CLOUDWATCH_KMS_KEY_ALIAS    = "###APP_NAME###-###ENV_NAME###-cloudwatch-secret-key"


