---
id: backend-node-001
domain: [backend]
role: [backend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [node, fastify, postgres]
---

# Node Prod Deep-Dive

## 1. Scaffold
Fastify + `pg` pool (max 20) + Redis + pino + helmet + rate-limit.

```js
import Fastify from 'fastify';
const app = Fastify({ logger: true });
app.get('/health', async () => ({ ok: true }));
```

## 2. Prod checklist
- [ ] Pool timeout, graceful shutdown
- [ ] BullMQ DLQ, idempotency-key header
- [ ] OTel -> Tempo/Jaeger, /metrics
- [ ] Dockerfile non-root, `npm ci --omit=dev`
