import boto3
from embeddings import get_embedding
from similarity import cosine_similarity

MODEL_ID = "amazon.titan-embed-text-v2:0"


def main() -> None:
    session = boto3.Session()
    client = session.client("bedrock-runtime")

    documents = [
        "Amazon DynamoDB is a NoSQL database service.",
        "Amazon S3 is an object storage service.",
        "AWS Lambda runs serverless functions.",
    ]

    question = "Which AWS service stores files?"
    question_embedding = get_embedding(client, MODEL_ID, question)

    best_document = ""
    best_score = -1.0

    for document in documents:
        document_embedding = get_embedding(client, MODEL_ID, document)
        score = cosine_similarity(question_embedding, document_embedding)

        print(f"{score:.4f} | {document}")

        if score > best_score:
            best_score = score
            best_document = document

    print("\nQuestion:")
    print(question)

    print("\nBest Match:")
    print(best_document)


if __name__ == "__main__":
    main()
