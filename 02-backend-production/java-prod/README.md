---
id: backend-java-001
domain: [backend, java]
role: [java-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [spring-boot3, kafka, virtual-threads]
---

# Java Prod Deep-Dive (Spring Boot 3)

## 1. Stack
Java 21 virtual threads (`spring.threads.virtual.enabled=true`), Spring Data JPA + Flyway, Kafka + Schema Registry, Resilience4j, Micrometer.

## 2. Snippet
```java
@RestController @RequestMapping("/orders")
class OrderController {
  @PostMapping public ResponseEntity<?> create(@Valid @RequestBody Order o) { /* idempotent save + outbox */ return ResponseEntity.accepted().build(); }
}
```

## 3. Prod checklist
- [ ] Flyway versioned, Testcontainers IT
- [ ] Kafka idempotent producer, DLQ + retry topic
- [ ] Resilience4j bulkhead/rate-limiter, Grafana SLO
