from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Checking link presence.")
    def _verify_link_presence(self, link_text):
        self.logger.info(f"Checking link: '{link_text}' presence...")
        try:
            self.logger.info(f"Link found")
            return WebDriverWait(self.browser, self.browser.timeout) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            self.logger.error('Link search timeout error.')
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    @allure.step("Checking web element presence.")
    def _verify_element_presence(self, locator: tuple):
        self.logger.info(f"Checking web element: '{locator}' presence...")
        try:
            self.logger.info(f"Element found")
            return WebDriverWait(self.browser, self.browser.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error('Element search timeout error.')
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    @allure.step("Running action chain to click element.")
    def _click_element(self, element):
        self.logger.info(f"Running action chain to click element: '{element}' ...")
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    @allure.step("Simple web element click")
    def _simple_click_element(self, element):
        self.logger.info(f"Simple web element : '{element}' click")
        element.click()

    @allure.step("Clicking web element.")
    def _click(self, locator: tuple):
        self.logger.info(f"Clicking web element: '{locator}'...")
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    @allure.step("Sending keys to input field.")
    def _clear_and_send_keys(self, locator, value):
        self.logger.info(f"Sending to: '{locator}' keys {value}.")
        self._element(locator).clear()
        self._element(locator).send_keys(value)

    @allure.step("Opening link.")
    def _open_link(self, url):
        self.logger.info(f"Opening link {url} ...")
        self.browser.get(url)
