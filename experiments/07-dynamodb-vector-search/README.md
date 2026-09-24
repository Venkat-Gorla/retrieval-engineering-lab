# DynamoDB Vector Search

## Problem

This experiment explores whether **Amazon DynamoDB** can provide a practical vector retrieval layer for a semantic-search workload.

## Experiment

The same golden dataset, embedding model, evaluation queries, Top-K configuration, and evaluation framework used in `06-vector-indexing` were reused.

The retrieval backend was changed from:

**Amazon OpenSearch Serverless → Amazon DynamoDB Vector Search**

This allows retrieval quality to be evaluated under the same conditions without introducing a new dataset or evaluation methodology.

## Success Criteria

| Check                                                    | Status |
| -------------------------------------------------------- | ------ |
| Golden dataset indexed into DynamoDB                     | ✅     |
| Retrieval quality evaluated using the existing benchmark | ✅     |
