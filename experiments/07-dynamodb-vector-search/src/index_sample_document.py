"""
uv run src/index_sample_document.py
"""

import boto3
from common.embeddings import get_embedding
from models import EMBEDDING_MODEL_ID


TABLE_NAME = "retrieval-lab-ddb-vector-search-documents"

documents = [
    {
        "documentId": "1",
        "text": "Amazon S3 stores objects in buckets.",
    },
    {
        "documentId": "2",
        "text": "Amazon S3 provides durable object storage.",
    },
]


def get_db_document(sample_document: dict, embedding: list[float]) -> dict:
    return {
        "documentId": {"S": sample_document["documentId"]},
        "text": {"S": sample_document["text"]},
        "embedding": {"L": [{"N": str(val)} for val in embedding]},
        "source": {"S": "manual"},
        "chunk_number": {"N": "1"},
    }


def main() -> None:
    dynamodb = boto3.client('dynamodb')
    bedrock = boto3.client("bedrock-runtime")

    for sample_document in documents:
        print("\nGenerating embedding...")
        embedding = get_embedding(
            client=bedrock,
            model_id=EMBEDDING_MODEL_ID,
            text=sample_document["text"],
        )

        print(f"Embedding dimension: {len(embedding)}")

        print(f"Indexing document into '{TABLE_NAME}'...")
        document = get_db_document(sample_document, embedding)
        dynamodb.put_item(TableName=TABLE_NAME, Item=document)

        print("Document indexed successfully.")
        print(f"Document ID: {document['documentId']}")


if __name__ == "__main__":
    main()
