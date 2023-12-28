import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.pdp_daily_moisture_lotion_selectors import PDP1Locators


class PdpPage1:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.pdp_daily_moisture_lotion)
        title = self.driver.title
        current_url = self.driver.current_url
        logging.info("Current Title is: %s", title)
        logging.info("Current URL is: %s", current_url)
        time.sleep(5)
        return self

    def close_pop_up(self):
        try:
            close_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.close_bottom_pop_up)))
            time.sleep(1)
            close_pop_up.click()

        except TimeoutException:
            logging.info("close_pop_up element not found within the specified time. %s")
        time.sleep(2)
        return self

    def product_image(self):
        try:
            main_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.main_image)))

            if main_image.is_displayed():
                alt_text = main_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

        except TimeoutException:
            logging.info("product_image element not found within the specified time. %s")
            time.sleep(2)
            return self

    def image_carousel(self):
        try:
            up_arrow = PDP1Locators.up_arrow
            down_arrow = PDP1Locators.down_arrow

            carousel_image2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.image2)))

            carousel_image3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.image3)))

            carousel_image4 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.image4)))

            carousel_image5 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.image5)))

            for _ in range(4):
                down_arrow_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, down_arrow)))
                time.sleep(1)
                down_arrow_element.click()
                time.sleep(2)

            for _ in range(4):
                up_arrow_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, up_arrow)))
                time.sleep(1)
                up_arrow_element.click()
                time.sleep(2)

            click_slide_dot2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, PDP1Locators.slide_dot2)))
            click_slide_dot2.click()
            time.sleep(2)

            if carousel_image2.is_displayed():
                alt_text = carousel_image2.get_attribute('alt')
                logging.info("Image Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! No image displayed !!!!!!!!!!")

            click_slide_dot3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.slide_dot3)))
            click_slide_dot3.click()
            time.sleep(2)

            if carousel_image3.is_displayed():
                alt_text = carousel_image3.get_attribute('alt')
                logging.info("Image Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! No image displayed !!!!!!!!!!")

            click_slide_dot4 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.slide_dot4)))
            click_slide_dot4.click()
            time.sleep(2)

            if carousel_image4.is_displayed():
                alt_text = carousel_image4.get_attribute('alt')
                logging.info("Image Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! No image displayed !!!!!!!!!!")

            click_slide_dot5 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.slide_dot5)))
            click_slide_dot5.click()
            time.sleep(2)

            if carousel_image5.is_displayed():
                alt_text = carousel_image5.get_attribute('alt')
                logging.info("Image Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! No image displayed !!!!!!!!!!")

        except TimeoutException:
            logging.info("PDP image_carousel element not found within the specified time. %s")
        time.sleep(2)
        return self
