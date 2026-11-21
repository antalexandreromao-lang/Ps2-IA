#!/usr/bin/env python3
"""Generate local OPL brand/library assets. Requires Pillow; not needed to compile the ELF."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
GFX = ROOT / "gfx"
INK = (4, 8, 16)
NAVY = (0, 55, 145)
BLUE = (30, 112, 226)
CYAN = (75, 183, 255)


def make_library_fallback():
    """Dark static fallback shown when no per-game _BG artwork is available."""
    width, height = 1024, 512
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    top, bottom = (11, 24, 43), (2, 5, 12)
    for y in range(height):
        t = y / max(1, height - 1)
        row = tuple(round(top[c] * (1 - t) + bottom[c] * t) for c in range(3))
        for x in range(width):
            pixels[x, y] = row

    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((640, 100, 1010, 470), fill=(22, 88, 190, 34))
    glow = glow.filter(ImageFilter.GaussianBlur(84))
    Image.alpha_composite(image.convert("RGBA"), glow).convert("RGB").save(GFX / "opl_library_bg.png", optimize=True)


def make_library_overlay(active_tab):
    """Transparent glass/HUD layer: dynamic selected-game BG art remains visible below it."""
    width, height = 1024, 512
    overlay = Image.new("RGBA", (width, height), (3, 8, 17, 105))
    d = ImageDraw.Draw(overlay)

    # Translucent panes retain the full-screen game's own background art beneath the UI.
    d.rounded_rectangle((22, 78, 674, 435), radius=10, fill=(2, 7, 15, 72), outline=(71, 144, 224, 108), width=1)
    d.line((680, 82, 680, 432), fill=(46, 132, 236, 155), width=2)
    d.rounded_rectangle((697, 91, 995, 427), radius=18, fill=(4, 11, 23, 76), outline=(54, 139, 242, 122), width=2)

    # Header plate where the black-and-blue OPL wordmark is rendered by a StaticText element.
    d.rounded_rectangle((25, 14, 225, 61), radius=8, fill=(248, 251, 255, 246), outline=(*BLUE, 218), width=2)
    d.rounded_rectangle((25, 14, 34, 61), radius=4, fill=(*BLUE, 255))
    d.line((47, 55, 204, 55), fill=(*CYAN, 210), width=1)

    # Separate PS2/PS1 tabs. The active pill changes with the library family.
    tabs = {"ps2": (245, 14, 358, 61), "ps1": (371, 14, 484, 61)}
    for name, box in tabs.items():
        if name == active_tab:
            d.rounded_rectangle(box, radius=8, fill=(*NAVY, 246), outline=(*CYAN, 240), width=2)
        else:
            d.rounded_rectangle(box, radius=8, fill=(4, 13, 28, 150), outline=(57, 128, 210, 150), width=1)

    # Quiet technical grid and hairlines across the whole screen.
    for x in range(32, width, 64):
        d.line((x, 64, x, 454), fill=(75, 150, 235, 15), width=1)
    for y in range(96, 448, 48):
        d.line((24, y, 1000, y), fill=(75, 150, 235, 13), width=1)
    d.line((510, 37, 988, 37), fill=(66, 137, 221, 112), width=1)
    d.line((24, 463, 1000, 463), fill=(41, 104, 178, 158), width=1)
    d.line((24, 463, 214, 463), fill=(*BLUE, 240), width=2)

    # Cover bay brackets, sized for a portrait PS2 cover or a square PS1 cover.
    for x, y, sx, sy in ((708, 102, 1, 1), (984, 102, -1, 1), (708, 416, 1, -1), (984, 416, -1, -1)):
        d.line((x, y, x + 24 * sx, y), fill=(*CYAN, 220), width=3)
        d.line((x, y, x, y + 24 * sy), fill=(*CYAN, 220), width=3)
    for i in range(5):
        x = 890 + i * 18
        d.rounded_rectangle((x, 31, x + 9, 35), radius=2, fill=(55 + i * 14, 139 + i * 12, 237, 210))
    for x in (62, 78, 94, 110, 126):
        d.ellipse((x, 443, x + 4, 447), fill=(*CYAN, 190))

    output = "opl_library_overlay.png" if active_tab == "ps2" else "opl_library_overlay_ps1.png"
    overlay.save(GFX / output, optimize=True)


def font_for(size):
    candidates = [
        ROOT / "third_party/fonts/PoeVeticaNew.ttf",
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(str(path), size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def make_wordmark(width, height):
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = font_for(90 if height <= 128 else 100)
    letters = "OPL"
    spacing = 16
    widths = [draw.textlength(letter, font=font) for letter in letters]
    total = sum(widths) + spacing * (len(letters) - 1)
    x = (width - total) / 2
    center_y = height / 2 - 4
    for letter, letter_width in zip(letters, widths):
        bbox = draw.textbbox((0, 0), letter, font=font, stroke_width=1)
        glyph_height = bbox[3] - bbox[1]
        y = center_y - glyph_height / 2 - bbox[1]
        draw.text((x + 2, y + 3), letter, font=font, fill=(30, 112, 226, 95), stroke_width=2, stroke_fill=(30, 112, 226, 110))
        draw.text((x, y), letter, font=font, fill=(*INK, 255), stroke_width=2, stroke_fill=(*NAVY, 255))
        x += letter_width + spacing
    line_y = min(height - 8, int(height * 0.87))
    line_w = min(138, width // 3)
    left = (width - line_w) // 2
    draw.rounded_rectangle((left, line_y, left + line_w // 2, line_y + 3), radius=2, fill=(*NAVY, 245))
    draw.rounded_rectangle((left + line_w // 2, line_y, left + line_w, line_y + 3), radius=2, fill=(*CYAN, 245))
    return image


def make_logo_assets():
    make_wordmark(512, 256).save(GFX / "logo.png", optimize=True)
    for n in range(7):
        make_wordmark(512, 128).save(GFX / f"logo{n}.png", optimize=True)


def make_small_icon():
    image = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((2, 2, 29, 29), radius=7, fill=(8, 18, 36, 240), outline=(*CYAN, 230), width=2)
    d.ellipse((8, 8, 24, 24), outline=(57, 151, 255, 255), width=3)
    d.ellipse((13, 13, 19, 19), fill=(235, 246, 255, 255))
    d.line((17, 7, 25, 3), fill=(*CYAN, 255), width=2)
    image.save(GFX / "ip.png", optimize=True)


if __name__ == "__main__":
    GFX.mkdir(parents=True, exist_ok=True)
    make_library_fallback()
    make_library_overlay("ps2")
    make_library_overlay("ps1")
    make_logo_assets()
    make_small_icon()
    print("Generated black-and-blue OPL wordmarks, dark fallback, translucent game-art overlay, and icon.")
