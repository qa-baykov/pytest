from pages.finance_page import FinancePage


def test_compare_stock_symbols(driver, finance_page_url, set_to_run):
    """
    Compares stock symbols retrieved from Google Finance against a predefined set of test data.
    :param driver: WebDriver instance used to control the browser.
    :param finance_page_url: The URL of the Google Finance page to be opened.
    :param set_to_run: Determines which comparison to run:
                       - 'not_in_test': Print symbols in actual data but not in test data.
                       - 'not_in_actual': Print symbols in test data but not in actual data.
                       - None: Perform both comparisons and print the results.
    """
    test_data = ["NFLX", "MSFT", "TSLA"]  # Test data for comparison

    finance_page = FinancePage(driver)
    finance_page.open(finance_page_url)

    expected_title = "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
    assert finance_page.title == expected_title, f"Expected title: {expected_title}, Actual: {finance_page.title}"

    stock_symbols = finance_page.stock_symbols
    assert stock_symbols, "No stocks symbols were found"

    actual_not_in_test = [stock for stock in stock_symbols if stock not in test_data]
    test_not_in_actual = [stock for stock in test_data if stock not in stock_symbols]

    if set_to_run is None or set_to_run == 'not_in_test':
        print(f"\nStock symbols that are in actual stocks but not in given test data: {actual_not_in_test}")

    if set_to_run is None or set_to_run == 'not_in_actual':
        print(f"\nStock symbols that are in given test data but not in actual stocks: {test_not_in_actual}")
