"""
uv run src/index_sample_document.py
"""

import boto3
from common.embeddings import get_embedding
from models import EMBEDDING_MODEL_ID


TABLE_NAME = "retrieval-lab-ddb-vector-search-documents"
SAMPLE_TEXT = "Amazon S3 stores objects in buckets."


def main() -> None:
    dynamodb = boto3.client('dynamodb')
    bedrock = boto3.client("bedrock-runtime")

    print("Generating embedding...")
    embedding = get_embedding(
        client=bedrock,
        model_id=EMBEDDING_MODEL_ID,
        text=SAMPLE_TEXT,
    )

    print(f"Embedding dimension: {len(embedding)}")

    document = {
        "documentId": {"S": "1"},
        "text": {"S": SAMPLE_TEXT},
        "embedding": {"L": [{"N": str(val)} for val in embedding]},
        "source": {"S": "manual"},
        "chunk_number": {"N": "1"},
    }

    print(f"Indexing document into '{TABLE_NAME}'...")

    dynamodb.put_item(TableName=TABLE_NAME, Item=document)

    print("Document indexed successfully.")
    print(f"Document ID: {document['documentId']}")


if __name__ == "__main__":
    main()
