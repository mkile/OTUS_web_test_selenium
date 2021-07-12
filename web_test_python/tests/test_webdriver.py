import pytest
from re import match
import allure


def test_title_value(browser, url):
    allure.dynamic.title(f'Проверка работы браузера при открытии ссылки {url}')
    allure.step(f'Open {url}')
    browser.get(url)
    assert match(r'.+o|Opencart.+', browser.title)
