# Barcode Scanner form Images

A small python practice project that detects and decodes barcodes from images using OpenCV and pyzbar.

## Features

- Reads barcode images
- Detects barcode data
- Extracts barcode data
- Displays the barcode type and decodes value
- Draws a bounding box around detected barcodes

## Requirements

- python 3
- OpenCV
- pyzbar

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python barcode_scanner_image.py -i "path/to/image.png"
```

### Example
```bash
python barcode_scanner_image.py -i "Sample Images/HP.png"
```