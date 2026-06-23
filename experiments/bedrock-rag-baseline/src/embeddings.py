import json
import boto3

MODEL_ID = "amazon.titan-embed-text-v2:0"


def main() -> None:
    session = boto3.Session()

    print(f"AWS Profile: {session.profile_name}")
    print(f"AWS Region : {session.region_name}")

    client = session.client("bedrock-runtime")

    text = "Amazon DynamoDB is a fully managed NoSQL database."

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(
            {
                "inputText": text,
            }
        ),
    )

    response_body = json.loads(response["body"].read())
    embedding = response_body["embedding"]

    print(f"\nInput Text: {text}")
    print(f"Vector Dimensions: {len(embedding)}")


if __name__ == "__main__":
    main()
