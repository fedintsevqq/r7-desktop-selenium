import sys
import ctypes
import ctypes.util


def get_keyboard_layout():
    """Определение текущей раскладки клавиатуры"""
    if sys.platform == 'win32':
        return _get_windows_layout()
    elif sys.platform.startswith('linux'):
        return _get_linux_layout()
    elif sys.platform == 'darwin':
        return _get_macos_layout()
    else:
        return "unknown"


def _get_windows_layout():
    """Для Windows"""
    user32 = ctypes.windll.user32
    keyboard_layout = user32.GetKeyboardLayout(0)
    lang_id = keyboard_layout & 0xFFFF
    if hex(lang_id) == '0x419':
        return 'ru-ru'
    elif hex(lang_id) == '0x409':
        return 'en-us'
    else:
        return 'unknown'


def _get_linux_layout():
    """Для Linux (требует установки xkbgroup)"""
    try:
        from xkbgroup import XKeyboard
        xkb = XKeyboard()
        return xkb.group_symbol
    except ImportError:
        return _get_linux_layout_fallback()


def _get_linux_layout_fallback():
    """Альтернативный способ для Linux"""
    try:
        import subprocess
        result = subprocess.run(['setxkbmap', '-query'],
                                capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'layout:' in line:
                return line.split(':')[1].strip()
    except:
        pass
    return "unknown"


def _get_macos_layout():
    """Для macOS"""
    try:
        import subprocess
        result = subprocess.run([
            'defaults', 'read',
            '~/Library/Preferences/com.apple.HIToolbox.plist',
            'AppleSelectedInputSources'
        ], capture_output=True, text=True, shell=True)

        if 'KeyboardLayout Name' in result.stdout:
            lines = result.stdout.split('\n')
            for line in lines:
                if 'KeyboardLayout Name' in line:
                    return line.split('=')[1].strip().strip(';').strip('"')
    except:
        pass
    return "unknown"