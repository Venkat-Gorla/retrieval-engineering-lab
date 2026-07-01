"""
uv run src/retrieval_demo.py
"""

from textwrap import dedent

import boto3

from chunking import (
    split_into_chunks,
    split_into_fixed_chunks,
)
from common.embeddings import get_embedding
from common.retrieval import (
    build_embedding_index,
    rank_embeddings,
)

MODEL_ID = "amazon.titan-embed-text-v2:0"


def run_retrieval(
    client,
    title: str,
    query_embedding: list[float],
    chunks: list[str],
) -> None:
    embedding_index = build_embedding_index(
        client,
        MODEL_ID,
        chunks,
    )

    results = rank_embeddings(query_embedding, embedding_index)

    print(f"\n{title}")
    print("-" * len(title))
    print(f"{results[0][1]:.4f} | {results[0][0]}")


def main() -> None:
    session = boto3.Session()
    client = session.client("bedrock-runtime")

    document = dedent("""
    Amazon DynamoDB is a NoSQL database service.

    Amazon S3 is an object storage service.

    AWS Lambda runs serverless functions.

    Amazon Bedrock provides access to foundation models.
    """).strip()

    paragraph_chunks = split_into_chunks(document)
    fixed_chunks = split_into_fixed_chunks(document, chunk_size=80)
    overlap_chunks = split_into_fixed_chunks(
        document,
        chunk_size=80,
        overlap=20,
    )

    question = "Which AWS service stores files?"
    query_embedding = get_embedding(client, MODEL_ID, question)

    print("Question:")
    print(question)

    run_retrieval(
        client,
        "Paragraph Chunking",
        query_embedding,
        paragraph_chunks,
    )

    run_retrieval(
        client,
        "Fixed-Size Chunking",
        query_embedding,
        fixed_chunks,
    )

    run_retrieval(
        client,
        "Overlap Chunking",
        query_embedding,
        overlap_chunks,
    )


if __name__ == "__main__":
    main()
