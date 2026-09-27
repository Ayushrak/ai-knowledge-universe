---
id: backend-prod-001
domain: [backend]
role: [backend-developer, dotnet-developer, java-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [node, dotnet, spring, prod]
---

# Backend in Production — Master Checklist

## 1. Cross-cutting
Auth (JWT short + refresh rotate / OAuth2 / Entra ID), TLS, CORS strict, rate-limit (Redis token bucket), idempotency-key, pagination (cursor), ProblemDetails/RFC7807.

## 2. Data
Pool sizing = (2*cpu)+spindle, statement timeout 5s, migrations backward-compatible, outbox for events, Redis cache-aside with TTL + stampede guard.

## 3. Reliability
Health `/health` + readiness, graceful shutdown 30s, retry with jitter + circuit breaker, DLQ, chaos test.

## 4. Observability
JSON logs (traceId), OTel traces, RED/USE metrics, SLO p95/p99, alerts on burn rate.

## 5. Per-stack
- Node: `02-backend-production/node-prod/README.md`
- .NET: `02-backend-production/dotnet-prod/README.md`
- Java: `02-backend-production/java-prod/README.md`
