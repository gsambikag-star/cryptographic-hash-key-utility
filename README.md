
# Cryptographic Hash & Key Derivation Utility

A Python-based cybersecurity utility demonstrating cryptographic hashing, secure key derivation, HMAC authentication, and file integrity verification.

## Project Overview

This project provides a command-line cryptographic utility designed to demonstrate important cybersecurity concepts using Python.

## Features

- SHA-256 text hashing
- SHA-512 text hashing
- SHA-256 file hashing
- SHA-512 file hashing
- Secure random salt generation (planned)
- PBKDF2 key derivation (planned)
- HMAC generation and verification (planned)
- File integrity verification (planned)
- Secure random salt generation using Python's secrets module.
- PBKDF2-based cryptographic key derivation.
- Support for PBKDF2-HMAC-SHA256 and PBKDF2-HMAC-SHA512.
- Configurable iteration count and derived key length.
- Password verification using derived keys.
- Timing-resistant key comparison using hmac.compare_digest().
- HMAC generation using SHA-256 and SHA-512.
- HMAC verification using shared secret keys.
- Message integrity and tampering detection.
- Timing-resistant HMAC comparison using hmac.compare_digest().

## Technology Stack

- Python 3
- hashlib
- secrets
- hmac
- argparse
- unittest
- Git and GitHub

## Project Structure

```text
cryptographic-hash-key-utility/
├── src/
│   ├── __init__.py
│   └── hashing.py
├── tests/
│   └── test_hashing.py
├── samples/
│   └── sample.txt
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/gsambikag-star/cryptographic-hash-key-utility
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Run the hashing demonstration:

```bash
python test_hashing.py
```

Run automated tests:

```bash
python -m unittest discover -s tests -v
```

## Testing

The hashing module is tested using:

- Known SHA-256 test vectors
- Known SHA-512 test vectors
- Hash output length verification
- Invalid algorithm handling
- File hashing verification

## Project Status

Phase 1: Environment and repository setup.

Phase 2: SHA-256 and SHA-512 hashing implementation and testing.

Further features are under development.


## Secure Salt Generation and PBKDF2

This project implements secure password-based key derivation using PBKDF2.

### 1. Salt Generation

- Uses Python's `secrets` module.
- Generates cryptographically secure random salts.
- Default salt length: 16 bytes (128 bits).
- Each password can have a unique salt.

### 2. PBKDF2 Key Derivation

Uses Python's `hashlib.pbkdf2_hmac()` function.

Supported algorithms:
- SHA-256
- SHA-512

Default configuration:
- Iterations: 600,000
- Salt length: 16 bytes
- Derived key length: 32 bytes

### 3. Password Verification

The utility verifies passwords by:
1. Accepting the entered password.
2. Using the previously generated salt.
3. Deriving a new key using PBKDF2.
4. Comparing the new key with the stored derived key.
5. Returning True if they match, otherwise False.

The comparison uses `hmac.compare_digest()`.

### 4. Running Key Derivation

Run the manual testing script:

```bash
python test_key_derivation.py
```

### 5. Running Automated Tests

Run all project tests:

```bash
python -m unittest discover -s tests -v
```

### 6. Security Notes

- Salts are not secret and should be stored with the derived key.
- Never store plaintext passwords.
- Store the iteration count, algorithm and key length alongside the salt.
- Use a unique random salt for each password.
- Use secure comparison methods when verifying derived keys.


## HMAC Generation and Verification

HMAC stands for Hash-based Message Authentication Code.

It verifies message integrity and authenticity using a shared secret key.

### Supported Algorithms
- HMAC-SHA256
- HMAC-SHA512

### Features
- Generate HMAC authentication codes.
- Verify messages using shared secret keys.
- Detect modified or tampered messages.
- Reject incorrect secret keys.
- Secure comparison using hmac.compare_digest().

### Running HMAC

Run the manual testing script:

```bash
python test_hmac.py
```

### Running Automated Tests

```bash
python -m unittest discover -s tests -v
```

### Security Notes
- Keep secret keys confidential.
- HMAC does not encrypt messages.
- The same message and key produce the same HMAC.
- Use secure comparison methods during verification.

## Phase 5: File Integrity Verification

Implemented file integrity verification using SHA-256 and SHA-512 hashing.

### Features
- Generates a checksum for a file.
- Verifies file integrity by comparing the actual checksum with the expected checksum.
- Detects whether a file has been modified.
- Uses `hmac.compare_digest()` for secure checksum comparison.

### Testing
- Original file verification: True
- Modified file verification: False
- SHA-512 verification: Passed
- Invalid checksum verification: False

All 25 automated tests passed successfully.


## Phase 6: Main Application Integration

Integrated all cryptographic utilities into a single menu-driven Python application.

### Features
1. Generate Text Hash (SHA-256 / SHA-512)
2. Generate File Hash (SHA-256 / SHA-512)
3. Generate Secure Salt
4. Derive Key using PBKDF2
5. Verify Password
6. Generate HMAC
7. Verify HMAC
8. Verify File Integrity
9. Exit

### Input Validation
- Handles empty inputs.
- Detects invalid algorithms.
- Handles incorrect file paths.
- Validates hexadecimal salt and derived key inputs.
- Handles invalid menu choices.

### Testing
- All 25 automated tests passed.
- All eight application features manually tested.
- Successful and unsuccessful verification scenarios tested.

## Author

Ambika G.S 
