---
id: role-java-001
domain: [backend, java]
role: [java-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [spring-boot, kafka]
---

# Role: Java Developer

## 1. Responsibilities
Spring Boot 3 services, Kafka eventing, resilience + observability.

## 2. Required skills
Java 21 (virtual threads), Spring Boot/WebFlux, JPA/Flyway, Kafka, Resilience4j, Testcontainers, Micrometer+Grafana.

## 3. 90-day roadmap
- Days 0-30: `02-backend-production/java-prod/` — REST + Flyway + Testcontainers.
- Days 30-60: Kafka producer/consumer, exactly-once semantics, schema registry.
- Days 60-90: K8s deploy, HPA, chaos test.

## 4. Interview / Prod checklist
- [ ] Virtual threads pinning pitfalls
- [ ] Consumer rebalance + DLQ
- [ ] Backpressure

## 5. Linked docs
`02-backend-production/java-prod/README.md`
