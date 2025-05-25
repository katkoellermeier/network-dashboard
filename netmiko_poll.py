from netmiko import ConnectHandler
import yaml
from concurrent.futures import ThreadPoolExecutor
from logger import log_success, log_failure

def poll_device(device):
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("show ip interface brief")
        log_success(device["host"], output)
        conn.disconnect()
    except Exception as e:
        log_failure(device["host"], str(e))

def poll_all_devices():
    with open("inventory.yaml") as f:
        inventory = yaml.safe_load(f)["devices"]
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(poll_device, inventory)
