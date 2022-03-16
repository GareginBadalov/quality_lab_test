import os
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Класс для основной страницы с письмами
    """
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self._BUTTON_CREATE_MAIL = "//span[@class='compose-button__txt']"
        self._INPUT_RECIPIENT = "//input[@class='container--H9L5q size_s--3_M-_' and @tabindex='100']"
        self._INPUT_TERM = "//input[@class='container--H9L5q size_s--3_M-_' and @tabindex='400']"
        self._INPUT_MESSAGE_BODY = "//div[@tabindex='505']/div"
        self._BUTTON_SEND_MESSAGE = "//span[@class='button2__txt']"
        self.email_of_recipient = os.environ['EMAIL_OF_RECIPIENT']

    def create_and_send_message(self, term, body):
        self.click_element(self._BUTTON_CREATE_MAIL)
        self.fill_field(self._INPUT_RECIPIENT, self.email_of_recipient)
        self.fill_field(self._INPUT_TERM, term)
        self.fill_field(self._INPUT_MESSAGE_BODY, body)
        self.click_element(self._BUTTON_SEND_MESSAGE)