EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"

EMBEDDING_DIMENSION = 1024
INDEX_NAME = "rag-documents"

INDEX_MAPPING = {
    "settings": {
        "index": {
            "knn": True
        }
    },
    "mappings": {
        "properties": {
            "id": {
                "type": "keyword"
            },
            "text": {
                "type": "text"
            },
            "embedding": {
                "type": "knn_vector",
                "dimension": EMBEDDING_DIMENSION
            },
            "source": {
                "type": "keyword"
            },
            "chunk_number": {
                "type": "integer"
            }
        }
    }
}
