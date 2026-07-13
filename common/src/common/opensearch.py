from boto3 import Session
from opensearchpy import (
    AWSV4SignerAuth,
    OpenSearch,
    RequestsHttpConnection,
)


def create_client(host: str) -> OpenSearch:
    """
    Creates an authenticated Amazon OpenSearch Serverless client.

    Args:
        host: OpenSearch Serverless endpoint
              (for example: abc123.ap-south-1.aoss.amazonaws.com)

    Returns:
        Authenticated OpenSearch client.
    """

    session = Session()

    credentials = session.get_credentials()
    region = session.region_name

    if region is None:
        raise RuntimeError(
            "AWS region could not be determined from the current session."
        )

    auth = AWSV4SignerAuth(
        credentials=credentials,
        region=region,
        service="aoss",
    )

    return OpenSearch(
        hosts=[
            {
                "host": host,
                "port": 443,
            }
        ],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        timeout=30,
    )
