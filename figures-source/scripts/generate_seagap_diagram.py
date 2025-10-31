#!/usr/bin/env python3
"""
Generate SeaGaP workflow diagram
Requires: graphviz Python package and graphviz system package
"""

import sys
from pathlib import Path

try:
    from graphviz import Source
except ImportError:
    print("Error: graphviz Python package not installed")
    print("Install with: pip install graphviz")
    sys.exit(1)

def generate_diagram():
    """Generate SeaGaP pattern diagram from DOT file"""

    # Paths
    script_dir = Path(__file__).parent
    dot_file = script_dir.parent / "graphviz" / "fig05_seagap_pattern.dot"
    output_dirs = [
        script_dir.parent.parent / "paper-research" / "figures",
        script_dir.parent.parent / "paper-engineering" / "figures",
        script_dir.parent.parent / "engineering-brief" / "figures",
    ]

    if not dot_file.exists():
        print(f"Error: DOT file not found: {dot_file}")
        sys.exit(1)

    # Read DOT file
    with open(dot_file, 'r') as f:
        dot_source = f.read()

    # Create graphviz source
    graph = Source(dot_source)

    # Generate PNG for each output directory
    for output_dir in output_dirs:
        if not output_dir.exists():
            print(f"Creating directory: {output_dir}")
            output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "fig05_seagap_pattern"

        try:
            # Render to PNG (high DPI)
            graph.render(
                filename=str(output_file),
                format='png',
                cleanup=True,
                engine='dot'
            )
            print(f"Generated: {output_file}.png")

        except Exception as e:
            print(f"Error generating diagram for {output_dir}: {e}")
            print("Make sure graphviz system package is installed:")
            print("  Ubuntu/Debian: sudo apt-get install graphviz")
            print("  macOS: brew install graphviz")
            print("  Fedora: sudo dnf install graphviz")
            continue

if __name__ == "__main__":
    generate_diagram()
