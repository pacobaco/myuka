# rotate_onion.py
from stem.control import Controller
import shutil, os

HS_DIR = "/tmp/rotator_hs"

def rotate_hidden_service():
    if os.path.exists(HS_DIR):
        shutil.rmtree(HS_DIR)

    with Controller.from_port(port=9051) as ctl:
        ctl.authenticate()
        result = ctl.create_hidden_service(HS_DIR, 80, target_port=8080, await_publication=True)
        addr = f"{result.service_id}.onion"
        print(f"[+] New onion address: http://{addr}")
        return addr

if __name__ == "__main__":
    rotate_hidden_service()