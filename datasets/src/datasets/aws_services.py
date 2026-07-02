documents = [
    "Amazon S3 is an object storage service.",
    "Amazon DynamoDB is a NoSQL database service.",
    "AWS Lambda runs serverless functions.",
    "Amazon Bedrock provides access to foundation models.",
]

evaluation_cases = [
    {
        "question": "Which AWS service stores files?",
        "relevant_documents": [
            "Amazon S3 is an object storage service.",
        ],
    },
    {
        "question": "Which AWS service is a NoSQL database?",
        "relevant_documents": [
            "Amazon DynamoDB is a NoSQL database service.",
        ],
    },
    {
        "question": "Which AWS service runs serverless functions?",
        "relevant_documents": [
            "AWS Lambda runs serverless functions.",
        ],
    },
    {
        "question": "Which AWS service provides foundation models?",
        "relevant_documents": [
            "Amazon Bedrock provides access to foundation models.",
        ],
    },
]
