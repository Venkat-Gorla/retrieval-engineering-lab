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

### Next Steps

- Evaluate retrieval quality using overlapping chunks.
- Test retrieval on longer documents.
- Compare different chunk sizes.
- Measure prompt size and token usage.
