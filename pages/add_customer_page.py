from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"

        self.first_name_input = (By.XPATH, '//input[@ng-model="fName"]')
        self.last_name_input = (By.XPATH, '//input[@ng-model="lName"]')
        self.post_code_input = (By.XPATH, '//input[@ng-model="postCd"]')
        self.add_customer_button = (By.XPATH, '//button[@type="submit"]')

    def open(self):
        self.open_page(self.url)
