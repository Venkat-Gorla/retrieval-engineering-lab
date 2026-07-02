documents = [
    # Storage
    "Amazon S3 is an object storage service.",
    "Amazon EBS provides persistent block storage for Amazon EC2.",
    "Amazon EFS provides scalable shared file storage.",
    "Amazon FSx provides managed high-performance file systems.",

    # Databases
    "Amazon DynamoDB is a NoSQL database service.",
    "Amazon RDS is a managed relational database service.",
    "Amazon Aurora is a cloud-native relational database.",
    "Amazon ElastiCache provides in-memory caching.",

    # Compute
    "Amazon EC2 provides virtual servers in the cloud.",
    "AWS Lambda runs serverless functions.",
    "Amazon ECS runs containerized applications.",
    "Amazon EKS provides managed Kubernetes clusters.",

    # AI / ML
    "Amazon Bedrock provides access to foundation models.",
    "Amazon SageMaker builds and trains machine learning models.",
    "Amazon Comprehend analyzes natural language text.",
    "Amazon Textract extracts text from documents.",

    # Messaging
    "Amazon SQS provides managed message queues.",
    "Amazon SNS provides publish-subscribe messaging.",
    "Amazon EventBridge routes application events.",
    "Amazon MQ provides managed message brokers.",
]


evaluation_cases = [
    {
        "question": "Which AWS service stores objects?",
        "relevant_documents": [
            "Amazon S3 is an object storage service.",
        ],
    },
    {
        "question": "Which AWS service provides shared file storage?",
        "relevant_documents": [
            "Amazon EFS provides scalable shared file storage.",
        ],
    },
    {
        "question": "Which AWS service provides block storage?",
        "relevant_documents": [
            "Amazon EBS provides persistent block storage for Amazon EC2.",
        ],
    },
    {
        "question": "Which AWS service is a NoSQL database?",
        "relevant_documents": [
            "Amazon DynamoDB is a NoSQL database service.",
        ],
    },
    {
        "question": "Which AWS service runs virtual machines?",
        "relevant_documents": [
            "Amazon EC2 provides virtual servers in the cloud.",
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
    {
        "question": "Which AWS service is used to build machine learning models?",
        "relevant_documents": [
            "Amazon SageMaker builds and trains machine learning models.",
        ],
    },
    {
        "question": "Which AWS service extracts text from documents?",
        "relevant_documents": [
            "Amazon Textract extracts text from documents.",
        ],
    },
    {
        "question": "Which AWS service provides message queues?",
        "relevant_documents": [
            "Amazon SQS provides managed message queues.",
        ],
    },
    {
        "question": "Which AWS services provide storage?",
        "relevant_documents": [
            "Amazon S3 is an object storage service.",
            "Amazon EBS provides persistent block storage for Amazon EC2.",
            "Amazon EFS provides scalable shared file storage.",
            "Amazon FSx provides managed high-performance file systems.",
        ],
    },
]
