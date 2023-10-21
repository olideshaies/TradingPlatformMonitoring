import psutil
import subprocess
import time

def is_gateway_running():
    # Check if 'IBGateway' process is running
    for process in psutil.process_iter():
        try:
            if "IBGateway" in process.name():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def start_gateway():
    # Path to the IBKR Gateway executable. Adjust as necessary.
    ib_gateway_path = "C:\\path\\to\\IBGateway.exe"
    subprocess.Popen(ib_gateway_path)

while True:
    if not is_gateway_running():
        print("IBKR Gateway is not running. Starting it...")
        start_gateway()
    else:
        print("IBKR Gateway is running.")

    time.sleep(60)  # Check every minute
