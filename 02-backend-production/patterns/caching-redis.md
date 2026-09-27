---
id: cache-redis-001
domain: [backend]
role: [backend-developer, dotnet-developer, java-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [redis, caching, lock, ratelimit]
---

# Redis Patterns (cache / pub-sub / lock / rate-limit)

## 1. Cache-aside + stampede guard
```csharp
// .NET (StackExchange.Redis)
var v = await db.StringGetAsync(key);
if (v.IsNull) { v = await LoadDb(); await db.StringSetAsync(key, v, TimeSpan.FromMinutes(5)); }
```
Single-flight via `SET key:lock NX PX 5000` or RedLock (RedLock.net / Redisson Java / ioredis Node).

## 2. Uses by stack
- SignalR scale-out: `.AddStackExchangeRedis(backplane)` (.NET) / Socket.IO adapter (Node) / STOMP relay (Java).
- Sessions: `services.AddStackExchangeRedisCache()` / Spring Session Redis / `connect-redis`.
- Rate-limit: `INCR key EX 60` token bucket (or6732 `INCRBY` sliding window via Lua).

## 3. Prod
Cluster 3 masters + replicas, eviction `allkeys-lru`, persistence AOF (cache) / RDB+AOF (jobs via BullMQ). Alert `used_memory >80%`, hit-rate <85%.

Docs: https://redis.io/docs/latest/develop
