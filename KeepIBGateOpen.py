import psutil
import subprocess
import time
import pyautogui
from cryptography.fernet import Fernet

def is_IB_app_running(running_app):
    if running_app == "TWS":
        target_process_name = "tws.exe"
    elif running_app == "Gateway":
        target_process_name = "ibgateway.exe"
    
    for process in psutil.process_iter():
        try:
            if target_process_name in process.name():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def start_IB_app(running_app):
    # Need to add the option to open based on the IB app used (TWS or Gateway)
    if running_app == "TWS":
        ib_gateway_path = r"C:\Jts\tws.exe"
    elif running_app == "Gateway":
        ib_gateway_path = r"C:\Jts\ibgateway\1024\ibgateway.exe"
    subprocess.Popen(ib_gateway_path)  # Removed the argument since it's probably unnecessary

def load_key():
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

def login_to_IB_app(running_app):
    if running_app == "TWS":
        # Coordinates for the Paper Trading
        coordinate_x = 801
        coordinate_y = 454
    elif running_app == "Gateway":
        # Coordinates for the Paper Trading
        coordinate_x = 801
        coordinate_y = 454

    pyautogui.click(x=coordinate_x, y=coordinate_y)
    
    time.sleep(1)
    
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

running_app = input("Which IB app are you using? (TWS or Gateway): ")

# Main loop
while True:
    if not is_IB_app_running(running_app):
        print("IBKR Gateway is not running. Starting it...")
        start_IB_app(running_app)
        
        # Add a bit more wait time for the app to fully launch
        if running_app == "TWS":
            time.sleep(5)
        elif running_app == "Gateway":
            time.sleep(3)
        login_to_IB_app(running_app)
    else:
        print("IB App is running.")
    
    # Check every minute
    time.sleep(3)
