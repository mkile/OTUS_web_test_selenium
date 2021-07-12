import pytest
from page_objects.MainPage import MainPage
from page_objects.CategoryPage import CategoryPage
from page_objects.ProductPage import ProductPage
from page_objects.UserLoginPage import UserLoginPage
from page_objects.AdminLoginPage import AdminLoginPage
import allure


@pytest.mark.parametrize("element", range(5))
def test_main_page_elements(browser, element, test_parameters):
    allure.dynamic.title(f'Поиск на главной странице элемента {test_parameters["mainpage"]["data"][element]}')
    MainPage(browser).wait_element(test_parameters["mainpage"]['data'][element])


@pytest.mark.parametrize("element", range(5))
def test_category_page_elements(browser, element, test_parameters):
    allure.dynamic.title(f'Поиск на странице категорий элемента {test_parameters["categorypage"]["data"][element]}')
    MainPage(browser).open_category()
    CategoryPage(browser).wait_element(test_parameters['categorypage']['data'][element])


@pytest.mark.parametrize("element", range(5))
def test_product_page_elements(browser, element, test_parameters):
    allure.dynamic.title(f'Поиск на странице продукта элемента {test_parameters["productpage"]["data"][element]}')
    MainPage(browser).open_tablet_category()
    CategoryPage(browser).open_tablet_product()
    ProductPage(browser).wait_element(test_parameters['productpage']['data'][element])


@pytest.mark.parametrize("element", range(5))
def test_userlogin_page_elements(browser, element, test_parameters):
    allure.dynamic.title(f'Поиск на странице входа пользователя {test_parameters["userloginpage"]["data"][element]}')
    MainPage(browser).open_user_login()
    UserLoginPage(browser).wait_element(test_parameters['userloginpage']['data'][element])


@pytest.mark.parametrize("element", range(5))
def test_adminlogin_page_elements(browser, element, test_parameters):
    allure.dynamic.title(f'Поиск на странице входа администратора {test_parameters["adminloginpage"]["data"][element]}')
    MainPage(browser).open_admin_login()
    AdminLoginPage(browser).wait_element(test_parameters['adminloginpage']['data'][element])
