from typing import Any


def print_documents(
    title: str,
    document_ids: list[str],
    documents_by_id: dict[str, dict],
) -> None:
    print(f"\n{title}:")

    for document_id in document_ids:
        print(documents_by_id[document_id]["text"])


def print_metrics(
    metrics: dict[str, Any],
    documents_by_id: dict[str, dict],
    top_k: int,
) -> None:
    print("\n" + "-" * 40)

    print("\nQuestion:")
    print(metrics["question"])

    print_documents(
        "Expected",
        metrics["expected_ids"],
        documents_by_id,
    )

    print_documents(
        "Retrieved",
        metrics["retrieved_ids"],
        documents_by_id,
    )

    print(f"\nPrecision@{top_k}: {metrics['precision_at_k']:.2%}")
    print(f"Recall@{top_k}: {metrics['recall_at_k']:.2%}")

    print("\nResult:")
    print("PASS" if metrics["top1_correct"] else "FAIL")
