import datetime
import pytest
import pytest_check as check
import pyperclip
from selenium.webdriver.common.keys import Keys
from configs import config
from editors.presentation_editor import MainTabLocators, PresentationEditor, Samples, InsertTabLocators
from resources.presentation import ExpectedImages
from utils import screenshot_comparsion


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_add_slide(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
    .click_on_element(InsertTabLocators.ADD_SLIDE_BTN)
    .click_on_element_coord_with_offset(InsertTabLocators.INSERT_CHART_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка добавления слайда')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_SLIDE_LEFT_FIELD, presentation_editor.LEFT_CANVAS), 'Скриншот бокового поля не соответствует эталонному')

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_SLIDE_MAIN_FIELD, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_add_type_slide(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
    .click_on_element(InsertTabLocators.ADD_SLIDE_DROPDOWN_BTN)
    .click_on_element_coord(InsertTabLocators.ADD_ONLY_HEADER_SLIDE)
    .click_on_element_coord_with_offset(InsertTabLocators.INSERT_CHART_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка добавления слайда со стилем')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TYPE_SLIDE_MAIN_FIELD, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TYPE_SLIDE_LEFT_FIELD, presentation_editor.LEFT_CANVAS), 'Скриншот бокового поля не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_table(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
    .click_on_element(InsertTabLocators.INSERT_TABLE_BTN)
    .click_on_element_coord(InsertTabLocators.INSERT_TABLE_MOUSECATCHER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TABLE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_user_table(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
    .click_on_element(InsertTabLocators.INSERT_TABLE_BTN)
    .click_on_element_coord(InsertTabLocators.INSERT_USER_TABLE)
    .send_keys_to_element(InsertTabLocators.INSERT_TABLE_CELLS, Keys.BACKSPACE)
    .send_keys_to_element(InsertTabLocators.INSERT_TABLE_CELLS, 3)
    .send_keys_to_element(InsertTabLocators.INSERT_TABLE_ROWS, Keys.BACKSPACE)
    .send_keys_to_element(InsertTabLocators.INSERT_TABLE_ROWS, 3)
    .click_on_element(InsertTabLocators.CELLS_SPINNER_UP_BTN)
    .click_on_element(InsertTabLocators.ROWS_SPINNER_DOWN_BTN)
    .click_on_element(InsertTabLocators.INSERT_TABLE_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_USER_TABLE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_table_form(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_TABLE_BTN)
     .click_on_element_coord(InsertTabLocators.INSERT_TABLE_FORM)
     .switch_to_frame(InsertTabLocators.INSERT_TABLE_FRAME))

    for i in range(3):
        for j in range(3):
            (presentation_editor.send_keys_to_element(PresentationEditor.TEXT_FIELD, f'{i+1}')
             .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.RIGHT))

        (presentation_editor.send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
        .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.LEFT, 3))

    presentation_editor.driver.switch_to.parent_frame()

    (presentation_editor.click_on_element_coord(InsertTabLocators.INSERT_TABLE_SAVE_AND_EXIT_BTN)
    .action.pause(config.general_pause).perform())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TABLE_FORM, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_horizontal_text_by_btn(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
    .click_on_element(InsertTabLocators.INSERT_HORIZONTAL_TEXT_BTN)
    .click_on_element_coord_with_offset(InsertTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 200, 200)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Вставка горизонтальной надписи')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TAB_HORIZONTAL_TEXT_BY_BTN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_horizontal_text_by_link(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
    .click_on_element(InsertTabLocators.INSERT_TEXT_BTN)
    .click_on_element_coord(InsertTabLocators.INSERT_HORIZONTAL_TEXT)
    .click_on_element_coord_with_offset(InsertTabLocators.INSERT_TEXT_BTN, 200, 200)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Вставка горизонтальной надписи')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TAB_HORIZONTAL_TEXT_BY_LINK, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_vertical_text_by_link(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
    .click_on_element(InsertTabLocators.INSERT_TEXT_BTN)
    .click_on_element_coord(InsertTabLocators.INSERT_VERTICAL_TEXT)
    .click_on_element_coord_with_offset(InsertTabLocators.INSERT_TEXT_BTN, 250, 200)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Вставка вертикальной надписи')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TAB_VERTICAL_TEXT_BY_LINK, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_text_art(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_TEXT_ART_BTM)
     .click_on_element(InsertTabLocators.INSERT_TEXT_ART))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_TEXT_ART, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_linked_image(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_IMAGE_BTN)
     .click_on_element_coord(InsertTabLocators.INSERT_LINKED_IMAGE)
     .send_keys_to_element(InsertTabLocators.INSERT_IMAGE_INPUT_FIELD, InsertTabLocators.IMAGE_LINK)
     .click_on_element(MainTabLocators.INSERT_IMAGE_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_LINKED_IMAGE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_chart(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_CHART_BTN)
     .click_on_element_coord(InsertTabLocators.INSERT_PIE_CHART)
     .switch_to_frame(InsertTabLocators.INSERT_CHART_FRAME)
     .pause_in_test(config.general_pause))

    presentation_editor.driver.switch_to.parent_frame()

    (presentation_editor.click_on_element_coord(InsertTabLocators.INSERT_CHART_SAVE_AND_EXIT_BTN)
    .action.pause(config.general_pause).perform())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_CHART, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_smart_art(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SMART_ART_BTN)
     .click_on_element_coord(InsertTabLocators.INSERT_SMART_ART_PROCESS_LINK)
     .click_on_element_coord(InsertTabLocators.INSERT_SMART_GEAR_ART)
     .pause_in_test())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_SMART_ART, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_shape(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element_coord(InsertTabLocators.INSERT_SHAPE)
     .drag_n_drop(InsertTabLocators.INSERT_SHAPE, 300, 300, 0, 200))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_SHAPE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_shape_by_dropdown_btn(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .pause_in_test(config.general_pause)
     .click_on_element_coord(InsertTabLocators.INSERT_SHAPE_DROPDOWN_BTN)
     .click_on_element_coord(InsertTabLocators.INSERT_SHAPE_FROM_DROPDOWN_BTN)
     .drag_n_drop(InsertTabLocators.INSERT_SHAPE_DROPDOWN_BTN, 300, 300, 0, 200))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_SHAPE_BY_DROPDOWN_BTN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_comment(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_COMMENT_BTN)
     .send_keys_to_element(InsertTabLocators.INSERT_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(InsertTabLocators.INSERT_COMMENT_ADD_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_COMMENT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_hyperlink(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element_coord_with_offset(InsertTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 300, 450)
     .click_on_element(InsertTabLocators.INSERT_HYPERLINK_BTN)
     .send_keys_to_element(InsertTabLocators.INSERT_HYPERLINK_FIELD, InsertTabLocators.HYPERLINK)
     .pause_in_test(config.general_pause)
     .click_on_element_coord(InsertTabLocators.INSERT_HYPERLINK_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_HYPERLINK, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_edit_header(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_EDITHEADER_BTN)
     .pause_in_test(config.general_pause)
     .click_on_element(InsertTabLocators.INSERT_DATE_AND_TIME_EDITHEADER_CBX)
     .click_on_element(InsertTabLocators.INSERT_SLIDE_NUMBER_EDITHEADER_CBX)
     .click_on_element(InsertTabLocators.INSERT_DOWNTEXT_EDITHEADER_CBX)
     .send_keys_to_element(InsertTabLocators.INSERT_DOWNTEXT_EDITHEADER_FIELD, 'Этот текст будет внизу презентации!')
     .click_on_element(InsertTabLocators.INSERT_EDITHEADER_APPLY_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_EDIT_HEADER, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_date_and_time(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element_coord_with_offset(InsertTabLocators.INSERT_COMMENT_BTN, 0, 300)
     .click_on_element(InsertTabLocators.INSERT_DATE_AND_TIME_BTN)
     .click_on_element_coord(InsertTabLocators.DATE_AND_TIME_FORMAT)
     .click_on_element(InsertTabLocators.DATE_AND_TIME_WINDOW_OK_BTN)
     .click_on_element(PresentationEditor.SELECT_ALL)
     .click_on_element(PresentationEditor.COPY))

    clipboard = pyperclip.paste().strip()
    curr_date = datetime.datetime.now().strftime("%d.%m.%Y")
    check.is_true(clipboard == curr_date, 'Дата в редакторе не совпадает с текущей')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_slide_number(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element_coord_with_offset(InsertTabLocators.INSERT_COMMENT_BTN, 0, 300)
     .click_on_element(InsertTabLocators.INSERT_SLIDE_NUMBER_BTN)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_SLIDE_NUMBER, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_equation(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element_coord_with_offset(InsertTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 300, 450)
     .click_on_element(InsertTabLocators.INSERT_EQUATION_BTN)
     .click_on_element_coord(InsertTabLocators.INSERT_RADICAL_EQUATION)
     .click_on_element_coord(InsertTabLocators.INSERT_QUADRATIC_EQUATION)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ESCAPE))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_EQUATION, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_equation_by_dropdown_btn(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element_coord_with_offset(InsertTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 300, 450)
     .click_on_element(InsertTabLocators.INSERT_EQUATION_DROPDOWN_BTN)
     .click_on_element_coord(InsertTabLocators.INSERT_LOGARITHM_EQUATION_LINK)
     .click_on_element_coord(InsertTabLocators.INSERT_LIMIT_EQUATION)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ESCAPE))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_EQUATION_BY_DROPDOWN_BTN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.insert_tab
def test_presentation_insert_symbol(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.INSERT_TAB)
     .click_on_element_coord_with_offset(InsertTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 300, 450)
     .click_on_element(InsertTabLocators.INSERT_SYMBOL_BTN)
     .pause_in_test(config.general_pause)
     .click_on_element_coord(InsertTabLocators.INSERT_SPECIAL_SYMBOLS_BTN)
     .pause_in_test(config.general_pause)
     .click_on_element_coord(InsertTabLocators.INSERT_TRADEMARK_SYMBOL)
     .click_on_element(InsertTabLocators.INSERT_BTN, 5)
     .click_on_element_coord(InsertTabLocators.INSERT_SYMBOL_WINDOW_CLOSE_BTN)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_SYMBOL, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')
