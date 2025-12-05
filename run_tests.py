#!/usr/bin/env python3
"""
Скрипт для запуска тестов с отчетом
"""
import subprocess
import sys
import os
from datetime import datetime


def run_tests():
    """Запускает тесты и создает отчеты"""

    # Создаем директорию для отчетов
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    # Генерируем имя файла с временной меткой
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_report = os.path.join(report_dir, f"report_{timestamp}.html")
    xml_report = os.path.join(report_dir, f"junit_{timestamp}.xml")

    # Команда для запуска тестов
    cmd = [
        "python3", "-m", "pytest",
        "tests/document/",
        "-v",
        f"--html={html_report}",
        "--self-contained-html",
        f"--junitxml={xml_report}",
        "--tb=short"  # короткий traceback
    ]

    print(f"Запускаю тесты...")
    print(f"Команда: {' '.join(cmd)}")
    print(f"Отчеты будут сохранены в: {report_dir}/")
    print("-" * 50)

    # Запускаем тесты
    result = subprocess.run(cmd)

    print("-" * 50)
    print(f"\nОтчеты созданы:")
    print(f"HTML: {html_report}")
    print(f"XML (JUnit): {xml_report}")

    if result.returncode == 0:
        print("\n✅ Все тесты прошли успешно!")
    else:
        print(f"\n❌ Тесты завершились с кодом: {result.returncode}")

    return result.returncode


if __name__ == "__main__":
    sys.exit(run_tests())