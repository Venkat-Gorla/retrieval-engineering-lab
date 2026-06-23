import json
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


def main() -> None:
    session = boto3.Session()

    print(f"AWS Profile: {session.profile_name}")
    print(f"AWS Region : {session.region_name}")

    client = session.client("bedrock-runtime")

    text = "Amazon DynamoDB is a fully managed NoSQL database."
    embedding = get_embedding(client, MODEL_ID, text)

    print(f"\nInput Text: {text}")
    print(f"Vector Dimensions: {len(embedding)}")


if __name__ == "__main__":
    main()
