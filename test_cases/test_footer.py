import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.footer_po import Footer


class TestFooter:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.Footer = Footer(self.driver)
        yield
        self.driver.quit()

    def test_back_to_top(self):
        self.Footer.load()
        self.Footer.back_to_top()
