---
id: msg-kafka-001
domain: [backend, architecture]
role: [backend-developer, dotnet-developer, java-developer, dotnet-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [kafka, outbox, saga, idempotency]
---

# Kafka Deep-Dive (.NET / Java / Node)

## 1. Core
Topics + partitions (parallelism) + consumer groups (scale) + offsets (resume). Retention 7d, replication 3. Key = ordering unit (orderId). Schema Registry (Avro/JSON schema) prevents breaking changes.

## 2. Outbox relay (no lost msg)
DB `outbox` (same txn) -> relay worker polls `WHERE published=false FOR UPDATE SKIP LOCKED` -> Kafka `orders.created` (key=orderId, header idempotency_key) -> consumer inbox dedupe.

## 3. Per-stack
- **.NET (MassTransit)**: `AddConsumer<OrderConsumer>().Endpoint(e => e.Name="orders")`, retry + DLQ, `UseMessageRetry(r=>r.Interval(3,5s))`. https://masstransit.io
- **Java (Spring Kafka)**: `@KafkaListener(topics="orders.created", groupId="billing")`, `AckMode.MANUAL`, `SeekToCurrentErrorHandler` + DLQ topic, idempotent producer `enable.idempotence=true`.
- **Node (NestJS)**: `ClientsModule.register([{name:'KAFKA', transport:Transport.KAFKA, options:{client:{brokers:['kafka:9092']}, consumer:{groupId:'api'}}}])`, `@MessagePattern('orders.created')`.

```java
@KafkaListener(topics="orders.created") public void on(Order e, Acknowledgment a){ if(processed(e.idem())){a.acknowledge(); return;} handle(e); a.acknowledge(); }
```

## 4. Prod checklist
- [ ] 3 brokers min, `min.insync.replicas=2`
- [ ] Consumer lag alert (>10k), DLQ + replay runbook
- [ ] Compaction for state topics, delete for events
- [ ] Chaos: kill broker, rebalance safe

Docs: https://kafka.apache.org/documentation | https://docs.confluent.io
