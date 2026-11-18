# S3 Vector Search

## Experiment

The same golden dataset, embedding model, evaluation queries, Top-K configuration, and evaluation framework used in `06-vector-indexing` were reused.

The retrieval backend was changed from:

**Amazon OpenSearch Serverless → Amazon S3 Vector Search**

## Success Criteria

| Check                                                    | Status |
| -------------------------------------------------------- | ------ |
| Golden dataset indexed into S3                           | ✅     |
| Retrieval quality evaluated using the existing benchmark | ✅     |
