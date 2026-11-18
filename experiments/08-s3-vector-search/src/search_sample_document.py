"""
uv run src/search_sample_document.py
"""

import boto3
from common.embeddings import get_embedding

EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"
BUCKET_NAME = "retrieval-lab-s3-vector-documents"
INDEX_NAME = "document-embedding-index"

# Semantic query relevant to "Amazon S3 stores objects in buckets."
QUERY_TEXT = "How does Amazon S3 hold data?"


def search_vector_index(
    s3vectors_client,
    query_embedding: list[float],
    doc_source: str,
    top_k: int = 3,
) -> dict:
    response = s3vectors_client.query_vectors(
        vectorBucketName=BUCKET_NAME,
        indexName=INDEX_NAME,
        queryVector={"float32": query_embedding},
        topK=top_k,
        filter={"source": doc_source},
        returnDistance=True,
        returnMetadata=True
    )

    return response


def main() -> None:
    bedrock = boto3.client("bedrock-runtime")
    s3vectors_client = boto3.client("s3vectors")

    print(f"Generating query embedding for: '{QUERY_TEXT}'...")
    query_embedding = get_embedding(
        client=bedrock,
        model_id=EMBEDDING_MODEL_ID,
        text=QUERY_TEXT,
    )

    print(f"Searching vector index '{INDEX_NAME}' in '{BUCKET_NAME}'...")
    response = search_vector_index(
        s3vectors_client=s3vectors_client,
        query_embedding=query_embedding,
        doc_source="evaluation",
    )

    print("\nSearch results:")
    for vector in response["vectors"]:
        distance = vector["distance"]
        print(
            f"  - {vector['metadata']['text']} (Distance: {distance:.6f})")


if __name__ == "__main__":
    main()
