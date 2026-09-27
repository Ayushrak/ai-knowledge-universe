---
id: azure-50-001
domain: [devops]
role: [devops-engineer, dotnet-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [azure, pipeline]
---

# Azure — 50 Services + End-to-End Use

Compute: App Service, Container Apps (microservices), AKS, Functions, Batch. Storage: Blob (docs), Files, Disks. DB: Postgres Flexible+pgvector, SQL DB, CosmosDB, Redis Cache. Network: VNet, Subnets/NSG, App Gateway/WAF, Front Door (global routing ~ Route53+CloudFront), Azure DNS (A/CNAME/Alias), Private Endpoint/Link, VNet Peering, VPN/ExpressRoute, Load Balancer, NAT Gateway. Messaging: Service Bus (outbox consumer), Event Grid/Hubs, Queue Storage. DevOps: DevOps Pipelines/GitHub Actions, ACR, Monitor/App Insights, KeyVault, Entra ID/RBAC, Policy. AI: Azure OpenAI, AI Search (vector), Document Intelligence. End-to-end: Azure DNS -> Front Door -> App Gateway -> Container Apps (private VNet, NAT) -> Postgres(private endpoint) + Redis + Service Bus; Blob event -> Function -> queue -> worker; CI ACR+pipeline; logs App Insights.

Docs: https://learn.microsoft.com/azure
