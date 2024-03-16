import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.homepage_selectors import HomepageLocators


def handle_exception(driver: object, error_message: object) -> object:
    logging.error(error_message)
    driver.close()
    assert False, error_message


class Homepage:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.base_url)
        title = self.driver.title
        current_url = self.driver.current_url
        logging.info("Current Title is: %s", title)
        logging.info("Current URL is: %s", current_url)
        time.sleep(5)
        return self

    def close_pop_up(self):
        try:
            close_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.close_bottom_pop_up)))
            time.sleep(1)
            close_pop_up.click()

        except TimeoutException:
            handle_exception(self.driver, "Pop-Up element not found within the specified time. %s")
        time.sleep(2)
        return self

    def banner_section(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_header_text)))
            logging.info(grab_banner_header_text.text)
            time.sleep(1)

            grab_banner_sub_copy_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_sub_copy_text)))
            logging.info(grab_banner_sub_copy_text.text)
            time.sleep(1)

            click_on_banner_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_banner_cta.text)
            time.sleep(1)
            click_on_banner_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            banner_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_image_locators)))

            if banner_image.is_displayed():
                alt_text = banner_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

        except TimeoutException:
            handle_exception(self.driver, "Banner element not found within the specified time. %s")
        time.sleep(2)
        return self

    def shop_by_collection(self):
        try:
            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            grab_section_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.section_header_text)))
            logging.info(grab_section_header_text.text)
            time.sleep(1)

            click_on_see_all_product_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.see_all_product_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_see_all_product_cta.text)
            time.sleep(1)
            click_on_see_all_product_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            daily_moisture_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image1)))

            if daily_moisture_image.is_displayed():
                alt_text = daily_moisture_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

            click_on_daily_moisture_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image1)))
            time.sleep(1)
            click_on_daily_moisture_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            daily_moisture_details_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.daily_moisture_details_header_text)))
            logging.info(daily_moisture_details_header.text)
            time.sleep(1)
            daily_moisture_details_header.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            grab_daily_moisture_details_sub_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.daily_moisture_details_sub_text)))
            logging.info(grab_daily_moisture_details_sub_text.text)
            time.sleep(1)

            click_on_daily_moisture_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.daily_moisture_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_daily_moisture_cta.text)
            time.sleep(1)
            click_on_daily_moisture_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            handle_exception(self.driver, "Banner element not found within the specified time. %s")
        time.sleep(2)
        return self
