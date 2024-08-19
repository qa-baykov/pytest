from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        """
        Initializes the BasePage with a WebDriver instance and a default wait time.

        :param driver: The WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self, url):
        """
        Navigates to the specified URL in the browser.

        :param url: The URL to open in the browser.
        """
        self.driver.get(url)

    def find_elements(self, locator):
        """
        Waits for all elements matching the given locator to be present on the page and returns them.

        :param locator: A tuple containing the strategy to locate elements (By.ID, By.XPATH)
                        and the value to search for.
        :return: A list of WebElement instances matching the locator.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))
