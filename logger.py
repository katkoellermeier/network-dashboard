from datetime import datetime
import os

def log_success(source, output):
    os.makedirs("logs", exist_ok=True)
    with open("logs/success.log", "a") as f:
        f.write(f"[{datetime.now()}] SUCCESS [{source}]\n{output}\n\n")

def log_failure(source, error):
    os.makedirs("logs", exist_ok=True)
    with open("logs/failure.log", "a") as f:
        f.write(f"[{datetime.now()}] ERROR [{source}]\n{error}\n\n")
