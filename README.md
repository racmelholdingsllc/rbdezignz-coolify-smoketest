# RBDEZIGNZ Coolify smoke test

Minimal credential-free static website for an unpublished, internal-only staging integration test.

Runtime: Python standard-library HTTP server, nonroot UID/GID 10001, internal port 8080. No runtime external services, API keys, packages, forms, analytics, or environment variables are required. Building requires access to the public Python base image registry.

Routes: `/` is the smoke-test page; `/health` returns HTTP 200 with `ok` and a trailing newline. The Dockerfile includes a health check.

Tests: `python3 -m unittest discover -s tests -v`.

Local preview: `python3 -m http.server 8080 --bind 127.0.0.1 --directory site`.

Staging: use the Dockerfile build pack and internal port 8080. Do not assign a domain or published host port. Public source code does not authorize public application publication. The noindex metadata is not access control. This server is for a minimal smoke test, not production use.
