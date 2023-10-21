import pyautogui
import time
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Load the encrypted credentials
with open("encrypted_credentials.txt", "rb") as file:
    lines = file.readlines()
    encrypted_username = lines[0].strip()
    encrypted_password = lines[1].strip()

key = load_key()
username = decrypt_message(encrypted_username, key)
password = decrypt_message(encrypted_password, key)

def login_to_gateway():
    # This part might need adjustments based on your screen resolution, application position, etc.
    pyautogui.click(x=coordinate_x, y=coordinate_y)  # Position where the login window is
    
    time.sleep(2)  # Adjust as needed
    
    pyautogui.write(username)
    pyautogui.press('tab')  
    
    pyautogui.write(password)
    pyautogui.press('enter')  

login_to_gateway()
