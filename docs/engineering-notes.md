# Engineering Notes

## OpenSearch Serverless

### Collection Creation Time

- VECTORSEARCH collection creation took approximately 4 minutes in ap-south-1.

### Security Policy Naming Limits

- Security policy names have a maximum length of 32 characters.
- Long project prefixes can exceed the limit.

### CDK Diff Observation

- Adding tags to an existing OpenSearch Serverless collection triggered resource replacement.
- Always review `cdk diff` output before deployment.

### CDK / Windows

- Observed intermittent jsii temporary directory cleanup warnings on Windows.
- Did not impact synth, diff, or deploy operations.

## 2026-06-23

Measured end-to-end Bedrock Nova Lite invocation latency from local workstation in ap-south-1.

Observed latency: ~0.96 seconds

**Conclusion:**
Interactive response times are suitable for CLI-based AI applications without additional optimization.

## 2026-06-23

Validated semantic similarity using Titan Text Embeddings V2.

**Results:**

Similarity(
"DynamoDB is a NoSQL database",
"DynamoDB stores key-value data"
) = 0.8513

Similarity(
"DynamoDB is a NoSQL database",
"Pizza is a popular Italian food"
) = 0.0747

**Conclusion:**

Embedding vectors preserve semantic meaning.
Cosine similarity can distinguish related and unrelated concepts, forming the basis of retrieval systems and vector search.

## 2026-06-24

Implemented a minimal Retrieval-Augmented Generation (RAG) pipeline.

**Flow:**

1. Generate embeddings for documents.
2. Store document embeddings in an in-memory index.
3. Generate an embedding for the user question.
4. Rank documents using cosine similarity.
5. Retrieve the highest-scoring document.
6. Provide retrieved context to Amazon Nova Lite.
7. Generate an answer constrained to the retrieved context.

**Observation:**

The model answered using the retrieved document rather than relying solely on foundation model knowledge.

**Conclusion:**

Validated the core RAG architecture without introducing a vector database.
