import pytest
from selenium.webdriver import Keys
from editors.base_editor import Editor
from editors.spreadsheet_editor import LayoutTabLocators, CommonLocators, TopMenu, InsertTabLocators
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages
import pytest_check as check


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_change_page_margins(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_MARGINS_BTN)
        .click_on_element(LayoutTabLocators.PAGE_MARGINS_DROPDOWN_NARROW)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка изменения полей страницы' + Keys.ENTER, 8)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_PAGE_MARGINS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_change_page_orient(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_ORIENT_BTN)
        .click_on_element(LayoutTabLocators.PAGE_ORIENT_DROPDOWN_LANDSCAPE)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка изменения ориентации страницы' + Keys.ENTER, 8)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_PAGE_ORIENT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_change_page_size(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_SIZE_BTN)
        .click_on_element(LayoutTabLocators.PAGE_SIZE_DROPDOWN_A5)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка изменения размера страницы' + Keys.ENTER, 8)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_PAGE_SIZE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_set_print_area(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка задания области печати' + Keys.ENTER, 8)
        .send_hotkey(Keys.CONTROL, Keys.HOME)
        .hold_key_down_and_press_key_count_times(Keys.SHIFT, Keys.ARROW_DOWN, 3)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_AREA_BTN)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_AREA_DROPDOWN_SET_PRINT_AREA)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SET_PRINT_AREA, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_remove_print_area(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка удаления области печати' + Keys.ENTER, 8)
        .send_hotkey(Keys.CONTROL, Keys.HOME)
        .hold_key_down_and_press_key_count_times(Keys.SHIFT, Keys.ARROW_DOWN, 3)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_AREA_BTN)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_AREA_DROPDOWN_SET_PRINT_AREA)
        .click_on_element(TopMenu.PRINT)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_AREA_BTN)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_AREA_DROPDOWN_REMOVE_PRINT_AREA)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_REMOVE_PRINT_AREA, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_insert_page_breaks(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.LAYOUT_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка вставки разрыва' + Keys.ENTER, 4)
        .click_on_element(LayoutTabLocators.PAGE_BREAKS_BTN)
        .click_on_element(LayoutTabLocators.PAGE_BREAKS_DROPDOWN_INSERT_BREAK)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка вставки разрыва' + Keys.ENTER, 4)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_PAGE_BREAKS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_remove_page_breaks(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.LAYOUT_TAB)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка удаления разрыва' + Keys.ENTER, 4)
        .click_on_element(LayoutTabLocators.PAGE_BREAKS_BTN)
        .click_on_element(LayoutTabLocators.PAGE_BREAKS_DROPDOWN_INSERT_BREAK)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка удаления разрыва' + Keys.ENTER, 4)
        .click_on_element(LayoutTabLocators.PAGE_BREAKS_BTN)
        .click_on_element(LayoutTabLocators.PAGE_BREAKS_DROPDOWN_REMOVE_ALL_BREAKS)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_REMOVE_PAGE_BREAKS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_insert_headers_footers_layout_tab(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.LAYOUT_HF_BTN)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_HEADER_PRESET_BTN)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_HEADER_PRESET_DROPDOWN_PAGE_1_OF)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_HEADER_INSERT_BTN)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_HEADER_INSERT_DROPDOWN_LIST_NAME)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_FOOTER_PRESET_BTN)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_FOOTER_PRESET_DROPDOWN_PAGE_1_OF)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_FOOTER_INSERT_BTN)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_FOOTER_INSERT_DROPDOWN_LIST_NAME)
        .click_on_element(InsertTabLocators.INSERT_HF_MODAL_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка вставки колонтитулов' + Keys.ENTER, 8)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_HEADERS_FOOTERS_LAYOUT_TAB, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_change_page_scale(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка изменения масштаба страницы' + Keys.ENTER, 8)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_SCALE_BTN)
        .click_on_element(LayoutTabLocators.PAGE_SCALE_DROPDOWN_CUSTOM_UP_BTN, 8)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_PAGE_SCALE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
# TODO: после реализации импорта данных из файла - переделать на больший объем данных в таблице
def test_print_table_titles(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Заголовок' + Keys.TAB, 8)
        .send_hotkey(Keys.CONTROL, Keys.HOME)
        .press_key(Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка печати заголовков')
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_TITLES_BTN)
        .send_keys_to_element(LayoutTabLocators.PAGE_PRINT_MODAL_TOP_RANGE_INPUT, '$1:$1' + Keys.ENTER)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_PRINT_TABLE_TITLES, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_print_gridlines(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка печати сетки таблицы' + Keys.ENTER, 8)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_GRID_LINES_CHK)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_PRINT_GRIDLINES, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_print_headings(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка печати заголовков' + Keys.ENTER, 8)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.PAGE_PRINT_HEADINGS_CHK)
        .click_on_element(TopMenu.PRINT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_PRINT_HEADINGS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_move_shape_forward(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 250, 250, 100, 100)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 200, 200, 100, 100)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_BTN)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_RED_FILL_COLOR)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.MOVE_IMG_FWD_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_MOVE_SHAPE_FORWARD, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_move_shape_backward(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 250, 250, 100, 100)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 200, 200, 100, 100)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_BTN)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_RED_FILL_COLOR)
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.MOVE_IMG_BWD_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_MOVE_SHAPE_BACKWARD, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_align_shapes(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 250, 250, 100, 100)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 150, 150, 100, 100)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_BTN)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_RED_FILL_COLOR)
        .send_hotkey(Keys.CONTROL, 'ф')
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.ALIGN_IMG_BTN)
        .click_on_element(LayoutTabLocators.ALIGN_IMG_DROPDOWN_ALIGN_CENTER)
        .click_on_element(LayoutTabLocators.ALIGN_IMG_BTN)
        .click_on_element(LayoutTabLocators.ALIGN_IMG_DROPDOWN_ALIGN_MIDDLE)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_SHAPES, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_group_shapes(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 250, 250, 100, 100)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 150, 150, 100, 100)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_BTN)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_RED_FILL_COLOR)
        .send_hotkey(Keys.CONTROL, 'ф')
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.GROUP_IMG_BTN)
        .click_on_element(LayoutTabLocators.GROUP_IMG_DROPDOWN_GROUP)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_GROUP_SHAPES, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_ungroup_shapes(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 250, 250, 100, 100)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 150, 150, 100, 100)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_BTN)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_RED_FILL_COLOR)
        .send_hotkey(Keys.CONTROL, 'ф')
        .click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.GROUP_IMG_BTN)
        .click_on_element(LayoutTabLocators.GROUP_IMG_DROPDOWN_GROUP)
        .click_on_element(LayoutTabLocators.GROUP_IMG_BTN)
        .click_on_element(LayoutTabLocators.GROUP_IMG_DROPDOWN_UNGROUP)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_UNGROUP_SHAPES, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.layout_tab
def test_change_color_schema(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.LAYOUT_TAB)
        .click_on_element(LayoutTabLocators.COLOR_SCHEMAS_BTN)
        .click_on_element(LayoutTabLocators.COLOR_SCHEMAS_DROPDOWN_TORRENT)
        .click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 250, 250, 100, 100)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_BTN)
        .click_on_element(LayoutTabLocators.SHAPE_PANEL_COLOR_FILL_DROPDOWN_BLUE_GREEN_ACCENT_3_FILL_COLOR)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_COLOR_SCHEMA, spreadsheet_editor.SP_CANVAS))
