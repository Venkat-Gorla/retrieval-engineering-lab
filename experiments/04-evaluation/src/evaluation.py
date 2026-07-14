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
TOP_K = 4


def run_evaluation_case(
    client,
    embedding_index: list[tuple[str, list[float]]],
    evaluation_case: dict,
) -> bool:
    question = evaluation_case["question"]
    relevant_documents = evaluation_case["relevant_documents"]

    query_embedding = get_embedding(client, MODEL_ID, question)
    ranked_results = rank_embeddings(query_embedding, embedding_index)

    top_documents = [
        text
        for text, _ in ranked_results[:TOP_K]
    ]
    top1_correct = top_documents[0] in relevant_documents

    relevant_retrieved = len(
        set(top_documents) & set(relevant_documents)
    )

    precision = (
        relevant_retrieved / len(top_documents)
        if top_documents
        else 0.0
    )

    recall = (
        relevant_retrieved / len(relevant_documents)
        if relevant_documents
        else 0.0
    )

    print("\n" + "-" * 40)
    print("\nQuestion:")
    print(question)

    print("\nRelevant:")
    for document in relevant_documents:
        print(document)

    print("\nRetrieved:")
    for document in top_documents:
        print(document)

    print(f"\nPrecision@{TOP_K}: {precision:.2%}")
    print(f"Recall@{TOP_K}: {recall:.2%}")

    print("\nResult:")
    print("PASS" if top1_correct else "FAIL")

    return top1_correct


def main() -> None:
    session = boto3.Session()
    client = session.client("bedrock-runtime")

    document_texts = [document["text"] for document in documents]
    embedding_index = build_embedding_index(
        client,
        MODEL_ID,
        document_texts,
    )

    top1_correct_count = 0
    for evaluation_case in evaluation_cases:
        if run_evaluation_case(
            client,
            embedding_index,
            evaluation_case,
        ):
            top1_correct_count += 1

    print("\n" + "-" * 40)
    print("\nSummary:")
    print(f"{top1_correct_count}/{len(evaluation_cases)} passed")

    accuracy = top1_correct_count / len(evaluation_cases)
    print(f"\nAccuracy@1: {accuracy:.2%}")


if __name__ == "__main__":
    main()
