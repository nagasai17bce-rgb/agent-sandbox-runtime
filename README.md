# Agent Sandbox Runtime

## Overview
A reference execution boundary for agent-generated code with runtime and output limits, designed to evolve toward isolated microVM/container execution.

This repository demonstrates a small, inspectable service contract that can run locally without external credentials. It is designed as an engineering starting point: clear API boundaries, isolated domain logic, tests, container packaging, and a path to production infrastructure.

## Architecture
```
Client -> API validation -> Domain service -> Processing boundary -> Structured result
```

## Repository structure
- `app/main.py` — FastAPI application
- `app/service.py` — domain implementation
- `tests/test_api.py` — automated tests
- `examples/request.sh` — runnable example
- `Dockerfile` — container packaging
- `pyproject.toml` — dependency metadata
- `.github/workflows/ci.yml` — CI pipeline

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Then:
```bash
curl http://localhost:8000/health
bash examples/request.sh
pytest -q
```

## API
### GET /health
Returns a simple readiness response.

### POST /v1/run
Request:
```json
{"value":"demo input"}
```

The response uses structured JSON so downstream systems can inspect individual fields and decisions.

## Important security boundary
The local implementation is a reference, not a claim of production isolation. Any system that processes untrusted code, documents, files, or model-generated actions must enforce strong resource and privilege boundaries outside the application process.

## Production architecture
Use isolated containers or microVMs where appropriate, read-only filesystems, resource quotas, network policies, workload identity, object storage, asynchronous queues, durable metadata, audit logs, OpenTelemetry, and centralized security monitoring.

## Reliability
Add deadlines, retries where safe, idempotency, queue backpressure, dead-letter handling, graceful shutdown, health probes, resource exhaustion protection, and SLO-based alerting.

## Testing
Run:
```bash
pytest -q
```

Production test suites should include malformed inputs, large payloads, timeout behavior, resource exhaustion, concurrency, integration contracts, and adversarial security cases.

## Docker
```bash
docker build -t agent-sandbox-runtime .
docker run --rm -p 8000:8000 agent-sandbox-runtime
```

## CI/CD
The repository includes automated tests on pushes and pull requests. Extend CI with static analysis, dependency scanning, image scanning, signed artifacts, integration tests, staging deployment, and smoke tests.

## Design principles
- Explicit limits instead of implicit trust
- Provenance for processed data
- Deterministic domain logic where possible
- Replaceable infrastructure adapters
- Least privilege
- Observable processing stages

## Roadmap
- Durable metadata
- Authentication and tenant isolation
- Async processing
- Real infrastructure adapters
- OpenTelemetry
- Load and security testing
- Infrastructure as code
- Kubernetes or managed-container deployment

## Project-specific design
**Core problem:** A reference execution boundary for agent-generated code with runtime and output limits, designed to evolve toward isolated microVM/container execution.

**Production path:** keep the API and domain contract stable while moving untrusted processing into a separately isolated execution/data plane.