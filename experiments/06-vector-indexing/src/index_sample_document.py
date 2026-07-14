"""
uv run src/index_sample_document.py
"""
import os
from boto3 import Session

from common.embeddings import get_embedding
from common.opensearch import create_client
from models import EMBEDDING_MODEL_ID, INDEX_NAME


TEXT = "Amazon S3 stores objects in buckets."


def main() -> None:
    host = os.environ["OPENSEARCH_HOST"]
    session = Session()

    bedrock = session.client("bedrock-runtime")
    opensearch = create_client(host)

    print("Generating embedding...")
    embedding = get_embedding(
        client=bedrock,
        model_id=EMBEDDING_MODEL_ID,
        text=TEXT,
    )

    print(f"Embedding dimension: {len(embedding)}")

    document = {
        "id": "1",
        "text": TEXT,
        "embedding": embedding,
        "source": "manual",
        "chunk_number": 1,
    }

    print(f"Indexing document into '{INDEX_NAME}'...")

    response = opensearch.index(
        index=INDEX_NAME,
        id=document["id"],
        body=document,
    )

    print("Document indexed successfully.")
    print(f"Result: {response['result']}")


if __name__ == "__main__":
    main()
