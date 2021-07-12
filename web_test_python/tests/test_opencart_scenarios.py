import pytest
from page_objects.MainPage import MainPage
from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage
from page_objects.AddProductPage import AddProductPage
from page_objects.UserRegisterPage import UserRegisterPage
import time
import allure


def test_add_new_product(browser, admin_credentials, product_description):
    allure.dynamic.title(f'Добавление продукта {product_description} через админку')
    MainPage(browser).open_admin_login()
    AdminLoginPage(browser).login_with(*admin_credentials)
    AdminPage(browser).open_products_page()
    AdminPage(browser).add_new_product_click()
    AddProductPage(browser).add_test_product(*product_description)
    AdminPage(browser).check_test_product_present(*product_description)


def test_delete_new_product(browser, admin_credentials, product_description):
    allure.dynamic.title(f'Удаление продукта {product_description} через админку')
    MainPage(browser).open_admin_login()
    AdminLoginPage(browser).login_with(*admin_credentials)
    AdminPage(browser).open_products_page()
    AdminPage(browser).check_test_product_present(*product_description)
    time.sleep(1)
    AdminPage(browser).delete_test_product()
    time.sleep(1)


def test_add_new_user(browser, new_user_credentials):
    allure.dynamic.title(f'Добавление пользователя  {new_user_credentials}')
    MainPage(browser).open_user_register()
    time.sleep(1)
    UserRegisterPage(browser).add_new_user(new_user_credentials)
    time.sleep(1)


def test_switch_currency(browser):
    allure.dynamic.title(f'Переключение валюты')
    MainPage(browser).switch_currency(0)
    time.sleep(1)
    MainPage(browser).switch_currency(1)
    time.sleep(1)
