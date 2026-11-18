"""
"""

import boto3
from datasets.aws_services import documents
from common.embeddings import get_embedding

EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"


def main() -> None:
    bedrock = boto3.client("bedrock-runtime")

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

    print("\nDone.")


if __name__ == "__main__":
    main()
