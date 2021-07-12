from selenium.webdriver.common.by import By
from .BasePage import BasePage
from .elements.ProductFilterForm import ProductFilterForm


class AdminPage(BasePage):
    CATEGORY_SELECTOR = (By.CSS_SELECTOR, "li#menu-catalog")
    PRODUCT_PAGE_SELECTOR = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_NEW_PRODUCT_SELECTOR = (By.CSS_SELECTOR, ".btn.btn-primary[data-original-title='Add New']")
    FILTERED_PRODUCTS_SELECTOR = (By.CSS_SELECTOR, "tbody > tr > td.text-left")
    FILTERED_PRODUCT_CHECKBOX_SELECTOR = (By.CSS_SELECTOR, "tbody > tr > td.text-center > input[type='checkbox']")
    DELETE_PRODUCT_SELECTOR = (By.CSS_SELECTOR, "i.fa.fa-trash-o")

    def open_products_page(self):
        element = self._verify_element_presence(self.CATEGORY_SELECTOR)
        self._click_element(element)
        element = self._verify_element_presence(self.PRODUCT_PAGE_SELECTOR)
        self._click_element(element)

    def add_new_product_click(self):
        element = self._verify_element_presence(self.ADD_NEW_PRODUCT_SELECTOR)
        self._click_element(element)

    def check_test_product_present(self, product_name, product_desc, product_meta, product_model):
        ProductFilterForm(self.browser).filter_product_by_test_params(product_name, product_model)
        self._verify_element_presence(self.FILTERED_PRODUCTS_SELECTOR)

    def delete_test_product(self):
        element = self._verify_element_presence(self.FILTERED_PRODUCT_CHECKBOX_SELECTOR)
        self._click_element(element)
        element = self._verify_element_presence(self.DELETE_PRODUCT_SELECTOR)
        self._click_element(element)
        self.logger.info(f'Admin page clicking alert')
        alert = self.browser.switch_to.alert
        alert.accept()
