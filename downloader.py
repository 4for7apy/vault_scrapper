import os
import requests
from urllib.parse import urlparse
from utils import ensure_dir, log

def download_file(url, download_dir):
    parsed = urlparse(url)
    local_path = os.path.join(download_dir, parsed.netloc, parsed.path.lstrip('/'))
    ensure_dir(os.path.dirname(local_path))
    if os.path.exists(local_path):
        log(f"Already downloaded: {url}")
        return
    try:
        with requests.get(url, stream=True, timeout=30) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        log(f"Downloaded: {url}")
    except Exception as e:
        log(f"Failed to download {url}: {e}") 