from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class ProductFilterForm(BasePage):
    FILTER_PRODUCT_NAME_SELECTOR = (By.CSS_SELECTOR, "input#input-name")
    FILTER_PRODUCT_MODEL_SELECTOR = (By.CSS_SELECTOR, "input#input-model")
    FILTER_BUTTON = (By.CSS_SELECTOR, "button#button-filter")

    def filter_product_by_test_params(self, product_name, product_model):
        self._clear_and_send_keys(self.FILTER_PRODUCT_NAME_SELECTOR, product_name)
        self._clear_and_send_keys(self.FILTER_PRODUCT_MODEL_SELECTOR, product_model)
        self._element(self.FILTER_BUTTON).click()
