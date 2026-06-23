# Bedrock RAG Baseline

## Problem

Modern AI applications often need access to private or domain-specific knowledge that is not part of a foundation model's training data. A Retrieval-Augmented Generation (RAG) pipeline addresses this by retrieving relevant context and supplying it to the model at runtime.

## Goal

Build a minimal end-to-end RAG implementation using Amazon Bedrock and a local document corpus.

The experiment will focus on understanding the core RAG workflow:

1. Document ingestion
2. Text chunking
3. Embedding generation
4. Similarity search
5. Context retrieval
6. LLM response generation

## Expected Outcome

- Working RAG pipeline implemented in Python.
- Local document corpus used as the knowledge source.
- Amazon Bedrock used for embeddings and text generation.
- No vector database or agent framework required.
- Clear understanding of the retrieval lifecycle before introducing additional infrastructure such as OpenSearch.

## Success Criteria

- User can ask questions about the document corpus.
- Relevant document chunks are retrieved.
- Retrieved context is included in the prompt.
- Generated answers are grounded in the retrieved content.
- End-to-end workflow can be demonstrated from the command line.
