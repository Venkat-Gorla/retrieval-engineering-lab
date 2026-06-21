# OpenSearch Serverless - Cost Experiment Notes

Date: 2026-06-20

## Objective

Validate the idle cost of an OpenSearch Serverless VECTORSEARCH collection before using OpenSearch as the retrieval layer for Retrieval Engineering Lab.

## Environment

- Collection Name: retrieval-lab-cost
- Region: ap-south-1 (Mumbai)
- Collection Type: VECTORSEARCH
- Deployment Method: AWS CDK

## Result

- An idle OpenSearch Serverless VECTORSEARCH collection incurred approximately USD 7.42/day in ap-south-1.

## Cost Observations

- Cost Explorer reported SearchOCU and IndexingOCU charges.

## Key Learning

- The collection incurred billable SearchOCU and IndexingOCU charges despite having no indexes, documents, or application traffic.
- The observed behavior differs from my initial interpretation of recent OpenSearch Serverless marketing announcements.

## Open Questions

- What AWS specifically means by "Next Generation OpenSearch Serverless".
- Whether scale-to-zero requires a different deployment model.
- Whether collection groups and NextGen features are available in my region and through CDK.
- Whether OpenSearch remains the best retrieval engine for a personal learning environment.

## Decision

- Delete the collection after documenting findings.
