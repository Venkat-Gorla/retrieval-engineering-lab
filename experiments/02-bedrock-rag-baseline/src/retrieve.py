import boto3
from embeddings import get_embedding
from similarity import cosine_similarity

MODEL_ID = "amazon.titan-embed-text-v2:0"


def build_document_index(
    client,
    documents: list[str],
) -> list[tuple[str, list[float]]]:
    document_index = []

    for document in documents:
        embedding = get_embedding(client, MODEL_ID, document)

        document_index.append(
            (document, embedding)
        )

    return document_index


def rank_documents(
    client,
    question: str,
    document_index: list[tuple[str, list[float]]],
) -> list[tuple[str, float]]:
    question_embedding = get_embedding(client, MODEL_ID, question)
    results = []

    for document, document_embedding in document_index:
        score = cosine_similarity(question_embedding, document_embedding)
        results.append((document, score))

    results.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    return results


def main() -> None:
    session = boto3.Session()
    client = session.client("bedrock-runtime")

    documents = [
        "Amazon DynamoDB is a NoSQL database service.",
        "Amazon S3 is an object storage service.",
        "AWS Lambda runs serverless functions.",
    ]

    document_index = build_document_index(client, documents)
    print(f"Indexed {len(document_index)} documents")

    question = "Which AWS service stores files?"
    ranked_documents = rank_documents(client, question, document_index)

    print("\nQuestion:")
    print(question)

    print("\nResults:")
    for document, score in ranked_documents:
        print(f"{score:.4f} | {document}")


if __name__ == "__main__":
    main()
