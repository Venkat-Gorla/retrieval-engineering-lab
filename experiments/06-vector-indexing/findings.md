# Findings

- **2026-07-13** – Verified that creating a vector index on an OpenSearch Serverless NextGen collection did **not** leave Search or Index OCUs allocated after the collection became idle (Search OCU = 0.0, Index OCU = 0.0).

- **2026-07-13** – OpenSearch Serverless does not support the `refresh=true` indexing policy. Documents become searchable through the service-managed refresh mechanism.

- **2026-07-13** – The first document indexing request timed out with the default 10-second client timeout while Index OCU increased from 0.0. Increasing the OpenSearch client timeout to 30 seconds allowed the indexing request to complete successfully.

- **2026-07-13** – After approximately 20 minutes of inactivity, runtime Search OCU and Index OCU both returned to 0.0 on the test OpenSearch Serverless NextGen collection, consistent with scale-to-zero behavior for idle search and indexing compute.

- **2026-07-13** – The first vector search after the collection had been idle (runtime Search OCU observed at 0.0 before the request) completed significantly slower than subsequent searches (observed: 16.69 s vs. 0.52–1.17 s). The observed latency is consistent with search compute being provisioned after the collection had scaled to zero.
  - This observation is based on the experimental workload and is **not** intended as a general performance characterization.

- **2026-07-14** – Retrieval quality using Amazon OpenSearch Serverless matched the in-memory vector retrieval baseline for the evaluation dataset. Both implementations achieved **100% Accuracy@1**, indicating that the indexed vector search produced rankings consistent with the reference implementation for the evaluated queries.
