from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class UserRegisterForm(BasePage):
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD_1 = (By.CSS_SELECTOR, "#input-password")
    INPUT_PASSWORD_2 = (By.CSS_SELECTOR, "#input-confirm")
    POLICY_AGREE = (By.CSS_SELECTOR, 'input[name="agree"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")

    def login_with(self, firstname, lastname, email, phone, password):
        self._clear_and_send_keys(self.INPUT_FIRST_NAME, firstname)
        self._clear_and_send_keys(self.INPUT_LAST_NAME, lastname)
        self._clear_and_send_keys(self.INPUT_EMAIL, email)
        self._clear_and_send_keys(self.INPUT_PHONE, phone)
        self._clear_and_send_keys(self.INPUT_PASSWORD_1, password)
        self._clear_and_send_keys(self.INPUT_PASSWORD_2, password)
        self._element(self.POLICY_AGREE).click()
        self._element(self.LOGIN_BUTTON).click()
