---
id: testing-auto-001
domain: [devops, backend, frontend]
role: [backend-developer, frontend-developer, devops-engineer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [k6, postman, playwright, load-test]
---

# Testing Automation — k6, Postman/Newman, Playwright, Generators

## 1. Load (k6 — why: JS, CI-friendly)
```js
import http from 'k6/http'; import { check } from 'k6';
export const options = { stages: [{duration:'2m',target:100},{duration:'5m',target:500}], thresholds: { http_req_failed:['rate<0.01'], http_req_duration:['p(95)<500'] } };
export default function(){ const r = http.get('https://api.app.com/health'); check(r,{ok:(x)=>x.status===200}); }
```
Run: `k6 run load.js`. Gate deploy if p95>500ms. Docs: https://k6.io/docs

## 2. API (Postman + Newman auto)
Collection per service + envs. CI: `newman run api.json -e prod.json --reporters cli,junit`. Contract test via OpenAPI import. Auto-generate from Fastify/Swagger (`/docs/json` -> postman).

## 3. E2E (Playwright automation)
```ts
import { test, expect } from '@playwright/test';
test('checkout', async ({ page }) => { await page.goto('/'); await page.getByRole('button',{name:'Buy'}).click(); await expect(page).toHaveURL(/success/); });
```
CI sharded, trace on failure, daily cron vs staging. Docs: https://playwright.dev

## 4. Pipeline order
Unit (Vitest/xUnit) -> contract (Postman) -> E2E (Playwright) -> load (k6 nightly) -> prod canary + auto-rollback on SLO burn.
