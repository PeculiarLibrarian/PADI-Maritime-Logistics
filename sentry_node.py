import os
import json
import requests

def run_audit():
    PC_IP = "192.168.1.10"
    url = f"http://{PC_IP}:8000"
    print("[%] Running SOVEREIGN AUDIT...")
    payload = {"node": "NAIROBI-01", "status": "VERIFIED"}
    try:
        r = requests.post(url, json=payload, timeout=5)
        print(f"[%] Relay: {r.status_code}")
    except Exception as e:
        print(f"[!] Failure: {e}")

if name == "main__":
    run_audit()
