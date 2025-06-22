import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, base_url="https://stellarburgers.nomoreparties.site"):
        self.driver = driver
        self.base_url = base_url

    def open(self, url=""):
        with allure.step(f"Открываем страницу: {self.base_url + url}"):
            self.driver.get(self.base_url + url)

    def find(self, locator, timeout=10):
        with allure.step(f"Ищем элемент на странице: {locator}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

    def find_clickable(self, locator, timeout=10):
        with allure.step(f"Ожидаем, пока элемент станет кликабельным: {locator}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )

    def find_all(self, locator, timeout=10):
        with allure.step(f"Ищем все элементы: {locator}"):
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return self.driver.find_elements(*locator)

    def click(self, locator, timeout=10):
        with allure.step(f"Кликаем по элементу: {locator}"):
            self.find_clickable(locator, timeout).click()

    def js_click(self, locator):
        with allure.step(f"Кликаем по элементу с помощью JavaScript: {locator}"):
            element = self.find(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def is_displayed(self, locator, timeout=10):
        with allure.step(f"Проверяем, отображается ли элемент: {locator}"):
            try:
                return self.find(locator, timeout).is_displayed()
            except TimeoutException:
                return False

    def is_not_displayed(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
