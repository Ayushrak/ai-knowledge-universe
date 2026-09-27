---
id: auth-001
domain: [backend, architecture]
role: [backend-developer, dotnet-developer, java-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [jwt, oauth2, entra, keycloak]
---

# Auth — JWT + OAuth2/OIDC (.NET / Java / Node)

## 1. Flow (prod)
Access JWT 5-15min (httpOnly cookie, `SameSite=Lax`) + rotating refresh (DB hashed, reuse detection) + OIDC login (Entra ID/Keycloak) -> `tenantId` claim for multi-tenancy.

## 2. Per-stack
- **.NET**: `AddAuthentication(JwtBearer).AddMicrosoftIdentityWebApi`, `[Authorize(Roles="admin")]`, `IClaimsTransformation` for tenant. https://learn.microsoft.com/entra/identity-platform
- **Java**: `spring-boot-starter-oauth2-resource-server`, `JwtAuthenticationConverter` mapping `realm_access.roles`.
- **Node (NestJS)**: `@nestjs/passport` JwtStrategy + `jwks-rsa`, `@nestjs/throttler` for login brute-force.

```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
  .AddMicrosoftIdentityWebApi(builder.Configuration.GetSection("AzureAd"));
```

## 3. Checklist
- [ ] JWKS cache, `aud/iss` validate, clockSkew 2min
- [ ] Refresh rotate + revoke on logout/breach
- [ ] Scope per API (`orders:write`), not just role
- [ ] Secrets in KeyVault/SecretsManager, never appsettings prod

Docs: https://oauth.net/2 | https://www.keycloak.org/documentation
