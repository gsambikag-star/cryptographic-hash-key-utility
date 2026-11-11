
from src.hashing import generate_hash

text = "Hello World"

sha256_result = generate_hash(text, "sha256")
sha512_result = generate_hash(text, "sha512")

print("Original Text:", text)

print("\nSHA-256 Hash:")
print(sha256_result)

print("\nSHA-512 Hash:")
print(sha512_result)

print("\nSHA-256 Length:", len(sha256_result))
print("SHA-512 Length:", len(sha512_result))
