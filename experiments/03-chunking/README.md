# 03 - Chunking

## Problem

Large documents often contain both relevant and irrelevant information. Sending an entire document to a large language model increases token usage and may reduce answer quality.

## Goal

Understand common document chunking strategies and evaluate their effect on semantic retrieval in a Retrieval-Augmented Generation (RAG) pipeline.

## Experiments

- Paragraph-based chunking
- Fixed-size chunking (word-aware)
- Overlapping chunking
- Retrieval comparison across chunking strategies

## Result

Implemented and compared paragraph, fixed-size, and overlapping chunking strategies, and evaluated their impact on retrieval.

## Key Takeaways

- Chunking is a critical step in a RAG pipeline.
- Different chunking strategies produce different embeddings and retrieval results.
- Well-structured chunks generally produce more coherent semantic representations.
- Overlap preserves context across chunk boundaries but introduces duplicated content.
