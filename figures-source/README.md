# Figure Sources

This directory contains source files and scripts for generating figures used in all three paper versions.

## Directory Structure

```
figures-source/
├── png/                          # Master PNG files (edit these!)
│   ├── ChRIS_arch_IAS - Status Quo.png   # Current architecture (fig01)
│   └── ChRIS_arch_IAS - IAS.png          # External IAS architecture (fig04)
├── graphviz/                     # Graphviz DOT sources
│   └── fig05_seagap_pattern.dot  # SeaGaP workflow diagram
└── scripts/                      # Generation and copy scripts
    ├── copy_figures.sh           # Copy PNG files to all paper directories
    ├── generate_seagap_diagram.py # Generate SeaGaP diagram from DOT
    ├── generate_diagrams.py      # DEPRECATED: Old matplotlib generation
    └── generate_diagrams_pil.py  # DEPRECATED: Old PIL generation
```

## Workflow: Updating Figures

### Status Quo and IAS Architectural Diagrams

These are the main architectural diagrams showing current state and proposed IAS architecture.

**To update:**

1. Edit the PNG files directly in `png/` directory using your preferred tool:
   - `ChRIS_arch_IAS - Status Quo.png`
   - `ChRIS_arch_IAS - IAS.png`

2. Run the copy script to distribute to all three paper directories:
   ```bash
   ./scripts/copy_figures.sh
   ```

3. This automatically copies:
   - `Status Quo.png` → `fig01_current_architecture_v2.png` (all papers)
   - `IAS.png` → `fig04_external_ias_v2.png` (all papers)

4. Verify the figures appear correctly:
   ```bash
   # Build papers to check
   ../scripts/build.sh
   ```

### SeaGaP Diagram (Graphviz)

The SeaGaP workflow diagram is generated from Graphviz DOT source.

**To update:**

1. Edit `graphviz/fig05_seagap_pattern.dot`

2. Run the generator:
   ```bash
   python3 scripts/generate_seagap_diagram.py
   ```

3. This generates `fig05_seagap_pattern.png` in all three paper figure directories

## Figure Mapping

| Source File | Target Filename | Used In | Description |
|-------------|----------------|---------|-------------|
| `ChRIS_arch_IAS - Status Quo.png` | `fig01_current_architecture_v2.png` | All papers, Section 1 | Current architecture showing embedded orchestration in UI |
| `ChRIS_arch_IAS - IAS.png` | `fig04_external_ias_v2.png` | All papers, Section 3 | Proposed external IAS architecture |
| `fig05_seagap_pattern.dot` | `fig05_seagap_pattern.png` | All papers, Section 3 | SeaGaP (Search-Gather-Pipeline) workflow pattern |

## Legacy Scripts (Deprecated)

The following scripts are no longer used but kept for reference:

- `generate_diagrams.py` - Old matplotlib-based figure generation
- `generate_diagrams_pil.py` - Old PIL-based figure generation

The new workflow uses manually created/edited PNG files instead of programmatic generation for better control over diagram appearance.
