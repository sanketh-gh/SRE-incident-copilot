# SRE Incident Copilot

An educational project for learning LLM operations, retrieval-augmented generation (RAG), vector search, AI agents, and OpenTelemetry by building a read-only SRE incident investigation assistant.

## Goal

Given an alert or incident question, the copilot will retrieve relevant runbooks and postmortems, inspect metrics and Kubernetes logs through read-only tools, and return a diagnosis with cited evidence. It is an investigation aid: it will not change infrastructure or execute remediation actions.

## Learning path

Build one working milestone at a time:

1. **API foundation:** FastAPI in Docker Compose, configuration, and draft service-level objectives.
2. **RAG and vector databases:** ingest runbooks and postmortems, embed and index chunks in Qdrant, retrieve relevant passages, and cite sources. Compare retrieval options against a small evaluation set.
3. **LLM operations:** put a model gateway behind a stable interface; record latency, token usage, cost, errors, and model choice; add evaluation and reliability checks.
4. **Agents:** create a bounded tool-using investigation loop, then compare a hand-built loop with LangGraph. Keep tools read-only and require approval for any future action proposals.
5. **Observability:** use OpenTelemetry traces and metrics across API, retrieval, model calls, and tools; inspect them in a local observability stack.
6. **Live incident exercise:** connect read-only Prometheus and Kubernetes tools to a local demo service, induce failures, and evaluate the evidence-backed diagnosis.

Each milestone should be runnable and committed before moving on. See [draft SLOs](docs/SLOs.md).

## Initial technology choices

- **FastAPI and Docker Compose** for the API and local development environment.
- **Ollama behind LiteLLM** to start with a local model while learning a swappable model gateway and usage tracking.
- **Qdrant** for vector search over runbooks and postmortems; add keyword search and reranking only after measuring a baseline.
- **A small Python tool loop, then LangGraph** to learn agent control flow before adopting a framework.
- **MCP** to expose read-only Prometheus, Kubernetes, and runbook search tools through a standard tool interface.
- **OpenTelemetry**, with Phoenix for traces and Prometheus/Grafana for service metrics, to follow each request through retrieval, model calls, and tools.
- **A versioned evaluation set in CI** to measure retrieval and answer quality as the system changes.

## Run the starter API

Requirements: Docker with the Compose plugin.

```sh
cp .env.example .env
docker compose up --build
```

Open <http://localhost:8000/> for the hello response, <http://localhost:8000/health> for the health check, or <http://localhost:8000/docs> for interactive API documentation. Stop with `Ctrl-C`; `docker compose down` removes the container.

## Configuration and secrets

`.env.example` is the committed template. Copy it to `.env` for local overrides; `.env` is ignored by Git and must not contain values you intend to share. Use descriptive variable names such as `API_PORT` and `MODEL_PROVIDER_API_KEY` as integrations are added. Never commit real API keys.

## Planned project layout

```text
services/api/            FastAPI chat and agent endpoints
services/ingest/         document loading, chunking, and embedding
services/mcp-prometheus/ read-only Prometheus tools
services/mcp-k8s/        read-only Kubernetes tools
services/mcp-runbooks/   runbook and postmortem search
evals/                   golden questions and evaluation runner
docs/                    architecture, SLOs, and learning notes
data/                    local source documents (large/private data ignored)
infra/                   deployment configuration, added in a later phase
```

Add each service only when its milestone needs it. Start with small local models and a small document set; measure retrieval and answer quality before expanding scope.
