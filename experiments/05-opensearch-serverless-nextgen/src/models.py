from dataclasses import dataclass


@dataclass
class CollectionInfo:
    name: str
    group_name: str
    status: str
    collection_type: str
