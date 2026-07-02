# Findings

## 2026-06-27

### Paragraph Chunking

- Split a document into paragraph-sized chunks using blank lines.
- Generated embeddings for each chunk using Amazon Titan Text Embeddings V2.

### Retrieval Comparison

Question:

> Which AWS service stores files?

Observations:

- Whole-document retrieval returned the complete document as context.
- Chunk retrieval returned only the paragraph describing Amazon S3.
- For small documents, both approaches identified the correct information.
- Chunk retrieval is expected to provide greater benefits as document size increases.

### Fixed-Size Chunking

Observations:

- Splitting by a fixed character count can divide sentences across chunk boundaries.
- Naive character-based chunking may also split words, reducing readability.
- Preserving word boundaries produces cleaner and more coherent chunks.

### Overlap Chunking

Observations:

- Overlap repeats a portion of text between adjacent chunks.
- Repeated context helps reduce information loss near chunk boundaries.
- Combining overlap with word-boundary preservation increases implementation complexity.

## 2026-07-01

### Chunking Strategy Comparison

Question:

> Which AWS service stores files?

Observations:

- Paragraph chunking produced the highest similarity score in this experiment.
- Each paragraph contained a single topic, resulting in a semantically coherent embedding.
- Fixed-size chunking grouped multiple topics into a single chunk, reducing retrieval precision.
- Overlap chunking preserved additional context near chunk boundaries but also produced chunks containing multiple topics.
- The effectiveness of a chunking strategy depends on the **structure of the source document**.

### Future Exploration

- Test retrieval on longer documents.
- Compare different chunk sizes.
- Measure prompt size and token usage.
- Experiment with sentence-aware chunking.
