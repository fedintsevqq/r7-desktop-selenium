import pytest
from editors.base_editor import Editor
from editors.spreadsheet_editor import Samples, CommonLocators, InsertTabLocators, TopMenu
from selenium.webdriver.common.keys import Keys
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages
import pytest_check as check


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_pivot_table(spreadsheet_editor):
    for row in Samples.PIVOT_DATA_SET_RAW.split('.'):
        for col in row.split(','):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col + Keys.TAB)
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.ENTER + Keys.ARROW_LEFT)
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.PIVOT_TABLE_BTN)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_SOURCE_RANGE_INPUT, Keys.BACKSPACE, 12)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_SOURCE_RANGE_INPUT, 'Лист1!$A$1:$H$20')
        .click_on_element(InsertTabLocators.PIVOT_TABLE_MODAL_EXIST_SHEET_RADIO_SPAN)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_EXIST_SHEET_DEST_RANGE_INPUT, Keys.BACKSPACE, 12)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_EXIST_SHEET_DEST_RANGE_INPUT, 'Лист1!$J$1')
        .click_on_element(InsertTabLocators.PIVOT_TABLE_MODAL_OK_BTN)
    )
    pivot_table_right_menu_btn = spreadsheet_editor.find_element(InsertTabLocators.PIVOT_TABLE_RIGHT_MENU_BTN)
    if 'active' not in pivot_table_right_menu_btn.get_attribute('class'):
        pivot_table_right_menu_btn.click()
    pt_fields = spreadsheet_editor.driver.find_elements(*InsertTabLocators.PIVOT_TABLE_LIST_FIELDS_CHK_LABEL)
    if pt_fields:
        for field in pt_fields:
            field.click()
    else:
        print('No pt_fields:' + pt_fields)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_PIVOT_TABLE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_table(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_TABLE_BTN)
        .send_keys_to_element(InsertTabLocators.INSERT_TABLE_MODAL_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(InsertTabLocators.INSERT_TABLE_MODAL_INPUT, '$A$1:$H$8')
        .click_on_element_with_offset_from_top_left(InsertTabLocators.INSERT_TABLE_MODAL_TITLE_LABEL, 2, 2)
        .click_on_element(InsertTabLocators.INSERT_TABLE_MODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_TABLE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_image(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_IMAGE_BTN)
        .click_on_element(InsertTabLocators.INSERT_IMAGE_DROPDOWN_IMAGE_URL)
        .send_keys_to_element(InsertTabLocators.INSERT_IMAGE_MODAL_INPUT_URL, Samples.CAPYBARA_IMG_URL)
        .press_key(Keys.ENTER)
        .pause_in_test()
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_IMAGE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_shape(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SHAPE_DROPDOWN_ARROW_RIGHT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 150, 150, 60, 60)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_SHAPE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_text(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_HORIZONTAL_TEXT_BTN)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 150, 80, 60, 60)
        .action.send_keys('Проверка вставки горизонтального текста')
    )
    spreadsheet_editor.pause_in_test()
    (
        spreadsheet_editor.click_on_element(InsertTabLocators.INSERT_TEXT_DROPDOWN_BTN)
        .click_on_element(InsertTabLocators.INSERT_TEXT_DROPDOWN_VERTICAL_TEXT)
        .drag_n_drop(CommonLocators.WORKSHEET_TEXT_AREA, 80, 150, 120, -80)
        .action.send_keys('Проверка вставки вертикального текста')
    )
    spreadsheet_editor.pause_in_test()
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_text_art(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_TEXT_ART_BTN)
        .click_on_element(InsertTabLocators.INSERT_TEXT_ART_DROPDOWN_FIRST_TEXT_ART)
        .action.send_keys('Проверка вставки Text Art')
    )
    spreadsheet_editor.pause_in_test()
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_TEXT_ART, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_chart(spreadsheet_editor):
    for raw in Samples.CHART_DATA_METAL.split('.'):
        for col in raw.split(','):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col + Keys.TAB)
        (spreadsheet_editor.press_key(Keys.ENTER).press_key(Keys.HOME))
    (spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME).send_hotkey(Keys.CONTROL, Keys.SHIFT, Keys.END))
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_CHART_BTN)
        .click_on_element(InsertTabLocators.INSERT_CHART_DROPDOWN_CHART_COLUMN_NORMAL)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_CHART, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_sparkline(spreadsheet_editor):
    for i, row in enumerate(Samples.CHART_DATA_METAL.split('.')):
        for col in row.split(','):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col + Keys.TAB)
        (spreadsheet_editor.press_key(Keys.ENTER).press_key(Keys.HOME))
        if i == 3:
            break
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_DROPDOWN_CHART_SPARK_COLUMN)
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_RANGE_INPUT, '$B$2:$D$2')
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_DEST_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_DEST_INPUT, '$E$2')
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_OK_BTN)
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_DROPDOWN_CHART_SPARK_LINE)
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_RANGE_INPUT, '$B$3:$D$3')
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_DEST_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_DEST_INPUT, '$E$3')
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_OK_BTN)
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_BTN)
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_DROPDOWN_CHART_SPARK_WIN)
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_RANGE_INPUT, '$B$4:$D$4')
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_DEST_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_DEST_INPUT, '$E$4')
        .click_on_element(InsertTabLocators.INSERT_SPARKLINE_MODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_SPARKLINE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_smart_art(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SMART_ART_BTN)
        .click_on_element(InsertTabLocators.INSERT_SMART_ART_DROPDOWN_LIST_SUBMENU_BTN)
        .click_on_element(InsertTabLocators.INSERT_SMART_ART_DROPDOWN_LIST_SUBMENU_ARC_MODEL)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_SMART_ART, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_add_comment(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(InsertTabLocators.ADD_COMMENT_POPOVER_TEXTAREA, 'Проверка добавления комментария')
        .click_on_element(InsertTabLocators.ADD_COMMENT_POPOVER_ADD_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ADD_COMMENT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_hyperlink(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_HYPERLINK_BTN)
        .send_keys_to_element(InsertTabLocators.INSERT_HYPERLINK_MODAL_URL_INPUT, Samples.CAPYBARA_IMG_URL)
        .send_keys_to_element(InsertTabLocators.INSERT_HYPERLINK_MODAL_DISPLAY_INPUT, 'Capybara Hyperlink')
        .send_keys_to_element(InsertTabLocators.INSERT_HYPERLINK_MODAL_TIP_INPUT, 'Capybara Hyperlink Tip')
        .click_on_element(InsertTabLocators.INSERT_HYPERLINK_MODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_HYPERLINK, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_headers_footers(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_HF_BTN)
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
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_HEADERS_FOOTERS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_equation(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_EQUATION_BTN)
        .click_on_element(InsertTabLocators.INSERT_EQUATION_CONTAINER_EQUATION_6)
        .click_on_element(InsertTabLocators.INSERT_EQUATION_CONTAINER_EQUATION_6_DROPDOWN_ROUND_BRACKETS)
        .press_key(Keys.ESCAPE, 2)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_EQUATION, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_symbol(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_SYMBOL_BTN)
        .click_on_element(InsertTabLocators.INSERT_SYMBOL_MODAL_EXCL_MARK)
        .click_on_element(InsertTabLocators.INSERT_SYMBOL_MODAL_OK_BTN)
        .click_on_element(InsertTabLocators.INSERT_SYMBOL_MODAL_CLOSE_BTN)
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_SYMBOL, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.insert_tab
def test_insert_slicers(spreadsheet_editor):
    for row in Samples.CHART_DATA_METAL.split('.'):
        for col in row.split(','):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col + Keys.TAB)
        spreadsheet_editor.press_key(Keys.ENTER).press_key(Keys.HOME)
    (spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME).send_hotkey(Keys.CONTROL, Keys.SHIFT, Keys.END))
    (
        spreadsheet_editor.click_on_element(Editor.INSERT_TAB)
        .click_on_element(InsertTabLocators.INSERT_TABLE_BTN)
        .click_on_element_with_offset_from_top_left(InsertTabLocators.INSERT_TABLE_MODAL_TITLE_LABEL, 2, 2)
        .click_on_element(InsertTabLocators.INSERT_TABLE_MODAL_OK_BTN)
        .click_on_element(InsertTabLocators.INSERT_SLICERS_BTN)
    )
    slicer_fields = spreadsheet_editor.driver.find_elements(*InsertTabLocators.INSERT_SLICERS_MODAL_CHKBX_LABEL)
    if slicer_fields:
        for field in slicer_fields:
            field.click()
    spreadsheet_editor.click_on_element(InsertTabLocators.INSERT_SLICERS_MODAL_OK_BTN)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_SLICERS, spreadsheet_editor.SP_CANVAS))


# TODO: сделать вставку Объекта
