import boto3

SEARCH_TERM = "nova"


def main() -> None:
    client = boto3.client("bedrock")
    paginator = client.get_paginator("list_inference_profiles")

    for page in paginator.paginate():
        for profile in page["inferenceProfileSummaries"]:
            profile_id = profile["inferenceProfileId"]

            if SEARCH_TERM.lower() not in profile_id.lower():
                continue

            print(f"ID     : {profile_id}")
            print(f"NAME   : {profile['inferenceProfileName']}")
            print(f"STATUS : {profile['status']}")
            print("-" * 60)


if __name__ == "__main__":
    main()
