#!/usr/bin/python3
"""Unittest for the BaseModel Class """
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(expected_str, str(self.base_model))

    def test_save(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        expected_dict = {
                '__class__': 'BaseModel',
                'id': self.base_model.id,
                'created_at': self.base_model.created_at.isoformat(),
                'updated_at': self.base_model.updated_at.isoformat()
                }
        self.assertDictEqual(expected_dict, self.base_model.to_dict())

if __name__ == '__main__':
    unittest.main()

