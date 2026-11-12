from src.hashing import generate_hash, hash_file, verify_file_hash
from src.key_derivation import generate_salt, derive_key, verify_password
from src.hmac_utility import generate_hmac, verify_hmac

def generate_text_hash():
    message = input("Enter the text to hash: ").strip()

    if not message:
        print("Error: Text cannot be empty!")
        return

    algorithm = input("Choose algorithm (sha256/sha512): ").lower().strip()

    try:
        result = generate_hash(message, algorithm)

        print("\nGenerated Hash:")
        print(result)

    except ValueError as error:
        print("Error:", error)



def generate_file_hash():
    file_path = input("Enter the file path: ").strip()

    if not file_path:
        print("Error: File path cannot be empty!")
        return

    algorithm = input("Choose algorithm (sha256/sha512): ").lower().strip()

    try:
        result = hash_file(file_path, algorithm)

        print("\nGenerated File Hash:")
        print(result)

    except FileNotFoundError:
        print("Error: File not found!")

    except ValueError as error:
        print("Error:", error)



def generate_secure_salt():
    try:
        salt_length = input(
            "Enter salt length in bytes (default 16): "
        ).strip()

        if salt_length:
            salt_length = int(salt_length)
        else:
            salt_length = 16

        if salt_length <= 0:
            print("Error: Salt length must be positive!")
            return

        salt = generate_salt(salt_length)

        print("\nGenerated Secure Salt:")
        print(salt.hex())

        print("\nSalt Length:", len(salt), "bytes")

    except ValueError as error:
        print("Error:", error)



def derive_password_key():
    password = input("Enter your password: ")

    if not password.strip():
        print("Error: Password cannot be empty!")
        return

    salt_hex = input("Enter salt in hexadecimal: ").strip()

    if not salt_hex:
        print("Error: Salt cannot be empty!")
        return

    try:
        salt = bytes.fromhex(salt_hex)

        if len(salt) == 0:
            print("Error: Salt cannot be empty!")
            return

        derived_key = derive_key(password, salt)

        print("\nGenerated Derived Key:")
        print(derived_key.hex())

        print("\nDerived Key Length:", len(derived_key), "bytes")

    except ValueError as error:
        print("Error:", error)



def verify_user_password():
    password = input("Enter password: ")

    if not password:
        print("Error: Password cannot be empty!")
        return

    salt_hex = input("Enter salt in hexadecimal: ").strip()
    expected_key_hex = input(
        "Enter stored derived key in hexadecimal: "
    ).strip()

    if not salt_hex or not expected_key_hex:
        print("Error: Salt and derived key cannot be empty!")
        return

    try:
        salt = bytes.fromhex(salt_hex)
        expected_key = bytes.fromhex(expected_key_hex)

        if not salt or not expected_key:
            print("Error: Salt and derived key cannot be empty!")
            return

        result = verify_password(
            password,
            salt,
            expected_key
        )

        if result:
            print("\nPassword verification successful!")
        else:
            print("\nIncorrect password!")

    except ValueError as error:
        print("Error:", error)



def generate_message_hmac():
    message = input("Enter the message: ")

    if not message:
        print("Error: Message cannot be empty!")
        return

    secret_key = input("Enter the secret key: ")

    if not secret_key:
        print("Error: Secret key cannot be empty!")
        return

    algorithm = input(
        "Choose algorithm (sha256/sha512): "
    ).lower().strip()

    try:
        result = generate_hmac(
            message,
            secret_key,
            algorithm
        )

        print("\nGenerated HMAC:")
        print(result)

    except ValueError as error:
        print("Error:", error)


def verify_message_hmac():
    message = input("Enter the original message: ")

    if not message:
        print("Error: Message cannot be empty!")
        return

    secret_key = input("Enter the secret key: ")

    if not secret_key:
        print("Error: Secret key cannot be empty!")
        return

    expected_hmac = input("Enter the expected HMAC: ").strip()

    if not expected_hmac:
        print("Error: Expected HMAC cannot be empty!")
        return

    algorithm = input(
        "Choose algorithm (sha256/sha512): "
    ).lower().strip()

    try:
        result = verify_hmac(
            message,
            secret_key,
            expected_hmac,
            algorithm
        )

        if result:
            print("\nHMAC Verification Successful!")
            print("Message integrity is verified.")
        else:
            print("\nHMAC Verification Failed!")
            print("Message or secret key may be incorrect.")

    except ValueError as error:
        print("Error:", error)



def verify_file_integrity():
    file_path = input("Enter the file path: ").strip()

    if not file_path:
        print("Error: File path cannot be empty!")
        return

    expected_hash = input("Enter the expected checksum: ").strip()

    if not expected_hash:
        print("Error: Expected checksum cannot be empty!")
        return

    algorithm = input(
        "Choose algorithm (sha256/sha512): "
    ).lower().strip()

    try:
        result = verify_file_hash(
            file_path,
            expected_hash,
            algorithm
        )

        if result:
            print("\nFile Integrity Verified!")
            print("The file has not been modified.")
        else:
            print("\nFile Integrity Verification Failed!")
            print("The file may have been modified.")

    except FileNotFoundError:
        print("Error: File not found!")

    except ValueError as error:
        print("Error:", error)


def display_menu():
    print("\n====================================")
    print("  CRYPTOGRAPHIC HASH & KEY UTILITY")
    print("====================================")

    print("1. Generate Text Hash")
    print("2. Generate File Hash")
    print("3. Generate Secure Salt")
    print("4. Derive Key using PBKDF2")
    print("5. Verify Password")
    print("6. Generate HMAC")
    print("7. Verify HMAC")
    print("8. Verify File Integrity")
    print("9. Exit")

    print("====================================")



def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-9): ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid choice! Please enter a number from 1 to 9.")
            continue

        if choice == "9":
            print("Thank you for using the utility!")
            break

        elif choice == "1":
            generate_text_hash()

        elif choice == "2":
            generate_file_hash()

        elif choice == "3":
            generate_secure_salt()

        elif choice == "4":
            derive_password_key()

        elif choice == "5":
            verify_user_password()

        elif choice == "6":
            generate_message_hmac()

        elif choice == "7":
            verify_message_hmac()
        
        elif choice == "8":
            verify_file_integrity()

        else:
            print("Invalid choice! Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
