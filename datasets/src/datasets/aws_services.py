documents = [
    # Storage
    {
        "id": "s3",
        "text": "Amazon S3 is an object storage service.",
    },
    {
        "id": "ebs",
        "text": "Amazon EBS provides persistent block storage for Amazon EC2.",
    },
    {
        "id": "efs",
        "text": "Amazon EFS provides scalable shared file storage.",
    },
    {
        "id": "fsx",
        "text": "Amazon FSx provides managed high-performance file systems.",
    },

    # Databases
    {
        "id": "dynamodb",
        "text": "Amazon DynamoDB is a NoSQL database service.",
    },
    {
        "id": "rds",
        "text": "Amazon RDS is a managed relational database service.",
    },
    {
        "id": "aurora",
        "text": "Amazon Aurora is a cloud-native relational database.",
    },
    {
        "id": "elasticache",
        "text": "Amazon ElastiCache provides in-memory caching.",
    },

    # Compute
    {
        "id": "ec2",
        "text": "Amazon EC2 provides virtual servers in the cloud.",
    },
    {
        "id": "lambda",
        "text": "AWS Lambda runs serverless functions.",
    },
    {
        "id": "ecs",
        "text": "Amazon ECS runs containerized applications.",
    },
    {
        "id": "eks",
        "text": "Amazon EKS provides managed Kubernetes clusters.",
    },

    # AI / ML
    {
        "id": "bedrock",
        "text": "Amazon Bedrock provides access to foundation models.",
    },
    {
        "id": "sagemaker",
        "text": "Amazon SageMaker builds and trains machine learning models.",
    },
    {
        "id": "comprehend",
        "text": "Amazon Comprehend analyzes natural language text.",
    },
    {
        "id": "textract",
        "text": "Amazon Textract extracts text from documents.",
    },

    # Messaging
    {
        "id": "sqs",
        "text": "Amazon SQS provides managed message queues.",
    },
    {
        "id": "sns",
        "text": "Amazon SNS provides publish-subscribe messaging.",
    },
    {
        "id": "eventbridge",
        "text": "Amazon EventBridge routes application events.",
    },
    {
        "id": "mq",
        "text": "Amazon MQ provides managed message brokers.",
    },
]


DOCUMENTS_BY_ID = {
    document["id"]: document
    for document in documents
}


evaluation_cases = [
    {
        "question": "Which AWS service stores objects?",
        "expected_ids": ["s3"],
        "relevant_documents": [
            "Amazon S3 is an object storage service.",
        ],
    },
    {
        "question": "Which AWS service provides shared file storage?",
        "expected_ids": ["efs"],
        "relevant_documents": [
            "Amazon EFS provides scalable shared file storage.",
        ],
    },
    {
        "question": "Which AWS service provides block storage?",
        "expected_ids": ["ebs"],
        "relevant_documents": [
            "Amazon EBS provides persistent block storage for Amazon EC2.",
        ],
    },
    {
        "question": "Which AWS service is a NoSQL database?",
        "expected_ids": ["dynamodb"],
        "relevant_documents": [
            "Amazon DynamoDB is a NoSQL database service.",
        ],
    },
    {
        "question": "Which AWS service runs virtual machines?",
        "expected_ids": ["ec2"],
        "relevant_documents": [
            "Amazon EC2 provides virtual servers in the cloud.",
        ],
    },
    {
        "question": "Which AWS service runs serverless functions?",
        "expected_ids": ["lambda"],
        "relevant_documents": [
            "AWS Lambda runs serverless functions.",
        ],
    },
    {
        "question": "Which AWS service provides foundation models?",
        "expected_ids": ["bedrock"],
        "relevant_documents": [
            "Amazon Bedrock provides access to foundation models.",
        ],
    },
    {
        "question": "Which AWS service is used to build machine learning models?",
        "expected_ids": ["sagemaker"],
        "relevant_documents": [
            "Amazon SageMaker builds and trains machine learning models.",
        ],
    },
    {
        "question": "Which AWS service extracts text from documents?",
        "expected_ids": ["textract"],
        "relevant_documents": [
            "Amazon Textract extracts text from documents.",
        ],
    },
    {
        "question": "Which AWS service provides message queues?",
        "expected_ids": ["sqs"],
        "relevant_documents": [
            "Amazon SQS provides managed message queues.",
        ],
    },
    {
        "question": "Which AWS services provide storage?",
        "expected_ids": [
            "s3",
            "ebs",
            "efs",
            "fsx",
        ],
        "relevant_documents": [
            "Amazon S3 is an object storage service.",
            "Amazon EBS provides persistent block storage for Amazon EC2.",
            "Amazon EFS provides scalable shared file storage.",
            "Amazon FSx provides managed high-performance file systems.",
        ],
    },
]
