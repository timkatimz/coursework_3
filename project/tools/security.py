import hashlib
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


def generate_password_digest(password):
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=PWD_HASH_SALT,
        iterations=PWD_HASH_ITERATIONS,
    )
