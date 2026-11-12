import hmac
import hashlib


def generate_hash(text, algorithm="sha256"):
    """
    Generate a cryptographic hash for the given text.
    Supports SHA-256 and SHA-512.
    """

    # Convert text into bytes
    text_bytes = text.encode("utf-8")

    # Select the hashing algorithm
    if algorithm == "sha256":
        hash_object = hashlib.sha256(text_bytes)

    elif algorithm == "sha512":
        hash_object = hashlib.sha512(text_bytes)

    else:
        raise ValueError("Unsupported hashing algorithm")

    # Convert hash into hexadecimal format
    return hash_object.hexdigest()


def hash_file(file_path, algorithm="sha256"):
    """
    Generate a cryptographic hash for a file.
    """

    if algorithm not in ("sha256", "sha512"):
        raise ValueError("Unsupported hashing algorithm")

    # Create the selected hash object
    hash_object = hashlib.new(algorithm)

    # Open the file in binary read mode
    with open(file_path, "rb") as file:

        # Read the file in small chunks
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)

    # Return the final hash
    return hash_object.hexdigest()


def verify_file_hash(file_path, expected_hash, algorithm="sha256"):
    """
    Verify file integrity by comparing its actual hash
    with the expected checksum.
    """

    actual_hash = hash_file(file_path, algorithm)

    return hmac.compare_digest(
        actual_hash.lower(),
        expected_hash.strip().lower()
    )
