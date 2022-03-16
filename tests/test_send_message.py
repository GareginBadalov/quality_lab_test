"""Тест отправки письма на мэйл.ру"""
from pages.auth_page import AuthPage
from pages.main_page import MainPage


class TestSendMessage:
    """Класс для тестов отправки письма на мэйл.ру"""
    def test_send_message(self, driver):
        """Тест отправки письма"""
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        auth_page.go_to_site()
        auth_page.log_in()
        main_page.create_and_send_message('test', 'Тестовое письмо')
