"""
uv run src/chunking.py
"""
from textwrap import dedent
import boto3
from common.embeddings import get_embedding
from common.retrieval import (
    build_embedding_index,
    rank_embeddings,
)

MODEL_ID = "amazon.titan-embed-text-v2:0"


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


def print_ranked_results(results: list[tuple[str, float]]):
    for chunk, score in results:
        print(f"{score:.4f} | {chunk}")


def main():
    session = boto3.Session()
    client = session.client("bedrock-runtime")
    print(f"AWS Profile: {session.profile_name}")
    print(f"AWS Region : {session.region_name}")

    document = dedent("""
    Amazon DynamoDB is a NoSQL database service.

    Amazon S3 is an object storage service.

    AWS Lambda runs serverless functions.

    Amazon Bedrock provides access to foundation models.
    """).strip()

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

    # chunk_index = build_embedding_index(client, MODEL_ID, paragraph_chunks)
    # whole_document_index = build_embedding_index(client, MODEL_ID, [document])

    # question = "Which AWS service stores files?"
    # query_embedding = get_embedding(client, MODEL_ID, question,)

    # chunk_results = rank_embeddings(query_embedding, chunk_index,)
    # document_results = rank_embeddings(query_embedding, whole_document_index,)

    # print("\nQuestion:")
    # print(question)
    # print("\nWhole Document Retrieval:")
    # print_ranked_results(document_results)

    # print("\nChunk Retrieval:")
    # print_ranked_results(chunk_results)


if __name__ == "__main__":
    main()
