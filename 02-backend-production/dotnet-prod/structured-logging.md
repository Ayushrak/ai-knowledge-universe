---
id: dotnet-logging-001
domain: [backend, dotnet]
role: [dotnet-developer, dotnet-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [serilog, seq, opentelemetry, structured-logging]
---

# .NET Structured Logging (senior focus)

## 1. Why structured (not string concat)
Query by fields: `traceId, userId, elapsedMs`. Word-for-word: use message templates, not interpolation.

```csharp
// GOOD — template preserved
Log.Information("Order {OrderId} created for {UserId} in {ElapsedMs}ms", id, user, ms);
// BAD — breaks Seq search
Log.Information($"Order {id} created");
```

## 2. Libraries
- **Serilog** + Sinks: Console(JSON), Seq, ApplicationInsights, File. https://serilog.net
- **Seq** (local structured viewer, why "Seq": search `ElapsedMs > 500`) — https://datalust.co/seq
- **OpenTelemetry .NET** — traces + logs correlation. https://opentelemetry.io/docs/net/

```csharp
builder.Host.UseSerilog((ctx, c) => c
  .ReadFrom.Configuration(ctx.Configuration)
  .Enrich.FromLogContext().Enrich.WithMachineName()
  .WriteTo.Console(new JsonFormatter())
  .WriteTo.Seq("http://seq:5341")
  .WriteTo.ApplicationInsights(builder.Configuration["APPINSIGHTS"]));
```

## 3. How maintained end-to-end
`traceId (HttpContext.TraceIdentifier)` -> `LogContext.PushProperty` -> Seq/App Insights -> alert if error rate >1%. No `Console.WriteLine` in prod. Log levels: Debug dev only, Information business events, Warning degraded, Error exception + stack.

## 4. Interview Q
- Template vs interpolation? Scope via `BeginScope`? Sampling to cut cost?
