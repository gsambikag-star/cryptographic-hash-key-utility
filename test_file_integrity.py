
from src.hashing import hash_file, verify_file_hash

# File to be tested
file_path = "samples/sample.txt"

# Generate original checksum
original_hash = hash_file(file_path, "sha256")

print("Original File:", file_path)

print("\nOriginal SHA-256 Checksum:")
print(original_hash)

# Verify the original file
result = verify_file_hash(
    file_path,
    original_hash,
    "sha256"
)

print("\n--- Original File Verification ---")
print("File Integrity:", result)


# Modify the file to simulate tampering
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nThis content has been modified.")

# Verify the modified file against the original checksum
result = verify_file_hash(
    file_path,
    original_hash,
    "sha256"
)

print("\n--- Modified File Verification ---")
print("File Integrity:", result)
