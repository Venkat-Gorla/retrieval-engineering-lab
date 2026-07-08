# Vector Indexing

## Problem

Large language models require a retrieval layer to answer questions using private or domain-specific knowledge. Building that retrieval layer involves more than storing documents—it requires designing an effective vector index that supports accurate, scalable semantic search.

This experiment explores the core building blocks of vector indexing using Amazon OpenSearch Serverless.

## Goal

Build a production-oriented understanding of vector indexing by implementing and evaluating:

- Index schema design
- Embedding generation
- Document indexing
- Metadata modeling
- Vector similarity search
- Retrieval quality

The emphasis is on understanding the design decisions behind a Retrieval-Augmented Generation (RAG) pipeline rather than simply integrating managed services.

## Expected Outcome

By the end of this experiment, the repository will demonstrate:

- A well-defined vector index schema
- Document ingestion and embedding generation
- Indexed documents with searchable metadata
- Semantic search using vector similarity
- Design rationale and engineering trade-offs for each major decision

## Technology Stack

- Python
- Amazon Bedrock
- Amazon Titan Embeddings
- Amazon OpenSearch Serverless (NextGen)

## Success Criteria

- Create and configure a vector index
- Generate embeddings for sample documents
- Index documents and associated metadata
- Execute semantic similarity searches
- Retrieve relevant documents for representative queries
- Document key architectural decisions and lessons learned

## Notes

This experiment builds on the validated OpenSearch Serverless NextGen environment established in **05-opensearch-serverless-nextgen**. The focus now shifts from infrastructure validation to designing and implementing the retrieval layer of a production-oriented RAG system.
