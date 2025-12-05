import pytest
from selenium.webdriver import Keys
from editors.spreadsheet_editor import CommonLocators, Samples, DataTabLocators, MainTabLocators
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages
import pytest_check as check


# TODO: после реализации открытия - реализовать тесты получения данных из текстового файла и показ внешних ссылок и таблицы данных
@pytest.mark.skip(reason="отсутствует работа с системными окнами")
@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_receive_data_from_text_files(spreadsheet_editor):
    pass


@pytest.mark.skip(reason="отсутствует работа с системными окнами")
@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_show_external_links(spreadsheet_editor):
    pass


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_goal_seek(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка Поиск цели' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '2' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '4' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '=A2*A3' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.GOAL_SEEK_BTN)
        .send_keys_to_element(DataTabLocators.GOAL_SEEK_MODAL_DEFINE_CELL_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(DataTabLocators.GOAL_SEEK_MODAL_DEFINE_CELL_INPUT, 'A4')
        .send_keys_to_element(DataTabLocators.GOAL_SEEK_MODAL_VARIABLE_CELL_INPUT, 'A3')
        .send_keys_to_element(DataTabLocators.GOAL_SEEK_MODAL_EXPECTED_RESULT_INPUT, '32' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_GOAL_SEEK, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_insert_data_table_with_column_variable(spreadsheet_editor):
    for row in Samples.DATA_TABLE_COLUMN_VARIABLE.split('.'):
        for col in row.split(';'):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col + Keys.TAB)
        (spreadsheet_editor.press_key(Keys.ENTER).press_key(Keys.HOME))
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, 'C6' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '=C4/(C2*C3)' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, 'E13' + Keys.ENTER)
        .hold_key_down_and_press_key_count_times(Keys.SHIFT, Keys.UP, 11)
        .send_hotkey(Keys.SHIFT, Keys.RIGHT)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.DATA_TABLE_BTN)
        .send_keys_to_element(DataTabLocators.DATA_TABLE_MODAL_VAR_COL_INPUT, 'C3' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_DATA_TABLE_WITH_COLUMN_VARIABLE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_insert_auto_filter_in_data_tab(spreadsheet_editor):
    for char in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, char + Keys.ENTER)
    (
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.ADD_AUTO_FILTER_BTN)
        .click_on_element_with_offset_from_top_left(CommonLocators.WORKSHEET_EDITOR_SDK, 80, 25)
        .send_keys_to_element(MainTabLocators.FILTER_MODAL_SEARCH_INPUT, 'Й')
        .click_on_element(MainTabLocators.FILTER_MODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_AUTO_FILTER_IN_DATA_TAB, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_clear_filter_in_data_tab(spreadsheet_editor):
    for char in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, char + Keys.ENTER)
    (
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.ADD_AUTO_FILTER_BTN)
        .click_on_element_with_offset_from_top_left(CommonLocators.WORKSHEET_EDITOR_SDK, 80, 25)
        .send_keys_to_element(MainTabLocators.FILTER_MODAL_SEARCH_INPUT, 'Й')
        .click_on_element(MainTabLocators.FILTER_MODAL_OK_BTN)
        .click_on_element(DataTabLocators.CLEAR_FILTER_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CLEAR_FILTER_IN_DATA_TAB, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_sort_descending_in_data_tab(spreadsheet_editor):
    for symb in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, symb + Keys.ENTER)
    (
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.SORT_DESCENDING_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SORT_DESCENDING_IN_DATA_TAB, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_sort_ascending_in_data_tab(spreadsheet_editor):
    for symb in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, symb + Keys.ENTER)
    (spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME).click_on_element(spreadsheet_editor.DATA_TAB).click_on_element(DataTabLocators.SORT_ASCENDING_BTN))
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SORT_ASCENDING_IN_DATA_TAB, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_insert_text_to_columns(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка разделение по столбцам' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '1,2,3,4,5,6,7,8' + Keys.ENTER)
        .press_key(Keys.UP)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.TEXT_TO_COLUMN_BTN)
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_TEXT_TO_COLUMNS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_remove_duplicates(spreadsheet_editor):
    spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка удаления дубликатов' + Keys.ENTER)
    for char in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, char + Keys.ENTER, 2)
    (
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.SHIFT, Keys.HOME)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.REMOVE_DUPLICATES_BTN)
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_REMOVE_DUPLICATES, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_validate_data(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка данных' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.DATA_VALIDATION_BTN)
        .click_on_element(DataTabLocators.DATA_VALIDATION_MODAL_CMB_ALLOW_DROPDOWN_BTN)
        .click_on_element(DataTabLocators.DATA_VALIDATION_MODAL_CMB_ALLOW_DROPDOWN_INTEGER)
        .click_on_element(DataTabLocators.DATA_VALIDATION_MODAL_CMB_DATA_DROPDOWN_BTN)
        .click_on_element(DataTabLocators.DATA_VALIDATION_MODAL_CMB_DATA_DROPDOWN_EQUAL)
        .send_keys_to_element(DataTabLocators.DATA_VALIDATION_MODAL_TEXT_SOURCE_INPUT, '1')
        .press_key(Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '2' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_VALIDATE_DATA, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_group_area(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка группировки' + Keys.ENTER)
        .hold_key_down_and_press_key_count_times(Keys.SHIFT, Keys.DOWN, 8)
        .hold_key_down_and_press_key_count_times(Keys.SHIFT, Keys.RIGHT, 8)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.GROUP_BTN)
        .press_key(Keys.ENTER)
        .click_on_element(DataTabLocators.GROUP_DROPDOWN_BTN)
        .click_on_element(DataTabLocators.GROUP_DROPDOWN_GROUP_COLS)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_GROUP_AREA, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.data_tab
def test_ungroup_area(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка разгруппировки' + Keys.ENTER)
        .hold_key_down_and_press_key_count_times(Keys.SHIFT, Keys.DOWN, 8)
        .hold_key_down_and_press_key_count_times(Keys.SHIFT, Keys.RIGHT, 8)
        .click_on_element(spreadsheet_editor.DATA_TAB)
        .click_on_element(DataTabLocators.GROUP_BTN)
        .press_key(Keys.ENTER)
        .click_on_element(DataTabLocators.GROUP_DROPDOWN_BTN)
        .click_on_element(DataTabLocators.GROUP_DROPDOWN_GROUP_COLS)
        .click_on_element(DataTabLocators.UNGROUP_BTN)
        .press_key(Keys.ENTER)
        .click_on_element(DataTabLocators.UNGROUP_DROPDOWN_BTN)
        .click_on_element(DataTabLocators.UNGROUP_DROPDOWN_UNGROUP_ALL_STRUCTURE)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_UNGROUP_AREA, spreadsheet_editor.SP_CANVAS))
