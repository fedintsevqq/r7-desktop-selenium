import pytest
import pytest_check as check

from selenium.webdriver.common.keys import Keys
from editors.base_editor import Editor
from editors.document_editor import Samples, MainTabLocators, InsertTabLocators, LinksTabLocators
from resources.document import ExpectedImages
from utils import screenshot_comparsion


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_add_text(document_editor):
    (document_editor.click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL1)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 1\n')
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL2)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 2\n')
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL3)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 3\n'))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ADD_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_contents(document_editor):
    (document_editor.click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL1)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 1\n')
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL2)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 2\n')
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL3)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 3\n')
     .click_on_element(LinksTabLocators.CONTENTS))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CONTENTS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_contents_update(document_editor):
    (document_editor.click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL1)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 1\n')
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL2)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 2\n')
     .click_on_element(LinksTabLocators.CONTENTS)
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL3)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Заголовок 3\n')
     .click_on_element(LinksTabLocators.CONTENTS_UPDATE))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CONTENTS_UPDATE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_notes(document_editor):
    (document_editor.send_keys_to_element(Editor.TEXT_FIELD, 'Проверка работы сноски')
     .click_on_element(MainTabLocators.SUPERSCRIPT_TEXT)
     .click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.NOTES)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Это сноска\n\n'))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_NOTES, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_add_hyperlink_links(document_editor):
    (document_editor.send_keys_to_element(Editor.TEXT_FIELD, 'Текст для гиперссылки')
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.INSERT_HYPERLINK)
     .send_keys_to_element(InsertTabLocators.INSERT_HYPERLINK_INPUT, Samples.CAPYBARA_IMG)
     .click_on_element(InsertTabLocators.INSERT_HYPERLINK_APPLY)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.END)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_HYPERLINK_LINKS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_bookmarks(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_BLANK_PAGE)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Проверка работы закладки')
     .click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.BOOKMARKS)
     .send_keys_to_element(LinksTabLocators.BOOKMARKS_INPUT, 'Закладка')
     .click_on_element(LinksTabLocators.BOOKMARKS_ADD)
     .click_on_element(LinksTabLocators.BOOKMARKS_CLOSE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_UP)
     .click_on_element(LinksTabLocators.BOOKMARKS)
     .click_on_element(LinksTabLocators.BOOKMARKS_SELECT)
     .click_on_element(LinksTabLocators.BOOKMARKS_GOTO)
     .click_on_element(LinksTabLocators.BOOKMARKS_CLOSE)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_BOOKMARKS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_caption(document_editor):
    (document_editor.click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.CAPTION)
     .click_on_element(LinksTabLocators.CAPTION_APPLY)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CAPTION, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.links_tab
def test_doc_crossref(document_editor):
    (document_editor.click_on_element(Editor.INSERT_TAB)
     .click_on_element(InsertTabLocators.INSERT_BLANK_PAGE)
     .send_keys_to_element(Editor.TEXT_FIELD, 'Проверка работы перекрестной ссылкa')
     .click_on_element(Editor.LINKS_TAB)
     .click_on_element(LinksTabLocators.ADD_TEXT)
     .click_on_element(LinksTabLocators.ADD_TEXT_LVL1)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.PAGE_UP)
     .click_on_element(LinksTabLocators.CROSSREF)
     .click_on_element(LinksTabLocators.CROSSREF_INPUT)
     .click_on_element(LinksTabLocators.CROSSREF_HEADER)
     .click_on_element(LinksTabLocators.CROSSREF_INSERT)
     .click_on_element(LinksTabLocators.CROSSREF_CLOSE)
     .send_key_and_click_by_offset(Editor.CURSOR, Keys.CONTROL, -5, 0)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.END)
     .send_keys_to_element(Editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CROSSREF, document_editor.CANVAS),'Скриншот не соответствует эталонному')

# TODO: разобрать сценарий и сделать TOF и TOF update тесты
