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

### Next Steps

- Compare different chunk sizes.
- Add chunk overlap.
- Test retrieval on longer documents.
- Measure prompt size and token usage.
