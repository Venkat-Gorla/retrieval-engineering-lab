import boto3
from embeddings import get_embedding
from similarity import cosine_similarity

MODEL_ID = "amazon.titan-embed-text-v2:0"


def rank_documents(
    client,
    question: str,
    documents: list[str],
) -> list[tuple[str, float]]:
    question_embedding = get_embedding(client, MODEL_ID, question)
    results = []

    for document in documents:
        document_embedding = get_embedding(client, MODEL_ID, document)
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

    question = "Which AWS service stores files?"
    results = rank_documents(client, question, documents)

    print("\nQuestion:")
    print(question)

    print("\nResults:")
    for document, score in results:
        print(f"{score:.4f} | {document}")


if __name__ == "__main__":
    main()
