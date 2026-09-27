---
id: js-react-next-releases-001
domain: [javascript, frontend]
role: [frontend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs, github-trending]
tags: [react19, nextjs15, hooks]
---

# React + Next Releases — Hooks & What's New

## 1. React 19 (stable)
- Actions + `useActionState`, `useOptimistic` for mutations.
- `use()` — unwrap promise/context in render.
- Server Components (RSC) by default in Next.
- Docs: https://react.dev/blog/2024/12/05/react-19

```tsx
import { useOptimistic, useActionState } from 'react';
const [optimistic, addOptimistic] = useOptimistic(list, (s, n) => [...s, n]);
```

## 2. Next.js 15
- Async `cookies()/headers()`, Partial Prerender, `after()` for background.
- `next/form`, typed routes. Docs: https://nextjs.org/blog/next-15

## 3. New hooks cheat
`useActionState` (form), `useOptimistic` (instant UI), `use` (data), `useTransition` (non-blocking) + `useDeferredValue`.

## 4. Agent task
Daily append new minor (e.g. 19.x, 15.x) + codemod link here + `_daily/`.
