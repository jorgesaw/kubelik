"""Core tests."""

# Python
import unittest

# Selenium
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_at_list_and_retrieve_it_later(self):
		"""Check out its homepage."""

		self.browser.get('http://localhost:8000')

		self.assertIn('Kubelik', self.browser.title)
		#self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()
