# Three Versions Guide

## Overview

This repository contains **three versions** of the Intent-Action Service proposal, each designed for different audiences and purposes:

1. **Research Paper** (`paper-research/`) - For academic submission
2. **Engineering Paper** (`paper-engineering/`) - For comprehensive internal documentation
3. **Engineering Brief** (`engineering-brief/`) - For concise team presentations

---

## Research Paper

**Location:** `paper-research/`

**Build output:** `build/paper_research.{html,pdf,docx}`

### Purpose
Academic journal submission with proper research framing

### Key Characteristics
- **Abstract:** Research framing with explicit research questions (RQ1-RQ5)
- **Conclusion:** Epistemic humility, validation framework, conditional claims
- **Tone:** "We propose to validate..." / "This remains to be tested..."
- **Length:** 50+ pages
- **Emphasis:** Hypothesis testing, acknowledges uncertainty
- **References:** Comprehensive (40+ citations)

### Target Audience
- Peer reviewers at academic journals
- HATEOAS/REST architecture research community
- Software engineering academics
- Conference presentation audiences

### Use Cases
- Submitting to IEEE Software, Journal of Systems and Software, etc.
- Academic conference presentations
- Building research collaborations
- Establishing academic credibility

---

## Engineering Paper (Full)

**Location:** `paper-engineering/`

**Build output:** `build/paper_engineering.{html,pdf,docx}`

### Purpose
Comprehensive internal technical documentation with advocacy framing

### Key Characteristics
- **Abstract:** "Executive Summary" presenting recommendation
- **Conclusion:** Three-phase implementation roadmap with concrete deliverables
- **Tone:** "We recommend..." / "The path forward is clear..."
- **Length:** 50+ pages
- **Emphasis:** Action-oriented, benefits-focused, comprehensive analysis
- **References:** Comprehensive (40+ citations)

### Target Audience
- ChRIS development team
- Technical stakeholders requiring detailed analysis
- Grant proposal reviewers
- External collaborators needing full context

### Use Cases
- Detailed internal technical review
- Comprehensive documentation for future reference
- Grant proposals requiring thorough analysis
- Onboarding new team members to architectural decisions

---

## Engineering Brief

**Location:** `engineering-brief/`

**Build output:** `build/engineering_brief.{html,pdf,docx}`

### Purpose
Concise proposal for busy developers and initial team presentation

### Key Characteristics
- **Structure:** Executive summary format
- **Tone:** Engineering rigor with academic references
- **Length:** 10 pages (including diagrams, TOC, references)
- **Emphasis:** Clear recommendation, preemptive objections, concrete next steps
- **References:** Core principles only (11 citations)
- **Alternatives:** Status quo and embedded cases compressed to 1-2 sentences

### Target Audience
- Busy developers with limited time
- Team meetings requiring concise presentation
- Initial technical reviews
- Decision-makers needing executive summary

### Use Cases
- Initial team presentation (distribute 1 week before meeting)
- Technical reviews with time constraints
- Executive summary for full engineering paper
- Quick reference for implementation phases

### Special Features
- Compact PDF theme (9.5pt font, tighter spacing)
- Six objections addressed preemptively
- Three-phase validation plan with explicit abort criteria
- Emphasis on incremental risk management

---

## Comparison Matrix

| Aspect | Research Paper | Engineering Paper (Full) | Engineering Brief |
|--------|----------------|--------------------------|-------------------|
| **File Location** | `paper-research/` | `paper-engineering/` | `engineering-brief/` |
| **Length** | 50+ pages | 50+ pages | 10 pages |
| **Tone** | Tentative, validation-focused | Confident, action-oriented | Rigorous, concise |
| **Abstract** | Research questions (RQ1-RQ5) | Executive summary | Executive summary |
| **Conclusion** | Validation criteria | Implementation roadmap | Validation plan |
| **Alternatives** | Full analysis | Full analysis | Compressed (1-2 sentences) |
| **Focus** | Balanced exploration | 50/50 analysis/IAS | 80%+ IAS recommendation |
| **Objections** | Threats to validity | Embedded in discussion | Preemptive FAQ (6 items) |
| **References** | 40+ citations | 40+ citations | 11 core citations |
| **Target Audience** | Academic reviewers | Technical stakeholders | Busy developers |
| **Primary Goal** | Publish research | Comprehensive documentation | Build consensus |

---

## Shared Content

All three versions share:
- Introduction (architectural context, problem statement)
- Core architectural analysis (status quo, embedded, external IAS)
- Discussion of alternatives
- Technical architecture details
- CONSOLIDATED_REFERENCES.adoc (40+ references)

Key differences are in:
- Abstract/executive summary framing
- Conclusion (validation vs. roadmap)
- Tone (tentative vs. prescriptive)
- Depth of alternatives analysis (full vs. compressed)

---

## Building

```bash
# Build all three versions
./scripts/build.sh

# Outputs:
# - build/paper_research.{html,pdf,docx}
# - build/paper_engineering.{html,pdf,docx}
# - build/engineering_brief.{html,pdf,docx}
```

---

## Selection Guide

**Use Research Paper when:**
- Submitting to academic journals
- Presenting at research conferences
- Establishing academic credibility
- Need epistemic humility and proper research framing

**Use Engineering Paper when:**
- Comprehensive internal documentation needed
- Detailed technical review required
- Writing grant proposals
- Onboarding requires full context

**Use Engineering Brief when:**
- Initial team presentation
- Time-constrained technical reviews
- Decision-makers need executive summary
- Want concise, actionable recommendation

---

## Document History

**October 2025:** Initial creation with two versions (research and team proposal)

**October 2025:** Restructured into three versions:
- Research paper maintained research framing
- Team proposal renamed to Engineering Paper (Full)
- Engineering Brief created as concise version

All versions maintained, no content discarded - different presentations for different audiences.
