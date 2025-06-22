from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")  # Кнопка "Лента заказов"
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]")  # Вход на главной странице
    CREATE_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")  # Текст "Собери бургер"
    READY_TEXT = (By.XPATH, "//p[text()='Готовы:']")  # Текст "Готовы"
    BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # Кнопка "Флюоресцентная булка"
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")  # Поп-ап "Детали ингредиента")
    CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON = (By.XPATH, "(//button[contains(@class, 'close_modified')])[1]")  # Кнопка "Закрыть" на поп-апе Детали ингредиента
    SAUCES_BUTTON = (By.XPATH, "//h2[text()='Соусы']")  # Кнопка "Соусы"
    SPICY_SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")  # Соус Spicy-X
    CONSTRUCTOR_FIELD = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")  # Поле для создания бургера
    COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[3]") # Счетчик в правом верхнем углу над булкой
    ORDER_ID = (By.XPATH, "//p[text()='идентификатор заказа']")  # Идентификатор заказа
    ORDER_POP_UP = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")  # Поп-ап заказа
    CLOSE_POP_UP_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]") # Кнопка "Закрыть" поп-ап

class OrderPageLocators:
    ORDER_LIST = (By.XPATH, "(//div[contains(@class, 'OrderHistory_dataBox__1mkxK')])[1]")  # Первый элемент списка заказов
    STRUCTURE_TEXT = (By.XPATH, "//p[text()='Cостав']")  # Текст "Состав"
    ALL_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")  # Общее кол-во заказов
    TODAY_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")  # Выполнено за сегодня

class AccountPageLocators:
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input")  # Ввод Email
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/../input")  # Ввод пароля
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")  # Кнопка "Профиль"
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")  # Кнопка "История заказов"
    HISTORY_BUTTON_ACTIVE = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and @href='/account/order-history']")
    FIRST_ORDER = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')])[1]")  # Первый заказ
    LAST_ORDER = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')])[last()]")  # Последний заказ
    ORDER_COMPLETED_TEXT = (By.XPATH, "//p[text()='Выполнен']")  # Текст "Выполнен"
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"
