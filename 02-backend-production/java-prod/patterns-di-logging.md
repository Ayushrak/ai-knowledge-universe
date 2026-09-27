---
id: java-patterns-di-001
domain: [backend, java]
role: [java-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [factory, builder, di, mapstruct, logging]
---

# Java Mirror — Patterns, DI, Logging, MapStruct (AutoMapper equiv)

## 1. Factory + Builder with example
```java
interface Payment { void pay(double a); }
class UpiPayment implements Payment { public void pay(double a) {} }
class PaymentFactory { static Payment create(String k){ return switch(k){ case "upi" -> new UpiPayment(); default -> throw new IllegalArgumentException(); }; } }

// Builder (or Lombok @Builder)
class Report { String title; int rows;
  static class Builder { Report r = new Report();
    Builder title(String t){ r.title=t; return this; }
    Builder rows(int n){ r.rows=n; return this; }
    Report build(){ return r; } } }
var r = new Report.Builder().title("Sales").rows(100).build();
```

## 2. DI how it works (Spring)
Container wires `@Component/@Service` graph. Scopes: singleton (default), request, prototype. Constructor injection only (testable). Same captive-dependency trap as .NET.

```java
@Service record OrderService(OrderRepo repo) {}
```

## 3. Logging (Logback/Logstash = Serilog/Seq)
```xml
<!-- logback-spring.xml: JSON + traceId via MDC -->
```
`MDC.put("traceId", ...)` ~ `LogContext`. Ship to ELK/Loki. Template `%X{traceId} %msg`, never string concat in hot path.

## 4. MapStruct = AutoMapper
```java
@Mapper interface OrderMapper { OrderDto toDto(Order o); }
```
Compile-time, fast. Why sometimes: CRUD mapping only, hand-map money paths.

## 5. HttpContext equiv
`RequestContextHolder` / `HandlerInterceptor` for tenantId/traceId. Never store request in singleton field. Pass to `@Async` explicitly.

## 6. End-to-end
`Controller -> Service (factory/strategy) -> JPA + outbox (Debezium) -> Kafka -> WS (STOMP ~ SignalR) -> Micrometer`.

Docs: https://spring.io/projects/spring-boot | https://mapstruct.org | https://refactoring.guru/design-patterns/java
