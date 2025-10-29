# Paper Directory Structure

The Intent-Action Service paper now exists in **two separate, complete versions** for different audiences.

## Directory Structure

```
intent-server/
├── paper-research/              # Academic publication version
│   ├── main.adoc               # Master document
│   ├── sections/
│   │   ├── 00_abstract.adoc   # Research abstract with RQ1-RQ5
│   │   ├── 01_introduction.adoc
│   │   ├── 02_methods.adoc + subsections
│   │   ├── 03_discussion.adoc
│   │   └── 04_conclusion.adoc # Research conclusion (epistemic humility)
│   └── figures/
│
├── paper-engineering/           # Engineering decision document
│   ├── main.adoc               # Master document
│   ├── sections/
│   │   ├── 00_abstract.adoc   # Executive Summary (advocacy)
│   │   ├── 01_introduction.adoc
│   │   ├── 02_methods.adoc + subsections
│   │   ├── 03_discussion.adoc
│   │   └── 04_conclusion.adoc # Implementation Roadmap (prescriptive)
│   └── figures/
│
└── paper-archive/               # Original combined version (reference)
    └── [original files preserved]
```

## Two Versions

### paper-research/ - Academic Publication Version

**Purpose**: For journal submission and academic peer review

**Characteristics**:
- Research questions (RQ1-RQ5) explicitly stated
- Validation criteria with success/failure metrics
- "Research agenda" framing (not "completed solution")
- Epistemic humility: "what remains unknown"
- Commitment to transparent reporting of negative results
- Conditional language about broader implications
- Threats to validity section

**Target Audience**: Academic reviewers, research community

**Suitable For**:
- IEEE Software
- Journal of Biomedical Informatics
- Software: Practice and Experience
- PeerJ Computer Science
- Workshop/conference position papers

### paper-engineering/ - Engineering Decision Document

**Purpose**: Internal team planning and consensus building

**Characteristics**:
- Executive Summary with advocacy tone
- Clear recommendation for external IAS approach
- Detailed 18-month implementation roadmap (3 phases)
- Prescriptive language ("we recommend...")
- Concrete deliverables per phase
- Strategic positioning arguments
- Focus on pragmatic constraints and incremental adoption

**Target Audience**: ChRIS development team, engineering leadership

**Suitable For**:
- Team meetings and technical reviews
- Engineering proposals
- Stakeholder presentations
- Grant proposals
- Technical planning documents

## Key Differences

### Abstract/Executive Summary

| Research | Engineering |
|----------|-------------|
| Research questions (RQ1-RQ5) | Executive summary (advocacy) |
| "We propose to validate..." | "We recommend..." |
| Emphasizes unknowns | Emphasizes benefits |
| Conditional implications | Strategic advantages |

### Conclusion

| Research | Engineering |
|----------|-------------|
| "What we have established" | "Implementation roadmap" |
| "What remains unknown" | "Phase 1-3 timeline" |
| Success/failure criteria | Concrete deliverables |
| Epistemic humility | Confident recommendation |
| "May prove to be..." | "Path forward is clear" |

### Shared Content

Both versions share:
- Introduction (problem context, background)
- Methods (three architectural alternatives analysis)
- Discussion (comparative evaluation, implications)

This allows updates to shared analysis to propagate to both versions automatically.

## Building the Papers

### Build both versions:
```bash
./scripts/build.sh
```

### Output files:
```
build/
├── paper_research.html
├── paper_research.pdf
├── paper_research.docx
├── paper_engineering.html
├── paper_engineering.pdf
└── paper_engineering.docx
```

### Word counts:
```bash
./scripts/word-count.sh          # Count both
./scripts/word-count.sh research  # Research only
./scripts/word-count.sh engineering  # Engineering only
```

## Workflow Recommendations

### For Research Paper (publication):

1. Work primarily in `paper-research/`
2. Focus on:
   - Research questions remain clear and testable
   - Validation criteria are concrete and measurable
   - Limitations and threats to validity are honest
   - Language is appropriately hedged and academic
3. Update references for academic standards
4. Build and review `paper_research.pdf` regularly
5. Check word count against target journal limits

### For Engineering Document (internal):

1. Work primarily in `paper-engineering/`
2. Focus on:
   - Implementation roadmap is concrete and achievable
   - Phases have clear deliverables
   - Resource requirements are realistic
   - Timeline aligns with team capacity
3. Keep language confident but pragmatic
4. Build and share `paper_engineering.pdf` with team
5. Update as plans evolve

### When updating shared content:

If you modify:
- Introduction
- Methods (sections 2.1-2.4)
- Discussion

You'll need to update **both** directories since content is duplicated:
```bash
# Copy updated shared section to both
cp paper-research/sections/01_introduction.adoc paper-engineering/sections/
```

Or edit in both places simultaneously.

## Archive

The original `paper/` directory has been renamed to `paper-archive/` and contains:
- Original combined version (`main.adoc`)
- Original research version (`main_research.adoc`)
- Original team version (`main_team.adoc`)
- All original section files including both abstract/conclusion versions

This preserves the full history while keeping the active work clearly separated.

## Migration Complete

**Complete:**
- Directories created
- Files copied and organized
- Main documents created
- Build scripts updated
- Word count scripts updated
- Figures copied to both versions

Both papers are ready to build and work with independently.
