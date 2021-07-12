from .MainPage import MainPage
from .elements.UserRegisterForm import UserRegisterForm


class UserRegisterPage(MainPage):

    def add_new_user(self, params: tuple):
        UserRegisterForm(self.browser).login_with(*params)
