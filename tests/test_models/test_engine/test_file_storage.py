#!/usr/bin/python3

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstatiation(unittest.TeastCase):
    """
    Testing the instantiation of file storage.
    """
    def test_FileStorage_instantiation_no_args(self):
        # Test creating a FileStorage instance with no arguments.
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        # Test creating a FileStorage instace with an argument
        # (should raise TypeError).
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        # Test if the storage variable in models in an instance of FileStorage.
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.Testcase):

    def setUp(self):
        # Create a temporary test file for saving data
        self.test_file = "test_file.json"

    def tearDown(self):
        # Remove the temporary test file after the test
        if os.path.exists(self.test_file):
            os.remove(self, test_file)


