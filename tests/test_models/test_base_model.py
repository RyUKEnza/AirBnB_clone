#!/usr/bin/python3
"""Unittest for the BaseModel Class """
import os
import json
import unittest
from models.base_model import BaseModel
from models import storage
import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
    def tearDown(self):
        storage.delete(self.my_model)

    def test_attributes(self):
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str_method(self):
        expected_output = f"[BaseModel] ({self.my_model.id}) {self.my_model.__dict__}"
        self.assertEqual(str(self.my_model), expected_output)

    def test_save_method(self):
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        my_model_json = self.my_model.to_dict()
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

    def test_to_dict_method_format(self):
        my_model_json = self.my_model.to_dict()
        self.assertEqual(self.my_model.created_at.isoformat(), my_model_json['created_at'])
        self.assertEqual(self.my_model.updated_at.isoformat(), my_model_json['updated_at'])

    def test_new_method(self):
        key = "{}.{}".format(self.my_model.__class__.__name__, self.my_model.id)
        self.assertIn(key, storage.all())
    def test_reload_method(self):
        self.my_model.save()
        storage.reload()
        key = "{}.{}".format(self.my_model.__class__.__name__, self.my_model.id)
        self.assertIn(key, storage.all())

if __name__ == '__main__':
    unittest.main()
