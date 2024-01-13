#!/usr/bin/python3
"""
"""
import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """
    BaseModel Unittest
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """
        Test for Instance
        """
        my_model = BaseModel()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_save(self):
        """
        Test time after save
        """
        my_model = BaseModel()

        previous_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(previous_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Check .t0_dict return type and values
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],
                         my_model.updated_at.isoformat())

    def test_str(self):
        """
        Check string return
        """
        my_model = BaseModel()

        self.assertIsInstance(my_model.id, str)
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
