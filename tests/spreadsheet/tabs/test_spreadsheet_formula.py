import pytest
from selenium.webdriver import Keys
from editors.spreadsheet_editor import CommonLocators, FormulaTabLocators, Samples, MainTabLocators
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages
import pytest_check as check


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_additional_formula(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка вставки' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, ' Функции' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.ADDITIONAL_FORMULA_BTN)
        .send_keys_to_element(FormulaTabLocators.FORMULA_INSERT_MODAL_SEARCH_INPUT, 'сцеп' + Keys.ENTER)
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, 'A1')
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_2_INPUT, 'A2')
        .click_on_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_ADDITIONAL_FORMULA, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_auto_sum(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '10' + Keys.ENTER, 4)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.AUTO_SUM_FORMULA_BTN)
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_AUTO_SUM, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_auto_sum_dropdown_average(spreadsheet_editor):
    for i in range(4):
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, str(i) + '10' + Keys.ENTER)
    (
        spreadsheet_editor.click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.AUTO_SUM_FORMULA_DROPDOWN_BTN)
        .click_on_element(FormulaTabLocators.AUTO_SUM_FORMULA_DROPDOWN_AVERAGE)
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_AUTO_SUM_DROPDOWN_AVERAGE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_recent_formula_sum(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '20' + Keys.ENTER, 4)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.RECENT_FORMULA_BTN)
        .click_on_element(FormulaTabLocators.RECENT_FORMULA_DROPDOWN_SUM)
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_RECENT_FORMULA_SUM, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_financial_formula_apl(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '10000' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '5000' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '36' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.FINANCIAL_FORMULA_BTN)
        .click_on_element(FormulaTabLocators.FINANCIAL_FORMULA_DROPDOWN_APL)
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, 'A1')
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_2_INPUT, 'A2')
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_3_INPUT, 'A3' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_FINANCIAL_FORMULA_APL, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_logical_formula_if(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '1' + Keys.ENTER, 2)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.LOGICAL_FORMULA_BTN)
        .click_on_element(FormulaTabLocators.LOGICAL_FORMULA_DROPDOWN_IF)
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, 'A1=A2')
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_2_INPUT, 'Истина')
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_3_INPUT, 'Ложь' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_LOGICAL_FORMULA_IF, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_text_formula_unicode(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Вставки' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Текстовой' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Формулы' + Keys.ENTER)
        .press_key(Keys.TAB)
        .send_hotkey(Keys.CONTROL, Keys.ARROW_UP)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
    )
    for i in range(4):
        (
            spreadsheet_editor.click_on_element(FormulaTabLocators.TEXT_FORMULA_BTN)
            .click_on_element(FormulaTabLocators.TEXT_FORMULA_DROPDOWN_UNICODE)
            .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, 'A' + str(i + 1) + Keys.ENTER)
            .press_key(Keys.ENTER)
        )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_TEXT_FORMULA_UNICODE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_date_time_formula_date(spreadsheet_editor):
    spreadsheet_editor.click_on_element(spreadsheet_editor.FORMULA_TAB)
    for date in Samples.DATES:
        (
            spreadsheet_editor.click_on_element(FormulaTabLocators.DATE_TIME_FORMULA_BTN)
            .click_on_element(FormulaTabLocators.DATE_TIME_FORMULA_DROPDOWN_DATE)
            .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, date.split('.')[0])
            .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_2_INPUT, date.split('.')[1])
            .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_3_INPUT, date.split('.')[2])
            .press_key(Keys.ENTER, 2)
        )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_DATE_TIME_FORMULA_DATE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_lookup_formula_dvssyl(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка вставки ссылки' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.LOOKUP_FORMULA_BTN)
        .click_on_element(FormulaTabLocators.LOOKUP_FORMULA_DROPDOWN_DVSSYL)
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, r'"A1"')
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_2_INPUT, 'Истина' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_LOOKUP_FORMULA_DVSSYL, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_math_formula_cos(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '1,5' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.MATH_FORMULA_BTN)
        .click_on_element(FormulaTabLocators.MATH_FORMULA_DROPDOWN_COS)
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, 'A1' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_MATH_FORMULA_COS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_insert_more_formula_engineering_besseli(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '3,5' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '1' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.MORE_FORMULA_BTN)
        .click_on_element(FormulaTabLocators.MORE_FORMULA_DROPDOWN_ENGINEERING)
        .click_on_element(FormulaTabLocators.MORE_FORMULA_DROPDOWN_ENGINEERING_SUBMENU_BESSELI)
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT, 'A1')
        .send_keys_to_element(FormulaTabLocators.FORMULA_WIZARD_MODAL_ARGUMENT_2_INPUT, 'A2' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_MORE_FORMULA_ENGINEERING_BESSELI, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_add_named_range_in_formula_tab(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.NAMED_RANGE_HUGE_BTN)
        .click_on_element(FormulaTabLocators.NAMED_RANGE_HUGE_DROPDOWN_ADD_NAME)
        .send_keys_to_element(MainTabLocators.NAMED_RANGE_ADD_NAME_MODAL_NAME_INPUT, 'Новый_диапазон')
        .click_on_element(MainTabLocators.NAMED_RANGE_ADD_NAME_MODAL_OK_BTN)
        .click_on_element(FormulaTabLocators.NAMED_RANGE_HUGE_BTN)
        .click_on_element(FormulaTabLocators.NAMED_RANGE_HUGE_DROPDOWN_DISPATHER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ADD_NAMED_RANGE_IN_FORMULA_TAB, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_add_watch_control_value(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '1' + Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка вставки контрольного значения' + Keys.ENTER)
        .send_hotkey(Keys.CONTROL, Keys.HOME)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.WATCH_WINDOW_BTN)
        .click_on_element(FormulaTabLocators.WATCH_WINDOW_MODAL_ADD_CONTROL_VALUE_BTN)
        .click_on_element(FormulaTabLocators.WATCH_WINDOW_SUBMODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ADD_WATCH_CONTROL_VALUE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
# TODO: после реализации открытия тестовых файлов реализовать проверку пересчет книги и текущего листя из тестовых файлов
def test_calculate_formulas(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка пересчета формул' + Keys.ENTER)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.CALCULATE_FORMULAS_BTN)
        .click_on_element(FormulaTabLocators.CALCULATE_FORMULAS_DROPDOWN_BTN)
        .click_on_element(FormulaTabLocators.CALCULATE_FORMULAS_DROPDOWN_CALCULATE_BOOK)
        .click_on_element(FormulaTabLocators.CALCULATE_FORMULAS_DROPDOWN_BTN)
        .click_on_element(FormulaTabLocators.CALCULATE_FORMULAS_DROPDOWN_CALCULATE_CURRENT_SHEET)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CALCULATE_FORMULAS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_show_influencing_cells(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '10' + Keys.ENTER, 4)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.AUTO_SUM_FORMULA_BTN)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(FormulaTabLocators.FORMULA_INFLUENCING_CELLS_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SHOW_INFLUENCING_CELLS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_show_dependent_cells(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '10' + Keys.ENTER, 4)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.AUTO_SUM_FORMULA_BTN)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP, 4)
        .click_on_element(FormulaTabLocators.FORMULA_DEPENDENT_CELLS_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SHOW_DEPENDENT_CELLS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_remove_link_arrows(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '10' + Keys.ENTER, 4)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.AUTO_SUM_FORMULA_BTN)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(FormulaTabLocators.FORMULA_INFLUENCING_CELLS_BTN)
        .press_key(Keys.ARROW_UP, 2)
        .click_on_element(FormulaTabLocators.FORMULA_DEPENDENT_CELLS_BTN)
        .click_on_element(FormulaTabLocators.REMOVE_ARROWS_DROPDOWN_BTN)
        .click_on_element(FormulaTabLocators.REMOVE_ARROWS_DROPDOWN_TO_INFLUENCING_CELLS)
        .click_on_element(FormulaTabLocators.REMOVE_ARROWS_DROPDOWN_BTN)
        .click_on_element(FormulaTabLocators.REMOVE_ARROWS_DROPDOWN_TO_DEPENDENT_CELLS)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_REMOVE_LINK_ARROWS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.formula_tab
def test_show_formulas(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '10' + Keys.ENTER, 4)
        .click_on_element(spreadsheet_editor.FORMULA_TAB)
        .click_on_element(FormulaTabLocators.AUTO_SUM_FORMULA_BTN)
        .press_key(Keys.ENTER)
        .click_on_element(FormulaTabLocators.SHOW_FORMULAS_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SHOW_FORMULAS, spreadsheet_editor.SP_CANVAS))
