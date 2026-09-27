---
id: aws-50-001
domain: [devops]
role: [devops-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [aws, pipeline]
---

# AWS — 50 Services + End-to-End Use

Compute: EC2, ECS/Fargate (microservices), EKS, Lambda (event jobs), Batch. Storage: S3 (docs lake), EFS, EBS. DB: RDS Postgres+pgvector (RAG), Aurora, DynamoDB (sessions), ElastiCache Redis, Neptune. Network: VPC, Subnets public/private, IGW/NAT, ALB/NLB, Route53 DNS (A/CNAME/Alias+health check), CloudFront, API Gateway, VPC Peering/Transit, PrivateLink, WAF/Shield. Messaging: SQS, SNS, EventBridge, MSK Kafka, Step Functions. DevOps: CodeBuild/CodePipeline, ECR, CloudWatch/OTel, X-Ray, SecretsManager, IAM/KMS, SSM. AI: Bedrock (Claude/Llama), SageMaker, OpenSearch (vector alt). End-to-end: Route53 -> CloudFront -> ALB -> ECS(Fargate private subnet, NAT out) -> RDS(private) + ElastiCache + MSK; S3 events -> Lambda -> SQS -> ECS worker; CI ECR+CodePipeline; logs CloudWatch+X-Ray.

Docs: https://docs.aws.amazon.com
