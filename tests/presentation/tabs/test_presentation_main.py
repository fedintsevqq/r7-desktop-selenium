import pytest
import pytest_check as check
from selenium.webdriver.common.keys import Keys
from configs import config
from resources.presentation import ExpectedImages
from editors.presentation_editor import MainTabLocators, PresentationEditor, Samples
from utils import screenshot_comparsion


@pytest.mark.presentation
@pytest.mark.main_tab
def test_new_presentation(presentation_editor):
    result = presentation_editor.find_element(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN) is not None
    check.is_true(result, 'Ошибка создания новой презентации')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_font(presentation_editor):
    (presentation_editor
     .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .pause_in_test(config.general_pause)
     .send_keys_to_element(MainTabLocators.FONT_INPUT, Keys.BACKSPACE)
     .send_keys_to_element(MainTabLocators.FONT_INPUT, 'Asana')
     .send_keys_to_element(MainTabLocators.FONT_INPUT, Keys.ENTER)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка шрифта')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_FONT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_font_size(presentation_editor):
    (presentation_editor
     .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .send_keys_to_element(MainTabLocators.FONT_SIZE_INPUT, Keys.BACKSPACE, 2)
     .send_keys_to_element(MainTabLocators.FONT_SIZE_INPUT, '24')
     .send_keys_to_element(MainTabLocators.FONT_SIZE_INPUT, Keys.ENTER)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка 24 размера шрифта')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_FONT_SIZE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_increase_font_size(presentation_editor):
    (presentation_editor
     .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .click_on_element_coord(MainTabLocators.INCREASE_FONT, 3)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка увеличения размера текста')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INCREASE_FONT_SIZE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_decrease_font_size(presentation_editor):
    (presentation_editor
     .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .click_on_element_coord(MainTabLocators.DECREASE_FONT, 3)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка уменьшения размера текста')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_DECREASE_FONT_SIZE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_font_case(presentation_editor):
    (presentation_editor
     .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка смены регистра текста')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(PresentationEditor.SELECT_ALL)
     .click_on_element(MainTabLocators.FONT_CASE)
     .click_on_element(MainTabLocators.FONT_CASE_OPTION)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.DOWN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_FONT_CASE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_bold_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .click_on_element(MainTabLocators.BOLD_TEXT)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка жирного текста')
     .click_on_element(MainTabLocators.BOLD_TEXT)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_BOLD_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_italic_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .click_on_element(MainTabLocators.ITALIC_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка курсива')
    .click_on_element(MainTabLocators.ITALIC_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ITALIC_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_underline_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .click_on_element(MainTabLocators.UNDERLINE_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка подчеркнутого текста')
    .click_on_element(MainTabLocators.UNDERLINE_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_UNDERLINE_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_strikeout_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .click_on_element(MainTabLocators.STRIKEOUT_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка зачеркнутого текста')
    .click_on_element(MainTabLocators.STRIKEOUT_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_STRIKEOUT_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_superscript_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'А')
    .click_on_element(MainTabLocators.SUPERSCRIPT_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, ' Проверка надстрочного текста')
    .click_on_element(MainTabLocators.SUPERSCRIPT_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SUPERSCRIPT_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_subscript_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'А')
    .click_on_element(MainTabLocators.SUBSCRIPT_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, ' Проверка подстрочного текста')
    .click_on_element(MainTabLocators.SUBSCRIPT_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SUBSCRIPT_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_highlight_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Текст с зеленым выделением')
    .click_on_element(PresentationEditor.SELECT_ALL)
    .click_on_element(MainTabLocators.HIGHLIGHT)
    .click_on_element(MainTabLocators.HIGHLIGHT_COLOR_GREEN)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.RIGHT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_HIGHLIGHT_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_color_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Красный текст')
    .click_on_element(PresentationEditor.SELECT_ALL)
    .click_on_element(MainTabLocators.FONT_COLOR)
    .click_on_element(MainTabLocators.FONT_COLOR_RED)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.RIGHT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_COLOR_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_markers_on(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Маркированный список')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element(MainTabLocators.MARKERS)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'один')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'два')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_MARKERS_ON, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_numbering_on(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Нумерованный список')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element(MainTabLocators.NUMBERING)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'один')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'два')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_NUMBERING_ON, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_incoffset(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка увеличения отступов')
    .click_on_element(MainTabLocators.INCOFFSET, 3)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INCOFFSET, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_decoffset(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка уменьшения отступов')
    .click_on_element(MainTabLocators.INCOFFSET, 3)
    .click_on_element(MainTabLocators.DECOFFSET, 2)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_DECOFFSET, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_align_left(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Samples.WAR_AND_PEACE)
    .click_on_element(MainTabLocators.ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_LEFT_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ALIGN_LEFT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_align_center(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Samples.WAR_AND_PEACE)
    .click_on_element(MainTabLocators.ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_LEFT_LINK)
    .click_on_element(MainTabLocators.ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_CENTER_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ALIGN_CENTER, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_align_right(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Samples.WAR_AND_PEACE)
    .click_on_element(MainTabLocators.ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_RIGHT_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ALIGN_RIGHT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_align_just(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Samples.WAR_AND_PEACE)
    .click_on_element(MainTabLocators.ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_JUST_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ALIGN_JUST, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_linespace(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка междустрочного интервала')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Новая строка')
    .click_on_element(PresentationEditor.SELECT_ALL)
    .click_on_element(MainTabLocators.LINESPACE_BTN)
    .click_on_element(MainTabLocators.LINESPACE_OPTION)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.RIGHT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_LINESPACE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_align_top(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Выравнивание текста по верхнему краю')
    .click_on_element(MainTabLocators.VERTICAL_ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_BOTTOM_LINK)
    .click_on_element(MainTabLocators.VERTICAL_ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_TOP_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ALIGN_TOP, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_align_middle(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Выравнивание текста по центру')
    .click_on_element(MainTabLocators.VERTICAL_ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_MIDDLE_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ALIGN_MIDDLE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_align_bottom(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Выравнивание текста по нижнему краю')
    .click_on_element(MainTabLocators.VERTICAL_ALIGN_BTN)
    .click_on_element(MainTabLocators.ALIGN_BOTTOM_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ALIGN_BOTTOM, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_one_column_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Samples.WAR_AND_PEACE)
    .click_on_element(MainTabLocators.COLUMNS_BTN)
    .click_on_element(MainTabLocators.TWO_COLUMN_LINK)
    .click_on_element(MainTabLocators.COLUMNS_BTN)
    .click_on_element(MainTabLocators.ONE_COLUMN_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ONE_COLUMN_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_two_columns_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Samples.WAR_AND_PEACE)
    .click_on_element(MainTabLocators.COLUMNS_BTN)
    .click_on_element(MainTabLocators.TWO_COLUMN_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_TWO_COLUMNS_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_three_columns_text(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Samples.WAR_AND_PEACE)
    .click_on_element(MainTabLocators.COLUMNS_BTN)
    .click_on_element(MainTabLocators.THREE_COLUMN_LINK)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_THREE_COLUMNS_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_horizontal_text_by_btn(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN)
    .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 200)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Вставка горизонтальной надписи')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_HORIZONTAL_TEXT_BY_BTN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_horizontal_text_by_link(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.INSERT_TEXT_BTN)
    .click_on_element_coord(MainTabLocators.INSERT_HORIZONTAL_TEXT)
    .click_on_element_coord_with_offset(MainTabLocators.INSERT_TEXT_BTN, 0, 200)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Вставка горизонтальной надписи')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_HORIZONTAL_TEXT_BY_LINK, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_vertical_text_by_link(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.INSERT_TEXT_BTN)
    .click_on_element_coord(MainTabLocators.INSERT_VERTICAL_TEXT)
    .click_on_element_coord_with_offset(MainTabLocators.INSERT_TEXT_BTN, 0, 150)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Вставка вертикальной надписи')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_VERTICAL_TEXT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_insert_image_by_url(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.INSERT_IMAGE_BTN)
    .click_on_element_coord(MainTabLocators.INSERT_IMAGE_BY_URL)
    .send_keys_to_element(MainTabLocators.INSERT_IMAGE_INPUT_FIELD, MainTabLocators.IMAGE_LINK)
    .click_on_element(MainTabLocators.INSERT_IMAGE_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_IMAGE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_insert_rectangle(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.INSERT_SHAPE_BTN)
    .click_on_element_coord(MainTabLocators.INSERT_RECTANGLE)
    .drag_n_drop(MainTabLocators.INSERT_SHAPE_BTN, 200, 200, 0, 200))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_INSERT_RECTANGLE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_shape_arrange_back(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.INSERT_SHAPE_BTN)
    .click_on_element_coord(MainTabLocators.INSERT_RECTANGLE)
    .drag_n_drop(MainTabLocators.INSERT_SHAPE_BTN, 200, 200, 0, 200)
    .click_on_element(MainTabLocators.INSERT_SHAPE_BTN)
    .click_on_element_coord(MainTabLocators.INSERT_ELLIPSE)
    .drag_n_drop(MainTabLocators.INSERT_SHAPE_BTN, 200, 200, 100, 200)
    .click_on_element(MainTabLocators.SHAPE_ARRANGE_BTN)
    .click_on_element(MainTabLocators.SHAPE_ARRANGE_BACK_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHAPE_ARRANGE_BACK, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_shape_align_left(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.INSERT_SHAPE_BTN)
    .click_on_element_coord(MainTabLocators.INSERT_RECTANGLE)
    .drag_n_drop(MainTabLocators.INSERT_SHAPE_BTN, 200, 200, 0, 200)
    .click_on_element(MainTabLocators.SHAPE_ALIGN_BTN)
    .click_on_element_coord(MainTabLocators.SHAPE_ALIGN_LEFT_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SHAPE_ALIGN_LEFT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_clear_style(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Текст с зеленым выделением')
    .click_on_element(PresentationEditor.SELECT_ALL)
    .click_on_element(MainTabLocators.HIGHLIGHT)
    .click_on_element(MainTabLocators.HIGHLIGHT_COLOR_GREEN)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.RIGHT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.LEFT)
    .pause_in_test(config.general_pause))

    elem_cursor = presentation_editor.find_element(PresentationEditor.CURSOR)
    presentation_editor.action.double_click(elem_cursor).perform()
    (presentation_editor.click_on_element(MainTabLocators.CLEAR_STYLE)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.RIGHT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_CLEAR_STYLE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_copy_style(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .click_on_element(MainTabLocators.ITALIC_TEXT)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка копирования стиля. Курсив')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)

    .click_on_element(MainTabLocators.CLEAR_STYLE)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.UP)

    .click_on_element(MainTabLocators.COPY_STYLE)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.DOWN)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.LEFT)
    .click_on_element_coord(PresentationEditor.CURSOR)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.END)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_COPY_STYLE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_color_schemas(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка изменения цветовой схемы')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element(MainTabLocators.COLOR_SCHEMAS)
    .click_on_element(MainTabLocators.COLOR_SCHEMAS_STREAM)
    .click_on_element(MainTabLocators.FONT_COLOR))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_COLOR_SCHEMAS, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_slide_size(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка изменения размера слайда')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
    .click_on_element(MainTabLocators.SLIDE_SIZE)
    .click_on_element_coord(MainTabLocators.SLIDE_SIZE_STANDARD))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_SLIDE_SIZE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_style(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка установки темы презентации')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element_coord(MainTabLocators.SLIDE_STYLE_DROPDOWN_BTN)
     .click_on_element_coord(MainTabLocators.POINT_STYLE))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_POINT_STYLE, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_change_slide_layout(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка изменения макета презентации')
     .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(MainTabLocators.CHANGE_SLIDE_LAYOUT)
     .click_on_element(MainTabLocators.TWO_OBJECTS_SLIDE_LAYOUT))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_CHANGE_SLIDE_LAYOUT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_add_slide(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.ADD_SLIDE_BTN)
    .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка добавления слайда')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ADD_SLIDE_MAIN_FIELD, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ADD_SLIDE_LEFT_FIELD, presentation_editor.LEFT_CANVAS), 'Скриншот бокового поля не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_add_type_slide(presentation_editor):
    (presentation_editor.click_on_element(MainTabLocators.ADD_SLIDE_DROPDOWN_BTN)
    .click_on_element_coord(MainTabLocators.ADD_ONLY_HEADER_SLIDE)
    .click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Проверка добавления слайда со стилем')
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, Keys.ENTER))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ADD_TYPE_SLIDE_LEFT_FIELD, presentation_editor.LEFT_CANVAS), 'Скриншот бокового поля не соответствует эталонному')

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_ADD_TYPE_SLIDE_MAIN_FIELD, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.main_tab
def test_presentation_preview(presentation_editor):
    (presentation_editor.click_on_element_coord_with_offset(MainTabLocators.INSERT_HORIZONTAL_TEXT_BTN, 0, 450)
    .send_keys_to_element(PresentationEditor.TEXT_FIELD, 'Запуск просмотра презентации')
    .click_on_element(MainTabLocators.PREVIEW_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_PRESENTATION_PREVIEW, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')
