import datetime
import platform
import os
from yattag import Doc
from utils import diagram
from configs.config import ROOT_DIR

doc, tag, text, line = Doc().ttl()
today = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')

def get_os_info():
    if platform.system() == 'Linux':
        return platform.freedesktop_os_release()['PRETTY_NAME']
    if platform.system() == 'Darwin':
        import subprocess
        try:
            # Получаем информацию через системную команду
            result = subprocess.run(
                ['sw_vers'],
                capture_output=True,
                text=True,
                check=True
            )
            lines = result.stdout.strip().split('\n')
            # Преобразуем: ProductName: macOS -> macOS
            info = [line.split(': ')[1] for line in lines if ': ' in line]
            return ', '.join(info)
        except:
            # Fallback на platform.mac_ver()
            mac_info = platform.mac_ver()
            version = mac_info[0] or "macOS"
            return f"{version} (Darwin)"
    if platform.system() == 'Windows':
        return f'{platform.system()} {platform.release()} {platform.version()}'
    return 'no OS info'


def create_report(data, duration):
    doc.asis('<!DOCTYPE html>')
    with tag('html', lang='ru'):
        with tag('head'):
            with tag('meta', charset='UTF-8'):
                pass
            with tag('meta', name="viewport", content="width=device-width, initial-scale=1.0"):
                pass
            with tag('title'):
                text('Отчет о тестировании')
            with tag('link', rel='stylesheet', href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'):
                pass
            with tag('script', src='https://cdn.jsdelivr.net/npm/chart.js'):
                pass
            with tag('style'):
                text('.table-striped tbody tr:nth-of-type(odd) {background-color: #f2f2f2;}'
                     '.table-hover tbody tr:hover {background-color: #e6e6e6;}'
                     '.chart-container {position: relative; align-items: center; justify-content: center; display: flex; margin: 0 auto; margin-bottom: 5%; height: 40%; width: 40%;}')
        with tag('body'):
            with tag('div', klass='container my-5'):
                with tag('h2', klass='text-center mb-4'):
                    text('Отчет о прохождении автотестирования')
                    with tag('br/'):
                        text('Р7-Офис (десктопная версия)')
                with tag('h5', klass='text-right mb-4'):
                    text(f'от {today}')
                with tag('h5', klass='text-right mb-4'):
                        text(f'время прохождения {(int(duration) // 3600):02d}:{((int(duration) % 3600) // 60):02d}:{(int(duration) % 60):02d}')
                with tag('h5', klass='text-right mb-4'):
                    text(f'ОС {get_os_info()}')
                with tag('div', klass='chart-container'):
                    with tag('canvas', id='statusChart'):
                        pass
                with tag('table', klass='table table-striped table-hover'):
                    with tag('thead'):
                        with tag('tr'):
                            with tag('th'):
                                text('№')
                            with tag('th'):
                                text('Название сценария')
                            with tag('th'):
                                text('Статус')
                    with tag('tbody'):
                        number = 1
                        for test, result in data.items():
                            with tag('tr'):
                                with tag('td'):
                                    text(number)
                                with tag('td'):
                                    text(test)
                                with tag('td'):
                                    if result == 'passed':
                                        with tag('span', klass='badge badge-success'):
                                            text('Пройден')
                                    else:
                                        with tag('span', klass='badge badge-danger'):
                                            text('Провален')
                            number += 1
            with tag('script'):
                text(diagram.js)
    if not os.path.exists(f'{ROOT_DIR}/reports/'):
        os.makedirs(f'{ROOT_DIR}/reports')
    with open(f'{ROOT_DIR}/reports/report_' + datetime.datetime.now().strftime('%d-%m-%Y_%H-%M' + '.html'), 'w', encoding="UTF-8") as report:
        results = doc.getvalue()
        report.write(results.replace('&gt;', '>'))
