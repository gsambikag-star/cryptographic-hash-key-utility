# Cryptographic Hash & Key Derivation Utility

A Python-based cybersecurity utility demonstrating cryptographic hashing, secure key derivation, HMAC authentication, and file integrity verification, all in one menu-driven command-line application.

Built as an internship project at **Codenova**.

---

## Project Overview

This project provides a command-line cryptographic utility designed to demonstrate important cybersecurity concepts using Python's standard library. It covers how passwords are protected, how messages are authenticated, and how file tampering is detected.

## Features

- **Hashing:** SHA-256 and SHA-512 for both text and files
- **Secure salt generation:** cryptographically secure random salts using Python's `secrets` module
- **Key derivation:** PBKDF2-HMAC-SHA256 and PBKDF2-HMAC-SHA512 with configurable iteration count and key length
- **Password verification:** re-derives a key from the entered password and compares it with the stored key
- **HMAC:** generation and verification using HMAC-SHA256 and HMAC-SHA512 with shared secret keys
- **Tamper detection:** detects modified messages and rejects incorrect secret keys
- **File integrity verification:** compares the actual checksum of a file with an expected checksum
- **Timing-resistant comparison:** uses `hmac.compare_digest()` for all key, HMAC and checksum comparisons
- **Input validation:** handles empty inputs, invalid algorithms, incorrect file paths, invalid hexadecimal values and invalid menu choices

## Technology Stack

- Python 3
- `hashlib`
- `secrets`
- `hmac`
- `argparse`
- `unittest`
- Git and GitHub

## Project Structure

```
cryptographic-hash-key-utility/
├── src/                      # Core cryptographic modules
├── tests/                    # Automated unit tests
├── samples/
│   └── sample.txt            # Sample file for hashing and integrity checks
├── main.py                   # Menu-driven application
├── test_hashing.py           # Manual demo: text hashing
├── test_file_hashing.py      # Manual demo: file hashing
├── test_key_derivation.py    # Manual demo: salt and PBKDF2
├── test_hmac.py              # Manual demo: HMAC
├── test_file_integrity.py    # Manual demo: file integrity
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

**1. Clone the repository**

```
git clone https://github.com/gsambikag-star/cryptographic-hash-key-utility
cd cryptographic-hash-key-utility
```

**2. Create a virtual environment**

```
python -m venv venv
```

**3. Activate it**

Windows (PowerShell):

```
.\venv\Scripts\Activate.ps1
```

macOS / Linux:

```
source venv/bin/activate
```

**4. Run the application**

```
python main.py
```

## Application Menu

```
1. Generate Text Hash (SHA-256 / SHA-512)
2. Generate File Hash (SHA-256 / SHA-512)
3. Generate Secure Salt
4. Derive Key using PBKDF2
5. Verify Password
6. Generate HMAC
7. Verify HMAC
8. Verify File Integrity
9. Exit
```

## How It Works

### Hashing

Text and files are hashed with SHA-256 or SHA-512 using `hashlib`. The same input always produces the same hash, and any change to the input produces a completely different hash.

### Secure Salt Generation

- Uses Python's `secrets` module
- Generates cryptographically secure random salts
- Default salt length: 16 bytes (128 bits)
- Each password should use its own unique salt

### PBKDF2 Key Derivation

Uses `hashlib.pbkdf2_hmac()` with SHA-256 or SHA-512.

Default configuration:

| Setting            | Default       |
| ------------------ | ------------- |
| Iterations         | 600,000       |
| Salt length        | 16 bytes      |
| Derived key length | 32 bytes      |

### Password Verification

1. Accept the entered password.
2. Use the previously generated salt.
3. Derive a new key with PBKDF2.
4. Compare the new key with the stored derived key using `hmac.compare_digest()`.
5. Return `True` if they match, otherwise `False`.

### HMAC (Hash-based Message Authentication Code)

HMAC verifies message integrity and authenticity using a shared secret key. Supported algorithms: HMAC-SHA256 and HMAC-SHA512. A modified message or an incorrect key causes verification to fail.

### File Integrity Verification

Generates a checksum for a file and compares it with an expected checksum to detect whether the file has been modified.

## Testing

Run the full automated test suite:

```
python -m unittest discover -s tests -v
```

Manual demonstration scripts:

```
python test_hashing.py
python test_file_hashing.py
python test_key_derivation.py
python test_hmac.py
python test_file_integrity.py
```

**Test coverage includes:**

- Known SHA-256 and SHA-512 test vectors
- Hash output length verification
- Invalid algorithm handling
- File hashing verification
- Salt generation and PBKDF2 key derivation
- Correct and incorrect password verification
- HMAC generation, verification, tamper detection and wrong-key rejection
- File integrity: original file (`True`), modified file (`False`), SHA-512 verification, invalid checksum (`False`)

**Result:** all 25 automated tests pass. All eight application features were also tested manually, including successful and unsuccessful verification scenarios.

## Security Notes

- Never store plaintext passwords.
- Salts are not secret and should be stored alongside the derived key.
- Store the iteration count, algorithm and key length together with the salt.
- Use a unique random salt for each password.
- Keep HMAC secret keys confidential.
- HMAC provides integrity and authenticity, not encryption.
- The same message and key always produce the same HMAC.
- Always use constant-time comparison (`hmac.compare_digest()`) when verifying keys, HMACs and checksums.

## Project Status

Complete. All planned phases are implemented and tested:

- Phase 1: Environment and repository setup
- Phase 2: SHA-256 and SHA-512 hashing
- Phase 3: Secure salt generation and PBKDF2 key derivation
- Phase 4: HMAC generation and verification
- Phase 5: File integrity verification
- Phase 6: Main application integration

## Author

**Ambika G.S**