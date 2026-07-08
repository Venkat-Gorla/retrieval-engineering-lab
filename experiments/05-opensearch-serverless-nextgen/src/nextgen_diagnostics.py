"""
OpenSearch Serverless NextGen diagnostic utility.

Discovers collection configuration and reports current runtime
capacity using the OpenSearch Serverless and CloudWatch APIs.

Run:
uv run src/nextgen_diagnostics.py
"""
from __future__ import annotations

import boto3
from aoss import (
    create_client as create_aoss_client,
    discover_collection,
    discover_collection_group,
)
from cloudwatch_metrics import (
    create_client as create_cloudwatch_client,
    discover_runtime,
)

COLLECTION_NAME = "retrieval-lab-cost"


def print_header():
    title = "OpenSearch Serverless NextGen Diagnostics"

    print("=" * len(title))
    print(title)
    print("=" * len(title))


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
    print(f"Generation        : {group.generation}")
    print(f"Min Search OCU    : {group.min_search_ocu}")
    print(f"Max Search OCU    : {group.max_search_ocu}")
    print(f"Min Index OCU     : {group.min_indexing_ocu}")
    print(f"Max Index OCU     : {group.max_indexing_ocu}")


def print_runtime_info(runtime_info):
    print("Runtime")
    print("-------")
    print(f"Search OCU        : {runtime_info.search_ocu}")
    print(f"Indexing OCU      : {runtime_info.indexing_ocu}")


def main() -> None:
    sts_client = boto3.client("sts")
    account_id = sts_client.get_caller_identity()["Account"]
    aoss_client = create_aoss_client()
    cloudwatch_client = create_cloudwatch_client()

    collection = discover_collection(
        aoss_client,
        COLLECTION_NAME,
    )

    group = discover_collection_group(
        aoss_client,
        collection.group_name,
    )

    runtime_info = discover_runtime(
        client=cloudwatch_client,
        collection_group_id=group.id,
        collection_group_name=group.name,
        account_id=account_id,
    )

    print_header()

    print()
    print_collection_info(collection)

    print()
    print_collection_group_info(group)

    print()
    print_runtime_info(runtime_info)


if __name__ == "__main__":
    main()
