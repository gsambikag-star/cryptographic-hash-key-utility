
import hmac
import hashlib


def generate_hmac(message, secret_key, algorithm="sha256"):
    """
    Generate an HMAC for a given message.
    """

    supported_algorithms = {
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }

    if algorithm not in supported_algorithms:
        raise ValueError("Unsupported hashing algorithm")

    message_bytes = message.encode("utf-8")
    key_bytes = secret_key.encode("utf-8")

    authentication_code = hmac.new(
        key_bytes,
        message_bytes,
        supported_algorithms[algorithm]
    )

    return authentication_code.hexdigest()


def verify_hmac(message, secret_key, expected_hmac, algorithm="sha256"):
    """
    Verify whether the message HMAC is valid.
    """

    calculated_hmac = generate_hmac(
        message,
        secret_key,
        algorithm
    )

    return hmac.compare_digest(
        calculated_hmac,
        expected_hmac
    )
