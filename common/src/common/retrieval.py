from common.embeddings import get_embedding
from common.similarity import cosine_similarity


def build_embedding_index(
    client,
    model_id: str,
    texts: list[str],
) -> list[tuple[str, list[float]]]:
    embedding_index = []

    for text in texts:
        embedding = get_embedding(client, model_id, text)

        embedding_index.append(
            (text, embedding)
        )

    return embedding_index


def rank_embeddings(
    query_embedding: list[float],
    embedding_index: list[tuple[str, list[float]]],
) -> list[tuple[str, float]]:
    ranked_results = []

    for text, embedding in embedding_index:
        similarity_score = cosine_similarity(query_embedding, embedding)
        ranked_results.append((text, similarity_score))

    ranked_results.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    return ranked_results
