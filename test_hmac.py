
from src.hmac_utility import generate_hmac, verify_hmac


# Original message and shared secret key
message = "Transfer 500 rupees"
secret_key = "my_secret_key_123"

# Generate HMAC
sha256_hmac = generate_hmac(
    message,
    secret_key,
    "sha256"
)

sha512_hmac = generate_hmac(
    message,
    secret_key,
    "sha512"
)

print("Original Message:", message)

print("\nSHA-256 HMAC:")
print(sha256_hmac)

print("\nSHA-512 HMAC:")
print(sha512_hmac)


# Verify original message
print("\n--- HMAC Verification ---")

result = verify_hmac(
    message,
    secret_key,
    sha256_hmac,
    "sha256"
)

print("Original Message Verification:", result)


# Test modified message
modified_message = "Transfer 5000 rupees"

result = verify_hmac(
    modified_message,
    secret_key,
    sha256_hmac,
    "sha256"
)

print("Modified Message Verification:", result)
