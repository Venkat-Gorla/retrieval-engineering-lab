"""
Evaluates retrieval quality using the evaluation dataset.

uv run src/evaluate_dataset.py
"""

import boto3

from common.embeddings import get_embedding
from search_sample_document import search_vector_index
from common.evaluation import run_evaluation_case
from common.presentation import print_metrics
from datasets.aws_services import (
    DOCUMENTS_BY_ID,
    evaluation_cases,
)

EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"
TOP_K = 4


def retrieve(
    s3vectors_client,
    query_embedding: list[float],
) -> list[str]:
    response = search_vector_index(
        s3vectors_client=s3vectors_client,
        query_embedding=query_embedding,
        doc_source="evaluation",
        top_k=TOP_K,
    )

    document_ids = []
    for vector in response["vectors"]:
        doc_id = vector["key"]
        source = vector["metadata"]["source"]

        assert source == "evaluation", "Non-evaluation document returned."

        document_ids.append(doc_id)

    return document_ids


def main() -> None:
    bedrock = boto3.client("bedrock-runtime")
    s3vectors_client = boto3.client("s3vectors")

    correct_count = 0

    for evaluation_case in evaluation_cases:
        query_embedding = get_embedding(
            client=bedrock,
            model_id=EMBEDDING_MODEL_ID,
            text=evaluation_case["question"],
        )

        retrieved_ids = retrieve(s3vectors_client, query_embedding)

        metrics = run_evaluation_case(
            evaluation_case=evaluation_case,
            retrieved_ids=retrieved_ids,
            top_k=TOP_K,
        )

        print_metrics(metrics, DOCUMENTS_BY_ID, TOP_K)

        if metrics["top1_correct"]:
            correct_count += 1

    print("\n" + "-" * 40)
    print("\nSummary:")
    print(
        f"{correct_count}/{len(evaluation_cases)} passed"
    )

    accuracy = correct_count / len(evaluation_cases)
    print(f"\nAccuracy@1: {accuracy:.2%}")


if __name__ == "__main__":
    main()
