"""
Discover and inspect CloudWatch metrics for DynamoDB.

uv run tools/dynamodb_metrics.py
"""

import boto3


NAMESPACE = "AWS/DynamoDB"


INTERESTING_METRICS = {
    "ConsumedReadCapacityUnits",
    "ConsumedWriteCapacityUnits",
}


def print_metric_dimensions(
    metrics: list[dict],
    metric_name: str,
) -> None:
    """Print unique dimension-name sets for a metric."""
    dimension_sets = {
        tuple(sorted(dimension["Name"] for dimension in metric["Dimensions"]))
        for metric in metrics
        if metric["MetricName"] == metric_name
    }

    print(f"\n{metric_name} dimensions:")

    for dimensions in sorted(dimension_sets):
        print(f"  {', '.join(dimensions)}")


def main() -> None:
    cloudwatch = boto3.client("cloudwatch")
    paginator = cloudwatch.get_paginator("list_metrics")

    metrics = []

    for page in paginator.paginate(Namespace=NAMESPACE):
        metrics.extend(page["Metrics"])

    unique_metric_names = {
        metric["MetricName"]
        for metric in metrics
    }

    print(f"\nPrinting {NAMESPACE} metric names:")
    print("=" * 40)

    for name in sorted(unique_metric_names):
        print(name)

    print("\nPrinting dimensions for selected metrics:")
    print("=" * 40)

    for metric_name in sorted(INTERESTING_METRICS):
        print_metric_dimensions(metrics, metric_name)


if __name__ == "__main__":
    main()
