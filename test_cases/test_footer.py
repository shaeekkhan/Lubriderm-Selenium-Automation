import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.footer_po import Footer


class TestFooter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.Footer = Footer(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_back_to_top(self):
        self.Footer.load()
        self.Footer.back_to_top()


if __name__ == "__main__":
    unittest.main()
