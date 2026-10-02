# Agent Sandbox Runtime

A minimal execution boundary for agent-generated Python snippets with input and runtime limits.

> This is a reference implementation, not a production security boundary. Arbitrary code execution must run inside an isolated container/VM with a hardened syscall, network, filesystem, and resource policy.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Production extensions
Use disposable containers or microVMs, seccomp/AppArmor, network isolation, read-only filesystems, CPU/memory quotas, process limits, artifact scanning, and per-tenant policies.
