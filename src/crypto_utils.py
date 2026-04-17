"""Cryptographic key rotation utilities."""
from cryptography.fernet import Fernet


def generate_key() -> bytes:
    return Fernet.generate_key()


def rotate_key(old_key: bytes, ciphertext: bytes) -> tuple[bytes, bytes]:
    new_key = generate_key()
    plaintext = Fernet(old_key).decrypt(ciphertext)
    return new_key, Fernet(new_key).encrypt(plaintext)
