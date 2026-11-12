
import unittest
import tempfile
import os

from src.hashing import hash_file, verify_file_hash


class TestFileIntegrity(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            encoding="utf-8"
        )

        self.temp_file.write("Original file content")
        self.temp_file.close()

        self.original_hash = hash_file(
            self.temp_file.name,
            "sha256"
        )

    def tearDown(self):
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_original_file(self):
        result = verify_file_hash(
            self.temp_file.name,
            self.original_hash
        )

        self.assertTrue(result)

    def test_modified_file(self):
        with open(self.temp_file.name, "a", encoding="utf-8") as file:
            file.write(" Modified content")

        result = verify_file_hash(
            self.temp_file.name,
            self.original_hash
        )

        self.assertFalse(result)

    def test_sha512_verification(self):
        sha512_hash = hash_file(
            self.temp_file.name,
            "sha512"
        )

        result = verify_file_hash(
            self.temp_file.name,
            sha512_hash,
            "sha512"
        )

        self.assertTrue(result)

    def test_invalid_checksum(self):
        result = verify_file_hash(
            self.temp_file.name,
            "invalid_checksum"
        )

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
