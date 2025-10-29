# Completing the ChRIS Architecture: An Intent-Action Service

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **An architectural proposal for bridging declarative hypermedia APIs and procedural client workflows through an external Intent-Action Service**

## Abstract

This paper examines a fundamental architectural challenge in the ChRIS medical imaging platform: the impedance mismatch between CUBE's declarative Collection+JSON resource model and the procedural workflows that clients require. We analyze three architectural approaches—maintaining the status quo, embedding intent logic within CUBE, and deploying an external Intent-Action Service (IAS)—and argue that the external IAS represents the optimal balance between architectural purity, evolutionary sustainability, and readiness for agentic computing paradigms.

## Repository Structure

```
intent-server/
├── paper-research/            # Academic publication version
│   ├── main.adoc             # Master document (research framing)
│   ├── sections/             # Sections with RQ1-RQ5, validation criteria
│   └── figures/              # Publication-ready figures
├── paper-engineering/         # Engineering decision document
│   ├── main.adoc             # Master document (advocacy framing)
│   ├── sections/             # Sections with implementation roadmap
│   └── figures/              # Publication-ready figures
├── engineering-brief/         # 10-page concise proposal
│   ├── main.adoc             # Master document (executive summary)
│   ├── sections/             # Compressed alternatives, focused on IAS
│   ├── compact-theme.yml     # PDF theme for tight layout
│   └── figures/              # Publication-ready figures
├── figures-source/            # Editable figure sources
│   ├── drawio/               # Draw.io XML files
│   ├── graphviz/             # Graphviz DOT files
│   └── scripts/              # Figure generation scripts
├── scripts/                   # Build utilities
│   ├── build.sh              # Build all three versions
│   └── word-count.sh         # Check word count for all versions
├── docs/                      # Additional documentation
├── drafts/                    # Archived earlier versions
├── paper-archive/             # Original combined version (reference)
├── THREE_VERSIONS_GUIDE.md    # Detailed comparison of three versions
├── ENGINEERING_BRIEF.md       # Engineering brief documentation
└── CONSOLIDATED_REFERENCES.adoc  # Shared references (40+ citations)
```

## Three Paper Versions

This repository contains **three versions** of the Intent-Action Service proposal, each for different audiences:

1. **Research Paper** (`paper-research/`) - Academic journal submission with research questions (RQ1-RQ5), validation criteria, and epistemic humility
2. **Engineering Paper** (`paper-engineering/`) - Comprehensive internal documentation with implementation roadmap and advocacy framing
3. **Engineering Brief** (`engineering-brief/`) - 10-page concise proposal for busy developers with preemptive objections addressed

See **THREE_VERSIONS_GUIDE.md** for detailed comparison and usage recommendations.

## Building the Paper

### Prerequisites

**Required:**
- [Asciidoctor](https://asciidoctor.org/) - for HTML generation
  ```bash
  gem install asciidoctor
  ```

**Optional (for additional formats):**
- [Asciidoctor PDF](https://github.com/asciidoctor/asciidoctor-pdf) - for PDF generation
  ```bash
  gem install asciidoctor-pdf
  ```
- [Pandoc](https://pandoc.org/) - for DOCX generation
  ```bash
  # Termux/Android:
  pkg install pandoc

  # Ubuntu/Debian:
  apt-get install pandoc

  # macOS:
  brew install pandoc
  ```

### Build Commands

**Build all three versions (recommended):**
```bash
./scripts/build.sh
```

This generates:
- `build/paper_research.{html,pdf,docx}` - Academic version
- `build/paper_engineering.{html,pdf,docx}` - Engineering version
- `build/engineering_brief.{html,pdf,docx}` - Brief version (10 pages)

**Build individual versions:**
```bash
# Research paper only
asciidoctor -o build/paper_research.html paper-research/main.adoc
asciidoctor-pdf -o build/paper_research.pdf paper-research/main.adoc

# Engineering paper only
asciidoctor -o build/paper_engineering.html paper-engineering/main.adoc
asciidoctor-pdf -o build/paper_engineering.pdf paper-engineering/main.adoc

# Engineering brief only
asciidoctor -a pdf-theme=engineering-brief/compact-theme.yml \
  -o build/engineering_brief.pdf engineering-brief/main.adoc
```

**Check word count:**
```bash
./scripts/word-count.sh              # All versions
./scripts/word-count.sh research     # Research only
./scripts/word-count.sh engineering  # Engineering only
./scripts/word-count.sh brief        # Brief only
```

## Editing Figures

The diagrams are created in [draw.io](https://app.diagrams.net/):

1. Open `figures-source/drawio/figXX_*.drawio` in draw.io
2. Edit as needed
3. Export as PNG (300+ DPI) to all three figure directories:
   - `paper-research/figures/`
   - `paper-engineering/figures/`
   - `engineering-brief/figures/`
4. Commit both source (.drawio) and output (.png) files

## Key Contributions

1. **Architectural Analysis**: Systematic evaluation of three approaches to resolving the procedural-declarative mismatch in distributed systems
2. **External IAS Design**: Detailed architectural proposal for an Intent-Action Service that complements hypermedia APIs
3. **Security Architecture**: Integration with authCore for credential brokering without distribution
4. **Agentic Computing**: Positioning for LLM-driven interaction through intent-level APIs
5. **Broader Applicability**: General pattern applicable beyond ChRIS to scientific computing platforms

## Usage Guide

**For academic journal submission:**
- Use `paper-research/` version
- Research questions (RQ1-RQ5) and validation framework
- Target journals: IEEE Software, Journal of Biomedical Informatics, Software: Practice and Experience

**For team presentations and internal reviews:**
- Use `engineering-brief/` version for initial meetings (10 pages)
- Use `paper-engineering/` version for comprehensive technical review (50+ pages)
- Implementation roadmap with 3 phases

See **THREE_VERSIONS_GUIDE.md** for detailed selection criteria.

## Academic Paper Status and Roadmap

**Current Status (Research Paper):**

**Complete:**
- Core architectural analysis (three alternatives: status quo, embedded, external IAS)
- Problem characterization (intent-orchestration impedance mismatch)
- Research questions defined (RQ1-RQ5)
- Introduction with historical context (Collection+JSON, HATEOAS decline)
- Discussion section with comparative evaluation
- Comprehensive references (40+ citations)

**Still Needed:**
- Empirical validation data (currently proposal only, no implementation results)
- Developer experience metrics (time-to-implementation, API usability surveys)
- Performance benchmarks (latency, throughput overhead measurements)
- Client complexity metrics (LOC reduction, cognitive complexity comparison)
- Longitudinal study data (independent evolution claims untested)
- Case study from actual implementation in ChRIS
- Threats to validity section (partially addressed but needs expansion)
- Related work section (currently embedded in introduction, needs standalone section)
- Future work section (validation methodology outlined but needs detail)

**Next Steps for Publication:**
- **PREREQUISITE**: Implement IAS and collect telemetry data first
- Phase 1 implementation (1-3 intents, ~4-6 weeks)
- Phase 2 implementation (5-7 intents, ~8-10 weeks)
- Collect empirical metrics (complexity reduction, latency, developer experience)
- Expand related work into standalone section
- Add formal threats to validity analysis
- Write up empirical results and case study

**Target Timeline:**
- Q4 2025 (Nov-Dec): Implement Phase 1 IAS proof-of-concept
- Q1 2026 (Jan-Mar): Complete Phase 2, collect preliminary telemetry data
- Q2 2026 (Apr-Jun): Write empirical results, submit to IEEE Software or JSS
- Alternative: Submit position paper (current architectural analysis) earlier while implementation proceeds

**Note**: Academic paper submission requires empirical validation data from actual IAS implementation. Current papers are architectural proposals suitable for internal review and team consensus building.

See **THREE_VERSIONS_GUIDE.md** for version-specific details.

## Citation

If you reference this work, please cite:

```bibtex
@article{pienaar2025intent,
  title={Completing the ChRIS Architecture: An Intent-Action Service for Bridging Declarative Resources and Procedural Workflows},
  author={Pienaar, Rudolph},
  journal={Preprint},
  year={2025},
  institution={Boston Children's Hospital},
  url={https://github.com/rudolphpienaar/intent-server}
}
```

## Related Work

- **ChRIS Platform**: https://chrisproject.org/
- **CUBE Backend**: https://github.com/FNNDSC/ChRIS_ultron_backEnd
- **authCore**: https://github.com/rudolphpienaar/authCore

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit

## Authors

**Rudolph Pienaar**
Boston Children's Hospital
rudolph.pienaar@childrens.harvard.edu

## Contact

For questions or collaboration inquiries, please contact rudolph.pienaar@childrens.harvard.edu

---

**Status**: Draft (as of October 2025)
