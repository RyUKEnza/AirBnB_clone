import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime.datetime)
        self.assertIsInstance(bm.updated_at, datetime.datetime)

    def test_str(self):
        bm = BaseModel()
        expected = f"[BaseModel] ({bm.id}) {{\n    'id': '{bm.id}',\n    'created_at': {str(bm.created_at)},\n    'updated_at': {str(bm.updated_at)},\n}}"
        self.assertEqual(str(bm), expected)

    def test_save(self):
        bm = BaseModel()
        bm.save()
        self.assertGreater(bm.updated_at, bm.created_at)
