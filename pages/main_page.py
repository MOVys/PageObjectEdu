#Page Object для главной страницы сайта
from selenium.webdriver.common.by import By
#импорт базового класса BasePage
from .base_page import BasePage
#импортируем класс с локаторами из locators.py
from .locators import MainPageLocators
#создаем класс MainPage - наследник класса BasePage
class MainPage(BasePage):
#метод для авторизации
    def go_to_login_page(self):
        #Так как браузер хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 
    def should_be_login_link(self):
        #assert self.browser.find_element(By.CSS_SELECTOR, "#login_link"),"Login link is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

