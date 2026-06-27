"""
uv run src/chunking.py
"""


def split_into_chunks(text: str) -> list[str]:
    return [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]


def main():
    document = """
    Amazon DynamoDB is a NoSQL database service.

    Amazon S3 is an object storage service.

    AWS Lambda runs serverless functions.

    Amazon Bedrock provides access to foundation models.
    """

    chunks = split_into_chunks(document)

    print(f"Chunks: {len(chunks)}\n")

    for index, chunk in enumerate(chunks, start=1):
        print(f"Chunk {index}:")
        print(chunk)
        print()


if __name__ == "__main__":
    main()
