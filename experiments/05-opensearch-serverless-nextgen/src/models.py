from dataclasses import dataclass


@dataclass
class CollectionInfo:
    name: str
    group_name: str
    status: str
    collection_type: str


@dataclass
class CollectionGroupInfo:
    id: str
    name: str
    generation: str

    min_search_ocu: float
    max_search_ocu: float

    min_indexing_ocu: float
    max_indexing_ocu: float


@dataclass
class RuntimeInfo:
    search_ocu: float
    indexing_ocu: float
