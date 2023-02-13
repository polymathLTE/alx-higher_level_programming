#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines unittests for Rectangle class

Unittest classes:
    TestRectangle_initzn
    TestRectangle_width

"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_initzn(unittest.TestCase):
    """unittests for the initzn of the Rect. class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)


class TestRectangle_width(unittest.TestCase):
    """unittests for the width value of the Rect. class"""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", 2)

    def test_positive_width(self):
        with self.assertRaises(ValueError) as pos:
            Rectangle(-1, 2)
        self.assertEqual(str(pos.exception), 'width must be > 0')


class TestRectangle_height(unittest.TestCase):
    """unittests for the height value of the Rect. class"""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "str")

    def test_positive_height(self):
        with self.assertRaises(ValueError) as pos:
            Rectangle(2, -1)
        self.assertEqual(str(pos.exception), 'height must be > 0')
