import pytest
from selenium import webdriver
import json
import os

DRIVERS = './drivers/'


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     choices=['chrome', 'firefox', 'opera'],
                     default='chrome',
                     help='Укажите драйвер')
    parser.addoption('--url',
                     action='store',
                     default='https://demo.opencart.com',
                     help='Укажите ссылку на сайт Opencart')
    parser.addoption('--headless',
                     action='store_true',
                     default=False,
                     help='Запускать ли браузер в headless режиме')
    parser.addoption('--timeout',
                     action='store',
                     default=5,
                     type=int,
                     help='Время ожидания элемента на странице')
    parser.addoption('--oc_adm_name',
                     action='store',
                     default='demo',
                     type=str,
                     help='Логин от админки Opencart')
    parser.addoption('--oc_adm_pass',
                     action='store',
                     default='demo',
                     type=str,
                     help='Пароль от админки Opencart')


@pytest.fixture
def browser(request):
    browser = request.config.getoption('--browser')
    timeout = request.config.getoption('--timeout')
    url = request.config.getoption('--url')
    driver = None
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = request.config.getoption('--headless')
        driver = webdriver.Chrome(executable_path=DRIVERS + 'chromedriver.exe', options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = request.config.getoption('--headless')
        driver = webdriver.Firefox(executable_path=DRIVERS + 'geckodriver.exe', options=options)
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=DRIVERS + 'operadriver.exe')
    driver.timeout = timeout
    request.addfinalizer(driver.quit)
    driver.get(url)

    return driver


@pytest.fixture(scope='module')
def test_parameters():
    with open(os.path.abspath('data/test_data.json'), 'r') as file:
        json_data = json.loads(file.read())
    yield json_data


@pytest.fixture(scope='module')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='module')
def credentials(request):
    login = request.config.getoption('--oc_adm_name')
    password = request.config.getoption('--oc_adm_pass')
    return login, password


@pytest.fixture(scope='module')
def product_description():
    product_name = 'TestProduct'
    product_desc = 'TestDescription'
    product_meta = 'TestMeta'
    product_model = 'TestModel'
    return product_name, product_desc, product_meta, product_model
