"""Crea el carrusel de TikTok del día en tiktok/AAAA-MM-DD/.

Uso: python3 tiktok_diario.py AAAA-MM-DD "Título de portada" "frase 1" "frase 2" "frase 3" "frase 4"
"""
import os
import sys
from tiktok_carrusel import crear

# Usuario actual de TikTok. Cambiar a "@verdad.sinazucar" cuando se corrija en la app (tras el 13-nov-2026).
USUARIO_TIKTOK = "@verdad.sinazcar"

if __name__ == "__main__":
    fecha, titulo, *frases = sys.argv[1:]
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tiktok", fecha)
    crear(carpeta, titulo, frases, usuario=USUARIO_TIKTOK)
    for f in sorted(os.listdir(carpeta)):
        print(f"tiktok/{fecha}/{f}")
