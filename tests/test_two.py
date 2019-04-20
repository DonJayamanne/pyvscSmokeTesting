import json
import os.path
import time
import unittest

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

class TestThirdSuite(unittest.TestCase):
    def test_one_third_suite(self):
        data = getData()
        delay_running()
        self.assertEqual(1, data[0])

    def test_two_third_suite(self):
        data = getData()
        delay_running()
        self.assertEqual(2, data[1])

    def test_three_third_suite(self):
        data = getData()
        delay_running()
        self.assertEqual(3, data[2])
