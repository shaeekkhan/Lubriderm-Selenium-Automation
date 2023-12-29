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

    def products_description_section(self):
        try:
            eyebrow_tag = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.eyebrow)))
            logging.info(eyebrow_tag.text)

            bazarvoice_review = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.star_review)))
            logging.info(bazarvoice_review.text)

            product_description_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.h1_title)))
            logging.info(product_description_header.text)

            click_on_buy_now_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.buy_now_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_buy_now_cta.text)
            time.sleep(1)
            click_on_buy_now_cta.click()
            time.sleep(5)

            price_spider_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PDP1Locators.price_spider_pop_up)))
            if price_spider_pop_up.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PDP1Locators.price_spider_pop_up_close)))
            price_spider_pop_up_close.click()

            if price_spider_pop_up_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

            product_description_details = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.product_details)))
            logging.info(product_description_details.text)

        except TimeoutException:
            logging.info("product_description_header element not found within the specified time. %s")
        time.sleep(2)
        return self

    def jump_to_link_menu(self):
        try:
            product_over_view_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.jump_to_links)))

            ingredients_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.ingredients_section)))

            you_may_also_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.you_may_also_like_section)))

            reviews_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.review_section)))

            scroll_to_jump_to_links = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.jump_to_links)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_jump_to_links)
            time.sleep(1)

            jump_to_link_menu_lists = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.jum_to_links_lists)))
            logging.info(jump_to_link_menu_lists.text)

            click_on_product_over_view = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.product_over_view)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_product_over_view.text)
            time.sleep(1)
            click_on_product_over_view.click()
            time.sleep(2)

            if product_over_view_div.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            scroll_to_jump_to_links = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.jump_to_links)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_jump_to_links)
            time.sleep(1)

            click_on_ingredients_links = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.ingredients)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_ingredients_links.text)
            time.sleep(1)
            click_on_ingredients_links.click()
            time.sleep(5)

            if ingredients_div.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            click_on_you_may_also_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.you_may_also_like)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_you_may_also_link.text)
            time.sleep(1)
            click_on_you_may_also_link.click()
            time.sleep(5)

            if you_may_also_div.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            click_on_reviews = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PDP1Locators.reviews)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_reviews.text)
            time.sleep(1)
            click_on_reviews.click()
            time.sleep(5)

            if reviews_div.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

        except TimeoutException:
            logging.info("jump_to_link_menu element not found within the specified time. %s")
        time.sleep(2)
        return self

