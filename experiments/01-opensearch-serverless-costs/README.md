# OpenSearch Serverless Cost Study

## Objective

Validate the real-world cost characteristics of Amazon OpenSearch Serverless in a personal AWS account.

This experiment focuses on understanding:

- Idle cost behavior
- Scale-to-zero claims
- Storage-related charges
- Operational considerations for small workloads

## Scope

- Deploy a minimal OpenSearch Serverless collection using IaC
- Observe costs over multiple days with little or no activity
- Record findings and compare them against AWS expectations

## Expected Outcome

A documented understanding of the baseline cost profile of OpenSearch Serverless, helping inform architecture and technology decisions for future experiments in this lab.

## Finding

A standard OpenSearch Serverless VECTORSEARCH collection in ap-south-1 incurred approximately $12.36/day while idle.

This deployment did not use NextGen collection groups and therefore did not qualify for scale-to-zero behavior.
