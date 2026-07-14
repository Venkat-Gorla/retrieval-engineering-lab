"""
Evaluates retrieval quality using the evaluation dataset.

uv run src/evaluate_dataset.py
"""

from typing import Any
import os

from boto3 import Session

from common.embeddings import get_embedding
from common.evaluation import run_evaluation_case
from common.opensearch import create_client
from datasets.aws_services import (
    DOCUMENTS_BY_ID,
    evaluation_cases,
)

from models import (
    EMBEDDING_MODEL_ID,
    INDEX_NAME,
)

TOP_K = 4


def retrieve(
    opensearch,
    query_embedding: list[float],
) -> list[str]:
    response = opensearch.search(
        index=INDEX_NAME,
        body={
            "size": TOP_K,
            "query": {
                "bool": {
                    "must": {
                        "knn": {
                            "embedding": {
                                "vector": query_embedding,
                                "k": TOP_K,
                            }
                        }
                    },
                    "filter": [
                        {
                            "term": {
                                "source": "evaluation",
                            }
                        }
                    ],
                }
            },
        },
    )

    hits = response["hits"]["hits"]
    document_ids = []

    for hit in hits:
        assert (
            hit["_source"]["source"] == "evaluation"
        ), "Non-evaluation document returned."

        document_ids.append(hit["_source"]["id"])

    return document_ids


def print_documents(
    title: str,
    document_ids: list[str],
) -> None:
    print(f"\n{title}:")

    for document_id in document_ids:
        print(DOCUMENTS_BY_ID[document_id]["text"])


def print_metrics(metrics: dict[str, Any]) -> None:
    print("\n" + "-" * 40)

    print("\nQuestion:")
    print(metrics["question"])

    print_documents(
        "Expected",
        metrics["expected_ids"],
    )

    print_documents(
        "Retrieved",
        metrics["retrieved_ids"],
    )

    print(f"\nPrecision@{TOP_K}: {metrics['precision_at_k']:.2%}")
    print(f"Recall@{TOP_K}: {metrics['recall_at_k']:.2%}")

    print("\nResult:")
    print(
        "PASS"
        if metrics["top1_correct"]
        else "FAIL"
    )


def main() -> None:
    host = os.environ["OPENSEARCH_HOST"]
    session = Session()

    bedrock = session.client("bedrock-runtime")
    opensearch = create_client(host)

    correct_count = 0

    for evaluation_case in evaluation_cases:
        query_embedding = get_embedding(
            client=bedrock,
            model_id=EMBEDDING_MODEL_ID,
            text=evaluation_case["question"],
        )

        retrieved_ids = retrieve(
            opensearch,
            query_embedding,
        )

        metrics = run_evaluation_case(
            evaluation_case=evaluation_case,
            retrieved_ids=retrieved_ids,
            top_k=TOP_K,
        )

        print_metrics(metrics)

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
