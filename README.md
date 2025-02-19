# QR Code Generator and PDF Creator 📄✨

## Project Description
This project generates **QR codes** from a list of values and arranges them in a **PDF file**. You can configure the number of rows and columns, margins, and padding to customize the layout of the QR codes on the PDF. Each QR code is generated using the **`qrcode`** library and then embedded in a **PDF file** using **`reportlab`**.

### Key Features
- Generate individual QR codes with custom data.
- Save QR codes in a **single-page or multi-page** PDF format.
- Configure rows, columns, margins, and padding for grid-based QR code generation.
- Supports generating high-quality QR codes with custom sizes and error correction.

### Usage 
- To know more about how to use it : Please refer to the [Usage doc](https://github.com/manishk129/qr-pdf/blob/main/doc/usage.md)
---

## Installation

### Prerequisites
- Python 3.6
- **`qrcode`** library (`pip install qrcode[pil]`)
- **`reportlab`** library (`pip install reportlab`)

### Installation Steps
1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/manishk129/qr-code-pdf-generator.git
