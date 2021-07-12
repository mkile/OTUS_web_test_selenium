from selenium.webdriver.common.by import By
from .MainPage import MainPage


class CategoryPage(MainPage):
    ELEMENT_SELECTOR = (By.CSS_SELECTOR,
                       '#content > div:nth-child(3) > div > div > div:nth-child(2) > div.caption > h4 > a')

    def open_tablet_product(self):
        element = self._verify_element_presence(self.ELEMENT_SELECTOR)
        self._click_element(element)
