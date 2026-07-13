"""
uv run src/create_index.py
"""
import os

from common.opensearch import create_client
from models import INDEX_MAPPING, INDEX_NAME


def main() -> None:
    host = os.environ["OPENSEARCH_HOST"]
    client = create_client(host)

    print(f"Checking if index '{INDEX_NAME}' exists...")
    if client.indices.exists(index=INDEX_NAME):
        print("Index already exists.")
        return

    print("Creating index...")
    client.indices.create(
        index=INDEX_NAME,
        body=INDEX_MAPPING,
    )

    print("Index created successfully.")


if __name__ == "__main__":
    main()
