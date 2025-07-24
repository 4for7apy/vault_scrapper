# Vault Scrapper

A professional recursive file downloader for legal, finance, and tax documents (and any other files) from the web.

## Features
- Recursively downloads all files from a starting URL, up to 4 levels deep
- Skips HTML pages, only downloads files (PDF, DOC, XLS, images, etc.)
- Modular, production-quality Python code

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your starting URL in `config.py`:
   ```python
   START_URL = "https://example.com"
   ```
3. Run the script:
   ```bash
   python main.py
   ```

All files will be saved in the `downloaded_files` directory, preserving folder structure.

---

**Extendable:**
- Add keyword classification, authentication, or other features as needed. 