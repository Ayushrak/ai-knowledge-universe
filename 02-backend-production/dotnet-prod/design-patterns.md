---
id: dotnet-patterns-001
domain: [backend, dotnet, architecture]
role: [dotnet-developer, dotnet-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [factory, builder, strategy, mediatr]
---

# .NET Design Patterns — Factory + Builder (+ system design)

## 1. Factory (why: swap provider without if-else)
```csharp
interface IPayment { Task Pay(decimal a); }
class UpiPayment : IPayment { public Task Pay(decimal a) => Task.CompletedTask; }
static class PaymentFactory {
  public static IPayment Create(string kind) => kind switch { "upi" => new UpiPayment(), _ => throw new ArgumentOutOfRangeException() };
}
```

## 2. Builder (why: complex object, readable)
```csharp
class ReportBuilder {
  private readonly Report _r = new();
  public ReportBuilder WithTitle(string t) { _r.Title = t; return this; }
  public ReportBuilder WithRows(int n) { _r.Rows = n; return this; }
  public Report Build() => _r;
}
var r = new ReportBuilder().WithTitle("Sales").WithRows(100).Build();
```

## 3. System-design combo
Controller -> MediatR handler (CQRS) -> Strategy/Factory -> EF/outbox. Transitions: state machine for Order (Pending->Paid->Shipped) via Stateless lib.

Docs: https://refactoring.guru/design-patterns/csharp
