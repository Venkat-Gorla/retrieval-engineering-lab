"""
uv run src/search_sample_document.py
"""

import boto3
from common.embeddings import get_embedding
from models import EMBEDDING_MODEL_ID

TABLE_NAME = "retrieval-lab-ddb-vector-search-documents"
INDEX_NAME = "DocumentEmbeddingIndex"

# Semantic query relevant to "Amazon S3 stores objects in buckets."
QUERY_TEXT = "How does Amazon S3 hold data?"


def search_vector_index(dynamodb, query_embedding: list[float]) -> dict:
    response = dynamodb.search_vectors(
        TableName=TABLE_NAME,
        IndexName=INDEX_NAME,
        SearchVector=[{"N": str(val)} for val in query_embedding],
        TopK=3,
        SearchConditionExpression="#src = :source_val",
        ExpressionAttributeNames={"#src": "source"},
        ExpressionAttributeValues={":source_val": {"S": "manual"}},
        ReturnConsumedCapacity="INDEXES",
    )

    return response


def print_search_results(results: list[dict]) -> None:
    if not results:
        print("No matching documents found.")
        return

    print(f"\nFound {len(results)} matching document(s):")

    for match in results:
        item = match["Item"]
        distance = match["Score"]

        doc_id = item["documentId"]["S"]
        text = item["text"]["S"]
        source = item["source"]["S"]

        print(
            f"\n[Distance: {distance:.6f}] "
            f"Document ID: {doc_id} (Source: {source})"
        )
        print(f"Text: {text}")


def main() -> None:
    bedrock = boto3.client("bedrock-runtime")
    dynamodb = boto3.client("dynamodb")

    print(f"Generating query embedding for: '{QUERY_TEXT}'...")
    query_embedding = get_embedding(
        client=bedrock,
        model_id=EMBEDDING_MODEL_ID,
        text=QUERY_TEXT,
    )

    print(f"Searching vector index '{INDEX_NAME}' in '{TABLE_NAME}'...")
    response = search_vector_index(dynamodb, query_embedding)

    consumed = response.get("ConsumedCapacity", {})
    print(
        f"\nVectorSearchRequestBytes: {consumed.get('VectorSearchRequestBytes')}"
    )

    results = response["SearchResults"]
    print_search_results(results)


if __name__ == "__main__":
    main()
