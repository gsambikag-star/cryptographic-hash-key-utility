
import unittest

from src.hmac_utility import generate_hmac, verify_hmac


class TestHMAC(unittest.TestCase):

    def setUp(self):
        self.message = "Transfer 500 rupees"
        self.secret_key = "my_secret_key_123"

    def test_sha256_hmac_generation(self):
        result = generate_hmac(
            self.message,
            self.secret_key,
            "sha256"
        )

        self.assertEqual(len(result), 64)

    def test_sha512_hmac_generation(self):
        result = generate_hmac(
            self.message,
            self.secret_key,
            "sha512"
        )

        self.assertEqual(len(result), 128)

    def test_correct_message_verification(self):
        signature = generate_hmac(
            self.message,
            self.secret_key
        )

        result = verify_hmac(
            self.message,
            self.secret_key,
            signature
        )

        self.assertTrue(result)

    def test_modified_message_verification(self):
        signature = generate_hmac(
            self.message,
            self.secret_key
        )

        result = verify_hmac(
            "Transfer 5000 rupees",
            self.secret_key,
            signature
        )

        self.assertFalse(result)

    def test_wrong_secret_key(self):
        signature = generate_hmac(
            self.message,
            self.secret_key
        )

        result = verify_hmac(
            self.message,
            "wrong_secret_key",
            signature
        )

        self.assertFalse(result)

    def test_invalid_algorithm(self):
        with self.assertRaises(ValueError):
            generate_hmac(
                self.message,
                self.secret_key,
                "md5"
            )

    def test_hmac_consistency(self):
        first = generate_hmac(
            self.message,
            self.secret_key
        )

        second = generate_hmac(
            self.message,
            self.secret_key
        )

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
