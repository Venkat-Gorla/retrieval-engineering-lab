"""
uv run src/nextgen_diagnostics.py
"""
from __future__ import annotations

from aoss import (
    create_client,
    discover_collection,
    discover_collection_group,
)

COLLECTION_NAME = "retrieval-lab-cost"


def print_collection_info(collection):
    print("Collection")
    print("----------")
    print(f"Name      : {collection.name}")
    print(f"Status    : {collection.status}")
    print(f"Type      : {collection.collection_type}")
    print(f"Group     : {collection.group_name}")


def print_collection_group_info(group):
    print("Collection Group")
    print("----------------")
    print(f"Name              : {group.name}")
    print(f"Min Search OCU    : {group.min_search_ocu}")
    print(f"Max Search OCU    : {group.max_search_ocu}")
    print(f"Min Index OCU     : {group.min_indexing_ocu}")
    print(f"Max Index OCU     : {group.max_indexing_ocu}")


def main() -> None:
    client = create_client()

    collection = discover_collection(
        client,
        COLLECTION_NAME,
    )

    group = discover_collection_group(
        client,
        collection.group_name,
    )

    print("=" * 60)
    print("OpenSearch Serverless NextGen Diagnostics")
    print("=" * 60)

    print()
    print_collection_info(collection)

    print()
    print_collection_group_info(group)


if __name__ == "__main__":
    main()
