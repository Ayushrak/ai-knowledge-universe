---
id: dotnet-signalr-001
domain: [backend, dotnet]
role: [dotnet-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [signalr, websocket, realtime]
---

# .NET Real-time — SignalR

## 1. Why SignalR
WebSocket + fallback (SSE/long-poll), groups, scale-out via Redis/Azure SignalR Service.

```csharp
var b = WebApplication.CreateBuilder(args);
b.Services.AddSignalR();
b.Services.AddSingleton<IUserIdProvider, SubProvider>();
var app = b.Build();
app.MapHub<ChatHub>("/hubs/chat");

class ChatHub : Hub {
  public async Task Send(string msg) =>
    await Clients.Group(Context.UserIdentifier!).SendAsync("rx", new { user = Context.UserIdentifier, msg, at = DateTime.UtcNow });
}
```

```ts
// React client
import * as signalR from '@microsoft/signalr';
const c = new signalR.HubConnectionBuilder().withUrl('/hubs/chat').withAutomaticReconnect().build();
await c.start(); c.on('rx', m => console.log(m));
```

Docs: https://learn.microsoft.com/aspnet/core/signalr/introduction
Prod: sticky sessions NOT needed with Azure SignalR Service, use `UserIdentifier`, authorize hub, backpressure via Channels.
