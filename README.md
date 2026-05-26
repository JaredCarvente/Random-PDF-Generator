<div align="center">

# 📄 Random PDF Generator

**Bulk PDF document generator for load testing and system validation environments**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![ReportLab](https://img.shields.io/badge/ReportLab-4.x-0078D4?style=for-the-badge)](https://www.reportlab.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintenance-Active-22C55E?style=for-the-badge)]()

</div>

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Target Audience](#target-audience)
4. [System Requirements](#system-requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [CLI Parameters](#cli-parameters)
8. [Examples](#examples)
9. [Project Structure](#project-structure)

---

## Overview

**Random PDF Generator** is a Python command-line tool that automatically generates large volumes of PDF files with random readable text content and configurable file sizes.

Its primary purpose is to meet the need for realistic, high-volume PDF datasets during **load testing**, **performance validation**, and **storage capacity assessments** in document management systems (DMS), ECM platforms, and any file-processing infrastructure.

---

## Features

| Feature | Description |
|---|---|
| 📦 **Bulk generation** | Creates N PDF documents in a single execution |
| 📏 **Controlled file size** | Each file is randomly sized within the configured MB range |
| 🔤 **Valid content** | PDFs contain human-readable random text (not binary garbage) |
| 🏷️ **Custom naming** | File names follow the pattern `<PREFIX>-<NUMBER>.pdf` |
| 📊 **Progress bar** | Real-time visual tracking powered by `tqdm` |
| 📁 **Configurable output** | Destination folder is user-defined and auto-created if missing |

---

## Target Audience

This tool is aimed at technical profiles working in environments that require realistic document load simulation:

- **QA Engineers and Testers** who need to generate test datasets for document management systems.
- **Solution Architects and DevOps Engineers** conducting stress tests on file storage or management platforms.
- **Backend Developers** integrating or validating PDF processing APIs.
- **System Administrators** evaluating the capacity and performance of file servers or databases.

---

## System Requirements

- **Python** 3.8 or higher
- **pip** (Python package manager)
- Operating system: Windows, macOS, or Linux

### Dependencies

| Package | Version | Purpose |
|---|---|---|
| `reportlab` | 4.4.5 | PDF generation and rendering |
| `tqdm` | 4.67.1 | Console progress bar |
| `pillow` | 12.0.0 | Image support for ReportLab |
| `charset-normalizer` | 3.4.4 | Text encoding normalization |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JaredCarvente/Random-PDF-Generator.git
cd Random-PDF-Generator
```

### 2. (Optional) Create a virtual environment

Using a virtual environment is recommended to isolate project dependencies:

```bash
# Create the virtual environment
python -m venv venv

# Activate on Linux / macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

The script is executed from the command line using `generar_pdfs.py`. All parameters are required.

```bash
python generar_pdfs.py --cantidad <N> --tmin <MB> --tmax <MB> --patron <PREFIX> --salida <FOLDER>
```

---

## CLI Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `--cantidad` | `int` | ✅ | Total number of PDF documents to generate |
| `--tmin` | `int` | ✅ | Minimum file size per document in megabytes (MB) |
| `--tmax` | `int` | ✅ | Maximum file size per document in megabytes (MB) |
| `--patron` | `str` | ✅ | Prefix used in the generated file names |
| `--salida` | `str` | ✅ | Output folder path where PDFs will be saved |

> **Note:** The final size of each file is randomly chosen within the `[tmin, tmax]` range. File names are generated using the format `<patron>-<5 random digits>.pdf`.

---

## Examples

### Generate 10 documents between 1 and 3 MB

```bash
python generar_pdfs.py --cantidad 10 --tmin 1 --tmax 3 --patron DOCUMENT --salida ./output
```

### Generate 50 documents with a corporate prefix

```bash
python generar_pdfs.py --cantidad 50 --tmin 2 --tmax 5 --patron LOAD_REPORT --salida ./tests/batch_01
```

### Expected console output

```
📄 Generating 10 PDF documents...
File size range: 1 MB - 3 MB
Output folder: ./output

Progress: 100%|██████████████████████████| 10/10 [00:42<00:00,  4.2s/pdf]

✅ Process complete. PDFs generated successfully.
```

### Generated file structure

```
output/
├── DOCUMENT-47821.pdf
├── DOCUMENT-13904.pdf
├── DOCUMENT-82617.pdf
└── ...
```

---

## Project Structure

```
Random-PDF-Generator/
├── generar_pdfs.py      # Main PDF generation script
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

<div align="center">

Built for document system testing and validation purposes.

</div>
