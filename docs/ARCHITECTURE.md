# Architectural Notes

Internal notes on the Intent-Action Service architecture.

## Core Design Principles

1. **Separation of Concerns**
   - CUBE: Declarative resource model (Collection+JSON)
   - IAS: Procedural intent orchestration
   - Clients: Presentation and user interaction

2. **Evolutionary Independence**
   - CUBE evolves its semantic model independently
   - IAS evolves its workflow implementations independently
   - Clients evolve their UX independently

3. **Security by Design**
   - Credential brokering via authCore
   - No credential distribution to services
   - Defense in depth

## Three Architectural Paths Analyzed

### Path 1: Status Quo (Do Nothing)
- Intent translator embedded in ChRIS UI
- Fragmented client ecosystem
- Technical debt accumulation
- **Verdict:** Unacceptable long-term

### Path 2: Embed in CUBE
- Intent logic inside CUBE backend
- Tight coupling of declarative + procedural
- Single service but reduced flexibility
- **Verdict:** Pragmatic short-term, limited long-term

### Path 3: External IAS (Recommended)
- Separate orchestration service
- Clean boundaries and independent evolution
- Higher operational complexity, better architecture
- **Verdict:** Optimal for long-term sustainability

## IAS Responsibilities

1. **Intent API**: Expose task-oriented endpoints
2. **Orchestration**: Coordinate multi-step CUBE operations
3. **State Management**: Track workflow progress
4. **Authentication**: Integrate with authCore
5. **Error Handling**: Robust retry and recovery
6. **Observability**: Comprehensive logging and metrics

## Authentication Flows

### External Token Flow
1. Client authenticates with CUBE → receives CUBE token
2. Client sends intent + CUBE token to IAS
3. IAS passes token to authCore for validation
4. authCore validates against CUBE
5. IAS executes intent using validated context

### Stored Credentials Flow
1. User authenticates with authCore → receives authCore token
2. User stores CUBE credentials in authCore (once)
3. Client sends intent + authCore token to IAS
4. IAS requests authCore to broker CUBE operations
5. authCore uses stored credentials transparently

## Implementation Technology Stack

**Recommended:**
- **IAS Service**: FastAPI (Python) or Actix (Rust)
- **Authentication**: authCore (Python, MongoDB)
- **API Documentation**: OpenAPI/Swagger
- **Observability**: OpenTelemetry, Prometheus, Grafana
- **Deployment**: Docker/Kubernetes

## Open Questions

1. **Intent vocabulary governance**: How to manage intent additions/changes?
2. **Versioning strategy**: API versioning approach?
3. **Multi-institutional federation**: Single IAS or distributed?
4. **Workflow language integration**: How to integrate with CWL/Nextflow?
5. **Intent composition**: Support for composite workflows?

## Future Enhancements

- Natural language intent parsing via LLMs
- Intent recommendation based on usage patterns
- Workflow templates and libraries
- Multi-CUBE coordination
- Cross-institutional intent sharing
