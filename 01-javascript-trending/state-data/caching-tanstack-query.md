---
id: js-cache-tanstack-001
domain: [javascript, frontend]
role: [frontend-developer, software-developer]
level: [production]
updated: 2026-09-27
source: [official-docs, github-trending]
tags: [tanstack-query, caching, react]
---

# Caching — TanStack Query ( + trending alternatives )

## 1. What / Why
Server-state cache: dedupe, background refetch, stale-while-revalidate. Replaces hand-rolled useEffect fetch.

## 2. Libraries (trending — agent updates daily)
- **TanStack Query v5** — default. `staleTime, gcTime, optimistic updates`.
- **SWR 2.3** — Vercel light alternative.
- **RTK Query** — if already on Redux Toolkit.
- **tRPC + Query** — end-to-end types, no REST.

Docs: https://tanstack.com/query/latest | https://swr.vercel.app

## 3. Prod snippet
```tsx
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { z } from 'zod';
const User = z.object({ id: z.string(), name: z.string() });

export function useUsers() {
  return useQuery({
    queryKey: ['users'],
    queryFn: async () => User.array().parse(await fetch('/api/users').then(r => r.json())),
    staleTime: 30_000, gcTime: 5*60_000, retry: 2,
  });
}
// invalidation after mutation:
const qc = useQueryClient();
useMutation({ mutationFn: createUser, onSuccess: () => qc.invalidateQueries({ queryKey: ['users'] }) });
```

## 4. Pitfalls
- `staleTime: 0` default = refetch storms. Set 30s+.
- No Zod validation = runtime break on API change.
- Cache key collision (`['users']` vs `['users', id]`).

## 5. Updates feed
Track in `01-javascript-trending/_daily/` — TanStack v5.66 persistence, SWR 2.3 suspense fixes.
