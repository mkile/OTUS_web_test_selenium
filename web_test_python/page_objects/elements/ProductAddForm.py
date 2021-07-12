from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class ProductAddForm(BasePage):
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "input#input-name1.form-control")
    INPUT_DESCRIPTION = (By.CSS_SELECTOR, "div.note-editable.panel-body")
    INPUT_META = (By.CSS_SELECTOR, "input#input-meta-title1")
    INPUT_MODEL = (By.CSS_SELECTOR, "input#input-model")

    def enter_general_parameters(self, product_name, product_desc, product_meta):
        self._clear_and_send_keys(self.INPUT_PRODUCT_NAME, product_name)
        self._clear_and_send_keys(self.INPUT_DESCRIPTION, product_desc)
        self._clear_and_send_keys(self.INPUT_META, product_meta)

    def enter_model(self, product_model):
        self._clear_and_send_keys(self.INPUT_MODEL, product_model)
