from __future__ import annotations

import boto3
from models import CollectionInfo, CollectionGroupInfo


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


def discover_collection_group(
    client,
    collection_group_name: str,
) -> CollectionGroupInfo:
    """
    Retrieve collection group metadata.
    """
    response = client.batch_get_collection_group(
        names=[collection_group_name]
    )

    groups = response["collectionGroupDetails"]
    if not groups:
        raise RuntimeError(
            f"Collection group '{collection_group_name}' not found."
        )

    group = groups[0]
    limits = group["capacityLimits"]

    return CollectionGroupInfo(
        id=group["id"],
        name=group["name"],
        generation=group["generation"],
        min_search_ocu=limits["minSearchCapacityInOCU"],
        max_search_ocu=limits["maxSearchCapacityInOCU"],
        min_indexing_ocu=limits["minIndexingCapacityInOCU"],
        max_indexing_ocu=limits["maxIndexingCapacityInOCU"],
    )
