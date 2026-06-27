"""
uv run src/chunking.py
"""
import boto3
from common.embeddings import get_embedding
from common.retrieval import (
    build_embedding_index,
    rank_embeddings,
)

MODEL_ID = "amazon.titan-embed-text-v2:0"


def split_into_chunks(text: str) -> list[str]:
    return [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]


def main():
    session = boto3.Session()
    client = session.client("bedrock-runtime")
    print(f"AWS Profile: {session.profile_name}")
    print(f"AWS Region : {session.region_name}")

    document = """
    Amazon DynamoDB is a NoSQL database service.

    Amazon S3 is an object storage service.

    AWS Lambda runs serverless functions.

    Amazon Bedrock provides access to foundation models.
    """

    chunks = split_into_chunks(document)
    chunk_index = build_embedding_index(client, MODEL_ID, chunks)

    question = "Which AWS service stores files?"
    query_embedding = get_embedding(client, MODEL_ID, question,)

    results = rank_embeddings(query_embedding, chunk_index,)

    print("\nQuestion:")
    print(question)
    print("\nResults:")
    for chunk, score in results:
        print(f"{score:.4f} | {chunk}")


if __name__ == "__main__":
    main()
