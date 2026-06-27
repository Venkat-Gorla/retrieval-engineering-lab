"""
uv run src/chunking.py
"""
import boto3
from common.embeddings import get_embedding

MODEL_ID = "amazon.titan-embed-text-v2:0"


def split_into_chunks(text: str) -> list[str]:
    return [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]


def build_chunk_index(
    client,
    model_id: str,
    chunks: list[str],
) -> list[tuple[str, list[float]]]:
    chunk_index = []

    for chunk in chunks:
        embedding = get_embedding(
            client,
            model_id,
            chunk,
        )

        chunk_index.append(
            (chunk, embedding)
        )

    return chunk_index


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
    chunk_index = build_chunk_index(
        client,
        MODEL_ID,
        chunks,
    )

    print(f"Indexed {len(chunk_index)} chunks")


if __name__ == "__main__":
    main()
