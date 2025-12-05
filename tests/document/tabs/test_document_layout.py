import pytest
import pytest_check as check

from selenium.webdriver.common.keys import Keys
from editors.base_editor import Editor
from editors.document_editor import CommonLocators, Samples, LayoutTabLocators, InsertTabLocators
from resources.document import ExpectedImages
from utils import screenshot_comparsion


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_page_margins(document_editor):
    (document_editor.click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.PAGE_MARGINS)
     .click_on_element(LayoutTabLocators.PAGE_MARGINS_NARROW))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_PAGE_MARGINS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_page_orient(document_editor):
    (document_editor.click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.PAGE_ORIENT)
     .click_on_element(LayoutTabLocators.PAGE_ORIENT_LANDSCAPE))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_PAGE_ORIENT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_pagesize(document_editor):
    (document_editor.click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.PAGESIZE)
     .click_on_element(LayoutTabLocators.PAGESIZE_A5))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_PAGESIZE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_columns(document_editor):
    (document_editor.click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.COLUMNS)
     .click_on_element(LayoutTabLocators.COLUMNS_TWO))
    for row in range(60):
        document_editor.send_keys_to_element(Editor.TEXT_FIELD, 'Строка ' + str(row) + '\n')

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_COLUMNS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_page_brake(document_editor):
    (document_editor.click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.PAGE_BRAKE))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_PAGE_BRAKE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_line_numbers(document_editor):
    (document_editor.click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.LINE_NUMBERS)
     .click_on_element(LayoutTabLocators.LINE_NUMBERS_CONTINUOUS))
    for row in range(30):
        document_editor.send_keys_to_element(Editor.TEXT_FIELD, 'Строка ' + str(row) + '\n')

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_LINE_NUMBERS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_hyphenation(document_editor):
    (document_editor.send_keys_to_element(Editor.TEXT_FIELD, Samples.WAR_AND_PEACE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.HYPHENATION)
     .click_on_element(LayoutTabLocators.HYPHENATION_AUTO))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_HYPHENATION, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_wrapping(document_editor):
    (document_editor.send_keys_to_element(Editor.TEXT_FIELD, Samples.WAR_AND_PEACE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .send_hotkey(Keys.CONTROL, Keys.PAGE_UP)
     .click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 150, 150)
     .click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.WRAPPING)
     .click_on_element(LayoutTabLocators.WRAPPING_FRAME)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_DOWN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_WRAPPING, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_move_backward(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 250, 250)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 150, 150)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR_RED)
     .click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.MOVE_BWD)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ESCAPE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.UP))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_MOVE_BACKWARD, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_move_forward(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 250, 250)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 150, 150)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR_RED)
     .click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.MOVE_BWD)
     .click_on_element(LayoutTabLocators.MOVE_FWD)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ESCAPE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.UP))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_MOVE_FORWARD, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_align(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 250, 250)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 150, 150)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR_RED)
     .click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.ALIGN)
     .click_on_element(LayoutTabLocators.ALIGN_CENTER)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ESCAPE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.UP))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ALIGN, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_group(document_editor): #  TODO: сделать проверку разгруппировки
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 250, 250)
     .click_on_element(InsertTabLocators.INSERT_SHAPE)
     .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
     .drag_n_drop(Editor.CURSOR, 150, 150)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR)
     .click_on_element(CommonLocators.SHAPE_BACKGROUND_COLOR_RED)
     .click_on_element(Editor.LAYOUT_TAB)
     .send_key_and_click_by_offset(Editor.CURSOR, Keys.CONTROL, 160, 150)
     .click_on_element(LayoutTabLocators.GROUP)
     .click_on_element(LayoutTabLocators.GROUP_DO))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_GROUP, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.layout_tab
def test_doc_watermark(document_editor):
    (document_editor.click_on_element(Editor.LAYOUT_TAB)
     .click_on_element(LayoutTabLocators.WATERMARK)
     .click_on_element(LayoutTabLocators.WATERMARK_SET)
     .click_on_element(LayoutTabLocators.WATERMARK_TEXT)
     .click_on_element(LayoutTabLocators.WATERMARK_APPLY))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_WATERMARK, document_editor.CANVAS),'Скриншот не соответствует эталонному')