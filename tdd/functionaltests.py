# Spirit web site

# When i go to the home page, I should see the title, "Spirit" 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_for_home_page_items(self):
		# When I go to the home page
		self.browser.get('http://localhost:8000')

		# I should see the title as "Spirit"
		assert "Spirit" in self.browser.title


if __name__=="__main__":
	unittest.main()
