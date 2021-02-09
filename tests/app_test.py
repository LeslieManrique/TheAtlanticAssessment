import os
import sys
import unittest
import shutil
import sqlite3

_CWD = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(_CWD)

import app_utils

CWD = app_utils.CWD



class TestUploadFiles(unittest.TestCase):
    def setUp(self):
        os.chdir(CWD)
        shutil.copyfile('tests/ZKWDLhxw.txt', 'uploads/ZKWDLhxw.txt')

    def tearDown(self):
        os.chdir(_CWD)
        os.remove('uploads/ZKWDLhxw.txt')

    def test_get_uploaded_files(self):
        self.assertEqual(app_utils.get_uploaded_files(), ['ZKWDLhxw.txt'])

    def test_read_file(self):
        self.assertEqual(app_utils.read_files('ZKWDLhxw.txt').shape, (5,11))





if __name__ == '__main__':

    unittest.main()

