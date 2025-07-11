# publish_region.py
import os
from content_generator import generate_content
from stem.control import Controller
from datetime import datetime

REGION = os.getenv("REGION", "generic")
HS_DIR = f"/tmp/hs_{REGION}"

def rotate_hidden_service():
    if os.path.exists(HS_DIR):
        os.system(f"rm -rf {HS_DIR}")

    with Controller.from_port(port=9051) as ctl:
        ctl.authenticate()
        result = ctl.create_hidden_service(HS_DIR, 80, target_port=8080, await_publication=True)
        return f"{result.service_id}.onion"

def write_site(content):
    os.makedirs(f"regions/{REGION}", exist_ok=True)
    with open(f"regions/{REGION}/index.html", "w") as f:
        f.write(content)

def log_onion(onion_url):
    log_entry = f"{datetime.utcnow()},{REGION},{onion_url}\n"
    with open("logs/published_sites.csv", "a") as log:
        log.write(log_entry)

def main():
    html = generate_content(REGION)
    write_site(html)
    onion_url = rotate_hidden_service()
    log_onion(onion_url)
    print(f"[{REGION}] Published to: http://{onion_url}")

if __name__ == "__main__":
    main()