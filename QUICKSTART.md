# Quick Start Guide

Resume work in 5 minutes.

## TL;DR

```bash
# 1. Build the paper
./scripts/build.sh

# 2. View output
open build/paper.pdf     # or .html

# 3. Check word count
./scripts/word-count.sh

# 4. Edit figures
# Open figures-source/drawio/*.drawio in https://app.diagrams.net
# Export to paper/figures/ at 300 DPI
```

---

## Current Status

**Paper is COMPLETE** (~12,000-15,000 words)
- Abstract → Conclusion all written
- HATEOAS-framed for REST community
- Three architectural scenarios analyzed
- AuthCore security integration explained

**Figures need work**
- Source files exist (`.drawio`)
- Need manual export at high quality

---

## Critical Next Steps

### 1. Fix Figures (30-60 min)
```bash
# Open each file in draw.io:
figures-source/drawio/fig01_current_architecture.drawio
figures-source/drawio/fig02_null_case.drawio
figures-source/drawio/fig03_embedded_cube.drawio
figures-source/drawio/fig04_external_ias.drawio

# For each:
1. Open at https://app.diagrams.net
2. Review layout (should be close to ASCII originals)
3. Adjust spacing/fonts as needed
4. File → Export As → PNG
5. Set: 300 DPI, transparent background OFF
6. Save to: paper/figures/figXX_*.png
```

### 2. Review Paper (30 min)
```bash
./scripts/build.sh
open build/paper.pdf
# Read through, check flow and figures
```

### 3. Add Metadata (5 min)
Edit `paper/main.adoc`:
```asciidoc
:author: Your Name
:email: you@institution.edu
:affiliation: Your Institution
```

### 4. Check Length (1 min)
```bash
./scripts/word-count.sh
# If > 10,000 words, may need to condense for some journals
```

---

## File Locations

**Main content:** `paper/sections/*.adoc`
**Build from:** `paper/main.adoc`
**Outputs go to:** `build/`
**Figures:** `paper/figures/*.png` (need regeneration)
**Figure sources:** `figures-source/drawio/*.drawio`

---

## Build Requirements

**Required:**
- `asciidoctor` (for HTML)
  ```bash
  gem install asciidoctor
  ```

**Optional:**
- `asciidoctor-pdf` (for PDF)
- `pandoc` (for DOCX)

---

## Repository State

```
Paper: COMPLETE
Figures: NEED REGENERATION
Build: READY
Docs: COMPLETE
```

See **context/STATUS.md** for full details.
