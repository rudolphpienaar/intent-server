#!/usr/bin/env python3
"""
Generate publication-quality architectural diagrams using PIL/Pillow.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Colors (professional, colorblind-friendly)
COLOR_USER = (232, 244, 248)      # Light blue
COLOR_UI = (179, 217, 230)        # Medium blue
COLOR_IAS = (255, 229, 180)       # Peach
COLOR_CUBE = (200, 230, 201)      # Light green
COLOR_EMPHASIS = (255, 204, 204)  # Light red
COLOR_BORDER = (51, 51, 51)       # Dark grey
COLOR_ARROW = (85, 85, 85)        # Medium grey
COLOR_BG = (255, 255, 255)        # White

# Try to load a nice font, fallback to default
try:
    font_large = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 28)
    font_med = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 22)
    font_small = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 18)
    font_tiny = ImageFont.truetype("/system/fonts/Roboto-Italic.ttf", 16)
except:
    font_large = ImageFont.load_default()
    font_med = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_tiny = ImageFont.load_default()

def draw_rounded_rect(draw, xy, fill, outline, width=3, radius=15):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def draw_box(draw, x, y, w, h, text, fill_color, border_color=COLOR_BORDER, border_width=3, font=font_small):
    """Draw a box with centered text."""
    draw_rounded_rect(draw, (x, y, x+w, y+h), fill=fill_color, outline=border_color, width=border_width)

    # Draw text centered
    lines = text.split('\n')
    total_height = len(lines) * 25
    start_y = y + (h - total_height) // 2

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        draw.text((x + (w - text_width) // 2, start_y + i * 25), line, fill=COLOR_BORDER, font=font)

def draw_arrow(draw, x1, y1, x2, y2, color=COLOR_ARROW, width=4, multi=False):
    """Draw an arrow or multiple parallel arrows."""
    if multi:
        # Draw 4 parallel arrows
        offsets = [-20, -7, 7, 20]
        for offset in offsets:
            draw.line([(x1+offset, y1), (x2+offset, y2)], fill=color, width=2)
            # Arrowhead
            if y2 > y1:  # Downward
                draw.polygon([(x2+offset, y2), (x2+offset-6, y2-12), (x2+offset+6, y2-12)], fill=color)
            else:  # Upward
                draw.polygon([(x2+offset, y2), (x2+offset-6, y2+12), (x2+offset+6, y2+12)], fill=color)
    else:
        # Single arrow
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
        # Arrowhead
        if y2 > y1:  # Downward
            draw.polygon([(x2, y2), (x2-10, y2-20), (x2+10, y2-20)], fill=color)
        else:  # Upward
            draw.polygon([(x2, y2), (x2-10, y2+20), (x2+10, y2+20)], fill=color)

def create_figure_01():
    """Figure 1: Current Architecture"""
    img = Image.new('RGB', (1400, 1200), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((700, 30), "Figure 1: Current Architecture (Status Quo)", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # User intents
    draw_box(draw, 100, 100, 280, 100, "User Visualization\nIntent\n(\"show feeds\")", COLOR_USER)
    draw_box(draw, 1020, 100, 280, 100, "User Behavioral\nIntent\n(\"anonymize\")", COLOR_USER)

    # ChRIS UI container
    draw_rounded_rect(draw, (50, 280, 1350, 700), fill=COLOR_UI, outline=COLOR_BORDER, width=4)
    draw.text((700, 310), "ChRIS UI", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # React layer
    draw.line([(60, 360), (1340, 360)], fill=COLOR_BORDER, width=3)
    draw.text((700, 400), "React Components", fill=COLOR_BORDER, font=font_med, anchor="mm")
    draw.text((280, 450), "handles \"show feeds\" intent", fill=COLOR_ARROW, font=font_tiny, anchor="mm")

    # Intent Translator
    draw_rounded_rect(draw, (900, 490, 1200, 640), fill=COLOR_EMPHASIS, outline=COLOR_BORDER, width=3)
    draw.text((1050, 565), "Intent\nTranslator\n(embedded)", fill=COLOR_BORDER, font=font_small, anchor="mm")

    # JS library
    draw.line([(60, 660), (1340, 660)], fill=COLOR_BORDER, width=3)
    draw.text((700, 680), "JavaScript Thin Client Library", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # CUBE container
    draw_rounded_rect(draw, (50, 760, 1350, 1120), fill=COLOR_CUBE, outline=COLOR_BORDER, width=4)
    draw.text((700, 790), "CUBE", fill=COLOR_BORDER, font=font_large, anchor="mm")

    draw.line([(60, 850), (1340, 850)], fill=COLOR_BORDER, width=3)
    draw.text((700, 880), "Collection+JSON API", fill=COLOR_BORDER, font=font_med, anchor="mm")

    draw.line([(60, 950), (1340, 950)], fill=COLOR_BORDER, width=3)
    draw.text((700, 1000), "CUBE Python/Django Internals", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # Arrows
    draw_arrow(draw, 240, 200, 240, 280)  # Viz intent down
    draw_arrow(draw, 1160, 200, 1160, 280)  # Behavioral intent down
    draw_arrow(draw, 240, 360, 240, 760)  # Viz to CUBE
    draw_arrow(draw, 1050, 640, 700, 760, multi=True)  # Intent Translator to CUBE (multiple)

    img.save('figures/fig01_current_architecture.png', dpi=(300, 300))
    print("✓ Generated fig01_current_architecture.png")

def create_figure_02():
    """Figure 2: Null Case"""
    img = Image.new('RGB', (1400, 1200), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((700, 30), "Figure 2: Null Case (Do Nothing)", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # User intents
    draw_box(draw, 100, 100, 280, 100, "User Visualization\nIntent\n(\"show feeds\")", COLOR_USER)
    draw_box(draw, 1020, 100, 280, 100, "User Behavioral\nIntent\n(\"anonymize\")", COLOR_USER)

    # ChRIS UI container
    draw_rounded_rect(draw, (50, 280, 1350, 700), fill=COLOR_UI, outline=COLOR_BORDER, width=4)
    draw.text((700, 310), "ChRIS UI", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # React layer
    draw.line([(60, 360), (1340, 360)], fill=COLOR_BORDER, width=3)
    draw.text((700, 400), "React Components", fill=COLOR_BORDER, font=font_med, anchor="mm")
    draw.text((280, 450), "handles \"show feeds\" intent", fill=COLOR_ARROW, font=font_tiny, anchor="mm")

    # Intent Translator (refactored)
    draw_rounded_rect(draw, (900, 490, 1200, 640), fill=COLOR_EMPHASIS, outline=COLOR_BORDER, width=3)
    draw.text((1050, 565), "Intent\nTranslator\n(refactored)", fill=COLOR_BORDER, font=font_small, anchor="mm")

    # JS library
    draw.line([(60, 660), (1340, 660)], fill=COLOR_BORDER, width=3)
    draw.text((700, 680), "JavaScript Thin Client Library", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # CUBE container
    draw_rounded_rect(draw, (50, 760, 1350, 1120), fill=COLOR_CUBE, outline=COLOR_BORDER, width=4)
    draw.text((700, 790), "CUBE", fill=COLOR_BORDER, font=font_large, anchor="mm")

    draw.line([(60, 850), (1340, 850)], fill=COLOR_BORDER, width=3)
    draw.text((700, 880), "Collection+JSON API", fill=COLOR_BORDER, font=font_med, anchor="mm")

    draw.line([(60, 950), (1340, 950)], fill=COLOR_BORDER, width=3)
    draw.text((700, 1000), "CUBE Python/Django Internals", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # Arrows
    draw_arrow(draw, 240, 200, 240, 280)
    draw_arrow(draw, 1160, 200, 1160, 280)
    draw_arrow(draw, 240, 360, 240, 760)
    draw_arrow(draw, 1050, 640, 700, 760, multi=True)

    img.save('figures/fig02_null_case.png', dpi=(300, 300))
    print("✓ Generated fig02_null_case.png")

def create_figure_03():
    """Figure 3: Embedded in CUBE"""
    img = Image.new('RGB', (1400, 1200), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((700, 30), "Figure 3: Embedding Intent Logic Inside CUBE", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # User intents
    draw_box(draw, 100, 100, 280, 100, "User Visualization\nIntent", COLOR_USER)
    draw_box(draw, 1020, 100, 280, 100, "User Behavioral\nIntent", COLOR_USER)

    # ChRIS UI container (simpler)
    draw_rounded_rect(draw, (50, 280, 1350, 550), fill=COLOR_UI, outline=COLOR_BORDER, width=4)
    draw.text((700, 310), "ChRIS UI", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # React layer
    draw.line([(60, 360), (1340, 360)], fill=COLOR_BORDER, width=3)
    draw.text((700, 400), "React Components", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # JS library
    draw.line([(60, 490), (1340, 490)], fill=COLOR_BORDER, width=3)
    draw.text((700, 520), "JavaScript Thin Client Library", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # CUBE container (with intent logic)
    draw_rounded_rect(draw, (50, 630, 1350, 1120), fill=COLOR_CUBE, outline=COLOR_BORDER, width=4)
    draw.text((700, 660), "CUBE", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # Dual API
    draw.line([(60, 720), (1340, 720)], fill=COLOR_BORDER, width=3)
    draw.line([(700, 720), (700, 780)], fill=COLOR_BORDER, width=3)  # Vertical divider
    draw.text((350, 750), "Collection+JSON API", fill=COLOR_BORDER, font=font_med, anchor="mm")
    draw.text((1050, 750), "Intent API", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # Intent Logic Handler
    draw_rounded_rect(draw, (850, 810, 1200, 950), fill=COLOR_EMPHASIS, outline=COLOR_BORDER, width=3)
    draw.text((1025, 880), "Intent Logic\nHandler", fill=COLOR_BORDER, font=font_small, anchor="mm")

    draw.line([(60, 970), (1340, 970)], fill=COLOR_BORDER, width=3)
    draw.text((700, 1020), "CUBE Python/Django Internals", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # Arrows
    draw_arrow(draw, 240, 200, 240, 280)
    draw_arrow(draw, 1160, 200, 1160, 280)
    draw_arrow(draw, 240, 550, 240, 630)
    draw_arrow(draw, 1160, 550, 1160, 630)
    draw_arrow(draw, 240, 720, 240, 970)  # Viz through
    draw_arrow(draw, 1160, 720, 1025, 810)  # Behavioral to handler
    draw_arrow(draw, 1025, 950, 700, 970, multi=True)  # Handler to internals

    img.save('figures/fig03_embedded_cube.png', dpi=(300, 300))
    print("✓ Generated fig03_embedded_cube.png")

def create_figure_04():
    """Figure 4: External IAS"""
    img = Image.new('RGB', (1400, 1300), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((700, 30), "Figure 4: External Intent-Action Service (Proposed)", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # User intents
    draw_box(draw, 100, 100, 280, 100, "User Visualization\nIntent\n(\"show feeds\")", COLOR_USER)
    draw_box(draw, 1020, 100, 280, 100, "User Behavioral\nIntent\n(\"anonymize\")", COLOR_USER)

    # ChRIS UI container (thin)
    draw_rounded_rect(draw, (50, 280, 1350, 550), fill=COLOR_UI, outline=COLOR_BORDER, width=4)
    draw.text((700, 310), "ChRIS UI", fill=COLOR_BORDER, font=font_large, anchor="mm")

    # React layer
    draw.line([(60, 360), (1340, 360)], fill=COLOR_BORDER, width=3)
    draw.text((700, 400), "React Components (presentation only)", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # JS library
    draw.line([(60, 490), (1340, 490)], fill=COLOR_BORDER, width=3)
    draw.text((700, 520), "JavaScript Thin Client Library", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # IAS container (separate service)
    draw_rounded_rect(draw, (850, 640, 1300, 870), fill=COLOR_IAS, outline=COLOR_BORDER, width=4)
    draw.text((1075, 670), "Intent-Action Service\n(IAS)", fill=COLOR_BORDER, font=font_med, anchor="mm")

    # Intent Orchestrator
    draw_rounded_rect(draw, (900, 720, 1250, 840), fill=COLOR_EMPHASIS, outline=COLOR_BORDER, width=3)
    draw.text((1075, 780), "Intent Logic\nOrchestrator", fill=COLOR_BORDER, font=font_small, anchor="mm")

    # CUBE container
    draw_rounded_rect(draw, (50, 950, 1350, 1240), fill=COLOR_CUBE, outline=COLOR_BORDER, width=4)
    draw.text((700, 980), "CUBE", fill=COLOR_BORDER, font=font_large, anchor="mm")

    draw.line([(60, 1040), (1340, 1040)], fill=COLOR_BORDER, width=3)
    draw.text((700, 1070), "Collection+JSON API", fill=COLOR_BORDER, font=font_med, anchor="mm")

    draw.line([(60, 1130), (1340, 1130)], fill=COLOR_BORDER, width=3)
    draw.text((700, 1170), "CUBE Python/Django Internals", fill=COLOR_BORDER, font=font_med, anchor="mm")
    draw.text((700, 1210), "(declarative substrate preserved)", fill=COLOR_ARROW, font=font_tiny, anchor="mm")

    # Arrows
    draw_arrow(draw, 240, 200, 240, 280)
    draw_arrow(draw, 1160, 200, 1160, 280)

    # Viz bypasses IAS
    draw_arrow(draw, 240, 550, 240, 950)

    # Behavioral through IAS
    draw_arrow(draw, 1160, 550, 1075, 640)
    draw_arrow(draw, 1075, 870, 700, 950, multi=True)

    img.save('figures/fig04_external_ias.png', dpi=(300, 300))
    print("✓ Generated fig04_external_ias.png")

if __name__ == '__main__':
    print("Generating publication-quality architectural diagrams with PIL...")
    print()

    os.makedirs('figures', exist_ok=True)

    create_figure_01()
    create_figure_02()
    create_figure_03()
    create_figure_04()

    print()
    print("✓ All diagrams generated successfully in figures/")
    print("  Resolution: 300 DPI (publication quality)")
    print("  Format: PNG with white background")
