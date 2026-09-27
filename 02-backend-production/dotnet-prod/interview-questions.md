---
id: dotnet-interview-001
domain: [backend, dotnet]
role: [dotnet-developer, dotnet-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [interview]
---

# .NET Senior Interview Questions (with one-line answers)

1. Structured logging template vs interpolation? Template keeps fields queryable in Seq.
2. Serilog vs ILogger? Serilog enrich + sinks, plug into MEL.
3. Seq why? Local structured search `ElapsedMs > 500`, no Azure cost.
4. SignalR scale? Azure SignalR Service, no sticky session.
5. Factory vs Builder? Factory chooses type, Builder assembles step-by-step.
6. DI lifetimes? Singleton/Scoped/Transient; no Scoped in Singleton.
7. HttpContext in background? Pass ids explicitly, accessor is request-scoped.
8. AutoMapper when? CRUD DTOs yes, hot path ProjectTo/Mapster.
9. Outbox why? Atomic DB + event, no lost message.
10. Graceful shutdown? `CancellationToken` + 30s drain.
