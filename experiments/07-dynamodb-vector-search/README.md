```text
DynamoDB table
└── retrieval-lab-ddb-vector-search-documents
    ├── PK: documentId
    └── Vector index
        ├── embedding: 1024 dimensions
        ├── COSINE
        ├── source: INLINE_FILTER
        └── Projection: ALL
```

> The DynamoDB base table is deployed with AWS SAM. The vector index is added separately using the DynamoDB `UpdateTable` API because the required vector-index configuration is not currently supported adequately by the SAM/CloudFormation resource definition.
