"""
uv run src/chunking.py
"""
from textwrap import dedent


def split_into_chunks(text: str) -> list[str]:
    return [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]


def split_into_fixed_chunks(
    text: str,
    chunk_size: int,
    overlap: int = 0,
) -> list[str]:
    text = text.strip()
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        if end < len(text):
            split_at = text.rfind(" ", start, end)

            if split_at != -1:
                end = split_at

        chunks.append(text[start:end].strip())

        if end == len(text):
            break

        start = max(end - overlap, 0)

    return chunks


def print_chunks(title: str, chunks: list[str]) -> None:
    print(f"\n{title}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {index}:")
        print(chunk)


def demonstrate_chunking(
    document: str,
) -> None:
    paragraph_chunks = split_into_chunks(document)
    fixed_chunks = split_into_fixed_chunks(document, chunk_size=80)
    overlap_chunks = split_into_fixed_chunks(
        document,
        chunk_size=80,
        overlap=20,
    )

    print(f"\nParagraph Chunks: {len(paragraph_chunks)}")
    print(f"Fixed Chunks    : {len(fixed_chunks)}")
    print(f"Overlap Chunks  : {len(overlap_chunks)}")
    print_chunks("---Fixed-Size Chunking---", fixed_chunks)
    print_chunks("---Overlap Chunking---", overlap_chunks)


def main():
    document = dedent("""
    Amazon DynamoDB is a NoSQL database service.

    Amazon S3 is an object storage service.

    AWS Lambda runs serverless functions.

    Amazon Bedrock provides access to foundation models.
    """).strip()

    demonstrate_chunking(document)


if __name__ == "__main__":
    main()
