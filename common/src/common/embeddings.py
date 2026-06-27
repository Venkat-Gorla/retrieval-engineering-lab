import json


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
