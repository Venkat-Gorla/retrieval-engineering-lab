from datetime import datetime, timedelta, UTC

import boto3
from models import RuntimeInfo


def create_client():
    return boto3.client("cloudwatch")


def get_metric(
    client,
    metric_name: str,
    collection_group_id: str,
    collection_group_name: str,
    account_id: str,
) -> float:
    end_time = datetime.now(UTC)
    start_time = end_time - timedelta(minutes=30)

    response = client.get_metric_statistics(
        Namespace="AWS/AOSS",
        MetricName=metric_name,

        Dimensions=[
            {
                "Name": "CollectionGroupId",
                "Value": collection_group_id,
            },
            {
                "Name": "CollectionGroupName",
                "Value": collection_group_name,
            },
            {
                "Name": "ClientId",
                "Value": account_id,
            },
        ],

        StartTime=start_time,
        EndTime=end_time,

        Period=300,
        Statistics=["Average"],
    )

    datapoints = response["Datapoints"]

    if not datapoints:
        return 0.0

    latest = max(
        datapoints,
        key=lambda d: d["Timestamp"],
    )

    return latest["Average"]


def discover_runtime(
    client,
    collection_group_id: str,
    collection_group_name: str,
    account_id: str,
) -> RuntimeInfo:

    return RuntimeInfo(
        search_ocu=get_metric(
            client,
            "SearchOCU",
            collection_group_id,
            collection_group_name,
            account_id,
        ),

        indexing_ocu=get_metric(
            client,
            "IndexingOCU",
            collection_group_id,
            collection_group_name,
            account_id,
        ),
    )
