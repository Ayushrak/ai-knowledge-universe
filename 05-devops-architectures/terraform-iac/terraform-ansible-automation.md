---
id: iac-terraform-ansible-001
domain: [devops]
role: [devops-engineer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [terraform, ansible, iac]
---

# IaC Automation — Terraform + Ansible

## 1. Terraform (provision: VPC, subnets, ALB, ECS/RDS)
Remote state S3 + DynamoDB lock / AzureRM backend. Workspaces `dev/stage/prod`. `plan` in CI, `apply` manual approve prod.

```hcl
module "vpc" { source = "terraform-aws-modules/vpc/aws" version = "~> 5.0"
  name = "hub" cidr = "10.0.0.0/16" azs = ["ap-south-1a","ap-south-1b"]
  public_subnets = ["10.0.1.0/24","10.0.2.0/24"] private_subnets = ["10.0.10.0/24","10.0.11.0/24"] }
```

Docs: https://developer.hashicorp.com/terraform

## 2. Ansible (configure: Nginx, hardening, app deploy on VMs)
Idempotent playbooks: install Nginx template, rotate certs, deploy build. Dynamic inventory from AWS.

```yaml
- hosts: api
  tasks:
    - name: nginx conf
      ansible.builtin.template: { src: nginx.j2, dest: /etc/nginx/conf.d/api.conf }
      notify: reload nginx
```

Rule: Terraform = what exists, Ansible = what's inside. Both in `terraform-iac/` + CI `terraform plan / ansible-lint`.
