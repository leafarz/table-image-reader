# table-image-reader
- Test project to read images with table and convert to some sheet format

## Prerequisites
- Python 3.7

## Install (Windows)
- Create virtual environment:
<br>`python -m venv venv`
- Activate virtual environment:
<br>`venv\Scripts\activate.bat`
<br>`venv\Scripts\deactivate.bat` (to deactivate)
- Install packages from requirements:
<br>`pip install -r requirements.txt`
- Note: Tesseract is included in this repo. If you choose to use it, you don't have to follow the next steps.
    - Install Tesseract
        - Install [Tesseract prebuilt binaries](https://github.com/UB-Mannheim/tesseract/wiki)
        - Add installed Tesseract directory to environment variable (ie. Tesseract-OCR folder)
        - Comment out the line which has
        <br>`pytesseract.pytesseract.tesseract_cmd = os.path.join(basedir, 'vendor/Tesseract-OCR/tesseract')`

## Tools used
- VSCode
- Python v3.7
- OpenCV
- Tesseract (v5.0.0-alpha included in this repo, eng language only)