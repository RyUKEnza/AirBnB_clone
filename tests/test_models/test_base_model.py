#!/usr/bin/python3
"""Unittest for the BaseModel Class """
import os
import json
import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_output = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_output)

    def test_save_method(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

    def test_to_dict_method_format(self):
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(my_model.created_at.isoformat(), my_model_json['created_at'])
        self.assertEqual(my_model.updated_at.isoformat(), my_model_json['updated_at'])

if __name__ == '__main__':
    unittest.main()
