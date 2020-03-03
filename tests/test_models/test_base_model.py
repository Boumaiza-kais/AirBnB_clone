#!usr/bin/python3
"""
test base_model.py
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel
    """
    def setUp(self):
        self.base = BaseModel()

    def testId(self):
        """
        Test id
        """
        self.assertEqual(type(self.base.id), str)

    def testLen(self):
        """
        Test length of id
        """
        self.assertEqual(len(self.base.id), 36)

    @unittest.expectedFailure
    def testUnique(self):
        """
        Test if id is unique
        """
        self.base1 = BaseModel()
        self.assertEqual(self.base.id, self.base1.id)

    def testInstance(self):
        """
        Test the variable createdat is an instance
        """
        self.assertTrue(isinstance(self.base.created_at, datetime))

    def testUpdated_atInstance(self):
        """
        Test the variable updated_at is an instance
        """
        self.assertTrue(isinstance(self.base.updated_at, datetime))

    def testUpdated_at(self):
        """ Test updated_at """
        self.base.save()
        self.assertTrue(self.base.created_at != self.base.updated_at)

    def testStr(self):
        """
        Test the __str__
        """
        shoji = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(self.base.__str__(), shoji)

    def test_to_dict(self):
        """
        Test to_dict: ret value
        """
        test_dict = self.base.to_dict()
        self.assertTrue(type(test_dict) is dict)

    def test_to_dict_dunder(self):
        """
        Test return dunder of __dict__
        """
        dunder = self.base.__dict__
        for attr in dunder.keys():
            self.assertNotIn('__', attr)

    def test_class_to_dict(self):
        """
        Test if __class__ added into the dict or no
        """
        test_dict = self.base.to_dict()
        self.assertTrue('__class__' in test_dict)

    def test_new_attr(self):
        """
        Test a new attr to the object
        """
        self.base.chicken = 1
        test_dict = self.base.to_dict()
        self.assertTrue('chicken' in test_dict)

    def test_updated_at_to_dict(self):
        """
        Test if updated_at a inside of the dict
        """
        test_dict = self.base.to_dict()
        self.assertEqual(type(test_dict['updated_at']), str)

    def test_created_at_to_dict(self):
        """
        Test if created_at is inside of the dict
        """
        test_dict = self.base.to_dict()
        self.assertEqual(type(test_dict['created_at']), str)

    def test_save(self):
        """
        Test save, if date is datetime object
        """
        self.save_test = BaseModel()
        before = self.save_test.updated_at
        self.save_test.save()
        after = self.save_test.updated_at
        self.assertTrue(type(after) is datetime)
        before = str(before)
        after = str(after)
        self.assertFalse(after == before)
