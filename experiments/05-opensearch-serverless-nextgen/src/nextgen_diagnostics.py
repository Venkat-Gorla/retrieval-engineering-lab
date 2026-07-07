"""
uv run src/nextgen_diagnostics.py
"""
from __future__ import annotations

from aoss import (
    create_client,
    discover_collection,
)

COLLECTION_NAME = "retrieval-lab-cost"


def main() -> None:
    client = create_client()

    collection = discover_collection(
        client,
        COLLECTION_NAME,
    )

    print("=" * 60)
    print("OpenSearch Serverless NextGen Diagnostics")
    print("=" * 60)
    print()

    print("Collection")
    print("----------")
    print(f"Name      : {collection.name}")
    print(f"Status    : {collection.status}")
    print(f"Type      : {collection.collection_type}")
    print(f"Group     : {collection.group_name}")


if __name__ == "__main__":
    main()
