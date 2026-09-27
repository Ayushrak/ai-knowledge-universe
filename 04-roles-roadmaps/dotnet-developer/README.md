---
id: role-dotnet-dev-001
domain: [backend, dotnet]
role: [dotnet-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [dotnet, efcore, minimal-api]
---

# Role: Backend .NET Developer

## 1. Responsibilities
Build .NET 8/9 Minimal APIs, EF Core, background workers, Azure deploy.

## 2. Required skills
C# 12, ASP.NET Core, EF Core + migrations, MediatR, FluentValidation, Serilog, xUnit, Redis, Azure SDK.

## 3. 90-day roadmap
- Days 0-30: `02-backend-production/dotnet-prod/` — Minimal API + EF + health checks.
- Days 30-60: Auth (Entra ID), ServiceBus/Kafka, Polly resilience.
- Days 60-90: Container Apps/AKS, App Insights, load test (k6).

## 4. Interview / Prod checklist
- [ ] Async / DbContext lifetime
- [ ] Migration zero-downtime
- [ ] ProblemDetails + validation

## 5. Linked docs
`02-backend-production/dotnet-prod/README.md`
