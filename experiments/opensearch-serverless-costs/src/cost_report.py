"""
uv run cost_report.py
"""
from datetime import date, timedelta
import boto3


def main() -> None:
    yesterday = date.today() - timedelta(days=1)
    today = date.today()

    client = boto3.client("ce")

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": yesterday.isoformat(),
            "End": today.isoformat(),
        },
        Granularity="DAILY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE",
            }
        ],
    )

    for result in response["ResultsByTime"]:
        print(f"\nDate: {result['TimePeriod']['Start']}")

        for group in result["Groups"]:
            service_name = group["Keys"][0]
            cost = group["Metrics"]["UnblendedCost"]["Amount"]

            print(f"{service_name:<40} ${float(cost):.4f}")


if __name__ == "__main__":
    main()
