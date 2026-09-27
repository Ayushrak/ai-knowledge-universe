---
id: node-micro-001
domain: [backend, javascript]
role: [backend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs, github-trending]
tags: [nestjs, fastify, hono, nextjs-bff]
---

# Node Microservices — Trending Libs + Next.js BFF

## 1. Trending (daily agent tracks)
- **NestJS 11** — DI modules, microservice transports (Kafka/Redis/gRPC). https://nestjs.com
- **Fastify 5** — 60k rps gateway. https://fastify.io
- **Hono + Bun** — edge microservice. https://hono.dev
- **tRPC / ts-rest** — typed contracts, replaces OpenAPI drift.
- **BullMQ + IORedis** — queue/DLQ. **cockatiel** — bulkhead/circuit.

## 2. Pattern
Next.js (BFF: `/app/api/*`, RSC) -> Gateway (Fastify+YARP) -> NestJS services -> Postgres (outbox) -> Kafka -> worker -> Redis cache.

```ts
// NestJS microservice with bulkhead
import { Controller } from '@nestjs/common';
import { MessagePattern } from '@nestjs/microservices';
@Controller() export class PayController {
  @MessagePattern('pay.created') async handle(d: any) { /* idempotent + outbox */ }
}
```

## 3. Next.js as Node lib
Route handlers + Server Actions = BFF validation (Zod) + TanStack prefetch + Vercel AI SDK streaming to LangGraph backend.
