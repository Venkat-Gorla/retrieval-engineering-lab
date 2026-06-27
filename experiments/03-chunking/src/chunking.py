"""
uv run src/chunking.py
"""
import boto3

from common.embeddings import get_embedding

MODEL_ID = "amazon.titan-embed-text-v2:0"


def main() -> None:
    session = boto3.Session()

    print(f"AWS Profile: {session.profile_name}")
    print(f"AWS Region : {session.region_name}")

    client = session.client("bedrock-runtime")

    text = "Amazon S3 is an object storage service."

    embedding = get_embedding(
        client,
        MODEL_ID,
        text,
    )

    print(f"\nInput Text: {text}")
    print(f"Vector Dimensions: {len(embedding)}")


if __name__ == "__main__":
    main()
