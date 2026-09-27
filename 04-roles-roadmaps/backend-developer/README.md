---
id: role-backend-001
domain: [backend]
role: [backend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [node, api, postgres, redis]
---

# Role: Backend Developer (Node)

## 1. Responsibilities
Design APIs, queues, caching, observability, prod hardening.

## 2. Required skills
Node 20 / Express / Fastify / NestJS, Postgres pooling, Redis, BullMQ, Docker, OTel, JWT/OAuth2.

## 3. 90-day roadmap
- Days 0-30: `02-backend-production/node-prod/` + patterns checklist. CRUD + auth + tests.
- Days 30-60: Queues, idempotency, rate-limit, OpenAPI.
- Days 60-90: K8s/ECS deploy, autoscale, SLOs.

## 4. Interview / Prod checklist
- [ ] Pool sizing, N+1, migration rollback
- [ ] Exactly-once vs at-least-once
- [ ] p99 + error budget

## 5. Linked docs
`02-backend-production/node-prod/README.md`, `02-backend-production/patterns/production-checklist.md`
