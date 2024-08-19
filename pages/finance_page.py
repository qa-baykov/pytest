from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FinancePage(BasePage):
    def __init__(self, driver):
        """
        Initializes the FinancePage with a WebDriver instance.

        :param driver: The WebDriver instance used to control the browser.
        """
        super().__init__(driver)

    @property
    def title(self) -> str:
        """
        Retrieves the title of the current page.

        :return: The title of the current page as a string.
        """
        return self.driver.title

    @property
    def stocks(self) -> list:
        """
        Locates and returns the section containing stocks 'You may be interested in'.

        :return: A list of WebElement instances representing the stocks section.
        """
        path = "//section[.//div[@id='smart-watchlist-title'][text()='You may be interested in']]"
        return self.find_elements((By.XPATH, path))

    @property
    def stock_symbols(self) -> list:
        """
        Extracts and returns a list of stock symbols from the 'You may be interested in' section.

        :return: A list of strings representing the stock symbols found on the page.
        """
        stock_symbols = []
        for stock in self.stocks:
            symbols = stock.find_elements(By.XPATH, ".//div[@class='COaKTb']")  # Use a relative path here
            stock_symbols.extend([symbol.text for symbol in symbols])
        return stock_symbols
