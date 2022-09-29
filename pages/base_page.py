from selenium.common.exceptions import NoSuchElementException
#создаем класс
class BasePage():
#добавляем в созданный класс методы
#метод Конструктор объявляется ключевым словом __init__ вызывается при создании объекта
#в качестве параметров передаем экземпляр драйвера и url 
    def __init__(self, browser, url):
#внутри конструктора сохраняем параметры, как аттрибуты класса
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)   # неявное ожидание со значением по умолчанию в 10
#метод open открывает нужную страницу, использует метод get     
    def open(self):
        self.browser.get(self.url)
#Чтобы перехватывать исключение, нужна конструкция try/except
#Метод для перехвата исключения        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
