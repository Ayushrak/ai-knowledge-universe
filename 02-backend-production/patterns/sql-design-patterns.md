---
id: sql-patterns-001
domain: [backend, architecture]
role: [backend-developer, dotnet-developer, java-developer, dotnet-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [sql, postgres, indexing, outbox]
---

# SQL Design Patterns (big-agency prod)

## 1. Schema
- Surrogate UUIDv7 PK + natural unique key. `created_at timestamptz default now()`.
- Soft-delete only for audit tables; else hard delete + archive.
- Migrations: expand-migrate-contract (add nullable -> backfill -> not null).

## 2. Indexing
- B-tree for equality/range, GIN for JSONB/tags, BRIN for time-series, pg_trgm for search.
- Covering index `INCLUDE (name)` to avoid heap fetch. Check `EXPLAIN (ANALYZE, BUFFERS)`.

## 3. Patterns
- **Outbox**: `outbox(id, aggregate, event, payload, published)` written in same txn, relay to Kafka/ServiceBus.
- **Inbox + idempotency_key UNIQUE** — exactly-once consumer.
- **Queue table**: `SELECT ... FOR UPDATE SKIP LOCKED` for jobs (or use BullMQ/Kafka).
- **Partitioning**: monthly `orders_2026_09` by range, retention drop.
- **CQRS read model**: materialized view `REFRESH CONCURRENTLY` for dashboards.

```sql
CREATE TABLE outbox (id uuid PRIMARY KEY, agg text, event text, payload jsonb, published bool DEFAULT false);
CREATE UNIQUE INDEX ux_orders_idem ON orders(idempotency_key);
```

Docs: https://www.postgresql.org/docs/current/indexes.html
