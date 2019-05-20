import unittest

from testing.phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        self.phonebook.add("Peter", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Peter"))
