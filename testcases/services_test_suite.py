import unittest
from webdriver import Driver
from values import strings
from pageobjects.servicespage import ServicesPage

class TestPopulixLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_login_correct_email_password(self):
        page = ServicesPage(self.driver)
        page.input_email_password(strings.correct_email, strings.correct_password)
        page.validate_correct_name_is_displayed()

    def test_login_incorrect_email_password(self):
        page = ServicesPage(self.driver)
        page.input_email_password(strings.incorrect_email, strings.incorrect_password)
        page.validate_error_email_is_displayed()

    def test_login_incorrect_email(self):
        page = ServicesPage(self.driver)
        page.input_email_password(strings.incorrect_email, strings.correct_password)
        page.validate_error_email_is_displayed()

    def test_login_incorrect_password(self):
        page = ServicesPage(self.driver)
        page.input_email_password(strings.correct_email, strings.incorrect_password)
        page.validate_error_password_is_displayed()

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()