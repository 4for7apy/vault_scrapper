import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlsplit
import os
from collections import deque
from utils import normalize_url, is_valid_url, log
from downloader import download_file

def crawl(start_url, start_depth, max_depth, download_dir):
    visited = set()
    queue = deque()
    queue.append((start_url, start_depth))

    def get_extension(url):
        path = urlsplit(url).path
        ext = os.path.splitext(path)[1].lower()
        return ext

    while queue:
        url, depth = queue.popleft()
        if depth > max_depth or url in visited:
            continue
        visited.add(url)
        try:
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            log(f"Failed to fetch {url}: {e}")
            continue
        content_type = resp.headers.get('content-type', '')
        ext = get_extension(url)
        # Download any file with an extension (not just specific types)
        if ext:
            log(f"Attempting to download valuable file: {url}")
            download_file(url, download_dir)
            continue
        if 'text/html' in content_type:
            soup = BeautifulSoup(resp.text, "html.parser")
            # Extract from <a> tags
            for link in soup.find_all("a", href=True):
                href = link['href']
                next_url = normalize_url(url, href)
                log(f"Found link: {next_url}")
                if is_valid_url(next_url) and next_url not in visited:
                    queue.append((next_url, depth + 1))
            # Extract from <iframe> and <embed> tags
            for tag in soup.find_all(['iframe', 'embed']):
                src = tag.get('src')
                if src:
                    pdf_url = normalize_url(url, src)
                    log(f"Found embedded file: {pdf_url}")
                    if is_valid_url(pdf_url):
                        # Check for 'file' query parameter
                        parsed = urlsplit(pdf_url)
                        query_params = dict([param.split('=', 1) for param in parsed.query.split('&') if '=' in param])
                        real_file_url = query_params.get('file')
                        if real_file_url:
                            log(f"Found real embedded file: {real_file_url}")
                            ext = get_extension(real_file_url)
                            if ext:
                                log(f"Attempting to download embedded valuable file: {real_file_url}")
                                download_file(real_file_url, download_dir)
                        else:
                            ext = get_extension(pdf_url)
                            if ext:
                                log(f"Attempting to download embedded valuable file: {pdf_url}")
                                download_file(pdf_url, download_dir) 