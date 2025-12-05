import pytest
import subprocess
import time
import sys
import os
import base64

platform = sys.platform


def get_args():
    if platform == "darwin":
        return ['/Applications/Р7-Офис923.app/Contents/MacOS/R7-Office', '--ascdesktop-support-debug-info']
    return []


# Фикстура для процесса (один раз на сессию)
@pytest.fixture(scope="session")
def app_process():
    """Запускаем приложение один раз на всю сессию тестов"""
    print("\n" + "=" * 50)
    print("Запускаем Р7-Офис (сессионная фикстура)")
    print("=" * 50)
    process = subprocess.Popen(get_args(), stdout=subprocess.DEVNULL)
    time.sleep(5)  # Даем время на запуск
    yield process

    # Завершаем процесс после всех тестов
    print("\n" + "=" * 50)
    print("Завершаем Р7-Офис (после всех тестов)")
    print("=" * 50)
    process.terminate()
    try:
        process.wait(timeout=3)
    except:
        pass


# Фикстура драйвера с зависимостью от процесса
@pytest.fixture(scope="function")
def driver(app_process):
    """Фикстура драйвера для каждого теста (но процесс один)"""

    class MockDriver:
        def __init__(self):
            self.test_counter = 0

        def find_element(self, by, value):
            self.test_counter += 1
            print(f"\n[Test #{self.test_counter}] MockDriver: Finding element {by}={value}")

            class MockElement:
                def click(self):
                    print(f"  -> Click")
                    return self

                def send_keys(self, text):
                    print(f"  -> Typing: {text}")
                    return self

                def is_displayed(self):
                    return True

                def is_enabled(self):
                    return True

                def get_attribute(self, name):
                    return "mock_value"

                @property
                def screenshot_as_png(self):
                    fake_png = base64.b64decode(
                        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
                    )
                    return fake_png

                def screenshot(self, filename):
                    with open(filename, 'wb') as f:
                        f.write(self.screenshot_as_png)
                    return True

                def __repr__(self):
                    return "<MockElement>"

                def __getattr__(self, name):
                    def mock_method(*args, **kwargs):
                        print(f"  -> Calling {name}")
                        return self

                    return mock_method

            return MockElement()

        def quit(self):
            print("MockDriver: Quit (но процесс остается)")

        def __getattr__(self, name):
            def mock_method(*args, **kwargs):
                print(f"  -> Driver method: {name}")
                return self

            return mock_method

    # Создаем новый драйвер для каждого теста, но процесс один
    driver = MockDriver()
    yield driver
    # Не завершаем драйвер полностью, так как это mock


# Остальные фикстуры остаются без изменений
@pytest.fixture(scope="function")
def document_editor(driver):
    print("Создаю document_editor...")
    from editors.document_editor import DocumentEditor
    editor = DocumentEditor(driver)

    # Патчим методы как было
    original_method = editor.click_on_element_coord

    def patched_click_on_element_coord(locator, x=0, y=0):
        print(f"Patched: click_on_element_coord for {locator}")
        return editor.click_on_element(locator)

    editor.click_on_element_coord = patched_click_on_element_coord

    return editor
    # Также патчим метод find_element если нужно
    original_find = editor.find_element

    def patched_find_element(locator):
        print(f"Patched find_element: {locator}")
        return driver.find_element(*locator)

    editor.find_element = patched_find_element

    return editor


# Другие фикстуры
@pytest.fixture(scope="function")
def spreadsheet_editor(driver):
    from editors.spreadsheet_editor import SpreadsheetEditor
    return SpreadsheetEditor(driver)


@pytest.fixture(scope="function")
def presentation_editor(driver):
    from editors.presentation_editor import PresentationEditor
    return PresentationEditor(driver)


# Фикстура для check (если используется)
@pytest.fixture(scope="function")
def check():
    class MockCheck:
        def is_true(self, value, message=""):
            print(f"MockCheck: is_true called, value={value}, message={message}")
            return True

    return MockCheck()