from __future__ import annotations

import boto3
from models import CollectionInfo


def create_client():
    return boto3.client("opensearchserverless")


def discover_collection(
    client,
    collection_name: str,
) -> CollectionInfo:
    """
    Retrieve collection metadata.
    """

    response = client.batch_get_collection(
        names=[collection_name]
    )

    collections = response["collectionDetails"]

    if not collections:
        raise RuntimeError(
            f"Collection '{collection_name}' not found."
        )

    collection = collections[0]

    return CollectionInfo(
        name=collection["name"],
        group_name=collection["collectionGroupName"],
        status=collection["status"],
        collection_type=collection["type"],
    )
