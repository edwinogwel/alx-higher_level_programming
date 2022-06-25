#!/usr/bin/python3
""" Unittest for max_integer([..]) """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ A collection of testcases for the max_integer(). """

    def test_max(self):
        """ Test with a list of ints: should return the largest. """
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_emptyList(self):
        """ Test with an empty list: should return None. """
        self.assertIs(max_integer([]), None)

    def test_negativeInt(self):
        """ Test with a list of -Ve ints: should return the largest. """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_withFloat(self):
        """ Test with a list of ints & floats: should return the largest. """
        self.assertEqual(max_integer([1, 3.5, 2]), 3.5)

    def test_unique(self):
        """ Test with a list with a single int: should return the int. """
        self.assertEqual(max_integer([1]), 1)

    def test_strings(self):
        """ Test with a list of strs: should return the last when sorted. """
        self.assertEqual(max_integer(["Apple", "Bag"]), "Bag")

    def test_notInt(self):
        """ Test a list with non-int value(s): should raise TypeError. """
        self.assertRaises(TypeError, max_integer, ["One", "Two", 3])

    def test_argNotList(self):
        """ Test with an arg that's not a list: should raise TypeError. """
        self.assertRaises(TypeError, max_integer, 1)

    def test_none(self):
        """ Test with None as arg: should raise a TypeError. """
        self.assertRaises(TypeError, max_integer, None)
