import pytest
import pytest_check as check

from selenium.webdriver.common.keys import Keys
from editors.document_editor import MainTabLocators, Samples
from resources.document import ExpectedImages
from utils import screenshot_comparsion


@pytest.mark.document
@pytest.mark.main_tab
def test_new_doc(document_editor):
    assert document_editor.find_element(MainTabLocators.BOLD_TEXT) is not None, 'Ошибка создания нового документа'


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_font(document_editor):
    (document_editor
     .send_keys_to_element(MainTabLocators.FONT_INPUT, Keys.BACKSPACE)
     .send_keys_to_element(MainTabLocators.FONT_INPUT, 'Asana')
     .send_keys_to_element(MainTabLocators.FONT_INPUT, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка шрифта Asana')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_FONT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_fontsize(document_editor):
    (document_editor
     .send_keys_to_element(MainTabLocators.FONTSIZE_INPUT, Keys.BACKSPACE)
     .send_keys_to_element(MainTabLocators.FONTSIZE_INPUT, '20')
     .send_keys_to_element(MainTabLocators.FONTSIZE_INPUT, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка 20-го размера шрифта')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_FONTSIZE, document_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_increase_fontsize(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.INCREASE_FONT, 3)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка увеличения размера текста')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INCREASE_FONTSIZE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_decrease_fontsize(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.DECREASE_FONT, 3)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка увеличения размера текста')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_DECREASE_FONTSIZE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_font_case(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка смены регистра текста')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER).send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(MainTabLocators.FONT_CASE)
     .click_on_element(MainTabLocators.FONT_CASE_OPTION)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.DOWN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_FONT_CASE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_bold_text(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.BOLD_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка жирного текста')
     .click_on_element(MainTabLocators.BOLD_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_BOLD_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_italic_text(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.ITALIC_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка курсива')
     .click_on_element(MainTabLocators.ITALIC_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ITALIC_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_underline_text(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.UNDERLINE_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка подчеркнутого текста')
     .click_on_element(MainTabLocators.UNDERLINE_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_UNDERLINE_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_strikeout_text(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.STRIKEOUT_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка зачеркнутого текста')
     .click_on_element(MainTabLocators.STRIKEOUT_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_STRIKEOUT_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_superscript_text(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'А')
     .click_on_element(MainTabLocators.SUPERSCRIPT_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка надстрочного текста')
     .click_on_element(MainTabLocators.SUPERSCRIPT_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_SUPERSCRIPT_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_subscript_text(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'А')
     .click_on_element(MainTabLocators.SUBSCRIPT_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка подстрочного текста')
     .click_on_element(MainTabLocators.SUBSCRIPT_TEXT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_SUBSCRIPT_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_highlight_text(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Текст с зеленым выделением')
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(MainTabLocators.HIGHLIGHT).
     click_on_element(MainTabLocators.HIGHLIGHT_COLOR_GREEN)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_HIGHLIGHT_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_color_text(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Красный текст')
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(MainTabLocators.FONT_COLOR)
     .click_on_element(MainTabLocators.FONT_COLOR_RED)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_COLOR_TEXT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_markers(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Маркированный список')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(MainTabLocators.MARKERS)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'один')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'два')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'три')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER, 2))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_MARKERS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_numbering(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Нумерованный список')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(MainTabLocators.NUMBERING)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'один')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'два')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'три')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER, 2))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_NUMBERING, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_multilevels(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Многоуровневый список')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(MainTabLocators.MULTILEVELS)
     .click_on_element(MainTabLocators.MULTILEVELS_OPTION)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'один')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'два')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'три')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER, 4))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_MULTILEVELS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_incoffset(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка увеличения отступов')
     .click_on_element(MainTabLocators.INCOFFSET, 2)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_INCOFFSET, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_decoffset(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка уменьшения отступов')
     .click_on_element(MainTabLocators.INCOFFSET, 3)
     .click_on_element(MainTabLocators.DECOFFSET, 2)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_DECOFFSET, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_linespace(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка междустрочного интервала')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Новая строка')
     .send_hotkey(Keys.CONTROL, 'ф')
     .click_on_element(MainTabLocators.LINESPACE)
     .click_on_element(MainTabLocators.LINESPACE_OPTION)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_LINESPACE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_align_left(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, Samples.LOREM_IPSUM)
     .click_on_element(MainTabLocators.ALIGN_LEFT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.LEFT)
     .click_on_element(MainTabLocators.ALIGN_LEFT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.RIGHT))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ALIGN_LEFT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_align_center(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, Samples.LOREM_IPSUM)
     .click_on_element(MainTabLocators.ALIGN_CENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ALIGN_CENTER, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_align_right(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, Samples.LOREM_IPSUM)
     .click_on_element(MainTabLocators.ALIGN_RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ALIGN_RIGHT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_align_just(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, Samples.LOREM_IPSUM)
     .click_on_element(MainTabLocators.ALIGN_JUST)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_ALIGN_JUST, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_hidenchars(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка непечатаемых символов')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER, 2)
     .click_on_element(MainTabLocators.HIDENCHARS))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_HIDENCHARS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_paracolor(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка заливки текста')
     .click_on_element(MainTabLocators.PARACOLOR)
     .click_on_element(MainTabLocators.PARACOLOR_INDIGO)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_PARACOLOR, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_clearstyle(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка очистки стиля')
     .click_on_element(MainTabLocators.PARACOLOR)
     .click_on_element(MainTabLocators.PARACOLOR_INDIGO)
     .click_on_element(MainTabLocators.CLEARSTYLE)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CLEARSTYLE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_colorschemas(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.COLORSCHEMAS)
     .click_on_element(MainTabLocators.COLORSCHEMAS_STREAM)
     .click_on_element(MainTabLocators.PARACOLOR))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_COLORSCHEMAS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_copystyle(document_editor):
    (document_editor
     .click_on_element(MainTabLocators.FONT_COLOR)
     .click_on_element(MainTabLocators.FONT_COLOR_RED)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка копирования стиля. Красный текст')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(MainTabLocators.CLEARSTYLE)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.PAGE_UP)
     .click_on_element(MainTabLocators.COPYSTYLE)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.PAGE_DOWN)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.LEFT)
     .click_on_element_coord(document_editor.CURSOR)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.END)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_COPYSTYLE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.main_tab
def test_doc_text_style(document_editor):
    (document_editor
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка смена стиля текста')
     .click_on_element(MainTabLocators.TEXT_STYLE)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_TEXT_STYLE, document_editor.CANVAS),'Скриншот не соответствует эталонному')
