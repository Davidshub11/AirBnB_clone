#!/usr/bin/python3
"""
    All the test for the base_model are implemented here.
"""

import unittest
from models.base_model import BaseModels


class TestBaseModel(unittest.TestCase):
    """
        Testing the base class model.
    """

    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my.model.created_at)
        self.assertIsNotNone(my.model.updated_at)

    def test_save(self):
        """
            Checks that after updating the instance; the dates differ in the
            updated_at attribute.
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
            Test to_dict if it is a dictionary and if the key are value are present
            and correct
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model, dict)
        self.assertEqual(["__class__"], "BaseModel")
        self.assertEqual(["id"], my_model.id)
        self.assertEqual(["created_at"], my_model.created_at.isoformat())
        self.assertEqual(["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        """
            Test _str_ if it's output a string and also check some values in the string
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startwith('[BaseModel]'))
        self.assertIn(mymodel.id, str(my_mode))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
