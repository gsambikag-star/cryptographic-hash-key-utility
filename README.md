
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

## Author

Ambika G.S 
