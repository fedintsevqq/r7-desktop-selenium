import pytest
import pytest_check as check
from selenium.webdriver.common.keys import Keys
from editors.presentation_editor import PresentationEditor, ViewTabLocators
from resources.presentation import ExpectedImages
from utils import screenshot_comparsion
from configs import config


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_zoom_input(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN , 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Масштаб 80%')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element_coord(ViewTabLocators.INPUT_ZOOM_FIELD)
     .send_keys_to_element(ViewTabLocators.INPUT_ZOOM_FIELD, '80%')
     .send_keys_to_element(ViewTabLocators.INPUT_ZOOM_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_VIEW_ZOOM_INPUT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_zoom_by_dropdown_btn(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Масштаб 150%')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INPUT_ZOOM_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.ZOOM_150))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_VIEW_ZOOM_BY_DROPDOWN_BTN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_zoom_to_slide(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка масштаба по размеру слайда')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INPUT_ZOOM_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.ZOOM_150)
     .click_on_element(ViewTabLocators.ZOOM_TO_SLIDE_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_VIEW_ZOOM_TO_SLIDE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_zoom_to_width(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка масштаба по ширине')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INPUT_ZOOM_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.ZOOM_150)
     .click_on_element(ViewTabLocators.ZOOM_TO_WIDTH_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_VIEW_ZOOM_TO_WIDTH, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_change_interface_theme(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка смены темы интерфейса')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INTERFACE_THEME_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.CLASSIC_LIGHT_INTERFACE_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_CLASSIC_LIGHT_INTERFACE_THEME, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    (presentation_editor.click_on_element(ViewTabLocators.INTERFACE_THEME_DROPDOWN_BTN)
     .pause_in_test(config.general_pause)
     .click_on_element_coord(ViewTabLocators.CONTRAST_DARK_INTERFACE_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_CONTRAST_DARK_INTERFACE_THEME, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_notes(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
    .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка "Заметки"')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element_coord(ViewTabLocators.NOTES_CBX))

    elem = presentation_editor.find_element(ViewTabLocators.NOTES_CHECK)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_NOTES_OFF, presentation_editor.NOTES_CANVAS), 'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")

    presentation_editor.click_on_element_coord(ViewTabLocators.NOTES_CBX)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_NOTES_ON, presentation_editor.NOTES_CANVAS), 'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_rulers(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
    .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка "Линейки"')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element_coord(ViewTabLocators.RULERS_CBX)
    .pause_in_test())

    elem = presentation_editor.find_element(ViewTabLocators.RULERS_CHECK)

    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_RULERS_ON, presentation_editor.RULERS_CANVAS),'Скриншот не соответствует эталонному')

    (presentation_editor.click_on_element_coord(ViewTabLocators.RULERS_CBX)
     .pause_in_test())

    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_RULERS_OFF, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_guides(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element(ViewTabLocators.GUIDES_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_GUIDES_ON, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    presentation_editor.click_on_element(ViewTabLocators.GUIDES_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_GUIDES_OFF, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_guides_by_dropdown_btn(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element(ViewTabLocators.GUIDES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.SHOW_GUIDES_LINK)
     .click_on_element(ViewTabLocators.GUIDES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.SHOW_VERTICAL_GUIDES_LINK)
     .click_on_element(ViewTabLocators.GUIDES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.SHOW_HORIZONTAL_GUIDES_LINK)
     .click_on_element(ViewTabLocators.GUIDES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.SHOW_SMART_GUIDES_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_GUIDES_ON_BY_DROPDOWN_BTN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    (presentation_editor.click_on_element(ViewTabLocators.GUIDES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.DELETE_GUIDES_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_GUIDES_OFF, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_grid_lines_by_dropdown_btn(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.SHOW_GRID_LINES)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.BIND_GRID_LINES)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.GRID_LINES_1_PER_8)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.GRID_LINES_1_PER_5))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHOW_GRID_LINES_BY_DROPDOWN_BTN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    presentation_editor.click_on_element(ViewTabLocators.GRID_LINES_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHOW_GRID_LINES_OFF, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_grid_lines(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.BIND_GRID_LINES)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.GRID_LINES_1_PER_8)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.GRID_LINES_1_PER_5)
     .click_on_element(ViewTabLocators.GRID_LINES_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHOW_GRID_LINES_ON, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    presentation_editor.click_on_element(ViewTabLocators.GRID_LINES_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHOW_GRID_LINES_OFF, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_user_grid_lines(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
     .click_on_element(ViewTabLocators.GRID_LINES_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.USER_GRID_LINES)
     .click_on_element_coord(ViewTabLocators.GRID_SPACING_COMBO_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.GRID_LINES_1_PER_8_LINK)
     .click_on_element_coord(ViewTabLocators.GRID_SPACING_COMBO_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.USER_GRID_LINES_LINK)
     .click_on_element_coord(ViewTabLocators.USER_GRID_LINES_SPINNER_DOWN, 3)
     .click_on_element_coord(ViewTabLocators.USER_GRID_LINES_SPINNER_UP, 10)
     .click_on_element(ViewTabLocators.WINDOW_GRID_SETTINGS_OK_BTN)
     .click_on_element(ViewTabLocators.GRID_LINES_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHOW_GRID_LINES_ON, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    presentation_editor.click_on_element(ViewTabLocators.GRID_LINES_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHOW_GRID_LINES_OFF, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_toolbar(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
    .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка "Всегда показывать панель инструментов"')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element_coord(ViewTabLocators.TOOLBAR_CBX))

    elem = presentation_editor.find_element(ViewTabLocators.TOOLBAR_CHECK)
    section = presentation_editor.find_element(ViewTabLocators.TOOLBAR_SECTION)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_TOOLBAR_OFF, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_true(len(section.text) == 0, "Меню toolbar не скрылось")

    presentation_editor.click_on_element_coord(ViewTabLocators.TOOLBAR_CBX)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_TOOLBAR_ON, presentation_editor.TOOLBAR), 'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(len(section.text) > 0, "Меню toolbar не появилось")


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_statusbar(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
    .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка "Строка состояния"')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element_coord(ViewTabLocators.STATUSBAR_CBX))

    elem = presentation_editor.find_element(ViewTabLocators.STATUSBAR_CHECK)
    button = presentation_editor.find_element(ViewTabLocators.STATUSBAR_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_STATUSBAR_OFF, presentation_editor.FULL_WINDOW), 'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected() is False, "Чекбокс должен быть выключен")
    check.is_false(button.is_displayed(), 'Меню statusbar не скрылось')

    presentation_editor.click_on_element_coord(ViewTabLocators.STATUSBAR_CBX)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_STATUSBAR_ON, presentation_editor.STATUSBAR), 'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected() is True, "Чекбокс должен быть включен")
    check.is_true(button.is_displayed(), 'Меню statusbar не появилось')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_left_panel(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
    .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка кнопки "Левая панель"')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element_coord(ViewTabLocators.LEFT_MENU_CBX))

    elem = presentation_editor.find_element(ViewTabLocators.LEFT_MENU_CHECK)
    button = presentation_editor.find_element(ViewTabLocators.LEFT_MENU_FIELD_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_LEFT_PANEL_OFF, presentation_editor.FULL_WINDOW), 'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_false(button.is_displayed(), 'Меню left panel не скрылось')

    (presentation_editor.click_on_element_coord(ViewTabLocators.LEFT_MENU_CBX)
     .click_on_element_coord(ViewTabLocators.LEFT_MENU_FIELD_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_LEFT_PANEL_ON_LEFT_CANVAS, presentation_editor.LEFT_CANVAS), 'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(button.is_displayed(), 'Меню left panel не появилось')


@pytest.mark.presentation
@pytest.mark.view_tab
def test_presentation_right_panel(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.VIEW_TAB)
    .click_on_element_coord_with_offset(ViewTabLocators.GRID_LINES_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка кнопки "Правая панель"')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element_coord(ViewTabLocators.RIGHT_MENU_CBX))

    elem = presentation_editor.find_element(ViewTabLocators.RIGHT_MENU_CHECK)
    button = presentation_editor.find_element(ViewTabLocators.RIGHT_MENU_PARAMS_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_RIGHT_PANEL_OFF, presentation_editor.FULL_WINDOW), 'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_false(button.is_displayed(), 'Меню right panel не скрылось')

    presentation_editor.click_on_element_coord(ViewTabLocators.RIGHT_MENU_CBX)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_RIGHT_PANEL_ON, presentation_editor.RIGHT_MENU), 'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(button.is_displayed(), 'Меню right panel не появилось')
