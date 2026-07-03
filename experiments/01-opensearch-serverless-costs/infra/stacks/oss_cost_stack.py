import json
from aws_cdk import (
    Stack,
    Tags,
    aws_opensearchserverless as aoss,
)
from constructs import Construct

PROJECT_NAME = "retrieval-lab"
EXPERIMENT_NAME = "cost"

collection_name = f"{PROJECT_NAME}-{EXPERIMENT_NAME}"


class OpenSearchServerlessCostStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Tags.of(self).add("Project", PROJECT_NAME)
        # Tags.of(self).add("Experiment", EXPERIMENT_NAME)

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
        encryption_policy_document = {
            "Rules": [
                {
                    "ResourceType": "collection",
                    "Resource": [
                        f"collection/{collection_name}",
                    ],
                }
            ],
            "AWSOwnedKey": True,
        }

        return aoss.CfnSecurityPolicy(
            self,
            "EncryptionPolicy",
            name=f"{collection_name}-encryption",
            type="encryption",
            policy=json.dumps(encryption_policy_document),
        )

    def _create_network_policy(self) -> aoss.CfnSecurityPolicy:
        network_policy_document = [
            {
                "Rules": [
                    {
                        "ResourceType": "collection",
                        "Resource": [
                            f"collection/{collection_name}",
                        ],
                    }
                ],
                "AllowFromPublic": True,
            }
        ]

        return aoss.CfnSecurityPolicy(
            self,
            "NetworkPolicy",
            name=f"{collection_name}-network",
            type="network",
            policy=json.dumps(network_policy_document),
        )
