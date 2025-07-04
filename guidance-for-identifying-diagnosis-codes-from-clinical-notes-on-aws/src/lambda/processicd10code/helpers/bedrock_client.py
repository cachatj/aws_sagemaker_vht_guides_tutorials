import boto3
from botocore.client import Config

class BedrockClient:
    """
    A class to interact with AWS Bedrock services, including Bedrock Runtime and Bedrock Agent Runtime.
    """

    # Model IDs for Claude-3 Sonnet and Claude-3 Haiku models
    CLAUDE_3_SONNET = "anthropic.claude-3-sonnet-20240229-v1:0"
    CLAUDE_3_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0"

    def __init__(self, region_name: str):
        """
        Initialize the BedrockClient instance.

        Args:
            region_name (str): The AWS region where the Bedrock services are located.
        """
        self.region = region_name
        self.session = boto3.Session(region_name=region_name)

    def get_bedrock_client(self):
        """
        Get a Boto3 client for the Bedrock Runtime service.

        Returns:
            botocore.client.BaseClient: A Boto3 client for the Bedrock Runtime service.
        """
        # Create a Boto3 client for the Bedrock Runtime service
        client = self.session.client('bedrock-runtime')
        return client

    def get_bedrock_agent_client(self):
        """
        Get a Boto3 client for the Bedrock Agent Runtime service with custom configuration.

        Returns:
            botocore.client.BaseClient: A Boto3 client for the Bedrock Agent Runtime service.
        """
        # Configure the client with increased timeouts and no retries
        bedrock_config = Config(connect_timeout=120, read_timeout=120, retries={'max_attempts': 0})

        # Create a Boto3 client for the Bedrock Agent Runtime service with the custom configuration
        bedrock_agent_client = self.session.client("bedrock-agent-runtime", config=bedrock_config, region_name=self.region)
        return bedrock_agent_client