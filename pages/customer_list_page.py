from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Tuple

from pages.base_page import BasePage

class CustomerListPage(BasePage):
    """Page object for the Customer List page in XYZ Bank application."""

    URL = "/manager/list"
    EXPECTED_TITLE = 'XYZ Bank'

    # Locators
    FIRST_NAME_HEADER: Tuple[str, str] = (
        By.XPATH, "//a[contains(@ng-click, \"'fName';\")]"
    )

    CUSTOMER_ROWS: Tuple[str, str] = (By.XPATH, '//tbody/tr')

    def __init__(self, browser):
        """Initialize the CustomerListPage.

        Args:
            browser: WebDriver instance
        """
        super().__init__(browser, base_url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#")

    def open(self) -> None:
        """Open the Customer List page."""
        self.open_page(self.URL)

    def is_page_loaded(self) -> bool:
        """Check if the page is loaded.

        Returns:
            bool: True if the page is loaded, False otherwise
        """
        return (self.get_title() == self.EXPECTED_TITLE and
                self.is_element_present(self.FIRST_NAME_HEADER))

    def click_first_name_header(self) -> None:
        """Click the first name header."""
        self.click_element(self.FIRST_NAME_HEADER)

    def get_customer_names(self) -> List[str]:
        """Get the list of customer first names.

        Returns:
            List[str]: List of customer first names
        """
        customer_rows: List[WebElement] = self.wait_for_elements(self.CUSTOMER_ROWS)
        return [row.find_element(By.XPATH, './td[1]').text for row in customer_rows]

    @staticmethod
    def sort_names_programmatically(names: List[str]) -> List[str]:
        """Return a list of names sorted alphabetically.

        Args:
            names (List[str]): List of names to sort

        Returns:
            List[str]: Sorted list of names
        """
        return sorted(names)
