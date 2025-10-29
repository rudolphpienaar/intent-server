#!/usr/bin/env python3
"""
Generate publication-quality architectural diagrams for the Intent-Action Service paper.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# Publication settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.5

# Color scheme (professional, colorblind-friendly)
COLOR_USER = '#E8F4F8'      # Light blue
COLOR_UI = '#B3D9E6'        # Medium blue
COLOR_IAS = '#FFE5B4'       # Peach
COLOR_CUBE = '#C8E6C9'      # Light green
COLOR_EMPHASIS = '#FFCCCC'  # Light red for emphasis
COLOR_BORDER = '#333333'    # Dark grey
COLOR_ARROW = '#555555'     # Medium grey

def add_box(ax, x, y, width, height, text, color, style='round', linewidth=2):
    """Add a styled box with text."""
    if style == 'round':
        box = FancyBboxPatch((x, y), width, height,
                            boxstyle="round,pad=0.05",
                            facecolor=color,
                            edgecolor=COLOR_BORDER,
                            linewidth=linewidth)
    elif style == 'emphasis':
        box = FancyBboxPatch((x, y), width, height,
                            boxstyle="round,pad=0.08",
                            facecolor=color,
                            edgecolor=COLOR_BORDER,
                            linewidth=linewidth,
                            linestyle='--')
    else:
        box = mpatches.Rectangle((x, y), width, height,
                                facecolor=color,
                                edgecolor=COLOR_BORDER,
                                linewidth=linewidth)
    ax.add_patch(box)

    # Add text
    ax.text(x + width/2, y + height/2, text,
           ha='center', va='center',
           fontsize=9, weight='normal',
           wrap=True)

def add_arrow(ax, x1, y1, x2, y2, style='single', color=COLOR_ARROW):
    """Add an arrow between two points."""
    if style == 'multi':
        # Multiple parallel arrows
        for offset in [-0.15, -0.05, 0.05, 0.15]:
            arrow = FancyArrowPatch((x1+offset, y1), (x2+offset, y2),
                                   arrowstyle='->',
                                   color=color,
                                   linewidth=1.5,
                                   mutation_scale=15)
            ax.add_patch(arrow)
    else:
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='->',
                               color=color,
                               linewidth=2,
                               mutation_scale=20)
        ax.add_patch(arrow)

def create_figure_01_current_architecture():
    """Figure 1: Current Architecture (Status Quo)"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # User intents at top
    add_box(ax, 0.5, 8.5, 2, 0.8, 'User Visualization\nIntent\n("show feeds")', COLOR_USER)
    add_box(ax, 7.5, 8.5, 2, 0.8, 'User Behavioral\nIntent\n("anonymize")', COLOR_USER)

    # ChRIS UI container
    add_box(ax, 0.2, 4.5, 9.6, 3.5, '', COLOR_UI, style='square', linewidth=2.5)
    ax.text(5, 7.7, 'ChRIS UI', ha='center', va='center', fontsize=11, weight='bold')

    # React components layer
    ax.plot([0.3, 9.7], [7.3, 7.3], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 7, 'React Components', ha='center', va='center', fontsize=9)
    ax.text(2, 6.5, 'handles "show feeds" intent', ha='center', va='center', fontsize=8, style='italic')

    # Intent Translator (emphasized)
    add_box(ax, 6.5, 5.5, 2.5, 1.2, 'Intent\nTranslator\n(embedded)', COLOR_EMPHASIS, style='emphasis', linewidth=2)

    # JS library layer
    ax.plot([0.3, 9.7], [5.2, 5.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 4.9, 'JavaScript Thin Client Library', ha='center', va='center', fontsize=9)

    # CUBE container
    add_box(ax, 0.2, 0.5, 9.6, 3, '', COLOR_CUBE, style='square', linewidth=2.5)
    ax.text(5, 3.2, 'CUBE', ha='center', va='center', fontsize=11, weight='bold')

    ax.plot([0.3, 9.7], [2.8, 2.8], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 2.5, 'Collection+JSON API', ha='center', va='center', fontsize=9)

    ax.plot([0.3, 9.7], [2.2, 2.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 1.5, 'CUBE Python/Django Internals', ha='center', va='center', fontsize=9)

    # Arrows
    add_arrow(ax, 1.5, 8.5, 1.5, 8.0)  # Viz intent down
    add_arrow(ax, 8.5, 8.5, 8.5, 6.7)  # Behavioral intent down

    add_arrow(ax, 1.5, 7.3, 1.5, 3.5)  # Viz through to CUBE

    # Multiple arrows from Intent Translator to CUBE
    add_arrow(ax, 7, 5.5, 4, 3.5, style='multi')

    plt.title('Figure 1: Current Architecture (Status Quo)', fontsize=12, weight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('figures/fig01_current_architecture.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig01_current_architecture.png")

def create_figure_02_null_case():
    """Figure 2: Null Case (Do Nothing) - nearly identical to Figure 1"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # User intents at top
    add_box(ax, 0.5, 8.5, 2, 0.8, 'User Visualization\nIntent\n("show feeds")', COLOR_USER)
    add_box(ax, 7.5, 8.5, 2, 0.8, 'User Behavioral\nIntent\n("anonymize")', COLOR_USER)

    # ChRIS UI container
    add_box(ax, 0.2, 4.5, 9.6, 3.5, '', COLOR_UI, style='square', linewidth=2.5)
    ax.text(5, 7.7, 'ChRIS UI', ha='center', va='center', fontsize=11, weight='bold')

    # React components layer
    ax.plot([0.3, 9.7], [7.3, 7.3], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 7, 'React Components', ha='center', va='center', fontsize=9)
    ax.text(2, 6.5, 'handles "show feeds" intent', ha='center', va='center', fontsize=8, style='italic')

    # Intent Translator (refactored but still embedded)
    add_box(ax, 6.5, 5.5, 2.5, 1.2, 'Intent\nTranslator\n(refactored)', COLOR_EMPHASIS, style='emphasis', linewidth=2)

    # JS library layer
    ax.plot([0.3, 9.7], [5.2, 5.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 4.9, 'JavaScript Thin Client Library', ha='center', va='center', fontsize=9)

    # CUBE container
    add_box(ax, 0.2, 0.5, 9.6, 3, '', COLOR_CUBE, style='square', linewidth=2.5)
    ax.text(5, 3.2, 'CUBE', ha='center', va='center', fontsize=11, weight='bold')

    ax.plot([0.3, 9.7], [2.8, 2.8], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 2.5, 'Collection+JSON API', ha='center', va='center', fontsize=9)

    ax.plot([0.3, 9.7], [2.2, 2.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 1.5, 'CUBE Python/Django Internals', ha='center', va='center', fontsize=9)

    # Arrows
    add_arrow(ax, 1.5, 8.5, 1.5, 8.0)
    add_arrow(ax, 8.5, 8.5, 8.5, 6.7)
    add_arrow(ax, 1.5, 7.3, 1.5, 3.5)
    add_arrow(ax, 7, 5.5, 4, 3.5, style='multi')

    plt.title('Figure 2: Null Case (Do Nothing)', fontsize=12, weight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('figures/fig02_null_case.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig02_null_case.png")

def create_figure_03_embedded_cube():
    """Figure 3: Embedded Intent Logic Inside CUBE"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # User intents at top
    add_box(ax, 0.5, 8.5, 2, 0.8, 'User Visualization\nIntent', COLOR_USER)
    add_box(ax, 7.5, 8.5, 2, 0.8, 'User Behavioral\nIntent', COLOR_USER)

    # ChRIS UI container (simpler now)
    add_box(ax, 0.2, 5.5, 9.6, 2.5, '', COLOR_UI, style='square', linewidth=2.5)
    ax.text(5, 7.7, 'ChRIS UI', ha='center', va='center', fontsize=11, weight='bold')

    # React components layer
    ax.plot([0.3, 9.7], [7.3, 7.3], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 7, 'React Components', ha='center', va='center', fontsize=9)

    # JS library layer
    ax.plot([0.3, 9.7], [6.2, 6.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 5.9, 'JavaScript Thin Client Library', ha='center', va='center', fontsize=9)

    # CUBE container (now contains intent logic)
    add_box(ax, 0.2, 0.5, 9.6, 4.5, '', COLOR_CUBE, style='square', linewidth=2.5)
    ax.text(5, 4.7, 'CUBE', ha='center', va='center', fontsize=11, weight='bold')

    # Dual API layer
    ax.plot([0.3, 9.7], [4.3, 4.3], color=COLOR_BORDER, linewidth=1.5)
    ax.text(2.5, 4, 'Collection+JSON API', ha='center', va='center', fontsize=9)
    ax.text(7.5, 4, 'Intent API', ha='center', va='center', fontsize=9)
    ax.plot([5, 5], [4.3, 3.8], color=COLOR_BORDER, linewidth=1.5)  # Vertical divider

    # Intent Logic Handler (emphasized)
    add_box(ax, 6, 2.5, 3, 1, 'Intent Logic\nHandler', COLOR_EMPHASIS, style='emphasis', linewidth=2)

    ax.plot([0.3, 9.7], [2.2, 2.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 1.5, 'CUBE Python/Django Internals', ha='center', va='center', fontsize=9)

    # Arrows
    add_arrow(ax, 1.5, 8.5, 1.5, 8.0)
    add_arrow(ax, 8.5, 8.5, 8.5, 8.0)

    add_arrow(ax, 1.5, 5.5, 1.5, 5.0)  # Viz path
    add_arrow(ax, 8.5, 5.5, 8.5, 5.0)  # Behavioral path

    add_arrow(ax, 1.5, 4.3, 1.5, 2.2)  # Viz through Cj API
    add_arrow(ax, 8.5, 4.3, 7.5, 3.5)  # Behavioral to Intent Handler

    # Multiple arrows from Intent Handler to internals
    add_arrow(ax, 7.5, 2.5, 5, 2.2, style='multi')

    plt.title('Figure 3: Embedding Intent Logic Inside CUBE', fontsize=12, weight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('figures/fig03_embedded_cube.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig03_embedded_cube.png")

def create_figure_04_external_ias():
    """Figure 4: External Intent-Action Service"""
    fig, ax = plt.subplots(figsize=(10, 9))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # User intents at top
    add_box(ax, 0.5, 8.8, 2, 0.8, 'User Visualization\nIntent\n("show feeds")', COLOR_USER)
    add_box(ax, 7.5, 8.8, 2, 0.8, 'User Behavioral\nIntent\n("anonymize")', COLOR_USER)

    # ChRIS UI container (thin again)
    add_box(ax, 0.2, 6.5, 9.6, 2, '', COLOR_UI, style='square', linewidth=2.5)
    ax.text(5, 8.2, 'ChRIS UI', ha='center', va='center', fontsize=11, weight='bold')

    # React components layer
    ax.plot([0.3, 9.7], [7.9, 7.9], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 7.6, 'React Components (presentation only)', ha='center', va='center', fontsize=9)

    # JS library layer
    ax.plot([0.3, 9.7], [7.2, 7.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 6.9, 'JavaScript Thin Client Library', ha='center', va='center', fontsize=9)

    # IAS container (separate service - emphasized)
    add_box(ax, 6, 4, 3.5, 2, '', COLOR_IAS, style='square', linewidth=2.5)
    ax.text(7.75, 5.8, 'Intent-Action\nService (IAS)', ha='center', va='center', fontsize=10, weight='bold')

    # Intent Logic Orchestrator
    add_box(ax, 6.3, 4.3, 2.9, 1.2, 'Intent Logic\nOrchestrator', COLOR_EMPHASIS, style='emphasis', linewidth=2)

    # CUBE container
    add_box(ax, 0.2, 0.5, 9.6, 3, '', COLOR_CUBE, style='square', linewidth=2.5)
    ax.text(5, 3.2, 'CUBE', ha='center', va='center', fontsize=11, weight='bold')

    ax.plot([0.3, 9.7], [2.8, 2.8], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 2.5, 'Collection+JSON API', ha='center', va='center', fontsize=9)

    ax.plot([0.3, 9.7], [2.2, 2.2], color=COLOR_BORDER, linewidth=1.5)
    ax.text(5, 1.5, 'CUBE Python/Django Internals', ha='center', va='center', fontsize=9)
    ax.text(5, 0.9, '(declarative substrate preserved)', ha='center', va='center', fontsize=8, style='italic')

    # Arrows - visualization path bypasses IAS
    add_arrow(ax, 1.5, 8.8, 1.5, 8.5)
    add_arrow(ax, 8.5, 8.8, 8.5, 8.5)

    # Viz goes straight to CUBE
    add_arrow(ax, 1.5, 6.5, 1.5, 3.5)

    # Behavioral goes through IAS
    add_arrow(ax, 8.5, 6.5, 7.75, 6.0)

    # IAS to CUBE (multiple arrows showing orchestration)
    add_arrow(ax, 7.5, 4, 5, 3.5, style='multi')

    plt.title('Figure 4: External Intent-Action Service (Proposed)', fontsize=12, weight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('figures/fig04_external_ias.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig04_external_ias.png")

if __name__ == '__main__':
    print("Generating publication-quality architectural diagrams...")
    print()

    create_figure_01_current_architecture()
    create_figure_02_null_case()
    create_figure_03_embedded_cube()
    create_figure_04_external_ias()

    print()
    print("✓ All diagrams generated successfully in figures/")
    print("  Resolution: 300 DPI (publication quality)")
    print("  Format: PNG with white background")
