import boto3
import os

def lambda_handler(event, context):
    """
    AWS Lambda function handler to start a knowledge base ingestion job in AWS Bedrock.

    Args:
        event (dict): The event data from AWS Lambda.
        context (object): The context object from AWS Lambda.

    Returns:
        dict: The response from the Bedrock start_ingestion_job API call.
    """
    # Initialize the Bedrock client
    bedrock_client = boto3.client('bedrock-agent')

    # Get the data source ID and knowledge base ID from environment variables
    data_source_id = os.environ.get('DataSourceId')
    knowledge_base_id = os.environ.get('KnowledgeBaseId')

    # Check if the required environment variables are set
    if not data_source_id or not knowledge_base_id:
        raise ValueError("DataSourceId and KnowledgeBaseId environment variables must be set.")

    # Start the knowledge base ingestion job
    response = bedrock_client.start_ingestion_job(
        dataSourceId=data_source_id,
        description='Start knowledge base S3 data source ingestion process.',
        knowledgeBaseId=knowledge_base_id
    )

    # Log the response from the API call
    print(response)

    return {
        'statusCode': 200,
        'body': 'KB Sync initiated'
    }