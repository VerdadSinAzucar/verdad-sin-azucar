"""Imagen vertical 1080x1920 (historias de Instagram/Facebook y carruseles de TikTok).

Uso: python3 generar_vertical.py "Texto de la frase" salida.jpg [--pie "texto abajo"]
"""
import os
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "assets", "fonts")
FB = os.path.join(FONTS, "Poppins-Bold.ttf")
FR = os.path.join(FONTS, "Poppins-Regular.ttf")
FM = os.path.join(FONTS, "Poppins-Medium.ttf")

S = 2
W, H = 1080 * S, 1920 * S
INK = (20, 20, 20)
GRAY = (110, 110, 110)
YEL = (255, 214, 10)
BLACK = (17, 17, 17)


def generar(texto, salida, pie="Más verdades en @verdad.sinazucar"):
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    # Tarjeta blanca tipo tuit centrada (zona segura: deja libres arriba y abajo para la interfaz)
    n = len(texto)
    size, wrap = (54, 26) if n <= 140 else (48, 29) if n <= 220 else (42, 33)
    body = ImageFont.truetype(FM, size * S)
    lines = []
    for para in texto.split("\n"):
        lines += textwrap.wrap(para, wrap) or [""]
    lh = int(size * 1.45) * S
    pad = 70 * S
    card_w = 940 * S
    card_h = pad * 2 + 150 * S + len(lines) * lh
    cx0 = (W - card_w) // 2
    cy0 = (H - card_h) // 2 - 40 * S
    d.rounded_rectangle([cx0, cy0, cx0 + card_w, cy0 + card_h], radius=40 * S, fill=YEL)
    d.rounded_rectangle([cx0, cy0, cx0 + card_w, cy0 + card_h - 22 * S], radius=40 * S, fill=(255, 255, 255),
                        corners=(True, True, False, False))
    # cabecera
    x0, y0 = cx0 + pad, cy0 + pad
    avatar = Image.open(os.path.join(BASE, "assets", "avatar.png")).convert("RGB")
    a = avatar.resize((110 * S, 110 * S), Image.LANCZOS)
    mask = Image.new("L", a.size, 0)
    ImageDraw.Draw(mask).ellipse([0, 0, a.size[0], a.size[1]], fill=255)
    img.paste(a, (x0, y0), mask)
    d.text((x0 + 135 * S, y0 + 14 * S), "Verdad Sin Azúcar", font=ImageFont.truetype(FB, 40 * S), fill=INK)
    d.text((x0 + 135 * S, y0 + 62 * S), "@verdad.sinazucar", font=ImageFont.truetype(FR, 31 * S), fill=GRAY)
    y = y0 + 150 * S
    for ln in lines:
        d.text((x0, y), ln, font=body, fill=INK)
        y += lh
    # pie
    if pie:
        f = ImageFont.truetype(FB, 38 * S)
        w = d.textlength(pie, font=f)
        d.text(((W - w) / 2, cy0 + card_h + 70 * S), pie, font=f, fill=YEL)
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    img.resize((1080, 1920), Image.LANCZOS).save(salida, quality=90)


if __name__ == "__main__":
    args = sys.argv[1:]
    pie = "Más verdades en @verdad.sinazucar"
    if "--pie" in args:
        i = args.index("--pie")
        pie = args[i + 1]
        del args[i:i + 2]
    generar(args[0], args[1], pie)
    print("ok", args[1])
