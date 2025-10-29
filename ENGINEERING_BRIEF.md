# Engineering Brief Documentation

## Overview

The **engineering-brief/** directory contains a concise, technically rigorous proposal document (approximately 10 pages) designed for busy developers and technical stakeholders who require clear recommendations with supporting evidence.

## Purpose

This brief addresses the practical reality that most developers:
- Have limited time to read comprehensive technical documents
- Want clear recommendations backed by established principles
- Need common objections addressed directly
- Require concrete next steps with explicit decision points

## Key Characteristics

**Short**: 10 pages total (vs. 50+ pages for full engineering paper)

**Rigorous**: Academic/engineering tone with references throughout

**Focused**: Status quo and embedded alternatives compressed to 1-2 sentences; 80%+ focus on IAS recommendation

**Action-oriented**: Three-phase incremental validation plan with explicit abort criteria

**Objection-ready**: Six common objections addressed with academic references

## Structure

```
engineering-brief/
├── main.adoc                       # Master document
├── compact-theme.yml               # PDF theme for tight layout
├── sections/
│   ├── 00_summary.adoc            # Problem + Recommendation
│   ├── 01_current_problem.adoc    # Status quo analysis
│   ├── 02_alternatives.adoc       # Brief comparison
│   ├── 03_ias_architecture.adoc   # Technical details
│   ├── 04_objections.adoc         # FAQ/responses
│   └── 05_next_steps.adoc         # Incremental validation plan
└── figures/                        # Architectural diagrams
```

## Content Summary

### Section 00: Executive Summary
- **Problem**: Client ecosystem stagnation due to orchestration burden
- **Recommendation**: External IAS architecture
- **Constraints**: Production system, cannot abandon Collection+JSON
- **References**: Parnas 1972, Lehman 1980, Kruchten 2012, Brooks 1987, Fielding 2000

### Section 01: Current Problem
- Architectural overview with diagram
- Orchestration problem explained
- UI architectural degradation
- Impact on development velocity
- Key point: Declarative APIs alone insufficient for procedural clients

### Section 02: Alternatives Analysis
- **Status quo**: Compressed to 1-2 sentences, leads to stagnation (Lehman 1980)
- **Embedded in CUBE**: Compressed to 1-2 sentences, couples fast/slow evolution (Parnas 1972)
- **External IAS**: 80% of section, recommended approach with full rationale
- Rationale grounded in established engineering principles

### Section 03: IAS Architecture
- System overview with architectural diagram (Figure 4)
- API design examples (task-oriented endpoints)
- Implementation considerations:
  - Independent deployment
  - Stateless operation
  - Authentication delegation
  - Centralized observability
- Technical benefits (shared orchestration, testability, progressive disclosure)
- Positioned as Backend-for-Frontend pattern (Newman 2021)

### Section 04: Objections and Responses

Addresses six predictable objections with technical responses:

1. **"Why not drop Collection+JSON entirely?"** - Explains philosophical rationale, incremental adoption impossibility, domain expertise loss
2. **"This adds unnecessary complexity"** - Relocates existing complexity, makes it manageable (Brooks 1987)
3. **"Just refactor the UI"** - Doesn't help Python/CLI clients, keeps orchestration in wrong tier
4. **"What if it fails?"** - Incremental validation with explicit abort criteria
5. **"Dual API burden"** - Reduces total maintenance by eliminating duplication
6. **"Over-engineering"** - Problems documented with concrete evidence (stagnated clients: python-chrisclient, chrs, ChILI, pipeline2cube)

Each response references established engineering principles.

### Section 05: Next Steps

**Phase 1** (Weeks 1-3): Proof of concept with 1 intent
- Success criteria: >30% complexity reduction, <300ms latency
- Decision point: Continue or abort (minimal sunk cost)

**Phase 2** (Weeks 4-10): 5-7 intents, Python/CLI integration
- Success criteria: Client ecosystem growth, 40% complexity reduction
- Decision point: Assess scalability

**Phase 3** (Weeks 11-18): 15-20 intents, production deployment
- Success metrics: >80% traffic via IAS, 50% complexity reduction

**Resource estimate**: 4-6 person-months over 18 weeks

## Comparison with Other Versions

| Feature | Engineering Brief | Engineering Paper (Full) | Research Paper |
|---------|------------------|--------------------------|----------------|
| **Length** | 10 pages | 50+ pages | 50+ pages |
| **Audience** | Busy developers | Technical stakeholders | Academic reviewers |
| **Tone** | Engineering rigor | Engineering advocacy | Research inquiry |
| **Alternatives** | Minimal (1-2 sentences each) | Full analysis | Full analysis |
| **Focus** | 80% IAS | 50/50 analysis/IAS | Balanced exploration |
| **Objections** | Preemptive FAQ | Embedded in discussion | Threats to validity |
| **Next steps** | Concrete phases | Implementation roadmap | Validation criteria |
| **References** | Core principles only | Comprehensive | Comprehensive |

## When to Use Each Version

**Engineering Brief**: Team meetings, technical reviews, initial proposal presentations

**Engineering Paper**: Comprehensive technical documentation, detailed internal reviews, grant proposals

**Research Paper**: Journal submission, academic peer review, conference presentations

## Building

```bash
# Build all three versions
./scripts/build.sh

# Output includes:
# - build/engineering_brief.html
# - build/engineering_brief.pdf
# - build/engineering_brief.docx
```

The PDF uses a compact theme (9.5pt font, tighter spacing) to fit content efficiently while maintaining readability.

## Status

**Complete and ready to use**
- All sections written with proper academic/engineering tone
- References verified and formatted
- Diagrams included
- Build script updated
- Compact PDF theme applied
- Approximately 10 pages when built (including 2 architectural diagrams, TOC, and references)
