from aws_cdk import (
    Stack,
    aws_opensearchserverless as aoss,
)
from constructs import Construct

PROJECT_NAME = "retrieval-lab"
EXPERIMENT_NAME = "cost-study"

collection_name = f"{PROJECT_NAME}-{EXPERIMENT_NAME}"


class OpenSearchServerlessCostStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        encryption_policy = self._create_encryption_policy()
        network_policy = self._create_network_policy()

        collection = aoss.CfnCollection(
            self,
            "Collection",
            name=collection_name,
            type="VECTORSEARCH",
        )

        collection.add_dependency(encryption_policy)
        collection.add_dependency(network_policy)

    def _create_encryption_policy(self) -> aoss.CfnSecurityPolicy:
        return aoss.CfnSecurityPolicy(
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

    def _create_network_policy(self) -> aoss.CfnSecurityPolicy:
        return aoss.CfnSecurityPolicy(
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
