---
id: devops-iac-001
domain: [devops]
role: [devops-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [terraform, aws, azure, iac]
---

# DevOps — Terraform / IaC / AWS / Azure

## 1. Terraform minimal
```hcl
resource "azurerm_resource_group" "rg" { name="rg-ai-hub" location="centralindia" }
# + openai account, vector db, app service — see terraform-iac/
```

## 2. Architectures
- AWS: ECS + RDS pgvector + Bedrock + S3 docs
- Azure: Container Apps + Postgres Flexible + Azure OpenAI + Blob

## 3. Prod checklist
Remote state, workspaces per env, CI `terraform plan`, secrets in KeyVault/SecretsManager, OTel.

## 4. Linked
`05-devops-architectures/terraform-iac/`, `aws-reference/`, `azure-reference/`
