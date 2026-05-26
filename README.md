<div align="center">

# 📄 Random PDF Generator

**Generador masivo de documentos PDF para entornos de prueba y validación de sistemas**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![ReportLab](https://img.shields.io/badge/ReportLab-4.x-0078D4?style=for-the-badge)](https://www.reportlab.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Mantenimiento-Activo-22C55E?style=for-the-badge)]()

</div>

---

## Índice

1. [Descripción general](#descripción-general)
2. [Características](#características)
3. [Dirigido a](#dirigido-a)
4. [Requisitos del sistema](#requisitos-del-sistema)
5. [Instalación](#instalación)
6. [Uso](#uso)
7. [Parámetros de la CLI](#parámetros-de-la-cli)
8. [Ejemplos de uso](#ejemplos-de-uso)
9. [Estructura del proyecto](#estructura-del-proyecto)

---

## Descripción general

**Random PDF Generator** es una herramienta de línea de comandos desarrollada en Python que permite generar de forma masiva y automatizada archivos PDF con contenido de texto aleatorio y tamaño configurable.

Su propósito principal es satisfacer la necesidad de contar con grandes volúmenes de documentos PDF realistas durante las etapas de **pruebas de carga**, **validación de rendimiento** y **verificación de capacidad de almacenamiento** en sistemas de gestión documental (DMS), plataformas ECM y cualquier infraestructura orientada al procesamiento de archivos.

---

## Características

| Característica | Descripción |
|---|---|
| 📦 **Generación masiva** | Crea N documentos PDF en una sola ejecución |
| 📏 **Tamaño controlado** | Cada archivo tiene un tamaño aleatorio dentro del rango MB configurado |
| 🔤 **Contenido válido** | Los PDFs incluyen texto aleatorio legible (no binario) |
| 🏷️ **Nomenclatura personalizable** | Los nombres siguen el patrón `<PATRON>-<NUMERO>.pdf` |
| 📊 **Barra de progreso** | Seguimiento visual en tiempo real mediante `tqdm` |
| 📁 **Directorio de salida** | Carpeta de destino configurable; se crea automáticamente si no existe |

---

## Dirigido a

Esta herramienta está orientada a perfiles técnicos que trabajan en entornos donde se requiere simular condiciones reales de carga documental:

- **Ingenieros de QA y Testers** que necesitan generar conjuntos de datos de prueba para sistemas documentales.
- **Arquitectos de soluciones y DevOps** que realizan pruebas de estrés en plataformas de almacenamiento o gestión de archivos.
- **Desarrolladores de backend** que integran o validan APIs de procesamiento de documentos PDF.
- **Administradores de sistemas** que evalúan la capacidad y rendimiento de servidores de archivos o bases de datos.

---

## Requisitos del sistema

- **Python** 3.8 o superior
- **pip** (gestor de paquetes de Python)
- Sistema operativo: Windows, macOS o Linux

### Dependencias

| Paquete | Versión | Función |
|---|---|---|
| `reportlab` | 4.4.5 | Generación y renderizado de archivos PDF |
| `tqdm` | 4.67.1 | Barra de progreso en consola |
| `pillow` | 12.0.0 | Soporte de imágenes para ReportLab |
| `charset-normalizer` | 3.4.4 | Normalización de codificación de texto |

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JaredCarvente/Random-PDF-Generator.git
cd Random-PDF-Generator
```

### 2. (Opcional) Crear un entorno virtual

Se recomienda el uso de un entorno virtual para aislar las dependencias del proyecto:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Linux / macOS
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Uso

El script se ejecuta desde la línea de comandos utilizando el archivo `generar_pdfs.py`. Todos los parámetros son obligatorios.

```bash
python generar_pdfs.py --cantidad <N> --tmin <MB> --tmax <MB> --patron <PREFIJO> --salida <CARPETA>
```

---

## Parámetros de la CLI

| Parámetro | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `--cantidad` | `int` | ✅ | Número total de documentos PDF a generar |
| `--tmin` | `int` | ✅ | Tamaño mínimo por documento en megabytes (MB) |
| `--tmax` | `int` | ✅ | Tamaño máximo por documento en megabytes (MB) |
| `--patron` | `str` | ✅ | Prefijo para los nombres de los archivos generados |
| `--salida` | `str` | ✅ | Ruta de la carpeta donde se guardarán los PDFs |

> **Nota:** El tamaño final de cada archivo es seleccionado aleatoriamente dentro del rango `[tmin, tmax]`. Los nombres se generan con el formato `<patron>-<5 dígitos aleatorios>.pdf`.

---

## Ejemplos de uso

### Generar 10 documentos de entre 1 y 3 MB

```bash
python generar_pdfs.py --cantidad 10 --tmin 1 --tmax 3 --patron DOCUMENTO --salida ./salida
```

### Generar 50 documentos con prefijo corporativo

```bash
python generar_pdfs.py --cantidad 50 --tmin 2 --tmax 5 --patron INFORME_CARGA --salida ./pruebas/batch_01
```

### Ejemplo de salida en consola

```
📄 Generando 10 documentos PDF...
Tamaño por archivo: 1 MB - 3 MB
Carpeta de salida: ./salida

Progreso: 100%|██████████████████████████| 10/10 [00:42<00:00,  4.2s/pdf]

✅ Proceso completado. PDFs generados correctamente.
```

### Archivos generados

```
salida/
├── DOCUMENTO-47821.pdf
├── DOCUMENTO-13904.pdf
├── DOCUMENTO-82617.pdf
└── ...
```

---

## Estructura del proyecto

```
Random-PDF-Generator/
├── generar_pdfs.py      # Script principal de generación de PDFs
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```

---

<div align="center">

Desarrollado con fines de prueba y validación de sistemas documentales.

</div>
