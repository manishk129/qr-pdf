# QRCodeOnSheet Documentation

## Overview
`QRCodeOnSheet` is a class used to generate a PDF file containing QR codes arranged in a grid. This document provides various examples of how to use it for different PDF layouts.

## Installation
Ensure you have the required package installed:

```sh
pip install qr-pdf
```

## Usage Examples

### 1. Basic QR Code PDF (Single QR Code)
```python
from qr-pdf import QRCodeOnSheet

values = ["https://example.com"]
qr_sheet = QRCodeOnSheet(values)
qr_sheet.generate_pdf()
```
This creates a PDF containing a single QR code.

### 2. Generating a Grid of QR Codes
```python
values = ["QR1", "QR2", "QR3", "QR4"]
qr_sheet = QRCodeOnSheet(values, rows_count=2, cols_count=2)
qr_sheet.generate_pdf()
```
This generates a 2x2 grid of QR codes.

### 3. Customizing Margin and Padding
```python
values = ["Custom Margin"]
qr_sheet = QRCodeOnSheet(values, rows_count=1, cols_count=1, margin=10, padding=6)
qr_sheet.generate_pdf()
```
This creates a single QR code with a larger margin and padding.

### 4. Saving PDF with a Custom Name
```python
values = ["Named PDF"]
qr_sheet = QRCodeOnSheet(values, file_name="custom_qr.pdf")
qr_sheet.generate_pdf()
```
This saves the generated PDF with the specified filename.

## Notes
- The default output filename is auto-generated if `file_name` is not provided.

## List of Keyword Arguments (kwargs)
Below are the keyword arguments that can be passed to the `QRCodeOnSheet` class:

- `values` (List[str]): List of data values to be encoded as QR codes.
- `rows_count` (int): Number of rows in the grid (default is 1).
- `cols_count` (int): Number of columns in the grid (default is 1).
- `file_name` (Optional[str]): Name of the output PDF file (default is None).
- `margin` (int): Margin percentage around the QR codes (default is 5).
- `padding` (int): Padding percentage between QR codes (default is 4).

## Conclusion
The `QRCodeOnSheet` class provides a flexible way to generate QR codes in a PDF file with customizable grid sizes, margins, and file names. Experiment with different parameters to fit your requirements.

