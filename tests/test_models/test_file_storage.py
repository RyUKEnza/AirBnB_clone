import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn("BaseModel." + self.base_model.id, all_objs)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)
        self.assertIn("BaseModel." + new_model.id, all_objs)

    def test_save_reload(self):
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn("BaseModel." + self.base_model.id, all_objs)

if __name__ == '__main__':
    unittest.main()
