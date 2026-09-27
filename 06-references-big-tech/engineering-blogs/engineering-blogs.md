---
id: ref-blogs-001
domain: [backend, architecture, devops, llm]
role: [software-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [engineering-blogs]
---

# Engineering Blogs (big companies — RSS for daily agent)

- Spotify: https://engineering.atspotify.com — microservices, data
- Netflix: https://netflixtechblog.com — resilience, chaos, encoding
- Uber: https://www.uber.com/blog/engineering — Kafka, maps, scale
- Airbnb: https://medium.com/airbnb-engineering — design systems
- Meta: https://engineering.fb.com — React, Infra
- Google Cloud: https://cloud.google.com/blog/products — Vertex, GKE
- AWS Architecture: https://aws.amazon.com/blogs/architecture
- Azure Architecture: https://learn.microsoft.com/azure/architecture/blog
- LinkedIn: https://www.linkedin.com/blog/engineering — Kafka (they built it)
- Shopify: https://shopify.engineering — Rails/Infra scale
- Slack: https://slack.engineering — realtime

Agent: poll `/feed` or Atom weekly, summarize new arch posts into `_daily/`.
