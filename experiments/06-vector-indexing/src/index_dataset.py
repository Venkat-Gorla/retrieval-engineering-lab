"""
Indexes the evaluation dataset into OpenSearch.

uv run src/index_dataset.py
"""

import os
from boto3 import Session

from common.opensearch import create_client
from common.embeddings import get_embedding
from datasets.aws_services import documents

from models import (
    EMBEDDING_MODEL_ID,
    INDEX_NAME,
)


def main() -> None:
    host = os.environ["OPENSEARCH_HOST"]
    session = Session()

    bedrock = session.client("bedrock-runtime")
    opensearch = create_client(host)

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

        opensearch.index(
            index=INDEX_NAME,
            id=document["id"],
            body={
                "id": document["id"],
                "text": document["text"],
                "embedding": embedding,
                "source": "evaluation",
                "chunk_number": 1,
            },
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
