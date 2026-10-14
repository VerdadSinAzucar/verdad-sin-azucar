"""Genera un carrusel vertical para TikTok: portada + frases + cierre.

Uso (desde Python): crear("carpeta", "Título portada", ["frase 1", ...])
"""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from generar_vertical import generar, BASE, FB, FR, YEL, BLACK

W, H = 1080, 1920


def _centrado(d, texto, font, y, fill):
    w = d.textlength(texto, font=font)
    d.text(((W - w) / 2, y), texto, font=font, fill=fill)


def portada(titulo, salida, usuario="@verdad.sinazucar"):
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    av = Image.open(os.path.join(BASE, "assets", "avatar.png")).convert("RGB").resize((360, 360), Image.LANCZOS)
    m = Image.new("L", av.size, 0)
    ImageDraw.Draw(m).ellipse([0, 0, 360, 360], fill=255)
    img.paste(av, ((W - 360) // 2, 470), m)
    f = ImageFont.truetype(FB, 84)
    y = 900
    for i, ln in enumerate(textwrap.wrap(titulo, 18)):
        _centrado(d, ln, f, y, (250, 250, 250) if i == 0 else YEL)
        y += 108
    _centrado(d, "Desliza  >>", ImageFont.truetype(FB, 46), y + 60, YEL)
    _centrado(d, usuario, ImageFont.truetype(FR, 38), 1560, (170, 170, 170))
    img.save(salida, quality=92)


def cierre(salida, usuario="@verdad.sinazucar"):
    img = Image.new("RGB", (W, H), YEL)
    d = ImageDraw.Draw(img)
    av = Image.open(os.path.join(BASE, "assets", "avatar.png")).convert("RGB").resize((300, 300), Image.LANCZOS)
    m = Image.new("L", av.size, 0)
    ImageDraw.Draw(m).ellipse([0, 0, 300, 300], fill=255)
    img.paste(av, ((W - 300) // 2, 560), m)
    f = ImageFont.truetype(FB, 72)
    _centrado(d, "¿Cuál te dolió más?", f, 940, BLACK)
    _centrado(d, "Sígueme para más", ImageFont.truetype(FB, 54), 1060, BLACK)
    _centrado(d, "verdades sin azúcar", ImageFont.truetype(FB, 54), 1130, BLACK)
    _centrado(d, usuario, ImageFont.truetype(FR, 42), 1260, (40, 40, 40))
    img.save(salida, quality=92)


def crear(carpeta, titulo, frases, usuario="@verdad.sinazucar"):
    os.makedirs(carpeta, exist_ok=True)
    portada(titulo, os.path.join(carpeta, "01_portada.jpg"), usuario)
    for i, fr in enumerate(frases, 2):
        pie = "Desliza  >>"
        generar(fr, os.path.join(carpeta, f"{i:02d}_frase.jpg"), pie=pie, usuario=usuario)
    cierre(os.path.join(carpeta, f"{len(frases) + 2:02d}_cierre.jpg"), usuario)
