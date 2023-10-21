from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Only run the generation of the key ONCE. Store this key securely.
#generate_key()

key = load_key()

username = "olilechef13"
password = "Olivier13!"

encrypted_username = encrypt_message(username, key)
encrypted_password = encrypt_message(password, key)

with open("encrypted_credentials.txt", "wb") as file:
    file.write(encrypted_username + b"\n" + encrypted_password)
