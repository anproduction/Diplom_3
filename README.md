# Stellar Burgers UI Tests
Автоматизированные UI тесты для веб-приложения Stellar Burgers, написанные на Python с использованием Selenium WebDriver, pytest и Allure для отчётности.


## Структура проекта

pages/ — классы страниц с методами взаимодействия

tests/ — тестовые сценарии

locators.py — локаторы элементов страницы

conftest.py — фикстуры и настройки pytest

requirements.txt — зависимости проекта

data.py - тестовые данные

## Установка
Клонируйте репозиторий:
``` git clone <URL_репозитория> ```
``` cd <имя_проекта> ```

Рекомендуется создать виртуальное окружение и активировать его:
``` python -m venv venv ```
``` source venv/bin/activate ```  # Linux/macOS
``` venv\Scripts\activate ```     # Windows

Установите зависимости:
``` pip install -r requirements.txt ```

Запуск тестов
``` pytest --browser=chrome ``` # Запуск в Chrome
``` pytest --browser=firefox ``` # Запуск в Firefox
