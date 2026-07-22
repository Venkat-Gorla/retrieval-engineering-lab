# OpenSearch Serverless NextGen

## Problem

The previous generation of OpenSearch Serverless maintained baseline compute capacity even when idle, making it impractical for low-duty-cycle development workloads.

This experiment evaluates whether OpenSearch Serverless NextGen successfully addresses this limitation through scale-to-zero compute.

## Objective

Validate that an idle NextGen Vector Search collection:

- scales search compute to zero
- scales indexing compute to zero
- incurs no idle compute charges

## Environment

- Region: ap-south-1
- Collection Type: VECTORSEARCH
- Deployment: NextGen
- Creation Method: Express Create

## Validation Steps

1. Create a NextGen Vector Search collection.
2. Verify the Collection Group configuration.
3. Confirm minimum search and indexing capacity is zero.
4. Verify CloudWatch OCU metrics.
5. Verify AWS Billing after an idle period.

## Results

| Check                                | Status           |
| ------------------------------------ | ---------------- |
| NextGen collection created           | ✅               |
| Collection Group created             | ✅               |
| Minimum Search OCU configured as 0   | ✅               |
| Minimum Indexing OCU configured as 0 | ✅               |
| Search OCU reached 0 during idle     | ✅               |
| Indexing OCU reached 0 during idle   | ✅               |
| Idle compute charges                 | ✅ None observed |

## Conclusion

The experiment confirms that OpenSearch Serverless NextGen supports scale-to-zero compute for idle Vector Search collections. This removes the primary cost concern identified during evaluation of the previous generation and makes the service suitable for subsequent RAG experiments.
