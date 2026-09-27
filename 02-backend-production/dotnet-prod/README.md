---
id: backend-dotnet-001
domain: [backend, dotnet]
role: [dotnet-developer, dotnet-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [dotnet8, minimal-api, efcore]
---

# .NET Prod Deep-Dive (.NET 8/9)

## 1. Minimal API template
```csharp
var b = WebApplication.CreateBuilder(args);
b.Services.AddDbContext<AppDb>(o => o.UseNpgsql(b.Configuration.GetConnectionString("db")));
b.Services.AddHealthChecks().AddNpgSql(b.Configuration.GetConnectionString("db")!);
var app = b.Build();
app.MapHealthChecks("/health");
app.MapGet("/users", async (AppDb db) => await db.Users.AsNoTracking().ToListAsync());
app.Run();
```

## 2. Prod checklist
- [ ] EF migrations in CI, backward-compatible
- [ ] Serilog JSON + App Insights, ProblemDetails
- [ ] Polly retry/circuit for HTTP, outbox for events
- [ ] Multi-stage Dockerfile, AOT where hot path
