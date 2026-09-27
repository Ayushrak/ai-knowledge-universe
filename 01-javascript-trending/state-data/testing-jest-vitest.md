---
id: js-testing-jest-001
domain: [javascript, frontend]
role: [frontend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [jest, vitest, testing]
---

# Testing — Jest / Vitest / RTL

## 1. Trending
- **Vitest 3** — Vite-native, replaces Jest for new projects. https://vitest.dev
- **Jest 30** — still dominant in CRA/Next legacy.
- **React Testing Library + Playwright** — unit + E2E combo.

```ts
// vitest example
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
describe('User', ()=>{ it('renders', ()=>{ render(<div>hi</div>); expect(screen.getByText('hi')).toBeTruthy(); }); });
```

## 2. Prod rule
Unit (Vitest) for logic/hooks, Playwright for critical flows, MSW for API mock. 70% coverage on utils, 100% on money paths.
