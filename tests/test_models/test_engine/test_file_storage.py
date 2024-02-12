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

    def test_all_storage_returns_dictionary(self):
        # Test if the all() method returns a dictionary.
        self.assertEqual(dict, type(models.storage.all())

    def test_new(self):
        # Test the new method by creating and storing a new object
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel,{}".format(obj, id), nmodels.storage.all())

    def test_new_with_args(self):
        # Test creating a new object with additional arguments
        # (should raise TypeError)
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        # Test creating a new object with None (should raise AttributError).
        with self.assertRaises(AttributeError):
        models.storage.new(None)

    def test_save_and_reload(self):
        #test saving objects to a file and then reloading them
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        #create a new storage instance to stimulate reloading
        new_storage = Filestorage()
        new_storage.reload()

        #check if the reload objects match the original objects
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

