# Detects if a client is being forced to use http
import requests

urls = ["http://google.com", "https://google.com"]

for url in urls:
    try:
        r = requests.get(url)
        if not r.url.startswith("https://"):
            print(f"[!] SSL Strip suspected: redirected to {r.url}")
    except Exception as e:
        print(f"Error checking {url}: {e}")

