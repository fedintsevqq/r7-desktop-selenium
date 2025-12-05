import pytest_check as check
import pytest
from selenium.webdriver.common.keys import Keys
from editors.spreadsheet_editor import SpreadsheetEditor, ViewTabLocators, CommonLocators
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_zoom_input(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(ViewTabLocators.INPUT_ZOOM_FIELD, '80%')
        .send_keys_to_element(ViewTabLocators.INPUT_ZOOM_FIELD, Keys.ENTER)
        .send_keys_to_element(CommonLocators.CELL_FORMULA_BAR_TEXTAREA, 'Проверка масштаба 80%')
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_ZOOM_INPUT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_zoom_from_dropdown_menu(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .click_on_element(ViewTabLocators.INPUT_ZOOM_DROPDOWN_BTN)
        .click_on_element_coord(ViewTabLocators.ZOOM_150_LINK)
        .send_keys_to_element(CommonLocators.CELL_FORMULA_BAR_TEXTAREA, 'Проверка масштаба 150% из выпадающего меню')
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_ZOOM_FROM_DROPDOWN_MENU, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_change_interface_theme(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.CELL_FORMULA_BAR_TEXTAREA, 'Проверка смены интерфейса')
        .click_on_element(ViewTabLocators.INTERFACE_THEME_DROPDOWN_MENU)
        .click_on_element_coord(ViewTabLocators.CONTRAST_DARK_INTERFACE_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_CHANGE_INTERFACE_THEME, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_view(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .click_on_element(ViewTabLocators.NEW_VIEW_BTN)
        .send_keys_to_element(CommonLocators.CELL_FORMULA_BAR_TEXTAREA, 'Проверка создания представления листа с помощью кнопки Новое')
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_VIEW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_close_view(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка закрытия представления листа с помощью кнопки Закрыть')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        .click_on_element(ViewTabLocators.NEW_VIEW_BTN)
        .click_on_element(ViewTabLocators.CLOSE_VIEW_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_CLOSE_VIEW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_view_by_manager(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .click_on_element(ViewTabLocators.SHEET_VIEW_BTN)
        .click_on_element_coord(ViewTabLocators.VIEW_MANAGER_LINK)
        .click_on_element(ViewTabLocators.NEW_VIEW_MANAGER_BTN)
        .click_on_element(ViewTabLocators.GO_TO_VIEW_MANAGER_BTN)
        .send_keys_to_element(CommonLocators.CELL_FORMULA_BAR_TEXTAREA, 'Проверка создания представления листа из диспетчера представлений')
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_VIEW_BY_MANAGER, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_view_page_brake(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Страничный режим')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )
    spreadsheet_editor.click_on_element(ViewTabLocators.VIEW_PAGE_BRAKE_BTN)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_VIEW_PAGE_BRAKE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_view_page_layout(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Разметка страницы')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )
    spreadsheet_editor.click_on_element(ViewTabLocators.VIEW_PAGE_LAYOUT_BTN)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_VIEW_PAGE_LAYOUT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_view_page_normal(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Обычный режим')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.VIEW_PAGE_LAYOUT_BTN)
        .click_on_element(ViewTabLocators.VIEW_PAGE_NORMAL_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_VIEW_PAGE_NORMAL, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_freeze_area(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Закрепить области')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.FREEZE_AREA_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_FREEZE_AREA, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_remove_freeze_area(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Снять закрепление области')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.FREEZE_AREA_LINK)
        .click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.REMOVE_FREEZE_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REMOVE_FREEZE_AREA, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_freeze_row(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Закрепить верхнюю строку')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.FREEZE_ROW_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_FREEZE_ROW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_freeze_column(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Закрепить первый столбец')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.FREEZE_COLUMN_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_FREEZE_COLUMN, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_freeze_area_shadow(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Показывать тень для закрепленных областей')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.FREEZE_AREA_LINK)
        .click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.SHOW_SHADOW_LINK)
        .click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.SHOW_SHADOW_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_FREEZE_AREA_SHADOW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_freeze_row_shadow(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Показывать тень для закрепленных строк')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
            )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.FREEZE_ROW_LINK)
        .click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.SHOW_SHADOW_LINK)
        .click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.SHOW_SHADOW_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_FREEZE_ROW_SHADOW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_freeze_column_shadow(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Показывать тень для закрепленных столбцов')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, f'{i}')
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.FREEZE_COLUMN_LINK)
        .click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.SHOW_SHADOW_LINK)
        .click_on_element(ViewTabLocators.FREEZE_FIELD_BTN)
        .click_on_element_coord(ViewTabLocators.SHOW_SHADOW_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_FREEZE_COLUMN_SHADOW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_formula_field(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Строка формул')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.FORMULA_FIELD_CHECK)
    button = spreadsheet_editor.find_element(ViewTabLocators.FORMULA_FIELD_BTN)

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.FORMULA_FIELD_CBX)
    check.is_false(elem.is_selected(), "Чекбокс должен быть выключен")
    check.is_false(button.is_displayed(), 'Меню formula field не скрылось')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.FORMULA_FIELD_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_true(button.is_displayed(), 'Меню formula field не появилось')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_FORMULA_FIELD, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_heading(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Заголовки')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.HEADING_CHECK)

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.HEADING_CBX)
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.HEADING_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_HEADING, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_grid_lines(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Линии сетки')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.GRID_LINES_CHECK)

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.GRID_LINES_CBX)
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.GRID_LINES_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_GRID_LINES, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_zeros(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Отображать нули')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.ZEROS_CHECK)

    for i in range(5):
        (
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 0)
            .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
        )

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.ZEROS_CBX)
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.ZEROS_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_ZEROS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_rulers(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Линейки')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.RULERS_CHECK)

    (
        spreadsheet_editor.click_on_element(ViewTabLocators.VIEW_PAGE_LAYOUT_BTN)
        .click_on_element_coord(ViewTabLocators.RULERS_CBX)
    )
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.RULERS_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_RULERS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_toolbar(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки всегда показывать панель инструментов')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.TOOLBAR_CHECK)
    section = spreadsheet_editor.find_element(ViewTabLocators.TOOLBAR_SECTION)

    (
        spreadsheet_editor.click_on_element_coord(ViewTabLocators.TOOLBAR_CBX)
        .pause_in_test()
    )
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')
    check.is_true(len(section.text) == 0, 'Меню toolbar не скрылось')

    (
        spreadsheet_editor.click_on_element_coord(ViewTabLocators.TOOLBAR_CBX)
        .pause_in_test()
    )
    check.is_true(elem.is_selected(),'Чекбокс должен быть включен')
    check.is_true(len(section.text) > 0, 'Меню toolbar не появилось')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_TOOLBAR, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_statusbar(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки объединить строки листов и состояния')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.STATUSBAR_CHECK)
    label = spreadsheet_editor.find_element(ViewTabLocators.STATUSBAR_LABEL)

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.STATUSBAR_CBX)
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')
    check.is_true(label.is_displayed(),'Меню statusbar не скрылось')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.STATUSBAR_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_false(label.is_displayed(), 'Меню statusbar не появилось')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_STATUSBAR, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_left_panel(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Левая панель')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.LEFT_MENU_CHECK)
    button = spreadsheet_editor.find_element(ViewTabLocators.LEFT_MENU_COMMENT_BUTTON)

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.LEFT_MENU_CBX)
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')
    check.is_false(button.is_displayed(), 'Меню left panel не скрылось')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.LEFT_MENU_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_true(button.is_displayed(), 'Меню left panel не появилось')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_LEFT_PANEL, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.view_tab
def test_spreadsheet_right_panel(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.VIEW_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка кнопки Правая панель')
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.DOWN)
    )

    elem = spreadsheet_editor.find_element(ViewTabLocators.RIGHT_MENU_CHECK)
    button = spreadsheet_editor.find_element(ViewTabLocators.RIGHT_MENU_BUTTON)

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.RIGHT_MENU_CBX)
    check.is_false(elem.is_selected(), 'Чекбокс должен быть выключен')
    check.is_false(button.is_displayed(), 'Меню right panel не скрылось')

    spreadsheet_editor.click_on_element_coord(ViewTabLocators.RIGHT_MENU_CBX)
    check.is_true(elem.is_selected(), 'Чекбокс должен быть включен')
    check.is_true(button.is_displayed(), 'Меню right panel не появилось')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_RIGHT_PANEL, spreadsheet_editor.SP_CANVAS))
