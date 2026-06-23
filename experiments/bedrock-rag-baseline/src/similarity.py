import json
from math import sqrt
import boto3

MODEL_ID = "amazon.titan-embed-text-v2:0"


def get_embedding(client, model_id: str, text: str) -> list[float]:
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(
            {
                "inputText": text,
            }
        ),
    )

    response_body = json.loads(response["body"].read())

    return response_body["embedding"]


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = sqrt(
        sum(b * b for b in vector_b)
    )

    return dot_product / (
        magnitude_a * magnitude_b
    )


def main() -> None:
    session = boto3.Session()

    print(f"AWS Profile: {session.profile_name}")
    print(f"AWS Region : {session.region_name}")

    client = session.client("bedrock-runtime")

    sentence_a = "DynamoDB is a NoSQL database."
    sentence_b = "DynamoDB stores key-value data."
    sentence_c = "Pizza is a popular Italian food."

    embedding_a = get_embedding(client, MODEL_ID, sentence_a)
    embedding_b = get_embedding(client, MODEL_ID, sentence_b)
    embedding_c = get_embedding(client, MODEL_ID, sentence_c)

    print(
        f"\nSimilarity(A, B): "
        f"{cosine_similarity(embedding_a, embedding_b):.4f}"
    )

    print(
        f"Similarity(A, C): "
        f"{cosine_similarity(embedding_a, embedding_c):.4f}"
    )


if __name__ == "__main__":
    main()
