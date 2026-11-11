
import unittest

from src.hashing import generate_hash, hash_file


class TestHashing(unittest.TestCase):

    def test_sha256_known_vector(self):
        result = generate_hash("abc", "sha256")

        expected = (
            "ba7816bf8f01cfea414140de5dae2223"
            "b00361a396177a9cb410ff61f20015ad"
        )

        self.assertEqual(result, expected)

    def test_sha512_known_vector(self):
        result = generate_hash("abc", "sha512")

        expected = (
            "ddaf35a193617abacc417349ae204131"
            "12e6fa4e89a97ea20a9eeee64b55d39a"
            "2192992a274fc1a836ba3c23a3feebbd"
            "454d4423643ce80e2a9ac94fa54ca49f"
        )

        self.assertEqual(result, expected)

    def test_sha256_length(self):
        result = generate_hash("Hello", "sha256")
        self.assertEqual(len(result), 64)

    def test_sha512_length(self):
        result = generate_hash("Hello", "sha512")
        self.assertEqual(len(result), 128)

    def test_invalid_algorithm(self):
        with self.assertRaises(ValueError):
            generate_hash("Hello", "md5")

    def test_file_hashing(self):
        with open("samples/test_temp.txt", "w") as file:
            file.write("abc")

        result = hash_file("samples/test_temp.txt", "sha256")

        expected = generate_hash("abc", "sha256")

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
