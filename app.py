from netmiko_poll import poll_all_devices
from api_client import poll_apis
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Starting network device dashboard...")
    poll_all_devices()
    poll_apis()

if __name__ == "__main__":
    main()
