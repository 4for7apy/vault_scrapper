import os
from urllib.parse import urljoin, urlparse

def normalize_url(base, link):
    return urljoin(base, link)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def is_valid_url(url):
    return urlparse(url).scheme in ("http", "https")

def log(msg):
    print(f"[vault_scrapper] {msg}") 