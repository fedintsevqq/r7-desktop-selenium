import pytest
import pytest_check as check

from selenium.webdriver.common.keys import Keys
from configs import config
from editors.document_editor import DocumentEditor, ViewTabLocators, MainTabLocators
from utils import screenshot_comparsion
from resources.document import ExpectedImages

from utils.screenshot_comparsion import smart_canvas_comparison


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_view_navigator(document_editor):
    test_text = 'Это заголовок'
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, test_text)
     .click_on_element(MainTabLocators.TEXT_STYLE)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(DocumentEditor.VIEW_TAB)
     .click_on_element(ViewTabLocators.VIEW_NAVIGATION_BTN))

    elem = document_editor.find_element(ViewTabLocators.NAVIGATION_TEXT)
    check.is_true(elem.text.rstrip() == test_text)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_VIEW_NAVIGATOR, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_zoom_input(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Масштаб 80%')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INPUT_ZOOM_FIELD)
     .send_keys_to_element(ViewTabLocators.INPUT_ZOOM_FIELD, '80%')
     .send_keys_to_element(ViewTabLocators.INPUT_ZOOM_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ZOOM_INPUT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_zoom_from_dropdown_menu(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Масштаб 150%')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INPUT_ZOOM_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.ZOOM_150))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ZOOM_FROM_DROPDOWN_MENU, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_zoom_to_page(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка масштаба по размеру страницы')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INPUT_ZOOM_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.ZOOM_150)
     .click_on_element(ViewTabLocators.ZOOM_TO_PAGE_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ZOOM_TO_PAGE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_zoom_to_width(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка масштаба по размеру страницы')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INPUT_ZOOM_DROPDOWN_BTN)
     .click_on_element_coord(ViewTabLocators.ZOOM_150)
     .click_on_element(ViewTabLocators.ZOOM_TO_WIDTH_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ZOOM_TO_WIDTH, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_change_interface_theme(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка смены темы интерфейса')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INTERFACE_THEME_DROPDOWN_MENU)
     .click_on_element_coord(ViewTabLocators.CONTRAST_DARK_INTERFACE_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CONTRAST_DARK_INTERFACE_THEME, document_editor.CANVAS),'Скриншот не соответствует эталонному')

    (document_editor.click_on_element(ViewTabLocators.INTERFACE_THEME_DROPDOWN_MENU)
     .click_on_element_coord(ViewTabLocators.SYSTEM_INTERFACE_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_SYSTEM_INTERFACE_THEME, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_dark_document(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка режима черный документ')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ViewTabLocators.INTERFACE_THEME_DROPDOWN_MENU)
     .click_on_element_coord(ViewTabLocators.CONTRAST_DARK_INTERFACE_LINK)
     .click_on_element(ViewTabLocators.DARK_DOCUMENT_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_DARK_DOCUMENT, document_editor.CANVAS),'Скриншот не соответствует эталонному')

    (document_editor.click_on_element(ViewTabLocators.INTERFACE_THEME_DROPDOWN_MENU)
     .click_on_element_coord(ViewTabLocators.SYSTEM_INTERFACE_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_DARK_DOCUMENT_SYSTEM_INTERFACE_THEME, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_toolbar(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
    .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка кнопки "Всегда показывать панель инструментов"')
    .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))
    elem = document_editor.find_element(ViewTabLocators.TOOLBAR_CHECK)
    section = document_editor.find_element(ViewTabLocators.TOOLBAR_SECTION)

    document_editor.click_on_element_coord(ViewTabLocators.TOOLBAR_CBX)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_TOOLBAR_OFF, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_true(len(section.text) == 0, "Меню toolbar не скрылось")

    document_editor.click_on_element_coord(ViewTabLocators.TOOLBAR_CBX)
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_TOOLBAR_ON, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(len(section.text) > 0, "Меню toolbar не появилось")


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_statusbar(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка кнопки "Строка состояния"')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))
    elem = document_editor.find_element(ViewTabLocators.STATUSBAR_CHECK)
    button = document_editor.find_element(ViewTabLocators.STATUSBAR_BUTTON)

    document_editor.click_on_element_coord(ViewTabLocators.STATUSBAR_CBX)
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_STATUSBAR_OFF, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_false(button.is_displayed(), "Меню statusbar не скрылось")

    document_editor.click_on_element_coord(ViewTabLocators.STATUSBAR_CBX)
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_STATUSBAR_ON, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(button.is_displayed(), "Меню statusbar не появилось")


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_right_panel(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка кнопки "Правая панель"')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))
    elem = document_editor.find_element(ViewTabLocators.RIGHT_MENU_CHECK)
    button = document_editor.find_element(ViewTabLocators.RIGHT_MENU_TEXT_BUTTON)

    document_editor.click_on_element_coord(ViewTabLocators.RIGHT_MENU_CBX)
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RIGHT_PANEL_OFF, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_false(button.is_displayed(), "Меню right panel не скрылось")

    document_editor.click_on_element_coord(ViewTabLocators.RIGHT_MENU_CBX)
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RIGHT_PANEL_ON, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(button.is_displayed(), "Меню right panel не появилось")


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_left_panel(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка кнопки "Левая панель"')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))
    elem = document_editor.find_element(ViewTabLocators.LEFT_MENU_CHECK)
    button = document_editor.find_element(ViewTabLocators.LEFT_MENU_COMMENT_BUTTON)

    document_editor.click_on_element_coord(ViewTabLocators.LEFT_MENU_CBX)
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_LEFT_PANEL_OFF, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_false(button.is_displayed(), "Меню left panel не скрылось")

    (document_editor.click_on_element_coord(ViewTabLocators.LEFT_MENU_CBX)
     .click_on_element_coord(ViewTabLocators.LEFT_MENU_COMMENT_BUTTON))
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_LEFT_PANEL_ON, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
    check.is_true(button.is_displayed(), "Меню left panel не появилось")


@pytest.mark.document
@pytest.mark.view_tab
def test_doc_rulers(document_editor):
    (document_editor.click_on_element(DocumentEditor.VIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка кнопки "Линейки"')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))
    elem = document_editor.find_element(ViewTabLocators.RULERS_CHECK)
    (document_editor.click_on_element_coord(ViewTabLocators.RULERS_CBX)
     .pause_in_test())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RULERS_OFF, document_editor.CANVAS),'Скриншот не соответствует эталонному')
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")

    (document_editor.pause_in_test().click_on_element_coord(ViewTabLocators.RULERS_CBX)
     .pause_in_test())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RULERS_ON, document_editor.RULERS_CANVAS),'Скриншот не соответствует эталонному')
    check.is_true(elem.is_selected(), "Чекбокс должен быть включен")
