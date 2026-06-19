from aws_cdk import (
    Stack,
    aws_opensearchserverless as aoss,
)
from constructs import Construct


class OpenSearchServerlessCostStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        collection_name = "cost-study"

        encryption_policy = aoss.CfnSecurityPolicy(
            self,
            "EncryptionPolicy",
            name="cost-study-encryption",
            type="encryption",
            policy="""
            {
              "Rules": [
                {
                  "ResourceType": "collection",
                  "Resource": [
                    "collection/cost-study"
                  ]
                }
              ],
              "AWSOwnedKey": true
            }
            """,
        )

        network_policy = aoss.CfnSecurityPolicy(
            self,
            "NetworkPolicy",
            name="cost-study-network",
            type="network",
            policy="""
            [
              {
                "Rules": [
                  {
                    "ResourceType": "collection",
                    "Resource": [
                      "collection/cost-study"
                    ]
                  }
                ],
                "AllowFromPublic": true
              }
            ]
            """,
        )

        collection = aoss.CfnCollection(
            self,
            "Collection",
            name=collection_name,
            type="VECTORSEARCH",
        )

        collection.add_dependency(encryption_policy)
        collection.add_dependency(network_policy)
