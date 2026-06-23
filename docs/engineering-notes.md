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

Conclusion:
Interactive response times are suitable for CLI-based AI applications without additional optimization.
