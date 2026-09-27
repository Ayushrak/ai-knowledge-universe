---
id: micro-patterns-001
domain: [backend, architecture]
role: [backend-developer, dotnet-architect, ai-architect]
level: [expert]
updated: 2026-09-27
source: [official-docs]
tags: [microservices, saga, outbox, bulkhead, cqrs]
---

# Microservices Patterns (agency-grade: .NET / Java / Node)

## 1. Core 12
Gateway (YARP/Kong) -> Auth -> Discovery -> Config -> Saga/Outbox -> CQRS -> Bulkhead ("ball" pattern = bulkhead: isolate thread pools so one slow dep can't sink all) -> Circuit breaker/Retry (Polly/Resilience4j) -> Cache-aside -> Event-carried state -> Strangler -> Sidecar.

## 2. Per-stack
- **.NET**: YARP gateway, MassTransit + outbox, MediatR CQRS, Polly bulkhead `Policy.BulkheadAsync(20, 50)`, HealthChecks.
- **Java**: Spring Cloud Gateway, Debezium outbox, Resilience4j `@Bulkhead(name="pay") + @CircuitBreaker`, Micrometer.
- **Node**: NestJS modules + `@nestjs/terminus`, BullMQ DLQ, `cockatiel` bulkhead/circuit.

```csharp
// .NET bulkhead (the "ball" isolation pattern)
var bulk = Policy.BulkheadAsync<HttpResponseMessage>(maxParallelization: 20, maxQueuingActions: 50);
```

```java
@Bulkhead(name = "pay", type = Bulkhead.Type.SEMAPHORE) @CircuitBreaker(name = "pay")
public Order pay(Order o) { return gateway.charge(o); }
```

## 3. Saga
Choreography (events) for 2-3 steps, Orchestration (Temporal/Camunda) for 5+. Compensate, never 2PC.

Docs: https://microservices.io/patterns | https://learn.microsoft.com/azure/architecture/patterns/bulkhead
