"""
Indexes the evaluation dataset into s3.

uv run src/index_dataset.py
"""

import boto3
from datasets.aws_services import documents
from common.embeddings import get_embedding

EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"
BUCKET_NAME = "retrieval-lab-s3-vector-documents"
INDEX_NAME = "document-embedding-index"


def get_s3_document(document: dict, embedding: list[float]) -> dict:
    return {
        "key": document["id"],
        "data": {"float32": embedding},
        "metadata": {"text": document["text"], "source": "evaluation"}
    }


def main() -> None:
    bedrock = boto3.client("bedrock-runtime")
    s3vectors_client = boto3.client("s3vectors")

    print(f"Indexing {len(documents)} documents...\n")

    vectors = []

    for document in documents:
        embedding = get_embedding(
            client=bedrock,
            model_id=EMBEDDING_MODEL_ID,
            text=document["text"],
        )

        vectors.append(get_s3_document(document, embedding))

    s3vectors_client.put_vectors(
        vectorBucketName=BUCKET_NAME,
        indexName=INDEX_NAME,
        vectors=vectors
    )

    print("Done.")


if __name__ == "__main__":
    main()
