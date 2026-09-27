---
id: role-devops-001
domain: [devops]
role: [devops-engineer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [terraform, aws, azure, cicd]
---

# Role: DevOps Engineer

## 1. Responsibilities
IaC, CI/CD, env parity, secrets, observability, cost.

## 2. Required skills
Terraform/OpenTofu, GitHub Actions/Azure DevOps, Docker, AWS (ECS/EKS/RDS/S3) + Azure (Container Apps/Postgres/Blob), KeyVault/SecretsManager, Prometheus/OTel.

## 3. 90-day roadmap
- Days 0-30: `05-devops-architectures/terraform-iac/README.md` — remote state, workspaces, plan in CI.
- Days 30-60: Pipeline: lint -> test -> image scan -> plan -> staged apply. Secrets rotation.
- Days 60-90: Autoscale, SLO alerts, FinOps dashboard, DR drill.

## 4. Interview / Prod checklist
- [ ] State lock + drift detection
- [ ] Immutable image + SBOM
- [ ] Zero-downtime deploy

## 5. Linked docs
`05-devops-architectures/**`
