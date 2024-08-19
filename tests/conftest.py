"""
This module sets up browser-based automated tests using Selenium and Pytest.

It includes:
- Loading configurations from a JSON file.
- Dynamic WebDriver setup for Chrome and Firefox.
- Fixtures for managing WebDriver instances and test URLs.
"""

import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_PATH = "settings.json"


def pytest_addoption(parser):
    """
    Adds a command-line option to the pytest command.

    :param parser: The argument parser object used to add custom command-line options.
    """
    parser.addoption("--set-to-run", action="store", default=None,
                     help="Set the value for set_to_run (None, not_in_test, not_in_actual)")


@pytest.fixture()
def set_to_run(request):
    """
    Retrieves the value of the `--set-to-run` command-line option.
    If no value is provided, it defaults to `None`.

    :param request: The pytest request object, used to access the command-line options.
    :return: The value of the `--set-to-run` command-line option.
    """
    return request.config.getoption("--set-to-run")


@pytest.fixture()
def settings():
    """
    Loads and returns the configuration settings from a JSON file.
    :return: A dictionary containing the configuration settings.
    """
    try:
        with open(CONFIG_PATH) as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        path = "../" + CONFIG_PATH
        with open(path) as config_file:
            return json.load(config_file)


@pytest.fixture()
def driver(request):
    """
    Initializes and returns a Chrome WebDriver instance.

    :param request: The pytest request object, which could be used for further configuration.
    :return: A Chrome WebDriver instance.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture()
def finance_page_url(settings):
    """
    Retrieves the URL of the finance page from the configuration settings.

    :param settings: A dictionary containing the configuration settings loaded from the JSON file.
    :return: The finance page URL as a string.
    """
    return settings.get('finance_page_url')
