
from src.key_derivation import (
    generate_salt,
    derive_key,
    verify_password
)

# Original password
password = "hello123"

# Generate a random salt
salt = generate_salt()

# Generate derived key
key = derive_key(password, salt)

print("Original Password:", password)

print("\nGenerated Salt:")
print(salt.hex())

print("\nDerived Key:")
print(key.hex())

print("\nSalt Length:", len(salt), "bytes")
print("Derived Key Length:", len(key), "bytes")


# --------------------------------
# PASSWORD VERIFICATION TESTING
# --------------------------------

print("\n--- Password Verification ---")

# Test 1: Correct password
result1 = verify_password(password, salt, key)
print("Correct Password:", result1)

# Test 2: Incorrect password
result2 = verify_password("wrong123", salt, key)
print("Incorrect Password:", result2)


# --------------------------------
# KEY CONSISTENCY TESTING
# --------------------------------

print("\n--- Key Consistency Testing ---")

# Same password + same salt
key2 = derive_key(password, salt)

print("Same Password + Same Salt:")
print("Keys Match:", key == key2)


# Different salt
salt2 = generate_salt()
key3 = derive_key(password, salt2)

print("\nSame Password + Different Salt:")
print("Keys Match:", key == key3)
