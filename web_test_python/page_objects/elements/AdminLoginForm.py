from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class AdminLoginForm(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")

    def login_with(self, username, password):
        self._clear_and_send_keys(self.INPUT_EMAIL, username)
        self._clear_and_send_keys(self.INPUT_PASSWORD, password)
        self._element(self.LOGIN_BUTTON).click()
