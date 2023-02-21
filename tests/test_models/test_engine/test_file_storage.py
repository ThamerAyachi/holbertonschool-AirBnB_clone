#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    def test_all(self):
        """check if returns dic<class>.<id> : {obj instance}"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsNotNone(all_objs)
        self.assertEqual(dict, type(all_objs))
        self.assertIs(all_objs, storage._FileStorage__objects)

    def test_new(self):
        """check if it has created new object"""
        storage = FileStorage()
        all_objs = storage.all()
        jacqueline = BaseModel()
        storage.new(jacqueline)
        key = jacqueline.__class__.__name__ + "." + str(jacqueline.id)
        self.assertIsNotNone(all_objs[key])

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        storage1 = FileStorage()
        all_objs = storage1.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        print(obj)
        self.assertIsNotNone(obj)


if __name__ == "__main__":
    unittest.main()
