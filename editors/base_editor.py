import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from sys import platform
from configs import config


class Editor:

    FRAME = (By.NAME, 'frameEditor')
    CURSOR = (By.ID, 'id_target_cursor')
    CANVAS = (By.ID, 'id_viewer')
    TEXT_FIELD = (By.ID, 'area_id')
    FILE_TAB = (By.XPATH, '//a[@data-tab="file"]')
    MAIN_TAB = (By.XPATH, '//a[@data-tab="home"]')
    INSERT_TAB = (By.XPATH, '//a[@data-tab="ins"]')
    DRAW_TAB = (By.XPATH, '//a[@data-tab="draw"]')
    LAYOUT_TAB = (By.XPATH, '//a[@data-tab="layout"]')
    LINKS_TAB = (By.XPATH, '//a[@data-tab="links"]')
    REVIEW_TAB = (By.XPATH, '//a[@data-tab="review"]')
    PROTECT_TAB = (By.XPATH, '//a[@data-tab="protect"]')
    VIEW_TAB = (By.XPATH, '//a[@data-tab="view"]')
    PLUGINS_TAB = (By.XPATH, '//a[@data-tab="plugins"]')
    CLOSE_DOC = (By.ID, 'fm-btn-exit')
    TEXT_LANG = (By.ID, 'btn-cnt-lang') #  Локатор кнопки проверки орфографии
    TEXT_LANG_RU = (By.XPATH, '//a[@langval="ru-RU"]') #  Русский (Россия) для орфографии
    TEXT_LANG_US = (By.XPATH, '//a[@langval="en-US"]') #  Английский (США) для орфографии

    def __init__(self, driver, cmdopt = ''):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.cmdopt = cmdopt

    def find_element(self, locator, timeout=config.timeout):
        """Поиск и ожидание элемента на странице"""
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator), f'{locator} \
        не обнаружен')

    def click_on_element(self, locator, clicks=1, timeout=config.timeout):
        """Ожидание и клик по элементу. Можно задать число кликов"""
        if clicks > 1:
            for i in range(clicks):
                WebDriverWait(self.driver, timeout)\
                    .until(ec.element_to_be_clickable(locator), f'{locator} не кликабелен').click()
        elif clicks == 1:
            WebDriverWait(self.driver, timeout)\
                .until(ec.element_to_be_clickable(locator), f'{locator} не кликабелен').click()
        return self

    def click_on_element_coord(self, locator, clicks=1):
        """Клик по координатам элемента. Применяется для некликабельных элементов или в случае перехвата клика"""
        elem = self.find_element(locator)
        if clicks > 1:
            for i in range(clicks):
                self.action.move_to_element(elem).click().perform()
        elif clicks == 1:
            self.action.move_to_element(elem).click().perform()
        return self

    def click_on_element_coord_with_offset(self, locator, x, y, clicks=1, timeout=config.timeout):
        """Клик по элементу со смещением по осям x и y в пикселях (Например, для работы с canvas, в котором нет объектов DOM"""
        elem = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
        if clicks > 1:
            for i in range(clicks):
                self.action.move_to_element_with_offset(elem, x, y).click().perform()
        elif clicks == 1:
            self.action.move_to_element_with_offset(elem, x, y).click().perform()
        return self

    def drag_n_drop(self, locator, drag_x, drag_y, move_x=0, move_y=0):
        """
        Метод тяни-бросай. Зажимает ЛКМ, перемещается к координате x;y, отпускает ЛКМ.
        От штатного метода в Selenium отличается перемещением к заданной координате, а не к локатору.
        Применимо для рисования объектов.
        """
        elem = self.find_element(locator)
        (self.action.move_to_element(elem)
         .move_by_offset(move_x, move_y)
         .click_and_hold()
         .move_by_offset(drag_x, drag_y)
         .release().perform())
        return self

    def send_keys_to_element(self, locator, keys, count=1, timeout=config.timeout):
        """Отправить строку или нажатие клавиши в элемент input. Поддерживается многократное действие"""
        if count > 1:
            for i in range(count):
                WebDriverWait(self.driver, timeout)\
                    .until(ec.element_to_be_clickable(locator), f'{locator} не обнаружен')\
                    .send_keys(keys)
        elif count == 1:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator)).send_keys(keys)
        return self

    def press_key(self, key1, count=1):
        """Нажать кнопку без привязки к конкретному элементу"""
        for i in range(count):
            self.action.key_down(key1).key_up(key1).perform()
        return self

    def send_hotkey(self, key1, key2, key3=None):
        """Нажать сочетание клавиш. Поддерживается до 3-х кнопок"""
        if platform == "darwin":
            if key1 == Keys.CONTROL:
                key1 = Keys.COMMAND
            if key2 == Keys.CONTROL:
                key2 = Keys.COMMAND
            if key3 == Keys.CONTROL:
                key3 = Keys.COMMAND

        if key3 is None:
            self.action.key_down(key1).key_down(key2).key_up(key2).key_up(key1).perform()
        else:
            self.action.key_down(key1).key_down(key2).key_down(key3).key_up(key3).key_up(key2).key_up(key1).perform()
        return self

    def send_key_and_click_by_offset(self, locator, key, x, y):
        """
        Зажать клавишу и сделать клик по координатам относительно желаемого элемента.
        Применимо, к примеру, для множественного выделения через Ctrl+ЛКМ
        """
        elem = self.find_element(locator)
        self.action.move_to_element_with_offset(elem, x, y).key_down(key).click().key_up(key).perform()
        return self

    def pause_in_test(self, seconds=config.general_pause):
        self.action.pause(seconds).perform()
        return self

    def get_element_state(self, locator, timeout=config.timeout):
        """Получить состояние элемента. Применяется для отладки кода"""
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        print(f'\nЭлемент виден: {element.is_displayed()}')
        print(f'Элемент активен: {element.is_enabled()}')
        print(f'Элемент выделен: {element.is_selected()}')
        return self

    def switch_to_tab(self, index=1):
        """
        Переключиться во вкладку (окно).
        По умолчанию переключение во вторую вкладку (первая вкладка с индексом [0] всегда основное окно редактора)
        """
        self.driver.switch_to.window(self.driver.window_handles[index])
        return self

    def switch_to_frame(self, locator):
        """Переключиться во фрейм в окне"""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)
        return self

    def new_file(self, locator):
        """Базовый метод создания нового файла (документа, таблицы, презентации)"""
        self.click_on_element(locator)
        self.pause_in_test(config.general_pause)
        self.switch_to_tab()
        self.switch_to_frame(self.FRAME)
        self.pause_in_test(config.pause_before_creating_file)
        return self

    def close_file(self):
        """Закрытие активного файла. В случае появления системного окна с предложением сохранения документа происходит отказ"""
        self.click_on_element(self.FILE_TAB)
        self.click_on_element(self.CLOSE_DOC)
        self.action.pause(config.general_pause).perform()
        pyautogui.press('right')
        pyautogui.press('enter')
        self.switch_to_tab(0)
        return self

    def change_spellcheck(self, lang):
        """Смена языка проверки орфографии. Поддерживается русский или английский"""
        self.click_on_element(self.TEXT_LANG)
        if lang == 'ru':
            element = self.driver.find_element(self.TEXT_LANG_RU)
            actions = ActionChains(self.driver)
            actions.scroll_to_element(element).perform()
            self.click_on_element(self.TEXT_LANG_RU)
        elif lang == 'us':
            element = self.driver.find_element(self.TEXT_LANG_US)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.click_on_element(self.TEXT_LANG_US)
        return self

    def do_element_screenshot(self, path, element=CANVAS):
        element = self.find_element(element)
        element.screenshot(path)
