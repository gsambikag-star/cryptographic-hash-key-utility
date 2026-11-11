
from src.hashing import hash_file

file_path = "samples/sample.txt"

sha256_result = hash_file(file_path, "sha256")
sha512_result = hash_file(file_path, "sha512")

print("File:", file_path)

print("\nSHA-256 File Hash:")
print(sha256_result)

print("\nSHA-512 File Hash:")
print(sha512_result)

print("\nSHA-256 Length:", len(sha256_result))
print("SHA-512 Length:", len(sha512_result))
