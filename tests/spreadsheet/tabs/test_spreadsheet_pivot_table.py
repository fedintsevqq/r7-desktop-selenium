import pytest
from selenium.webdriver import Keys
from editors.base_editor import Editor
from editors.spreadsheet_editor import Samples, CommonLocators, PivotTableTabLocators, InsertTabLocators
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages
import pytest_check as check


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def insert_pivot_table(spreadsheet_editor: Editor, test_str: str):
    spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, test_str + Keys.ENTER)
    for row in Samples.PIVOT_DATA_SET_RAW.split('.'):
        for col in row.split(','):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col + Keys.TAB)
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.ENTER + Keys.ARROW_LEFT)
    (
        spreadsheet_editor.click_on_element(spreadsheet_editor.PIVOT_TAB)
        .click_on_element(PivotTableTabLocators.INSERT_PIVOT_TABLE_BTN)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_SOURCE_RANGE_INPUT, Keys.BACKSPACE, 12)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_SOURCE_RANGE_INPUT, 'Лист1!$A$2:$H$21')
        .click_on_element(InsertTabLocators.PIVOT_TABLE_MODAL_EXIST_SHEET_RADIO_SPAN)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_EXIST_SHEET_DEST_RANGE_INPUT, Keys.BACKSPACE, 12)
        .send_keys_to_element(InsertTabLocators.PIVOT_TABLE_MODAL_EXIST_SHEET_DEST_RANGE_INPUT, 'Лист1!$J$2')
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


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_pivot_table(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка вставки сводной таблицы')
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_PIVOT_TABLE_IN_PIVOT_TABLE_TAB, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_change_report_layout_structure_form(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка изменения макета отчета - в форме структуры')
    (
        spreadsheet_editor.click_on_element(PivotTableTabLocators.REPORT_LAYOUT_BTN).click_on_element(
            PivotTableTabLocators.REPORT_LAYOUT_DROPDOWN_SHOW_IN_STRUCTURE_FORM
        )
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_REPORT_LAYOUT_STRUCTURE_FORM, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_insert_blank_row(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка вставки пустой строки после каждого элемента')
    (
        spreadsheet_editor.click_on_element(PivotTableTabLocators.BLANK_ROWS_BNT).click_on_element(
            PivotTableTabLocators.BLANK_ROWS_DROPDOWN_INSERT_BLANK_ROW_AFTER_EACH_ELEMENT
        )
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_BLANK_ROW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_show_subtotals_in_footer(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка показа промежуточных итогов в верхней части группы')
    (
        spreadsheet_editor.click_on_element(PivotTableTabLocators.SUBTOTALS_BNT).click_on_element(
            PivotTableTabLocators.SUBTOTALS_DROPDOWN_SHOW_ALL_SUBTOTALS_IN_FOOTER
        )
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SHOW_SUBTOTALS_IN_FOOTER, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_turn_on_grand_totals(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка включения общих итогов')
    (
        spreadsheet_editor.click_on_element(PivotTableTabLocators.GRAND_TOTALS_BTN).click_on_element(
            PivotTableTabLocators.GRAND_TOTALS_DROPDOWN_ON_FOR_ROWS_AND_COLS
        )
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_TURN_ON_GRAND_TOTALS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_refresh_pivot_table(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка обновления сводной таблицы')
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.BACKSPACE, 4).send_keys_to_element(
            CommonLocators.CELL_ADDRESS_BAR_INPUT, 'F3' + Keys.ENTER
        )
    )
    for i in range(9):
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '1000' + Keys.DOWN)
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.BACKSPACE, 4).send_keys_to_element(
            CommonLocators.CELL_ADDRESS_BAR_INPUT, 'G3' + Keys.ENTER
        )
    )
    for i in range(9):
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '1000' + Keys.DOWN)
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, 'J2' + Keys.ENTER)
        .click_on_element(PivotTableTabLocators.REFRESH_PIVOT_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_REFRESH_PIVOT_TABLE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_insert_pivot_chart(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка вставки сводной диаграммы')
    spreadsheet_editor.driver.find_elements(*PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN)[5].click()
    spreadsheet_editor.click_on_element(PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN_ADD_TO_VALUE)
    (
        spreadsheet_editor.click_on_element(PivotTableTabLocators.PIVOT_CHART_BTN).click_on_element(
            PivotTableTabLocators.PIVOT_CHART_DROPDOWN_CHART_COLUMN_NORMAL
        )
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_PIVOT_CHART, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_select_all_pivot_table(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка выделения всей сводной таблицы')
    spreadsheet_editor.click_on_element(PivotTableTabLocators.SELECT_ALL_PIVOT_TABLE_BTN)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SELECT_ALL_PIVOT_TABLE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_insert_calc_field(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка вставки вычисляемого поля')
    (
        spreadsheet_editor.click_on_element(PivotTableTabLocators.CALC_FIELD_BTN)
        .click_on_element(PivotTableTabLocators.CALC_FIELD_DROPDOWN_CALC_FIELD)
        .send_keys_to_element(PivotTableTabLocators.CALC_FIELD_MODAL_NAME_INPUT, Keys.BACKSPACE, 6)
        .send_keys_to_element(PivotTableTabLocators.CALC_FIELD_MODAL_NAME_INPUT, 'Сумма в валюте')
        .send_keys_to_element(PivotTableTabLocators.CALC_FIELD_MODAL_FORMULA_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(PivotTableTabLocators.CALC_FIELD_MODAL_FORMULA_INPUT, '=Сумма/86')
        .click_on_element(PivotTableTabLocators.CALC_FIELD_MODAL_ADD_FIELD_BTN)
        .click_on_element(PivotTableTabLocators.CALC_FIELD_MODAL_OK_BTN)
    )
    spreadsheet_editor.driver.find_elements(*InsertTabLocators.PIVOT_TABLE_LIST_FIELDS_CHK_LABEL)[-1].click()
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_CALC_FIELD, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_check_header_row_turn_off(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка отключения заголовков строк')
    spreadsheet_editor.click_on_element(PivotTableTabLocators.HEADER_ROW_CHK)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHECK_HEADER_ROW_TURN_OFF, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_check_header_col_turn_off(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка отключения заголовков столбцов')
    pt_fileds = spreadsheet_editor.driver.find_elements(*PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN)
    for i in range(3):
        pt_fileds[i].click()
        spreadsheet_editor.click_on_element(PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN_ADD_TO_VALUE)
    spreadsheet_editor.click_on_element(PivotTableTabLocators.HEADER_COL_CHK)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHECK_HEADER_COL_TURN_OFF, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_check_banded_row_turn_on(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка включения чередования строк')
    pt_fileds = spreadsheet_editor.driver.find_elements(*PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN)
    for i in range(3):
        pt_fileds[i].click()
        spreadsheet_editor.click_on_element(PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN_ADD_TO_VALUE)
    spreadsheet_editor.click_on_element(PivotTableTabLocators.BANDED_ROW_CHK)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHECK_BANDED_ROW_TURN_ON, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_check_banded_col_turn_on(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка включения чередования столбцов')
    pt_fileds = spreadsheet_editor.driver.find_elements(*PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN)
    for i in range(3):
        pt_fileds[i].click()
        spreadsheet_editor.click_on_element(PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN_ADD_TO_VALUE)
    spreadsheet_editor.click_on_element(PivotTableTabLocators.BANDED_COL_CHK)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHECK_BANDED_COL_TURN_ON, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.pivot_table_tab
def test_change_pivot_table_style(spreadsheet_editor):
    insert_pivot_table(spreadsheet_editor, 'Проверка изменения стиля')
    pt_fileds = spreadsheet_editor.driver.find_elements(*PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN)
    for i in range(3):
        pt_fileds[i].click()
        spreadsheet_editor.click_on_element(PivotTableTabLocators.PIVOT_TABLE_LIST_FIELDS_DROPDOWN_ADD_TO_VALUE)
    (
        spreadsheet_editor.click_on_element(PivotTableTabLocators.STYLE_PIVOT_TABLE_DROPDOWN_BTN).click_on_element(
            PivotTableTabLocators.STYLE_PIVOT_TABLE_DROPDOWN_LIGHT_8
        )
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_PIVOT_TABLE_STYLE, spreadsheet_editor.SP_CANVAS))
