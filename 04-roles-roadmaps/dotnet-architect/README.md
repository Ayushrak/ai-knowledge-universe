---
id: role-dotnet-arch-001
domain: [backend, dotnet, architecture]
role: [dotnet-architect]
level: [expert]
updated: 2026-09-27
source: [official-docs]
tags: [ddd, cqrs, microservices, azure]
---

# Role: .NET Architect

## 1. Responsibilities
Define microservices / modular monolith, DDD/CQRS, eventing, Azure landing zone, ADR governance.

## 2. Required skills
DDD, CQRS+MediatR, MassTransit / Azure Service Bus, YARP gateway, Bicep/Terraform, APIM, AKS/Container Apps, cost design.

## 3. 90-day roadmap
- Days 0-30: Domain cut, ADR backlog, reference Minimal API template.
- Days 30-60: Event contracts (Avro/JSON schema), saga vs outbox, API versioning.
- Days 60-90: IaC envs, chaos + perf gates, platform docs.

## 4. Interview / Prod checklist
- [ ] Monolith vs microservice tradeoff with team size
- [ ] Outbox + idempotent consumer
- [ ] Multi-region RPO/RTO

## 5. Linked docs
`02-backend-production/dotnet-prod/README.md`, `05-devops-architectures/azure-reference/`
