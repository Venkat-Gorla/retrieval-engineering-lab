from typing import Any


def run_evaluation_case(
    evaluation_case: dict[str, Any],
    retrieved_ids: list[str],
    top_k: int,
) -> dict[str, Any]:
    """
    Evaluates a retrieval result against the expected document IDs.

    Args:
        evaluation_case:
            Evaluation dataset entry.

        retrieved_ids:
            Ranked document IDs returned by the retrieval backend.

        top_k:
            Number of retrieved documents considered for evaluation.

    Returns:
        Dictionary containing evaluation metrics.
    """

    expected_ids = evaluation_case["expected_ids"]
    top_ids = retrieved_ids[:top_k]

    top1_correct = (
        bool(top_ids)
        and top_ids[0] in expected_ids
    )

    relevant_retrieved = len(
        set(top_ids) & set(expected_ids)
    )

    precision = (
        relevant_retrieved / len(top_ids)
        if top_ids
        else 0.0
    )

    recall = (
        relevant_retrieved / len(expected_ids)
        if expected_ids
        else 0.0
    )

    return {
        "question": evaluation_case["question"],
        "expected_ids": expected_ids,
        "retrieved_ids": top_ids,
        "top1_correct": top1_correct,
        "precision_at_k": precision,
        "recall_at_k": recall,
    }
