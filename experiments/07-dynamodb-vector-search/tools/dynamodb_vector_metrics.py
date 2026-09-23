"""
Measure DynamoDB consumption for the vector search experiment.

uv run tools/dynamodb_vector_metrics.py
"""

from datetime import UTC, datetime, timedelta
import boto3


TABLE_NAME = "retrieval-lab-ddb-vector-search-documents"
NAMESPACE = "AWS/DynamoDB"


def get_metric_sum(cloudwatch, metric_name, start_time, end_time) -> float:
    response = cloudwatch.get_metric_statistics(
        Namespace=NAMESPACE,
        MetricName=metric_name,
        Dimensions=[
            {
                "Name": "TableName",
                "Value": TABLE_NAME,
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=60,
        Statistics=["Sum"],
    )

    return sum(
        datapoint["Sum"]
        for datapoint in response["Datapoints"]
    )


def main() -> None:
    cloudwatch = boto3.client("cloudwatch")

    end_time = datetime.now(UTC)
    start_time = end_time - timedelta(minutes=10)

    consumed_writes = get_metric_sum(
        cloudwatch,
        "ConsumedWriteCapacityUnits",
        start_time,
        end_time,
    )

    consumed_reads = get_metric_sum(
        cloudwatch,
        "ConsumedReadCapacityUnits",
        start_time,
        end_time,
    )

    TIME_FORMAT = "%Y-%m-%d %H:%M:%S UTC"

    print("DynamoDB Metrics")
    print("-" * 40)
    print(f"Table      : {TABLE_NAME}")
    print(f"Start Time : {start_time.strftime(TIME_FORMAT)}")
    print(f"End Time   : {end_time.strftime(TIME_FORMAT)}")
    print()
    print(f"Consumed Write Capacity Units : {consumed_writes:.2f}")
    print(f"Consumed Read Capacity Units  : {consumed_reads:.2f}")


if __name__ == "__main__":
    main()
