from selenium.webdriver.common.by import By
from values import strings
from .basescreen import BaseScreen

class LoginPage(BaseScreen):
    """Models login functionality as a Page Object"""

    # login account
    email_input = (By.ID, "input_email")
    password_input = (By.ID, "input_password")
    login_button = (By.ID, "submit_login")
    error_email = (By.ID, "input_email-helper-text")
    error_password = (By.ID, "input_password-helper-text")
    full_name = (By.XPATH, "//*[@id='dashboard']/div[4]/div[2]/div/h4")

    # newly added
    def input_email_password(self, email, password):
        email_field = self.select_element(self.email_input)
        email_field.send_keys(email)
        self.wait_until_clickable(self.password_input).click()
        password_field = self.select_element(self.password_input)
        password_field.send_keys(password)
        self.hover_one_of_elements(self.login_button)
        self.wait_until_clickable(self.login_button).click()

    def validate_correct_name_is_displayed(self):
        full_name = self.select_element(self.full_name).text
        assert full_name.lower() == strings.full_name.lower(), "Incorrect fullname"

    def validate_error_email_is_displayed(self):
        error_email_is_displayed = self.is_element_visible(self.error_email)
        assert error_email_is_displayed, "Validation error email is displayed."

    def validate_error_password_is_displayed(self):
        error_password_is_displayed = self.is_element_visible(self.error_password)
        assert error_password_is_displayed, "Validation error password is displayed."
