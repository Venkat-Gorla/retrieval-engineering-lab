"""
uv run src/retrieval_demo.py
"""

from textwrap import dedent

import boto3

from chunking import split_into_chunks
from common.embeddings import get_embedding
from common.retrieval import (
    build_embedding_index,
    rank_embeddings,
)

MODEL_ID = "amazon.titan-embed-text-v2:0"


def main() -> None:
    session = boto3.Session()
    client = session.client("bedrock-runtime")

    document = dedent("""
    Amazon DynamoDB is a NoSQL database service.

    Amazon S3 is an object storage service.

    AWS Lambda runs serverless functions.

    Amazon Bedrock provides access to foundation models.
    """).strip()

    chunks = split_into_chunks(document)
    embedding_index = build_embedding_index(
        client,
        MODEL_ID,
        chunks,
    )

    question = "Which AWS service stores files?"
    query_embedding = get_embedding(client, MODEL_ID, question,)

    results = rank_embeddings(query_embedding, embedding_index,)

    print("Question:")
    print(question)

    print("\nTop Result:")
    print(f"{results[0][1]:.4f} | {results[0][0]}")


if __name__ == "__main__":
    main()
