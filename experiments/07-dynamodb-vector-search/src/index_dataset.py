"""
Indexes the evaluation dataset into DynamoDB.

uv run src/index_dataset.py
"""

import boto3
from datasets.aws_services import documents
from common.embeddings import get_embedding
from models import EMBEDDING_MODEL_ID

TABLE_NAME = "retrieval-lab-ddb-vector-search-documents"


def get_db_document(document: dict, embedding: list[float]) -> dict:
    return {
        "documentId": {"S": document["id"]},
        "text": {"S": document["text"]},
        "embedding": {"L": [{"N": str(val)} for val in embedding]},
        "source": {"S": "evaluation"},
        "chunk_number": {"N": "1"},
    }


def main() -> None:
    bedrock = boto3.client("bedrock-runtime")
    dynamodb = boto3.client("dynamodb")

    print(f"Indexing {len(documents)} documents...\n")

    for i, document in enumerate(documents, start=1):
        print(
            f"[{i}/{len(documents)}] "
            f"Indexing {document['id']}"
        )

        embedding = get_embedding(
            client=bedrock,
            model_id=EMBEDDING_MODEL_ID,
            text=document["text"],
        )

        db_document = get_db_document(document, embedding)
        dynamodb.put_item(TableName=TABLE_NAME, Item=db_document)

    print("\nDone.")


if __name__ == "__main__":
    main()
