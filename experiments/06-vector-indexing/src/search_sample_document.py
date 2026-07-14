"""
uv run src/search_documents.py
"""
import os
import time
from boto3 import Session

from common.opensearch import create_client
from common.embeddings import get_embedding
from models import EMBEDDING_MODEL_ID, INDEX_NAME

QUERY = "Where are S3 objects stored?"


def print_search_results(hits):
    print(f"\nFound {len(hits)} result(s).\n")

    for i, hit in enumerate(hits, start=1):
        source = hit["_source"]

        print(f"Result {i}")
        print("-" * 40)
        print(f"Score : {hit['_score']}")
        print(f"ID    : {source['id']}")
        print(f"Source: {source['source']}")
        print(f"Chunk : {source['chunk_number']}")
        print(f"Text  : {source['text']}")
        print()


def main() -> None:
    host = os.environ["OPENSEARCH_HOST"]
    session = Session()

    bedrock = session.client("bedrock-runtime")
    opensearch = create_client(host)

    print("Generating query embedding...")
    embedding = get_embedding(
        client=bedrock,
        model_id=EMBEDDING_MODEL_ID,
        text=QUERY,
    )

    print("Searching...")
    start = time.perf_counter()

    response = opensearch.search(
        index=INDEX_NAME,
        body={
            "size": 3,
            "query": {
                "knn": {
                    "embedding": {
                        "vector": embedding,
                        "k": 3,
                    }
                }
            },
        },
    )

    elapsed = time.perf_counter() - start
    print(f"Search completed in {elapsed:.2f} seconds.")

    hits = response["hits"]["hits"]
    print_search_results(hits)


if __name__ == "__main__":
    main()
