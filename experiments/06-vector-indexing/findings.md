# Findings

- **2026-07-13** – Verified that creating a vector index on an OpenSearch Serverless NextGen collection did not leave Search or Index OCUs allocated after the collection became idle (Search OCU = 0.0, Index OCU = 0.0).

- **2026-07-13** – OpenSearch Serverless does not support the `refresh=true` indexing policy. Documents become searchable through the service-managed refresh mechanism.

- **2026-07-13** – The first document indexing request timed out with the default 10-second client timeout while Index OCU increased from 0.0. Increasing the OpenSearch client timeout to 30 seconds allowed the indexing request to complete successfully.
