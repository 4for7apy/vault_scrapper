from config import START_URL, MAX_DEPTH, DOWNLOAD_DIR
from crawler import crawl
from utils import ensure_dir, log

def main():
    ensure_dir(DOWNLOAD_DIR)
    log(f"Starting crawl at {START_URL} (max depth {MAX_DEPTH})")
    crawl(START_URL, 1, MAX_DEPTH, DOWNLOAD_DIR)

if __name__ == "__main__":
    main() 