
import unittest

from src.key_derivation import (
    generate_salt,
    derive_key,
    verify_password
)


class TestKeyDerivation(unittest.TestCase):

    def setUp(self):
        self.password = "hello123"
        self.salt = generate_salt()
        self.iterations = 1000

        self.key = derive_key(
            self.password,
            self.salt,
            iterations=self.iterations
        )

    def test_salt_length(self):
        self.assertEqual(len(self.salt), 16)

    def test_salt_randomness(self):
        salt2 = generate_salt()
        self.assertNotEqual(self.salt, salt2)

    def test_same_password_same_salt(self):
        key2 = derive_key(
            self.password,
            self.salt,
            iterations=self.iterations
        )

        self.assertEqual(self.key, key2)

    def test_different_salts(self):
        salt2 = generate_salt()

        key2 = derive_key(
            self.password,
            salt2,
            iterations=self.iterations
        )

        self.assertNotEqual(self.key, key2)

    def test_correct_password(self):
        result = verify_password(
            self.password,
            self.salt,
            self.key,
            iterations=self.iterations
        )

        self.assertTrue(result)

    def test_incorrect_password(self):
        result = verify_password(
            "wrong123",
            self.salt,
            self.key,
            iterations=self.iterations
        )

        self.assertFalse(result)

    def test_sha512_algorithm(self):
        key = derive_key(
            self.password,
            self.salt,
            iterations=self.iterations,
            algorithm="sha512"
        )

        self.assertEqual(len(key), 32)

    def test_invalid_algorithm(self):
        with self.assertRaises(ValueError):
            derive_key(
                self.password,
                self.salt,
                iterations=self.iterations,
                algorithm="md5"
            )


if __name__ == "__main__":
    unittest.main()
