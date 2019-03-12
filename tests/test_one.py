import unittest
import json
import os.path
import time


with open(os.path.join('tests', 'test_discovery_delay'), 'r') as fs:
    delay = fs.readline()
    time.sleep(int(delay))

def delay_running():
    with open(os.path.join('tests', 'test_running_delay'), 'r') as fs:
        delay = fs.readline()
        time.sleep(int(delay))

def getData():
    with open(os.path.join('tests', 'data.json'), 'r') as fs:
        return json.load(fs)

class TestFirstSuite(unittest.TestCase):
    def test_one(self):
        data = getData()
        delay_running()
        self.assertEqual(1, data[0])

    def test_two(self):
        data = getData()
        delay_running()
        self.assertEqual(2, data[1])

    def test_three(self):
        data = getData()
        delay_running()
        self.assertEqual(3, data[2])

class TestSecondSuite(unittest.TestCase):
    def test_four(self):
        data = getData()
        self.assertEqual(4, data[3])

    def test_five(self):
        data = getData()
        self.assertEqual(5, data[4])

    def test_six(self):
        data = getData()
        self.assertEqual(6, data[5])
