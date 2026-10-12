"""Genera una imagen tipo tuit de Verdad Sin Azúcar.

Uso: python3 generar.py "Texto de la frase" posts/nombre.jpg
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
W = H = 1080 * S
INK = (20, 20, 20)
GRAY = (110, 110, 110)
YEL = (255, 214, 10)


def generar(texto, salida):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    # Texto más largo -> letra un poco más pequeña
    n = len(texto)
    size, wrap = (50, 30) if n <= 140 else (44, 34) if n <= 220 else (38, 40)
    body = ImageFont.truetype(FM, size * S)
    lines = []
    for para in texto.split("\n"):
        lines += textwrap.wrap(para, wrap) or [""]
    lh = int(size * 1.48) * S
    block = 160 * S + len(lines) * lh
    top = max(60 * S, (H - block) // 2)
    x0 = 110 * S
    avatar = Image.open(os.path.join(BASE, "assets", "avatar.png")).convert("RGB")
    a = avatar.resize((120 * S, 120 * S), Image.LANCZOS)
    mask = Image.new("L", a.size, 0)
    ImageDraw.Draw(mask).ellipse([0, 0, a.size[0], a.size[1]], fill=255)
    img.paste(a, (x0, top), mask)
    d.text((x0 + 145 * S, top + 18 * S), "Verdad Sin Azúcar", font=ImageFont.truetype(FB, 40 * S), fill=INK)
    d.text((x0 + 145 * S, top + 68 * S), "@verdad.sinazucar", font=ImageFont.truetype(FR, 32 * S), fill=GRAY)
    y = top + 160 * S
    for ln in lines:
        d.text((x0, y), ln, font=body, fill=INK)
        y += lh
    d.rectangle([0, H - 14 * S, W, H], fill=YEL)
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    img.resize((1080, 1080), Image.LANCZOS).save(salida, quality=90)


if __name__ == "__main__":
    generar(sys.argv[1], sys.argv[2])
    print("ok", sys.argv[2])
