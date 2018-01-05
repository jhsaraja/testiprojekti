#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `testiprojekti` package."""


import unittest

from testiprojekti import testiprojekti



class TestPerson(unittest.TestCase):
    """ Test for Person package. """

    @classmethod
    def setUpClass(cls):
        """ Set up our Person client for tests."""
        cls._person = person.Person("Testi", 34, '2342343434')
        cls._emp = person.Employee("Employee Tester", 45, "55555555555555", "Programmer", "3000", "Tampere")

    def test_000_object_exists(self):
        """ Test creating a new object """
        self.assertTrue(self._person.age == 34 and self._person.name == "Testi")

    def test_001_change_name(self):
        """ Test changing name """
        self._person.set_name("Testi Testaaja")
        self.assertEqual(self._person.name, "Testi Testaaja")

    def test_002_get_name(self):
        """ Test to get name """
        self.assertIsNotNone(self._person.get_name())

    def test_003_change_age(self):
        """ Test changing age """
        self._person.set_age(23)
        self.assertEqual(self._person.age, 23)

    def test_004_get_age(self):
        """ Test to get age """
        self.assertIsNotNone(self._person.get_age())

    def test_005_change_phone(self):
        """ Test changing phone """
        self._person.set_phone("6666666666")
        self.assertEqual(self._person.phone, "6666666666")

    def test_006_get_phone(self):
        """ Test to get phone """
        self.assertIsNotNone(self._person.get_phone())


if __name__ == '__main__':
    unittest.main(verbosity=2)
