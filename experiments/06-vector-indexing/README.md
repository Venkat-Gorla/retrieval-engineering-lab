# Vector Indexing

## Problem

Large language models require a retrieval layer to answer questions using private or domain-specific knowledge. Building that retrieval layer involves more than storing documents—it requires designing an effective vector index that supports accurate, scalable semantic search.

This experiment explores the core concepts of vector indexing using **Amazon OpenSearch Serverless**.

## Goal

Develop a production-oriented understanding of vector indexing through:

- Index schema design
- Metadata modeling
- Vector similarity search
- Retrieval quality evaluation

## Success Criteria

This experiment builds on the validated OpenSearch Serverless NextGen environment established in **05-opensearch-serverless-nextgen**.

| Check                                                              | Status |
| ------------------------------------------------------------------ | ------ |
| Retrieval pipeline implemented using OpenSearch Serverless NextGen | ✅     |
| Retrieval quality evaluated using a benchmark dataset              | ✅     |

## Key Learnings

- Stable document identifiers simplify retrieval evaluation across backends.
- OpenSearch Serverless NextGen scales to zero but introduces observable cold-start latency after idle periods.
- A reusable evaluation dataset makes retrieval quality measurable rather than anecdotal.

## Tech Stack

| Component           | Technology                             |
| ------------------- | -------------------------------------- |
| **Language**        | Python                                 |
| **LLM Platform**    | Amazon Bedrock                         |
| **Embedding Model** | Amazon Titan Embeddings                |
| **Vector Database** | Amazon OpenSearch Serverless (NextGen) |
