from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

BASE = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(BASE, "slides")
os.makedirs(SLIDES_DIR, exist_ok=True)

W, H = 1920, 1080
BASE_BG = (10, 14, 26)
ACCENT_STRONG = "#1D9E75"
TEXT = "#FFFFFF"
SUBTEXT = "#E4EFE9"

FONT_DIR = r"C:\Windows\Fonts"
FONT_BOLD = os.path.join(FONT_DIR, "seguibl.ttf")
FONT_REG = os.path.join(FONT_DIR, "segoeui.ttf")

LOGO_PATH = r"C:\Claude\Franz\Marketing\logo\logo-icon.png"
EMOJI_FONT = os.path.join(FONT_DIR, "seguiemj.ttf")


def emoji(text, size):
    return ImageFont.truetype(EMOJI_FONT, size)

# Blob palette: nur Markenfarben (Teal/Grün/Blau) — Orange/Magenta raus,
# damit der Hintergrund ruhiger wirkt und zum Kompass-Logo passt
BLOB_COLORS = [
    (29, 200, 150, 255),
    (70, 115, 230, 210),
    (18, 145, 115, 230),
    (45, 95, 175, 200),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_wrapped(draw, text, xy, f, fill, max_width, line_spacing=1.35):
    words = text.split(" ")
    lines = []
    cur = ""
    for word in words:
        test = (cur + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=f)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)

    x, y = xy
    line_h = f.size * line_spacing
    for i, line in enumerate(lines):
        draw.text((x, y + i * line_h), line, font=f, fill=fill)
    return y + len(lines) * line_h


_logo_cache = None
def get_logo(size=110):
    global _logo_cache
    if _logo_cache is None:
        _logo_cache = Image.open(LOGO_PATH).convert("RGBA")
    logo = _logo_cache.copy()
    logo.thumbnail((size, size), Image.LANCZOS)
    return logo


def vibrant_bg(seed=0):
    """Dark base with 4 blurred, saturated color blobs. Position varies per seed
    so every slide looks related but not identical."""
    img = Image.new("RGB", (W, H), BASE_BG)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)

    angle = seed * 0.9
    dx = math.cos(angle) * 160
    dy = math.sin(angle) * 120

    positions = [
        (-350 + dx, -450 - dy, 650 + dx, 550 - dy),
        (1300 - dx, -550 + dy, 2350 - dx, 550 + dy),
        (-250 - dx, 550 + dy, 750 - dx, 1500 + dy),
        (1350 + dx, 450 - dy, 2350 + dx, 1400 - dy),
    ]
    for pos, color in zip(positions, BLOB_COLORS):
        gd.ellipse(pos, fill=color)

    glow = glow.filter(ImageFilter.GaussianBlur(150))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    return img


def base_slide(kicker=None, seed=0, show_logo_corner=True):
    img = vibrant_bg(seed)
    d = ImageDraw.Draw(img, "RGBA")
    d.rectangle((0, 0, W, 10), fill=ACCENT_STRONG)
    f_small = font(FONT_REG, 28)
    d.text((80, H - 70), "Franz · KI-Lotse · Pattaya — KI & Automatisierung nebenbei", font=f_small, fill=SUBTEXT)
    if kicker:
        f_kicker = font(FONT_BOLD, 34)
        bbox = d.textbbox((0, 0), kicker.upper(), font=f_kicker)
        box_w = bbox[2] - bbox[0] + 100
        d.rounded_rectangle((60, 75, 60 + box_w, 142), radius=6, outline=(255, 255, 255, 255), width=2)
        d.text((80, 90), kicker.upper(), font=f_kicker, fill=(255, 255, 255, 255))
    if show_logo_corner:
        logo_bg = Image.new("RGBA", (180, 180), (0, 0, 0, 0))
        lbd = ImageDraw.Draw(logo_bg)
        lbd.ellipse((0, 0, 180, 180), fill=(255, 255, 255, 235))
        logo = get_logo(140)
        lx = (180 - logo.width) // 2
        ly = (180 - logo.height) // 2
        logo_bg.paste(logo, (lx, ly), logo)
        img.paste(logo_bg, (W - 180 - 50, 36), logo_bg)
    return img, d


def text_panel(img, box, radius=24, opacity=150):
    panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel)
    pd.rounded_rectangle(box, radius=radius, fill=(6, 20, 16, opacity))
    panel = panel.filter(ImageFilter.GaussianBlur(2))
    return Image.alpha_composite(img.convert("RGBA"), panel).convert("RGB")


def save(img, name):
    path = os.path.join(SLIDES_DIR, name)
    img.save(path)
    print("saved", path)


def phone_mockup(path="mynote screenshot.jpeg", phone_h=760):
    phone_w = int(phone_h * 720 / 1600)
    shot = Image.open(path).convert("RGB")
    shot = shot.resize((phone_w, phone_h), Image.LANCZOS)
    frame_pad = 14
    radius = 36
    frame_w = phone_w + frame_pad * 2
    frame_h = phone_h + frame_pad * 2
    frame = Image.new("RGBA", (frame_w, frame_h), (0, 0, 0, 0))
    fd = ImageDraw.Draw(frame)
    fd.rounded_rectangle((0, 0, frame_w - 1, frame_h - 1), radius=radius + frame_pad, fill=(20, 20, 20, 255))
    mask = Image.new("L", (phone_w, phone_h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, phone_w - 1, phone_h - 1), radius=radius, fill=255)
    frame.paste(shot, (frame_pad, frame_pad), mask)
    return frame


f_body = font(FONT_REG, 44)

# 01 Hook (10s)
img, d = base_slide(seed=1, show_logo_corner=True)
img = text_panel(img, (50, 150, 1200, 830))
d = ImageDraw.Draw(img, "RGBA")
d.rectangle((0, 0, W, 10), fill=ACCENT_STRONG)
d.text((80, 90), "FRANZ · KI-LOTSE · PATTAYA".upper(), font=font(FONT_BOLD, 30), fill=(255, 255, 255, 255))
d.text((80, H - 70), "Franz · KI-Lotse · Pattaya — KI & Automatisierung nebenbei", font=font(FONT_REG, 28), fill=SUBTEXT)
d.text((90, 220), "Du hast schon von KI gehört.", font=font(FONT_BOLD, 62), fill=TEXT)
y = 380
for q in ["Was ist das?", "Was kann das?", "Was bringt mir das?"]:
    d.rectangle((90, y + 14, 110, y + 14 + 32), fill=(93, 202, 165, 255))
    d.text((140, y), q, font=font(FONT_BOLD, 56), fill=(255, 255, 255, 255))
    y += 100
f_emoji = emoji("🤷", 460)
d.text((1280, 330), "🤷", font=f_emoji, embedded_color=True)
save(img, "01_hook.png")

# 02 Wer ich bin (15s)
img, d = base_slide(seed=2, show_logo_corner=False)
img = text_panel(img, (50, 110, 1300, 900))
d = ImageDraw.Draw(img, "RGBA")
d.rectangle((0, 0, W, 10), fill=ACCENT_STRONG)
d.text((80, H - 70), "Franz · KI-Lotse · Pattaya — KI & Automatisierung nebenbei", font=font(FONT_REG, 28), fill=SUBTEXT)
logo = get_logo(170)
img.paste(logo, (90, 150), logo)
d = ImageDraw.Draw(img, "RGBA")
d.text((290, 185), "Franz", font=font(FONT_BOLD, 70), fill=TEXT)
d.text((290, 275), "KI-Lotse · Pattaya", font=font(FONT_REG, 40), fill=(147, 226, 199, 255))
# persönliche Zeile zuerst — schafft Vertrauen und erklärt den Thailand-Bezug
end_y = draw_wrapped(d,
    "Ich bin Österreicher, lebe in Pattaya – und baue mir meine digitalen "
    "Helfer selbst.",
    (90, 430), f_body, TEXT, 1150)
draw_wrapped(d,
    "Ich erkläre dir nicht nur, wie KI funktioniert – ich helfe dir auch bei den "
    "ersten Schritten: die passende KI auswählen, richtig anwenden, und auf "
    "Wunsch übernehme ich auch die Umsetzung für dich.",
    (90, end_y + 40), f_body, TEXT, 1150)

def logo_badge(path, size, bg=True):
    icon = Image.open(path).convert("RGBA")
    icon.thumbnail((int(size * 0.66), int(size * 0.66)), Image.LANCZOS)
    badge = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    if bg:
        bdraw = ImageDraw.Draw(badge)
        bdraw.ellipse((0, 0, size, size), fill=(255, 255, 255, 235))
    ix = (size - icon.width) // 2
    iy = (size - icon.height) // 2
    badge.paste(icon, (ix, iy), icon)
    return badge

# question mark on its own transparent layer so alpha actually blends
qlayer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
qd = ImageDraw.Draw(qlayer)
f_q = font(FONT_BOLD, 420)
qbbox = qd.textbbox((0, 0), "?", font=f_q)
qw = qbbox[2] - qbbox[0]
qd.text((1600 - qw / 2, 300), "?", font=f_q, fill=(255, 255, 255, 70))
img = Image.alpha_composite(img.convert("RGBA"), qlayer).convert("RGB")

# drei gleich grosse Badges in einer Reihe (vorher: verschiedene Formen/
# Groessen, wild verteilt — wirkte unruhig)
badge_size = 170
claude_badge = logo_badge(os.path.join(BASE, "logos", "claude.png"), badge_size)
gemini_badge = logo_badge(os.path.join(BASE, "logos", "gemini.png"), badge_size)
chatgpt_badge = logo_badge(os.path.join(BASE, "logos", "chatgpt.png"), badge_size)

by = 810
bx = 1315
for badge in (claude_badge, gemini_badge, chatgpt_badge):
    img.paste(badge, (bx, by), badge)
    bx += badge_size + 30

save(img, "02_wer_ich_bin.png")

# 03 Überleitung (10s)
img, d = base_slide(seed=3)
img = text_panel(img, (50, 380, 1850, 620))
d = ImageDraw.Draw(img, "RGBA")
d.rectangle((0, 0, W, 10), fill=ACCENT_STRONG)
d.text((80, H - 70), "Franz · KI-Lotse · Pattaya — KI & Automatisierung nebenbei", font=font(FONT_REG, 28), fill=SUBTEXT)
draw_wrapped(d,
    "Statt nur zu reden, zeig ich dir lieber zwei Beispiele aus meinem Alltag – "
    "Tools, die ich mir selbst gebaut habe.",
    (90, 440), f_body, TEXT, 1700)

def photo_frame(path, w, h, radius=20):
    photo = Image.open(path).convert("RGB")
    pw, ph = photo.size
    target_ratio = w / h
    src_ratio = pw / ph
    if src_ratio > target_ratio:
        new_w = int(ph * target_ratio)
        x0 = (pw - new_w) // 2
        photo = photo.crop((x0, 0, x0 + new_w, ph))
    else:
        new_h = int(pw / target_ratio)
        y0 = (ph - new_h) // 2
        photo = photo.crop((0, y0, pw, y0 + new_h))
    photo = photo.resize((w, h), Image.LANCZOS)
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=255)
    frame = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    frame.paste(photo, (0, 0), mask)
    return frame

def paper_card(path, w, h, pad=14):
    """Weisses Papier-Karten-Crop (Kopfbereich eines Formulars) mit Rand,
    fuer den Formular-Stapel auf Slide 7. Quelle: Leer-Vorlagen aus
    MyDocs/system/muster (keine echten Personendaten)."""
    doc = Image.open(path).convert("RGB")
    iw, ih = doc.size
    crop_h = min(int(iw * h / w), ih)
    doc = doc.crop((0, 0, iw, crop_h)).resize((w, h), Image.LANCZOS)
    canvas = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (255, 255, 255, 255))
    canvas.paste(doc, (pad, pad))
    return canvas


def fan_of_cards(paths, card_w=260, card_h=360, angles=(-13, 0, 13), spread=110):
    cards = [paper_card(p, card_w, card_h) for p in paths]
    canvas_w = card_w + spread * (len(cards) - 1) + 200
    canvas_h = card_h + 200
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    cx = canvas_w // 2
    cy = canvas_h // 2
    for card, angle in zip(cards, angles):
        rotated = card.rotate(angle, expand=True, resample=Image.BICUBIC)
        shadow_alpha = rotated.split()[-1].filter(ImageFilter.GaussianBlur(16))
        shadow = Image.new("RGBA", rotated.size, (0, 0, 0, 0))
        shadow.putalpha(shadow_alpha.point(lambda a: int(a * 0.45)))
        x = cx - rotated.width // 2
        y = cy - rotated.height // 2
        canvas.paste(shadow, (x + 14, y + 18), shadow)
        canvas.paste(rotated, (x, y), rotated)
    return canvas


# ein zentriertes Foto ("machen statt reden") — STOP-Schild + Hoersaal-Foto
# wirkten wie Clipart und passten nicht zur Botschaft
photo_w, photo_h = 700, 360
center_frame = photo_frame(os.path.join(BASE, "photos", "pairprogramming.jpg"), photo_w, photo_h)
img.paste(center_frame, ((W - photo_w) // 2, 640), center_frame)

save(img, "03_ueberleitung.png")

# 04 mytm Problem (15s)
img, d = base_slide(kicker="Beispiel 1 — mytm", seed=4)
img = text_panel(img, (50, 220, 1300, 620))
d = ImageDraw.Draw(img, "RGBA")
draw_wrapped(d,
    "Ich hatte Aufgaben in einer Liste und Termine im Google-Kalender – "
    "getrennt, doppelte Arbeit, ständig was vergessen.",
    (90, 260), f_body, TEXT, 1150)

# Quelle ist nur 601x316 — nicht ueber Originalgroesse skalieren, sonst unscharf
problem_frame = photo_frame(os.path.join(BASE, "photos", "liste-kalender.jpg"), 560, 294)
img.paste(problem_frame, (1330, 360), problem_frame)
save(img, "04_mytm_problem.png")

# 05 mytm Lösung (20s)
img, d = base_slide(kicker="Beispiel 1 — mytm", seed=5)
img = text_panel(img, (50, 220, 1850, 480))
d = ImageDraw.Draw(img, "RGBA")
# Nutzen statt Technik-Detail ("korrekte Zeitzone" sagt der Zielgruppe nichts)
draw_wrapped(d,
    "Mit KI-Unterstützung hab ich mir ein Tool gebaut, das Aufgaben automatisch "
    "mit dem Kalender synchron hält – nichts mehr doppelt eintragen, nichts "
    "mehr vergessen.",
    (90, 260), f_body, TEXT, 1650)

def gcal_mockup(w=480, h=300):
    """Nachgebautes Google-Calendar-Wochenraster mit Test-Terminen (kein echter
    Screenshot/Login noetig - siehe STATUS.md)."""
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    bar_h = 46
    d.rectangle((0, 0, w, bar_h), fill=(241, 243, 244))
    dot_colors = [(66, 133, 244), (234, 67, 53), (251, 188, 5), (52, 168, 83)]
    dx = 16
    for c in dot_colors:
        d.ellipse((dx, bar_h / 2 - 7, dx + 14, bar_h / 2 + 7), fill=c)
        dx += 20
    d.text((dx + 10, bar_h / 2 - 11), "Juli 2026", font=font(FONT_REG, 20), fill=(60, 64, 67))

    days = ["Mo", "Di", "Mi", "Do", "Fr"]
    col_w = w / len(days)
    grid_top = bar_h + 26
    for i, day in enumerate(days):
        d.text((i * col_w + col_w / 2 - 10, grid_top - 24), day, font=font(FONT_BOLD, 18), fill=(95, 99, 104))
    for row in range(5):
        y = grid_top + row * (h - grid_top) / 5
        d.line((0, y, w, y), fill=(224, 226, 227), width=1)
    for i in range(1, len(days)):
        x = i * col_w
        d.line((x, grid_top, x, h), fill=(224, 226, 227), width=1)

    events = [
        (0, 0.1, 0.35, (66, 133, 244), "Kunde A"),
        (1, 0.45, 0.30, (52, 168, 83), "Rechnung"),
        (2, 0.15, 0.25, (251, 188, 5), "Blog"),
        (3, 0.55, 0.35, (66, 133, 244), "Kunde B"),
        (4, 0.25, 0.20, (234, 67, 53), "Termin"),
    ]
    grid_h = h - grid_top
    f_event = font(FONT_REG, 17)
    for col, start, dur, color, label in events:
        x0 = col * col_w + 4
        x1 = (col + 1) * col_w - 4
        y0 = grid_top + start * grid_h
        y1 = y0 + dur * grid_h
        d.rounded_rectangle((x0, y0, x1, y1), radius=4, fill=color)
        # Beschriftung, damit die Bloecke nach echten Terminen aussehen
        label_fill = (60, 64, 67) if color == (251, 188, 5) else (255, 255, 255)
        if y1 - y0 >= 26:
            d.text((x0 + 8, y0 + 5), label, font=f_event, fill=label_fill)
    return img

thumb_h = 300
# mytm_w = thumb_h * Quell-Seitenverhaeltnis (1230x535), damit das Board
# KOMPLETT sichtbar ist — vorher schnitt der Center-Crop die Spalten an
mytm_w, mynote_w, gcal_w = 690, 300, 460
mytm_thumb = photo_frame(os.path.join(BASE, "photos", "mytm_screenshot.png"), mytm_w, thumb_h)

mynote_src = Image.open(os.path.join(BASE, "mynote screenshot.jpeg")).convert("RGB").crop((0, 0, 720, 700))
mynote_crop_path = os.path.join(BASE, "photos", "_mynote_crop_tmp.png")
mynote_src.save(mynote_crop_path)
mynote_thumb = photo_frame(mynote_crop_path, mynote_w, thumb_h)
os.remove(mynote_crop_path)

gcal_thumb_img = gcal_mockup(gcal_w, thumb_h)
gcal_mask = Image.new("L", (gcal_w, thumb_h), 0)
ImageDraw.Draw(gcal_mask).rounded_rectangle((0, 0, gcal_w - 1, thumb_h - 1), radius=20, fill=255)
gcal_thumb = Image.new("RGBA", (gcal_w, thumb_h), (0, 0, 0, 0))
gcal_thumb.paste(gcal_thumb_img, (0, 0), gcal_mask)

gap = 60
total_w = mytm_w + mynote_w + gcal_w + 2 * gap
ty = 620
tx = (W - total_w) // 2
for thumb in (mytm_thumb, mynote_thumb, gcal_thumb):
    img.paste(thumb, (tx, ty), thumb)
    tx += thumb.width + gap
d = ImageDraw.Draw(img, "RGBA")
save(img, "05_mytm_loesung.png")

# 06 MyNote-Ergänzung (15s)
img, d = base_slide(kicker="Beispiel 1 — MyNote", seed=6, show_logo_corner=False)
img = text_panel(img, (50, 190, 1150, 650))
d = ImageDraw.Draw(img, "RGBA")
draw_wrapped(d,
    "Und weil nicht immer ein PC in der Nähe ist: Mit MyNote lege ich "
    "Aufgaben und Termine auch unterwegs vom Handy aus an – alles "
    "synchronisiert sich automatisch mit MyTM.",
    (90, 260), f_body, TEXT, 1000)
frame = phone_mockup()
rotated = frame.rotate(-7, expand=True, resample=Image.BICUBIC)
px = W - rotated.width - 110
py = (H - rotated.height) // 2 + 10

shadow_alpha = rotated.split()[-1].filter(ImageFilter.GaussianBlur(24))
shadow = Image.new("RGBA", rotated.size, (0, 0, 0, 0))
shadow.putalpha(shadow_alpha.point(lambda a: int(a * 0.5)))

img = img.convert("RGBA")
img.paste(shadow, (px + 26, py + 34), shadow)
img.paste(rotated, (px, py), rotated)

sync_sz = 130
sync_badge = Image.new("RGBA", (sync_sz, sync_sz), (0, 0, 0, 0))
sbd = ImageDraw.Draw(sync_badge)
sbd.ellipse((0, 0, sync_sz, sync_sz), fill=(29, 200, 150, 255))
f_sync = emoji("🔄", int(sync_sz * 0.55))
stb = sbd.textbbox((0, 0), "🔄", font=f_sync)
stw, sth = stb[2] - stb[0], stb[3] - stb[1]
sbd.text((sync_sz / 2 - stw / 2 - stb[0], sync_sz / 2 - sth / 2 - stb[1]), "🔄", font=f_sync, embedded_color=True)
bx = px - int(sync_sz * 0.32)
by_ = py + rotated.height - int(sync_sz * 0.75)
img.paste(sync_badge, (bx, by_), sync_badge)

img = img.convert("RGB")
save(img, "06_mynote.png")

# 07 MyDocs Problem (15s)
img, d = base_slide(kicker="Beispiel 2 — MyDocs", seed=7)
img = text_panel(img, (50, 220, 1850, 460))
d = ImageDraw.Draw(img, "RGBA")
draw_wrapped(d,
    "Das kennt hier fast jeder: die endlosen Behördenformulare in Thailand. "
    "TM47, TM7, Wohnsitzbestätigung, Lebensbestätigung.",
    (90, 260), f_body, TEXT, 1700)

fan = fan_of_cards([
    os.path.join(BASE, "photos", "formulare", "lebens.png"),
    os.path.join(BASE, "photos", "formulare", "tm7.png"),
    os.path.join(BASE, "photos", "formulare", "tm47.png"),
], card_w=210, card_h=300, spread=90, angles=(-13, 13, 0))
fx = (W - fan.width) // 2
fy = 520
img = img.convert("RGBA")
img.paste(fan, (fx, fy), fan)
img = img.convert("RGB")
save(img, "07_mydocs_problem.png")

# 08 MyDocs Lösung (20s)
img, d = base_slide(kicker="Beispiel 2 — MyDocs", seed=8)
img = text_panel(img, (50, 220, 1850, 480))
d = ImageDraw.Draw(img, "RGBA")
draw_wrapped(d,
    "Also hab ich mir einen Formular-Generator gebaut, der genau diese "
    "Dokumente automatisch für mich ausfüllt und vorbereitet – kein "
    "Formular-Chaos mehr.",
    (90, 260), f_body, TEXT, 1650)

def frame_from_image(pil_img, w, h, radius=20, pad=14):
    iw, ih = pil_img.size
    target_ratio = w / h
    src_ratio = iw / ih
    if src_ratio > target_ratio:
        new_w = int(ih * target_ratio)
        x0 = (iw - new_w) // 2
        pil_img = pil_img.crop((x0, 0, x0 + new_w, ih))
    else:
        new_h = int(iw / target_ratio)
        y0 = (ih - new_h) // 2
        pil_img = pil_img.crop((0, y0, iw, y0 + new_h))
    pil_img = pil_img.resize((w, h), Image.LANCZOS)
    canvas = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (255, 255, 255, 255))
    canvas.paste(pil_img, (pad, pad))
    mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, canvas.width - 1, canvas.height - 1), radius=radius, fill=255)
    out = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    out.paste(canvas, (0, 0), mask)
    return out

# "Leer -> ausgefuellt" Vergleich auf Basis der echten TM47-Blanko-Vorlage,
# mit erfundenen Beispieldaten (keine echten Personendaten - siehe STATUS.md)
tm47_full = Image.open(os.path.join(BASE, "photos", "formulare", "tm47.png")).convert("RGB")
field_crop = tm47_full.crop((0, 150, 1191, 720))
leer_crop = field_crop.copy()
befuellt_crop = field_crop.copy()
fd = ImageDraw.Draw(befuellt_crop)
f_ink = font(FONT_REG, 26)
ink = (25, 55, 140)
for xy, txt in [
    ((705, 86), "Pattaya"),
    ((645, 158), "12"), ((745, 158), "Juli"), ((965, 158), "2026"),
    ((335, 280), "Muster Max"),
    ((235, 353), "AUSTRIA"),
    ((330, 423), "01"), ((440, 423), "April"), ((600, 423), "26"), ((825, 423), "Flug"),
    ((315, 483), "P1234567"), ((755, 483), "A987654"),
]:
    fd.text(xy, txt, font=f_ink, fill=ink)

card_w, card_h = 560, 268
leer_frame = frame_from_image(leer_crop, card_w, card_h)
befuellt_frame = frame_from_image(befuellt_crop, card_w, card_h)

gap = 130
total_w = card_w + gap + card_w
cy = 610
cx0 = (W - total_w) // 2
img = img.convert("RGBA")
img.paste(leer_frame, (cx0, cy), leer_frame)
img.paste(befuellt_frame, (cx0 + card_w + gap, cy), befuellt_frame)

d = ImageDraw.Draw(img, "RGBA")
f_arrow2 = font(FONT_BOLD, 70)
d.text((cx0 + card_w + gap / 2 - 24, cy + card_h / 2 - 45), "→", font=f_arrow2, fill=(147, 226, 199, 255))
f_caption = font(FONT_REG, 30)
d.text((cx0 + card_w / 2 - 40, cy + card_h + 20), "leer", font=f_caption, fill=SUBTEXT)
d.text((cx0 + card_w + gap + card_w / 2 - 90, cy + card_h + 20), "automatisch ausgefüllt", font=f_caption, fill=SUBTEXT)

img = img.convert("RGB")
save(img, "08_mydocs_loesung.png")

# 09 Übertrag (20s)
img, d = base_slide(kicker="Referenz", seed=9)
img = text_panel(img, (50, 220, 1850, 800))
d = ImageDraw.Draw(img, "RGBA")
end_y = draw_wrapped(d,
    "Beides sind keine Sonderfälle – solche Lösungen baue ich in jeder "
    "Größe, z. B. für eine Poolbau-Firma:",
    (90, 260), f_body, TEXT, 1700)

f_item_label = font(FONT_BOLD, 34)
f_item_desc = font(FONT_REG, 34)
items = [
    ("Dashboard", "Steuerung und Übersicht"),
    ("Angebote", "voll automatisiert aus Anfragen"),
    ("Rechnungen", "erstellen und automatischer Versand"),
    ("CRM", "alle Kundenkontakte und Daten"),
    ("Lagerhaltung", "mit automatischer Nachbestellung"),
]
y = end_y + 40
for label, desc in items:
    d.rectangle((90, y + 8, 108, y + 8 + 24), fill=(93, 202, 165, 255))
    label_txt = f"{label}: "
    d.text((128, y), label_txt, font=f_item_label, fill=(147, 226, 199, 255))
    lb = d.textbbox((0, 0), label_txt, font=f_item_label)
    d.text((128 + (lb[2] - lb[0]), y), desc, font=f_item_desc, fill=TEXT)
    y += 60

save(img, "09_uebertrag.png")

# 10 Einstiegshilfe (20s)
img, d = base_slide(kicker="So arbeite ich mit dir", seed=10)
img = text_panel(img, (50, 190, 1850, 840))
d = ImageDraw.Draw(img, "RGBA")
d.text((90, 220), "Du entscheidest, wie weit wir gemeinsam gehen:",
       font=font(FONT_REG, 42), fill=(228, 239, 233, 255))

f_stage_label = font(FONT_BOLD, 40)
f_stage_desc = font(FONT_REG, 36)
stages = [
    ("Starthilfe", "Ich helfe dir bei deinen ersten Schritten."),
    ("Planung", "Wir erstellen gemeinsam einen kompletten Plan – ganz auf dich abgestimmt."),
    ("Umsetzung", "Die Umsetzung übernimmst du selbst – oder ich mache sie für dich."),
]
y = 360
for label, desc in stages:
    d.rectangle((90, y + 8, 110, y + 8 + 28), fill=(93, 202, 165, 255))
    d.text((140, y), label, font=f_stage_label, fill=(147, 226, 199, 255))
    end_y = draw_wrapped(d, desc, (140, y + 60), f_stage_desc, TEXT, 1600, line_spacing=1.3)
    y = end_y + 40

checklist_frame = photo_frame(os.path.join(BASE, "photos", "checkboxes.jpg"), 340, 240)
checklist_rot = checklist_frame.rotate(6, expand=True, resample=Image.BICUBIC)
shadow_alpha = checklist_rot.split()[-1].filter(ImageFilter.GaussianBlur(20))
shadow = Image.new("RGBA", checklist_rot.size, (0, 0, 0, 0))
shadow.putalpha(shadow_alpha.point(lambda a: int(a * 0.5)))
clx = 1850 - checklist_rot.width - 20
cly = 700
img = img.convert("RGBA")
img.paste(shadow, (clx + 18, cly + 24), shadow)
img.paste(checklist_rot, (clx, cly), checklist_rot)
img = img.convert("RGB")
save(img, "10_einstieg.png")

# 11 CTA (15s)
img, d = base_slide(seed=11, show_logo_corner=False)
img = text_panel(img, (50, 70, 1250, 1000))
d = ImageDraw.Draw(img, "RGBA")

logo_bg = Image.new("RGBA", (170, 170), (0, 0, 0, 0))
lbd = ImageDraw.Draw(logo_bg)
lbd.ellipse((0, 0, 170, 170), fill=(255, 255, 255, 235))
logo = get_logo(130)
lx = (170 - logo.width) // 2
ly = (170 - logo.height) // 2
logo_bg.paste(logo, (lx, ly), logo)
img = img.convert("RGBA")
img.paste(logo_bg, (90, 110), logo_bg)

# grosses rundes Portraitfoto rechts (webcam_bubble.png - echtes Foto von Franz)
photo_size = 480
webcam = Image.open(os.path.join(BASE, "webcam_bubble.png")).convert("RGBA")
webcam = webcam.resize((photo_size, photo_size), Image.LANCZOS)
ring_pad = 14
ring_size = photo_size + ring_pad * 2
ring = Image.new("RGBA", (ring_size, ring_size), (0, 0, 0, 0))
rd = ImageDraw.Draw(ring)
rd.ellipse((0, 0, ring_size - 1, ring_size - 1), fill=(29, 200, 150, 255))
ring.paste(webcam, (ring_pad, ring_pad), webcam)
shadow_alpha = ring.split()[-1].filter(ImageFilter.GaussianBlur(25))
shadow = Image.new("RGBA", ring.size, (0, 0, 0, 0))
shadow.putalpha(shadow_alpha.point(lambda a: int(a * 0.45)))
rx = 1585 - ring_size // 2
ry = 240  # etwas hoeher, damit unten Platz fuer den QR-Code bleibt
img.paste(shadow, (rx + 16, ry + 22), shadow)
img.paste(ring, (rx, ry), ring)

# QR-Code zum Calendly-Link — Zuschauer koennen Links im Video nicht anklicken
import qrcode
qr = qrcode.QRCode(border=2, box_size=6)
qr.add_data("https://calendly.com/franz-ki-lotse/30min")
qr.make()
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
qr_img = qr_img.resize((190, 190), Image.NEAREST)
qx = 1585 - 95
img.paste(qr_img, (qx, 800), qr_img)

img = img.convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
d.text((qx - 42, 998), "Scannen & Termin buchen", font=font(FONT_REG, 26), fill=SUBTEXT)
d.text((90, 290), "Lass uns reden!", font=font(FONT_BOLD, 80), fill=TEXT)
draw_wrapped(d, "Neugierig, was KI für dich tun könnte?",
             (90, 410), font(FONT_REG, 44), (228, 239, 233, 255), 1600)

y = 530
f_label = font(FONT_BOLD, 38)
f_value = font(FONT_REG, 38)
rows = [
    # "kostenlos" senkt die Huerde — nur "Termin buchen" klang verbindlich
    ("Kostenloses Erstgespräch (30 Min):", "calendly.com/franz-ki-lotse/30min"),
    ("Alle Links:", "linktr.ee/franz.ki.lotse"),
    ("LINE:", "franz.kilotse"),
]
for label, value in rows:
    d.rectangle((90, y + 8, 110, y + 8 + 28), fill=(93, 202, 165, 255))
    d.text((140, y), label, font=f_label, fill=(147, 226, 199, 255))
    d.text((140, y + 55), value, font=f_value, fill=TEXT)
    y += 140

save(img, "11_cta.png")

print("all slides done")
