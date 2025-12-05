import pyperclip
import pytest
import datetime
import pytest_check as check

from configs import config
from selenium.webdriver.common.keys import Keys
from editors.base_editor import Editor
from editors.document_editor import Samples, InsertTabLocators, DocumentEditor
from resources.document import ExpectedImages
from utils import screenshot_comparsion


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_blank_page(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_BLANK_PAGE))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_BLANK_PAGE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_page_break(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_PAGE_BREAK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_PAGE_BREAK, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_table(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_TABLE)
     .click_on_element_coord_with_offset(InsertTabLocators.INSERT_TABLE, 100, 100)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_DOWN)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_TABLE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_image(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_IMAGE)
     .click_on_element(InsertTabLocators.INSERT_IMAGE_BY_URL)
     .send_keys_to_element(InsertTabLocators.INSERT_IMAGE_INPUT, Samples.IMAGE_LINK)
     .click_on_element(InsertTabLocators.INSERT_IMAGE_INPUT_OK)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_DOWN)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.RIGHT)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .pause_in_test())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_IMAGE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_chart(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_CHART)
     .click_on_element(InsertTabLocators.INSERT_CHART_HISTOGRAM)
     .click_on_element(InsertTabLocators.INSERT_CHART_APPLY)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_DOWN)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.RIGHT)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_CHART, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_shape(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
      .click_on_element(InsertTabLocators.INSERT_SHAPE)
      .click_on_element(InsertTabLocators.INSERT_SHAPE_RIGHT_ARROW)
      .drag_n_drop(Editor.CURSOR, 150, 150)
      .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_DOWN)
      .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
      .send_keys_to_element(Editor.TEXT_FIELD, Keys.UP))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_SHAPE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_smartart(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SMART_ART)
     .click_on_element(InsertTabLocators.INSERT_SMART_ART_LIST)
     .click_on_element(InsertTabLocators.INSERT_SMART_ART_ARC_LAYOUT)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_DOWN)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.RIGHT)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_SMARTART, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_add_comment(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Текст для комментария')
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(InsertTabLocators.ADD_COMMENT)
     .send_keys_to_element(InsertTabLocators.ADD_COMMENT_INPUT, 'Комментарий')
     .click_on_element(InsertTabLocators.ADD_COMMENT_APPLY)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.END)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER, 3))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ADD_COMMENT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_add_hyperlink(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Текст для гиперссылки')
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(InsertTabLocators.INSERT_HYPERLINK)
     .send_keys_to_element(InsertTabLocators.INSERT_HYPERLINK_INPUT, Samples.CAPYBARA_IMG)
     .click_on_element(InsertTabLocators.INSERT_HYPERLINK_APPLY)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.END)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ADD_HYPERLINK, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_edit_header(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.EDIT_HEADER)
     .click_on_element(InsertTabLocators.EDIT_HEADER_UPPER)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Верхний колонтитул')
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ESCAPE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_EDIT_HEADER, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_datetime(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_DATETIME)
     .click_on_element(InsertTabLocators.INSERT_DATETIME_APPLY)
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(DocumentEditor.COPY))
    clipboard = pyperclip.paste().rstrip()
    curr_date = datetime.datetime.now().strftime("%d.%m.%Y")

    check.is_true(clipboard == curr_date, 'Дата в редакторе не совпадает с текущей')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_text(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_TEXT)
     .drag_n_drop(Editor.CURSOR, 150, 150)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Это текстовое поле')
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ESCAPE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.UP))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_textart(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_TEXTART)
     .click_on_element(InsertTabLocators.INSERT_TEXTART_FIRST)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Это объект TextArt')
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ESCAPE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.UP))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_TEXTART, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_equation(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_EQUATION)
     .send_keys_to_element(Editor.TEXT_FIELD, 'x/y=1')
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_EQUATION, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_symbol(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_SYMBOL)
     .click_on_element(InsertTabLocators.INSERT_SYMBOL_INPUT)
     .send_keys_to_element(InsertTabLocators.INSERT_SYMBOL_INPUT, Keys.BACKSPACE, count=5))

    for char in Samples.AT_SYMBOL_CODE:
        document_editor.press_key(char)
    (document_editor.click_on_element(InsertTabLocators.INSERT_SYMBOL_INSERT)
     .click_on_element(InsertTabLocators.INSERT_SYMBOL_CLOSE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_SYMBOL, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_dropcap(document_editor):
    (document_editor.send_keys_to_element(Editor.TEXT_FIELD, Samples.LOREM_IPSUM)
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_DROPCAP)
     .click_on_element(InsertTabLocators.INSERT_DROPCAP_IN_TEXT)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_DOWN)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.END)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_DROPCAP, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.insert_tab
def test_doc_insert_controls(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_CONTROLS)
     .click_on_element(InsertTabLocators.INSERT_CONTROLS_SIMPLE_TEXT)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Это элемент управления содержимым')
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.HOME)
     .pause_in_test(config.general_pause)
     .click_on_element_coord_with_offset(Editor.CURSOR, -3, 3))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INSERT_CONTROLS, document_editor.CANVAS),'Скриншот не соответствует эталонному')

# TODO: сделать тест на вставку содержимого другого документа
