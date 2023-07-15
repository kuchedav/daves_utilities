import os

from cryptography.fernet import Fernet

key = os.getenv("DAVID_SECRET")
fernet = Fernet(key)


def generate_key():
    return Fernet.generate_key()


def encrypt_message(message):
    return fernet.encrypt(message.encode())


def decrypt_message(enc_message):
    return fernet.decrypt(enc_message).decode()


if __name__ == "__main__":
    message = "this is a test"
    print(f"{message=}")

    enc_message = encrypt_message(message)
    print(f"{enc_message=}")

    dec_message = decrypt_message(enc_message)
    print(f"{dec_message=}")
