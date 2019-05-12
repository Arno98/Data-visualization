import unittest
from python_respons_test import url_python

class TestStatus(unittest.TestCase):
	
	def SetUp(self):
		self.statuscode = url_python()
		
	def test_status(self):
		self.assertEqual(self.statuscode, 200)
		
unittest.main()
