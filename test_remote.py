from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("Пробую Remote подключение...")
options = Options()
options.debugger_address = "localhost:8080"

try:
    # Способ 1: Remote
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    capabilities = DesiredCapabilities.CHROME.copy()
    driver = RemoteWebDriver(
        command_executor='http://localhost:8080',
        desired_capabilities=capabilities,
        options=options
    )
    print("✓ Успешно через RemoteWebDriver")
    driver.quit()
except Exception as e:
    print(f"✗ RemoteWebDriver ошибка: {e}")

    # Способ 2: Прямое создание
    try:
        driver = webdriver.Chrome(options=options)
        print("✓ Успешно через прямой Chrome")
        driver.quit()
    except Exception as e2:
        print(f"✗ Прямой Chrome ошибка: {e2}")
