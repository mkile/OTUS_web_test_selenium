from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    CATEGORY_PAGE_LI_SELECTOR = (By.CSS_SELECTOR,
                                 "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1) > a")
    CATEGORY_PAGE_LINK_SELECTOR = (By.CSS_SELECTOR,
                                   "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > "
                                   "ul > li:nth-child(1) > div > a")
    TABLET_CATEGORY_NAME = (By.CSS_SELECTOR,
                            "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(4) > a")
    USER_LOGIN_DROPDOWN_NAME = (By.CSS_SELECTOR, 'a.dropdown-toggle[title="My Account"]')
    USER_LOGIN_LINKS = (By.CSS_SELECTOR, "ul.dropdown-menu.dropdown-menu-right")
    CURRENCY_DROPDOWN_NAME = (By.CSS_SELECTOR, 'button.btn.btn-link.dropdown-toggle')
    CURRENCYS_LINKS = (By.CSS_SELECTOR, 'ul.dropdown-menu')
    ADMIN_PAGE = '/admin/'

    def wait_element(self, element):
        self._verify_element_presence((By.CSS_SELECTOR, element))

    def open_category(self):
        element = self._verify_element_presence(self.CATEGORY_PAGE_LI_SELECTOR)
        self._click_element(element)
        element = self._verify_element_presence(self.CATEGORY_PAGE_LINK_SELECTOR)
        self._click_element(element)

    def open_tablet_category(self):
        element = self._verify_element_presence(self.TABLET_CATEGORY_NAME)
        self._click_element(element)

    def open_user_login(self):
        element = self._verify_element_presence(self.USER_LOGIN_DROPDOWN_NAME)
        self._click_element(element)
        element = self._verify_element_presence(self.USER_LOGIN_LINKS)
        element = element.find_elements_by_css_selector("a")
        self._click_element(element[1])

    def open_user_register(self):
        element = self._verify_element_presence(self.USER_LOGIN_DROPDOWN_NAME)
        self._click_element(element)
        element = self._verify_element_presence(self.USER_LOGIN_LINKS)
        element = element.find_elements_by_css_selector("a")
        self._click_element(element[0])

    def open_admin_login(self):
        self._open_link(self.browser.current_url + self.ADMIN_PAGE)

    def switch_currency(self, currency):
        element = self._verify_element_presence(self.CURRENCY_DROPDOWN_NAME)
        self._click_element(element)
        element = self._verify_element_presence(self.CURRENCYS_LINKS)
        element = element.find_elements_by_css_selector("button")
        self._click_element(element[currency])
