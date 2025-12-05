import io
import os
import os.path
import time
from operator import sub, abs
import PIL.Image
from PIL import Image, ImageChops
from configs.config import confidence, ROOT_DIR


def compare_images_simple(img1, img2, max_different_pixels=0.01, pixel_tolerance=10):
    """
    Простое сравнение изображений
    max_different_pixels: максимальная доля отличающихся пикселей (0.01 = 1%)
    pixel_tolerance: допустимая разница в значениях каналов (0-255)
    """
    if sum(abs(a-b) for a,b in zip(img1.size, img2.size)) >= 10:
        print(f'Images has different size: canvas_image-{img1.size}, expected_image-{img2.size}')
        print(f'Image size difference absolute {sum(abs(a-b) for a,b in zip(img1.size, img2.size))}')
        print(f'Image size difference {tuple(map(sub, img1.size, img2.size))}')
        return False

    # Конвертируем в RGB
    img1_rgb = img1.convert('RGB')
    img2_rgb = img2.convert('RGB')

    different_pixels = 0
    total_pixels = img1_rgb.size[0] * img1_rgb.size[1]

    for pixel1, pixel2 in zip(img1_rgb.getdata(), img2_rgb.getdata()):
        # Сравниваем каждый канал
        diff = sum(abs(c1 - c2) for c1, c2 in zip(pixel1, pixel2))
        if diff > pixel_tolerance * 3:  # 3 канала
            different_pixels += 1

    different_ratio = different_pixels / total_pixels
    result = different_ratio <= max_different_pixels
    if not result:
        return ImageChops.difference(img1_rgb, img2_rgb)
    return result


def smart_canvas_comparison(editor, expected_image_path, canvas, tolerance=confidence):
    time.sleep(0.3)
    expected_results = None
    canvas = editor.find_element(canvas)
    canvas_screenshot = canvas.screenshot_as_png
    canvas_image = Image.open(io.BytesIO(canvas_screenshot))
    if editor.cmdopt == 'make-screenshots':
        expected_image_dir_folders = expected_image_path.split('/')
        expected_image_dir_folders.pop()
        expected_dir_path = '/'.join(expected_image_dir_folders)
        if not os.path.exists(expected_dir_path):
            os.makedirs(expected_dir_path)
        canvas_image.save(expected_image_path)
        print(f'Image saved to: {expected_image_path}')
        return True
    expected_image = Image.open(expected_image_path)
    result = compare_images_simple(canvas_image, expected_image, max_different_pixels = 1 - tolerance)
    if isinstance(result, PIL.Image.Image):
        expected_image_dir_folders = expected_image_path.split('/')
        diff_image_name = expected_image_dir_folders.pop()
        report_dir_folders = []
        while True:
            report_dir_folders.append(expected_image_dir_folders.pop())
            if expected_image_dir_folders[-1] == 'resources':
                break

        report_dir_folders.reverse()
        for folder in list(report_dir_folders):
            if folder in ['expected_results_mac', 'expected_results_windows', 'expected_results_linux']:
                report_dir_folders.remove(folder)
                break

        report_dir_path = f'{ROOT_DIR}/reports/{"/".join(report_dir_folders)}'
        if not os.path.exists(report_dir_path):
            os.makedirs(report_dir_path)
        diff_image_report_dir = f'{report_dir_path}/{time.strftime("%Y-%m-%d_%H-%M-%S")}_{diff_image_name}'
        result.save(diff_image_report_dir)
        print(f'\nDifference image save to {diff_image_report_dir}')
        return False
    return result