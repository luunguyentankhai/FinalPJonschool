import hashlib
import os

LOOP = 10000

def _safe_compare(a: bytes, b: bytes) -> bool:
    if len(a) != len(b):
        return False
    
    result = 0

    for x,y in zip(a,b):
        result|=x^y
    
    return result == 0

def hash_PW(Plain_Text_PW: str):
    salt = os.urandom(16)

    password_bytes = Plain_Text_PW.encode("utf-8")
    hash_bytes = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, LOOP)

    return f"{salt.hex()}:{hash_bytes.hex()}"


def check_PW(Plain_Text_PW: str, stored_hash: str) -> bool:
    try:
        salt_hex, stored_hash_hex = stored_hash.split(":")

        salt = bytes.fromhex(salt_hex)
        stored_hash_bytes = bytes.fromhex(stored_hash_hex)

        password_bytes = Plain_Text_PW.encode("utf-8")
        new_hash_bytes = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, LOOP)

        return _safe_compare(stored_hash_bytes, new_hash_bytes)
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    pw_admin = hash_PW("admin123")
    print(f"{pw_admin}")
    print("\n")
    pw_teacher = hash_PW("teacher123")
    print(f"{pw_teacher}")
    print("\n")
    pw_student = hash_PW("student123")
    print(f"{pw_student}")