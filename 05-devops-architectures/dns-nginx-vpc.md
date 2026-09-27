---
id: net-dns-nginx-001
domain: [devops]
role: [devops-engineer, backend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [dns, route53, nginx, vpc, subnet]
---

# DNS Routing + Nginx + VPC/Subnets

## 1. DNS (routing)
Route53 / Azure DNS: `api.app.com Alias -> ALB/FrontDoor`, health checks + failover (primary/secondary), weighted for canary. TTL 60s for API, 3600 static. Private hosted zone `svc.internal` for microservices.

## 2. Nginx (reverse proxy / ingress)
TLS terminate, rate-limit, gzip, cache static, `proxy_pass` to upstream with `keepalive + health_check`.

```nginx
upstream api { server api1:3000 max_fails=3 fail_timeout=30s; server api2:3000; }
server { listen 443 ssl; server_name api.app.com;
  location / { limit_req zone=api burst=50; proxy_pass http://api; proxy_set_header X-Request-ID $request_id; } }
```

Full guide: https://nginx.org/en/docs/http/ngx_http_proxy_module.html

## 3. VPC/Subnets pattern
VPC 10.0.0.0/16: public (ALB/NAT, 10.0.1.0/24 x2 AZ), private-app (ECS/AKS, 10.0.10.0/24), private-data (RDS, 10.0.20.0/24, no internet). NACL stateless + SG stateful least-privilege. Peering/Transit for shared services, PrivateLink/Endpoint for DB (no public IP).

## 4. Arch patterns
Public LB -> private app -> private data; bulkhead per AZ; multi-AZ RDS; S3 VPC endpoint to avoid NAT cost.
