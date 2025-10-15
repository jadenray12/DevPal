# cli/server.py (new helper file)
import subprocess
import requests

SERVER_URL = "http://127.0.0.1:8000"

def start_server_if_needed():
    try:
        requests.get(SERVER_URL)
        print("Server already running!")
        return
    except requests.ConnectionError:
        print("Starting local DevPal server...")

    # Start server as a background process
    subprocess.Popen(
        ["uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8000", '--reload'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("Server started!")
