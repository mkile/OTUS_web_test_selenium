from selenium.webdriver.common.by import By
from .BasePage import BasePage
from .elements.ProductAddForm import ProductAddForm


class AddProductPage(BasePage):
    DATA_SELECTOR = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
    SAVE_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button.btn.btn-primary[data-original-title='Save']")

    def add_test_product(self, product_name, product_desc, product_meta, product_model):
        ProductAddForm(self.browser).enter_general_parameters(product_name, product_desc, product_meta)
        element = self._verify_element_presence(self.DATA_SELECTOR)
        self._click_element(element)
        ProductAddForm(self.browser).enter_model(product_model)
        element = self._verify_element_presence(self.SAVE_BUTTON_SELECTOR)
        self._click_element(element)
