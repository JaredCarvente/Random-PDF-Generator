#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para generar múltiples archivos PDF con tamaño aproximado.
Cumple con requisitos para pruebas de carga en un sistema de gestión documental.

Características:
- Genera N documentos PDF.
- Cada documento tendrá un tamaño aproximado entre T_MIN y T_MAX megabytes.
- Cada documento incluye texto aleatorio válido para asegurar que el PDF sea legible.
- Los nombres siguen un patrón suministrado por el usuario, incluyendo un número aleatorio.
- Muestra una barra de progreso durante la generación.

Requisitos:
    pip install reportlab tqdm

Ejecución:
    python generar_pdfs.py --cantidad 50 --tmin 1 --tmax 3 --patron FILE_NAME --salida ./pdfs
"""

import os
import argparse
import random
import string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from tqdm import tqdm


def generar_texto_aleatorio(size_bytes: int) -> str:
    """
    Genera texto aleatorio aproximado para cumplir un tamaño específico.

    Args:
        size_bytes (int): Cantidad aproximada de bytes a generar.

    Returns:
        str: Texto aleatorio.
    """
    caracteres = string.ascii_letters + string.digits + " "
    # Generamos un texto suficientemente largo.
    texto = ''.join(random.choice(caracteres) for _ in range(size_bytes))
    return texto


def crear_pdf(ruta: str, tam_min_mb: int, tam_max_mb: int) -> None:
    """
    Crea un archivo PDF con un tamaño aproximado dentro del rango especificado.

    Args:
        ruta (str): Ruta completa donde guardar el PDF.
        tam_min_mb (int): Tamaño mínimo en MB.
        tam_max_mb (int): Tamaño máximo en MB.
    """
    size_mb = random.randint(tam_min_mb, tam_max_mb)
    size_bytes = size_mb * 1024 * 1024

    texto = generar_texto_aleatorio(size_bytes)

    c = canvas.Canvas(ruta, pagesize=LETTER)

    # Escribimos texto fragmentado en múltiples líneas
    linea = 0
    max_lineas_por_pagina = 50
    for i in range(0, len(texto), 100):
        fragmento = texto[i:i + 100]
        y = 750 - (linea * 14)
        c.drawString(40, y, fragmento)
        linea += 1

        if linea >= max_lineas_por_pagina:
            c.showPage()
            linea = 0

    c.save()


def nombre_pdf(patron: str) -> str:
    """
    Genera un nombre de archivo basado en un patrón más un número aleatorio.

    Args:
        patron (str): Prefijo del documento.

    Returns:
        str: Nombre final del PDF.
    """
    numero = random.randint(10000, 99999)
    return f"{patron}-{numero}.pdf"


def main():
    parser = argparse.ArgumentParser(description="Generador de PDFs para pruebas de carga.")
    parser.add_argument("--cantidad", type=int, required=True, help="Cantidad de documentos PDF a generar.")
    parser.add_argument("--tmin", type=int, required=True, help="Tamaño mínimo por documento (MB).")
    parser.add_argument("--tmax", type=int, required=True, help="Tamaño máximo por documento (MB).")
    parser.add_argument("--patron", type=str, required=True, help="Patrón para el nombre de los documentos.")
    parser.add_argument("--salida", type=str, required=True, help="Carpeta de salida para los PDF generados.")

    args = parser.parse_args()

    # Crear carpeta de salida si no existe
    os.makedirs(args.salida, exist_ok=True)

    print(f"\n📄 Generando {args.cantidad} documentos PDF...")
    print(f"Tamaño por archivo: {args.tmin} MB - {args.tmax} MB")
    print(f"Carpeta de salida: {args.salida}\n")

    for _ in tqdm(range(args.cantidad), desc="Progreso", unit="pdf"):
        nombre = nombre_pdf(args.patron)
        ruta_pdf = os.path.join(args.salida, nombre)
        crear_pdf(ruta_pdf, args.tmin, args.tmax)

    print("\n✅ Proceso completado. PDFs generados correctamente.\n")


if __name__ == "__main__":
    main()
