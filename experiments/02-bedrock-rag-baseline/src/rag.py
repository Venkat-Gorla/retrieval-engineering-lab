import json
import boto3
from retrieve import build_document_index, rank_documents


def create_nova_prompt(question: str, top_document: str) -> str:
    return f"""
    Context:
    {top_document}

    Question:
    {question}

    Answer using only the provided context.
    """


def get_nova_response(client, prompt: str) -> str:
    MODEL_ID = "apac.amazon.nova-lite-v1:0"

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

    response_body = json.loads(response["body"].read())
    answer = response_body["output"]["message"]["content"][0]["text"]

    return answer


def main() -> None:
    session = boto3.Session()
    client = session.client("bedrock-runtime")

    documents = [
        "Amazon DynamoDB is a NoSQL database service.",
        "Amazon S3 is an object storage service.",
        "AWS Lambda runs serverless functions.",
    ]

    document_index = build_document_index(client, documents)

    question = "Which AWS service stores files?"
    ranked_documents = rank_documents(client, question, document_index)
    if not ranked_documents:
        raise ValueError("No documents available for retrieval")

    top_document = ranked_documents[0][0]

    prompt = create_nova_prompt(question, top_document)
    answer = get_nova_response(client, prompt)

    print("\nQuestion:")
    print(question)
    print("\nRetrieved Context:")
    print(top_document)
    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()
