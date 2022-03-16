import os
from pages.base_page import BasePage


class AuthPage(BasePage):
    """
    Класс для страницы авторизации
    """
    def __init__(self, driver):
        super(AuthPage, self).__init__(driver)
        self._BUTTON_ENTER = "//button[@class='resplash-btn resplash-btn_primary resplash-btn_big svelte-y47oj9']"
        self._INPUT_EMAIL = "//input[@name='username']"
        self._BUTTON_ENTER_PASSWORD = "//button[@data-test-id='next-button']"
        self._INPUT_PASSWORD = "//input[@name='password']"
        self._BUTTON_SIGN_IN = "//button[@data-test-id='submit-button']"
        self.login = os.environ['LOGIN']
        self.password = os.environ['PASSWORD']

    def log_in(self):
        self.fill_field(self._INPUT_EMAIL, self.login)
        self.click_element(self._BUTTON_ENTER_PASSWORD)
        self.wait_until_element_to_be_visible(self._INPUT_PASSWORD)
        self.fill_field(self._INPUT_PASSWORD, self.password)
        self.click_element(self._BUTTON_SIGN_IN)
