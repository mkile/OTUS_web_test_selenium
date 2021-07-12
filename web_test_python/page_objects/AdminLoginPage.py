from .MainPage import MainPage
from .elements.AdminLoginForm import AdminLoginForm


class AdminLoginPage(MainPage):
    def login_with(self, username, password):
        AdminLoginForm(self.browser).login_with(username, password)
