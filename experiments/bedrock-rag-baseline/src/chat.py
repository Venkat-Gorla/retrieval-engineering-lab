import json
import time
import boto3

MODEL_ID = "apac.amazon.nova-lite-v1:0"


def main() -> None:
    session = boto3.Session()
    print(f"AWS Profile: {session.profile_name}")
    print(f"AWS Region : {session.region_name}")

    client = session.client("bedrock-runtime")

    user_question = input("\nQuestion: ").strip()
    prompt = (
        "Answer in 3-5 concise sentences.\n\n"
        f"{user_question}"
    )

    start = time.perf_counter()

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt,
                            }
                        ],
                    }
                ]
            }
        ),
    )

    latency = time.perf_counter() - start

    response_body = json.loads(response["body"].read())
    answer = response_body["output"]["message"]["content"][0]["text"]

    print(f"\nLatency: {latency:.2f}s")
    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()
