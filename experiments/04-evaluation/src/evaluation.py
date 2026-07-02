"""
uv run src/evaluation.py
"""

import boto3

from common.embeddings import get_embedding
from common.retrieval import (
    build_embedding_index,
    rank_embeddings,
)
from datasets.aws_services import (
    documents,
    evaluation_cases,
)

MODEL_ID = "amazon.titan-embed-text-v2:0"


def run_evaluation_case(
    client,
    embedding_index: list[tuple[str, list[float]]],
    evaluation_case: dict,
) -> bool:
    question = evaluation_case["question"]
    relevant_documents = evaluation_case["relevant_documents"]

    query_embedding = get_embedding(client, MODEL_ID, question)

    ranked_results = rank_embeddings(query_embedding, embedding_index)
    top_document = ranked_results[0][0]
    is_correct = top_document in relevant_documents

    print("\n" + "-" * 40)
    print("\nQuestion:")
    print(question)

    print("\nRelevant:")
    for document in relevant_documents:
        print(document)

    print("\nRetrieved:")
    print(top_document)

    print("\nResult:")
    print("PASS" if is_correct else "FAIL")

    return is_correct


def main() -> None:
    session = boto3.Session()
    client = session.client("bedrock-runtime")

    embedding_index = build_embedding_index(
        client,
        MODEL_ID,
        documents,
    )

    correct_count = 0
    for evaluation_case in evaluation_cases:
        if run_evaluation_case(
            client,
            embedding_index,
            evaluation_case,
        ):
            correct_count += 1

    print("\n" + "-" * 40)
    print("\nSummary:")
    print(f"{correct_count}/{len(evaluation_cases)} passed")

    accuracy = correct_count / len(evaluation_cases)
    print(f"\nAccuracy@1: {accuracy:.2%}")


if __name__ == "__main__":
    main()
