---
id: js-trending-001
domain: [javascript, frontend]
role: [frontend-developer, software-developer]
level: [production]
updated: 2026-09-27
source: [npm, github-trending]
tags: [react, nextjs, vite, bun]
---

# Trending JS Libraries (starter — agent updates daily)

## 1. Frontend frameworks
- React 19 + Next.js 15 (RSC, actions) — default for prod + Vercel AI SDK
- Vue/Nuxt, Svelte/SvelteKit — lighter alternatives

## 2. Build/runtime
- Vite 6, Bun, Turbopack — fast dev/bundle

## 3. State/data
- Zustand/Jotai, TanStack Query/Table, tRPC, Zod

## 4. Prod snippet
```js
// TanStack Query + Zod validation
import { z } from "zod";
const User = z.object({ id: z.string(), name: z.string() });
```

## 5. Agent task
Daily: fetch npm downloads + GitHub stars, write to `_daily/YYYY-MM-DD.md`.
