import psutil
import subprocess
import time
import pyautogui
from cryptography.fernet import Fernet

def is_gateway_running():
    # Process name to look for (adjust if needed based on the exact name from Task Manager)
    target_process_name = "ibgateway.exe"
    
    for process in psutil.process_iter():
        try:
            if target_process_name in process.name():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def start_gateway():
    ib_gateway_path = r"C:\Jts\ibgateway\1024\ibgateway.exe"
    subprocess.Popen(ib_gateway_path)  # Removed the argument since it's probably unnecessary

def load_key():
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

def login_to_gateway():
    coordinate_x = 954
    coordinate_y = 1909

    pyautogui.click(x=coordinate_x, y=coordinate_y)
    
    time.sleep(2)
    
    pyautogui.write(username)
    pyautogui.press('tab')  
    
    pyautogui.write(password)
    pyautogui.press('enter')  

# Load encrypted credentials
with open("encrypted_credentials.txt", "rb") as file:
    lines = file.readlines()
    encrypted_username = lines[0].strip()
    encrypted_password = lines[1].strip()

key = load_key()
username = decrypt_message(encrypted_username, key)
password = decrypt_message(encrypted_password, key)

# Main loop
while True:
    if not is_gateway_running():
        print("IBKR Gateway is not running. Starting it...")
        start_gateway()
        
        # Add a bit more wait time for the app to fully launch
        time.sleep(10)
        login_to_gateway()
    else:
        print("IBKR Gateway is running.")
    
    # Check every minute
    time.sleep(10)
