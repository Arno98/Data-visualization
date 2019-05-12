import unittest
from python_respons_test import url_python

class TestStatusCode(unittest.TestCase):
	
	def test_status_code(self):
		status_code = url_python()
		self.assertEqual(status_code, 200)
		
unittest.main()
