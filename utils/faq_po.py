import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.faq_selectors import FaqLocators


class Faq:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.faq)
        title = self.driver.title
        current_url = self.driver.current_url
        logging.info("Current Title is: %s", title)
        logging.info("Current URL is: %s", current_url)
        time.sleep(5)
        return self

    def close_pop_up(self):
        try:
            close_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.bottom_pop_up_close)))
            time.sleep(1)
            close_pop_up.click()

        except TimeoutException:
            logging.info("close_pop_up element not found within the specified time. %s")
        time.sleep(2)
        return self

    def banner(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.banner_header)))
            logging.info("Header Text: %s", grab_banner_header_text.text)

        except TimeoutException:
            logging.info("banner element not found within the specified time. %s")
        time.sleep(2)
        return self

    def product_recommendation(self):
        try:
            grab_section_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.section_title1)))
            logging.info("Header Text: %s", grab_section_title.text)

            accordion1_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1)))

            grab_accordion1_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_title)))
            logging.info("Header Text: %s", grab_accordion1_title.text)

            accordion1_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_plus_icon)))

            accordion1_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_minus_icon)))

            accordion1_scenarios.click()
            time.sleep(2)
            if accordion1_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion1_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_paragraph)))
            logging.info("Header Text: %s", grab_accordion1_paragraph.text)

            accordion1_scenarios.click()
            time.sleep(2)
            if accordion1_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion2_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2)))

            grab_accordion2_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_title)))
            logging.info("Header Text: %s", grab_accordion2_title.text)

            accordion2_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_plus_icon)))

            accordion2_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_minus_icon)))

            accordion2_scenarios.click()
            time.sleep(2)
            if accordion2_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion2_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_paragraph)))
            logging.info("Header Text: %s", grab_accordion2_paragraph.text)

            accordion2_scenarios.click()
            time.sleep(2)
            if accordion2_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion3_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3)))

            grab_accordion3_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_title)))
            logging.info("Header Text: %s", grab_accordion3_title.text)

            accordion3_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_plus_icon)))

            accordion3_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_minus_icon)))

            accordion3_scenarios.click()
            time.sleep(2)
            if accordion3_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion3_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_paragraph)))
            logging.info("Header Text: %s", grab_accordion3_paragraph.text)

            accordion3_scenarios.click()
            time.sleep(2)
            if accordion3_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

        except TimeoutException:
            logging.info("product_recommendation element not found within the specified time. %s")
        time.sleep(2)
        return self

