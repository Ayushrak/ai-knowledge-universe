---
id: dotnet-di-http-001
domain: [backend, dotnet]
role: [dotnet-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [di, httpcontext, automapper, mediatr]
---

# .NET — DI, HttpContext, AutoMapper/MediatR, End-to-End

## 1. DI how it works
Container builds graph per lifetime: Singleton (one), Scoped (per-request), Transient (each). Captive dependency = Singleton holding Scoped -> bug.

```csharp
builder.Services.AddScoped<IOrderService, OrderService>();
builder.Services.AddMediatR(c => c.RegisterServicesFromAssemblyContaining<Program>());
```

## 2. HttpContext (how maintained)
`IHttpContextAccessor` gives traceId/user/headers per request. Never store in Singleton field. Use for correlation + multi-tenant `tenantId` header.

```csharp
app.Use((ctx, next) => { using (LogContext.PushProperty("TraceId", ctx.TraceIdentifier)) return next(); });
```

## 3. Why AutoMapper / Mapster (sometimes)
Avoid hand mapping DTO<->Entity (word-for-word boring + drift). Use Mapster (faster) for prod. Keep mapping profile tested.

```csharp
config.NewConfig<Order, OrderDto>().Map(d => d.Total, s => s.Items.Sum(i => i.Price));
```

## 4. Why MediatR + transitions
Thin controllers, testable handlers, pipeline (validation/logging). Order state transitions guarded, not random status set.

## 5. End-to-end structure
`API -> MediatR handler -> domain service (factory/strategy) -> EF + outbox -> worker -> SignalR notify -> Serilog/Seq`. Health `/health`, versioned `/v1/`.

## 6. Interview Q
Scoped DbContext in Singleton? How to get userId in service? AutoMapper perf trap (ProjectTo vs Map)?
