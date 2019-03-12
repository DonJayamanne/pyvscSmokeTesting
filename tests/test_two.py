import unittest
import json
import os.path


def getData():
    with open(os.path.join('tests', 'data.json'), 'r') as fs:
        return json.load(fs)

class TestThirdSuite(unittest.TestCase):
    def test_one(self):
        data = getData()
        self.assertEqual(1, data[0])

    def test_two(self):
        data = getData()
        self.assertEqual(2, data[1])

    def test_three(self):
        data = getData()
        self.assertEqual(3, data[2])
