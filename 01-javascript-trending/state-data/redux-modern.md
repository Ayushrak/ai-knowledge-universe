---
id: js-redux-modern-001
domain: [javascript, frontend]
role: [frontend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [redux, zustand, jotai]
---

# Redux Modern + Alternatives (2026)

## 1. What / Why
Client-state: Redux Toolkit 2.x is still prod for complex flows. Zustand/Jotai for light.

## 2. Trending
- **Redux Toolkit 2.5 + RTK Query** — https://redux-toolkit.js.org
- **Zustand 5** — https://zustand.docs.pmnd.rs — 3-line store, no provider hell.
- **Jotai / Recoil successor** — atomic state.
- **XState 5** — state machines for checkout/wizard flows.

```ts
import { create } from 'zustand';
export const useCart = create<{items: string[], add:(s:string)=>void}>((set)=>({
  items: [], add: (s)=> set((st)=>({items:[...st.items,s]})),
}));
```

## 3. When to use what
Complex undo/cross-slice -> Redux. Simple -> Zustand. Async server -> TanStack (not Redux).

## 4. Docs links
Add version updates here via daily agent.
