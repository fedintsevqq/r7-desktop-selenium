import pytest
import pytest_check as check
from selenium.webdriver import Keys
from editors.spreadsheet_editor import MainTabLocators, CommonLocators, Samples
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_input_font_name(spreadsheet_editor):
    (
        spreadsheet_editor.pause_in_test(5)
        .click_on_element(MainTabLocators.FONT_NAME_INPUT)
        .send_keys_to_element(MainTabLocators.FONT_NAME_INPUT, Keys.BACKSPACE)
        .send_keys_to_element(MainTabLocators.FONT_NAME_INPUT, 'Roboto')
        .send_keys_to_element(MainTabLocators.FONT_NAME_INPUT, Keys.ENTER)
        .send_keys_to_element(CommonLocators.CELL_FORMULA_BAR_TEXTAREA, 'Проверка шрифта Roboto')
        .send_keys_to_element(CommonLocators.CELL_FORMULA_BAR_TEXTAREA, Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INPUT_FONT_NAME, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_change_font_name(spreadsheet_editor):
    (
        spreadsheet_editor.pause_in_test(5)
        .click_on_element(MainTabLocators.FONT_NAME_DROPDOWN)
        .click_on_element(MainTabLocators.FONT_NAME_DROPDOWN_ASANA)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка шрифта Asana')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_FONT_NAME, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_input_font_size(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.FONT_SIZE_INPUT)
        .send_keys_to_element(MainTabLocators.FONT_SIZE_INPUT, Keys.BACKSPACE)
        .send_keys_to_element(MainTabLocators.FONT_SIZE_INPUT, '18')
        .send_keys_to_element(MainTabLocators.FONT_SIZE_INPUT, Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка размера шрифта: 18')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INPUT_FONT_SIZE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_increase_font_size(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.INCREASE_FONT, 2)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка увеличения размера шрифта на 2 пункта')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INCREASE_FONT_SIZE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_decrease_font_size(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.DECREASE_FONT, 2)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка уменьшения размера шрифта на 2 пункта')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_DECREASE_FONT_SIZE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_change_case_text(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка изменения регистра текста')
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.CHANGE_FONT_CASE_DROPDOWN)
        .click_on_element(MainTabLocators.CHANGE_FONT_CASE_UPPER_REGISTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_CASE_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_bold_text(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.BOLD_TEXT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка жирного текста')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_BOLD_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_italic_text(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.ITALIC_TEXT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка курсива')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ITALIC_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_underline_text(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.UNDERLINE_TEXT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка подчеркнутого текста')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_UNDERLINE_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_strikeout_text(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.STRIKEOUT_TEXT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка зачеркнутого текста')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_STRIKEOUT_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_subscript_text(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.SUBSCRIPT_TEXT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка подстрочного текста')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SUBSCRIPT_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_superscript_text(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.SUBSCRIPT_DROPDOWN)
        .click_on_element(MainTabLocators.SUBSCRIPT_DROPDOWN_SUPERSCRIPT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка надстрочного текста')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SUPERSCRIPT_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_font_color_red(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.FONT_COLOR_DROPDOWN)
        .click_on_element(MainTabLocators.FONT_COLOR_DROPDOWN_RED)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка красного шрифта')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_FONT_COLOR_RED, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_highlight_green(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.HIGHLIGHT_DROPDOWN)
        .click_on_element(MainTabLocators.HIGHLIGHT_DROPDOWN_COLOR_GREEN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка зеленой подсветки')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_HIGHLIGHT_GREEN, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_borders_all(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.BORDERS_DROPDOWN)
        .click_on_element(MainTabLocators.BORDERS_DROPDOWN_ALL_BORDERS)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка границ: все')
        .pause_in_test(2)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_BORDERS_ALL, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_align_top(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.ALIGN_TOP)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка выравнивания по верхнему краю')
        .press_key(Keys.ENTER)
        .pause_in_test(5)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_TOP, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_align_middle(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.ALIGN_MIDDLE)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка выравнивания по середине')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_MIDDLE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_align_bottom(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.ALIGN_BOTTOM)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка выравнивания по нижнему краю')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_BOTTOM, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_align_left(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.ALIGN_LEFT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка выравнивания по левому краю')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_LEFT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_align_center(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.ALIGN_CENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка выравнивания по центру')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_CENTER, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_align_right(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.ALIGN_RIGHT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка выравнивания по правому краю')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_RIGHT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_align_just(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.ALIGN_JUST)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка выравнивания по ширине')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ALIGN_JUST, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_hyphenation(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.HYPHENATION)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка переноса текста')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_HYPHENATION, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_orient_text(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка вертикального текста')
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.TEXT_ORIENT_DROPDOWN)
        .click_on_element(MainTabLocators.TEXT_ORIENT_VERTICAL)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ORIENT_TEXT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_merge_cells(spreadsheet_editor):
    (
        spreadsheet_editor.send_key_and_click_by_offset(CommonLocators.WORKSHEET_TEXT_AREA, Keys.SHIFT, 260, 260)
        .click_on_element(MainTabLocators.MERGE_CELLS)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка объединения ячеек')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_MERGE_CELLS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_insert_sum(spreadsheet_editor):
    (
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '11')
        .press_key(Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '12')
        .press_key(Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '13')
        .press_key(Keys.ENTER)
        .click_on_element(MainTabLocators.SUM_INSERT)
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_SUM, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_add_named_range(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.NAMED_RANGE_DROPDOWN)
        .click_on_element(MainTabLocators.NAMED_RANGE_DROPDOWN_ADD_NAME)
        .send_keys_to_element(MainTabLocators.NAMED_RANGE_ADD_NAME_MODAL_NAME_INPUT, 'Новый_диапазон')
        .click_on_element(MainTabLocators.NAMED_RANGE_ADD_NAME_MODAL_OK_BTN)
        .click_on_element(MainTabLocators.NAMED_RANGE_DROPDOWN)
        .click_on_element(MainTabLocators.NAMED_RANGE_DROPDOWN_DISPATHER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ADD_NAMED_RANGE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_sort_descending(spreadsheet_editor):
    for char in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, char)
        spreadsheet_editor.press_key(Keys.ENTER)
    spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME)
    spreadsheet_editor.click_on_element(MainTabLocators.SORT_DES)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SORT_DESCENDING, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_sort_ascending(spreadsheet_editor):
    for char in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, char)
        spreadsheet_editor.press_key(Keys.ENTER)
    spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME)
    spreadsheet_editor.click_on_element(MainTabLocators.SORT_ASC)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SORT_ASCENDING, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_insert_filter(spreadsheet_editor):
    for char in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, char)
        spreadsheet_editor.press_key(Keys.ENTER)
    (
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME)
        .click_on_element(MainTabLocators.FILTER_INSERT_AUTO)
        .click_on_element_with_offset_from_top_left(CommonLocators.WORKSHEET_EDITOR_SDK, 80, 25)
        .send_keys_to_element(MainTabLocators.FILTER_MODAL_SEARCH_INPUT, 'Й')
        .click_on_element(MainTabLocators.FILTER_MODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_FILTER, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_clear_filter(spreadsheet_editor):
    for char in Samples.UNSORTED_DATA_SET:
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, char)
        spreadsheet_editor.press_key(Keys.ENTER)
    (
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.HOME)
        .click_on_element(MainTabLocators.FILTER_INSERT_AUTO)
        .click_on_element_with_offset_from_top_left(CommonLocators.WORKSHEET_EDITOR_SDK, 80, 25)
        .send_keys_to_element(MainTabLocators.FILTER_MODAL_SEARCH_INPUT, 'Й')
        .click_on_element(MainTabLocators.FILTER_MODAL_OK_BTN)
        .click_on_element(MainTabLocators.FILTER_CLEAR)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CLEAR_FILTER, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_change_data_format(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.DATA_FORMAT_DROPDOWN)
        .click_on_element(MainTabLocators.DATA_FORMAT_DROPDOWN_NUMERIC)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '123')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_DATA_FORMAT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_percents_data_format(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.DATA_FORMAT_PERCENTS)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '123')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_PERCENTS_DATA_FORMAT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_currency_data_format(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.DATA_FORMAT_CURRENCY_DROPDOWN)
        .click_on_element(MainTabLocators.DATA_FORMAT_CURRENCY_DROPDOWN_RUBLE)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '123')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CURRENCY_DATA_FORMAT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_decrement_digits_data_format(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.DATA_FORMAT_DROPDOWN)
        .click_on_element(MainTabLocators.DATA_FORMAT_DROPDOWN_NUMERIC)
        .click_on_element(MainTabLocators.DATA_FORMAT_DIGIT_DEC)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '123')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_DECREMENT_DIGITS_DATA_FORMAT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_increment_digits_data_format(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.DATA_FORMAT_DROPDOWN)
        .click_on_element(MainTabLocators.DATA_FORMAT_DROPDOWN_NUMERIC)
        .click_on_element(MainTabLocators.DATA_FORMAT_DIGIT_INC)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, '123')
        .press_key(Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INCREMENT_DIGITS_DATA_FORMAT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_insert_cell_with_move_right(spreadsheet_editor):
    for row in range(3):
        for col in range(3):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col)
            spreadsheet_editor.press_key(Keys.ENTER)
        spreadsheet_editor.press_key(Keys.ARROW_RIGHT)
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.ARROW_UP)
    (
        spreadsheet_editor.click_on_element(CommonLocators.CELL_ADDRESS_BAR_INPUT)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.BACKSPACE)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, 'B2')
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.ENTER)
        .click_on_element(MainTabLocators.INSERT_CELL_DROPDOWN)
        .click_on_element(MainTabLocators.INSERT_CELL_DROPDOWN_WITH_MOVE_RIGHT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_CELL_WITH_MOVE_RIGHT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_delete_cell_with_move_left(spreadsheet_editor):
    for row in range(3):
        for col in range(3):
            spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, col)
            spreadsheet_editor.press_key(Keys.ENTER)
        spreadsheet_editor.press_key(Keys.ARROW_RIGHT)
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.ARROW_UP)
    (
        spreadsheet_editor.click_on_element(CommonLocators.CELL_ADDRESS_BAR_INPUT)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.BACKSPACE)
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, 'B2')
        .send_keys_to_element(CommonLocators.CELL_ADDRESS_BAR_INPUT, Keys.ENTER)
        .click_on_element(MainTabLocators.DELETE_CELL_DROPDOWN)
        .click_on_element(MainTabLocators.DELETE_CELL_DROPDOWN_WITH_MOVE_LEFT)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_DELETE_CELL_WITH_MOVE_LEFT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_clear_style_formating(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.BOLD_TEXT)
        .click_on_element(MainTabLocators.ITALIC_TEXT)
        .click_on_element(MainTabLocators.UNDERLINE_TEXT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка очистки стиля')
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP)
        .click_on_element(MainTabLocators.CLEAR_STYLE_DROPDOWN)
        .click_on_element(MainTabLocators.CLEAR_STYLE_DROPDOWN_FORMATING)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CLEAR_STYLE_FORMATING, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_copy_style(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.BOLD_TEXT)
        .click_on_element(MainTabLocators.ITALIC_TEXT)
        .click_on_element(MainTabLocators.UNDERLINE_TEXT)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка копирования стиля источник')
        .press_key(Keys.ENTER)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка копирования стиля приемник')
        .press_key(Keys.ENTER)
        .press_key(Keys.ARROW_UP, 2)
        .click_on_element(MainTabLocators.COPY_STYLE)
        .click_on_element_coord_with_offset(CommonLocators.CELL_ADDRESS_BAR_INPUT, 0, 60)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_COPY_STYLE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_conditional_formating(spreadsheet_editor):
    for i in range(10):
        spreadsheet_editor.send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, str(i) + Keys.ENTER)
    (
        spreadsheet_editor.send_hotkey(Keys.CONTROL, Keys.SHIFT, Keys.HOME)
        .click_on_element(MainTabLocators.CONDITION_FORMAT_DROPDOWN)
        .click_on_element(MainTabLocators.CONDITION_FORMAT_DROPDOWN_EQUAL)
        .click_on_element(MainTabLocators.CONDITION_FORMAT_DROPDOWN_EQUAL_GRATE_OR_EQUAL)
        .send_keys_to_element(MainTabLocators.CONDITION_FORMAT_MODAL_VALUE_INPUT, '5')
        .click_on_element(MainTabLocators.CONDITION_FORMAT_MODAL_OK_BTN)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CONDITIONAL_FORMATING, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_insert_table_by_template(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.TEMPLATE_TABLE_DROPDOWN)
        .click_on_element(MainTabLocators.TEMPLATE_TABLE_DROPDOWN_LIGHT14)
        .send_keys_to_element(MainTabLocators.TEMPLATE_TABLE_MODAL_RANGE_INPUT, Keys.BACKSPACE, 4)
        .send_keys_to_element(MainTabLocators.TEMPLATE_TABLE_MODAL_RANGE_INPUT, '$A$1:$H$8')
        .send_keys_to_element(MainTabLocators.TEMPLATE_TABLE_MODAL_RANGE_INPUT, Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_INSERT_TABLE_BY_TEMPLATE, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.main_tab
def test_change_field_style(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(MainTabLocators.FIELD_STYLES_NEUTRAL)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка стиля Нейтральный' + Keys.ENTER)
        .click_on_element(MainTabLocators.FIELD_STYLES_DROPDOWN)
        .click_on_element(MainTabLocators.FIELD_STYLES_DROPDOWN_GOOD)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка стиля Хороший' + Keys.ENTER)
        .click_on_element(MainTabLocators.FIELD_STYLES_NORMAL)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, 'Проверка стиля Обычный' + Keys.ENTER)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_CHANGE_FIELD_STYLE, spreadsheet_editor.SP_CANVAS))
