import time

from selenium.common.exceptions import TimeoutException
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.footer_selectors import FooterLocators


class Footer:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.base_url)
        title = self.driver.title
        current_url = self.driver.current_url
        print("Current Title is:", title)
        print("Current URL is:", current_url)
        time.sleep(5)
        return self

    def back_to_top(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            click_on_back_to_top = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.back_to_top)))
            time.sleep(1)
            print("Footer Navigation Text:", click_on_back_to_top.text)
            time.sleep(1)
            click_on_back_to_top.click()
            time.sleep(2)

        except TimeoutException:
            print("Footer back_to_top element not found within the specified time.")
        time.sleep(2)
        return self
