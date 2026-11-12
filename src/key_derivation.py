import hashlib
import secrets
import hmac


def generate_salt(salt_length=16):
    """
    Generate a cryptographically secure random salt.

    Default salt length: 16 bytes (128 bits).
    """

    if not isinstance(salt_length, int) or isinstance(salt_length, bool) or salt_length <= 0:
        raise ValueError("Salt length must be a positive integer")

    salt = secrets.token_bytes(salt_length)

    return salt



def derive_key(password, salt, iterations=600000,
               algorithm="sha256", dklen=32):
    """
    Derive a cryptographic key using PBKDF2.
    """

    if not isinstance(password, str) or not password:
        raise ValueError("Password must not be empty")

    if not isinstance(salt, bytes) or not salt:
        raise ValueError("Salt must be non-empty bytes")

    if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations <= 0:
        raise ValueError("Iterations must be a positive integer")

    if not isinstance(dklen, int) or isinstance(dklen, bool) or dklen <= 0:
        raise ValueError("Key length must be a positive integer")

    if algorithm not in ("sha256", "sha512"):
        raise ValueError("Unsupported hashing algorithm")

    password_bytes = password.encode("utf-8")

    derived_key = hashlib.pbkdf2_hmac(
        algorithm,
        password_bytes,
        salt,
        iterations,
        dklen=dklen
    )

    return derived_key


def verify_password(password, salt, expected_key,
                    iterations=600000,
                    algorithm="sha256",
                    dklen=32):
    """
    Verify a password using PBKDF2.
    """

    new_key = derive_key(
        password,
        salt,
        iterations,
        algorithm,
        dklen
    )

    return hmac.compare_digest(new_key, expected_key)
