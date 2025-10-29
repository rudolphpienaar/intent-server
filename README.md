# Completing the ChRIS Architecture: An Intent-Action Service

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **An architectural proposal for bridging declarative hypermedia APIs and procedural client workflows through an external Intent-Action Service**

## Abstract

This paper examines a fundamental architectural challenge in the ChRIS medical imaging platform: the impedance mismatch between CUBE's declarative Collection+JSON resource model and the procedural workflows that clients require. We analyze three architectural approaches—maintaining the status quo, embedding intent logic within CUBE, and deploying an external Intent-Action Service (IAS)—and argue that the external IAS represents the optimal balance between architectural purity, evolutionary sustainability, and readiness for agentic computing paradigms.

## Repository Structure

```
intent-server/
├── paper/                      # Main paper content
│   ├── main.adoc              # Master document
│   ├── sections/              # Individual sections
│   └── figures/               # Publication-ready figures
├── figures-source/            # Editable figure sources
│   ├── drawio/               # Draw.io XML files
│   ├── graphviz/             # Graphviz DOT files
│   └── scripts/              # Figure generation scripts
├── scripts/                   # Build utilities
│   ├── build.sh              # Build PDF/HTML/DOCX
│   └── word-count.sh         # Check word count
├── docs/                      # Additional documentation
├── drafts/                    # Archived earlier versions
└── related-work/             # Related projects
```

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

**Build all formats:**
```bash
./scripts/build.sh
```

**Build specific formats:**
```bash
# HTML only
asciidoctor -o build/paper.html paper/main.adoc

# PDF only
asciidoctor-pdf -o build/paper.pdf paper/main.adoc

# DOCX (requires HTML first)
asciidoctor -o build/paper.html paper/main.adoc
pandoc -f html -t docx -o build/paper.docx build/paper.html
```

**Check word count:**
```bash
./scripts/word-count.sh
```

**Generated outputs:** `build/paper.{html,pdf,docx}`

## Editing Figures

The diagrams are created in [draw.io](https://app.diagrams.net/):

1. Open `figures-source/drawio/figXX_*.drawio` in draw.io
2. Edit as needed
3. Export as PNG (300+ DPI) to `paper/figures/`
4. Commit both source (.drawio) and output (.png)

## Key Contributions

1. **Architectural Analysis**: Systematic evaluation of three approaches to resolving the procedural-declarative mismatch in distributed systems
2. **External IAS Design**: Detailed architectural proposal for an Intent-Action Service that complements hypermedia APIs
3. **Security Architecture**: Integration with authCore for credential brokering without distribution
4. **Agentic Computing**: Positioning for LLM-driven interaction through intent-level APIs
5. **Broader Applicability**: General pattern applicable beyond ChRIS to scientific computing platforms

## Target Journals

Potential publication venues (in order of fit):

1. **IEEE Software** (6,000-8,000 words)
2. **Journal of Biomedical Informatics** (~10,000 words)
3. **Software: Practice and Experience** (8,000-10,000 words)
4. **ACM TOSEM** (requires empirical validation)
5. **PeerJ Computer Science** (open access, flexible length)

## Citation

If you reference this work, please cite:

```bibtex
@article{intent-action-service-2025,
  title={Completing the ChRIS Architecture: An Intent-Action Service for Bridging Declarative Resources and Procedural Workflows},
  author={[Author Names]},
  journal={[Journal Name]},
  year={2025},
  note={Preprint available at [URL]}
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

[Author information to be added]

## Acknowledgments

[Acknowledgments to be added]

## Contact

For questions or collaboration inquiries, please contact [author contact info].

---

**Status**: Draft (as of October 2025)
