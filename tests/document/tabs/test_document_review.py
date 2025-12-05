import pytest
import pytest_check as check

from selenium.webdriver.common.keys import Keys
from editors.document_editor import DocumentEditor, ReviewTabLocators, Samples
from utils import screenshot_comparsion
from resources.document import ExpectedImages
from utils.screenshot_comparsion import smart_canvas_comparison
import pytest_check as check


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_add_comment(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_REVIEW_ADD_COMMENT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_remove_comment(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.REMOVE_COMMENT_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_REVIEW_REMOVE_COMMENT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_remove_current_comments(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .send_hotkey(Keys.CONTROL, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Другой комментарий')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .send_hotkey(Keys.CONTROL, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Еще один комментарий')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.REMOVE_CURRENT_COMMENTS_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_REMOVE_CURRENT_COMMENTS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_remove_my_comments(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .send_hotkey(Keys.CONTROL, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Другой комментарий')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .send_hotkey(Keys.CONTROL, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Еще один комментарий')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.REMOVE_MY_COMMENTS_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_REMOVE_MY_COMMENTS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_remove_all_comments(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .send_hotkey(Keys.CONTROL, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Другой комментарий')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .send_hotkey(Keys.CONTROL, Keys.RIGHT)
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Еще один комментарий')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.REMOVE_ALL_COMMENTS_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_REMOVE_ALL_COMMENTS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_resolve_comment(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_BTN))

    element = document_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = document_editor.driver.execute_script("""
            const element = arguments[0];
            return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
        """, element)

    check.is_true(color_after_click != 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RESOLVE_COMMENT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_resolve_current_comments(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.RESOLVE_CURRENT_COMMENTS_LINK))

    element = document_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = document_editor.driver.execute_script("""
            const element = arguments[0];
            return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
        """, element)

    check.is_true(color_after_click != 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RESOLVE_CURRENT_COMMENTS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_resolve_my_comments(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.RESOLVE_MY_COMMENTS_LINK))

    element = document_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = document_editor.driver.execute_script("""
                const element = arguments[0];
                return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
            """, element)

    check.is_true(color_after_click != 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RESOLVE_MY_COMMENTS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_resolve_all_comments(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Добавление комментария')
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.RESOLVE_ALL_COMMENTS_LINK))

    element = document_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = document_editor.driver.execute_script("""
                    const element = arguments[0];
                    return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                """, element)

    check.is_true(color_after_click != 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_RESOLVE_ALL_COMMENTS, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_on(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка включения отслеживания изменений')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Отслеживание изменений включено'))

    button = document_editor.find_element(ReviewTabLocators.STATUSBAR_REVIEW_ON_BTN)
    class_list = button.get_attribute('class').split()

    check.is_true('active' in class_list, "Кнопка отслеживания изменений нижнего statusbar не включена")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_REVIEW_ON, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_review_for_me_on(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка включения отслеживания изменений ВКЛ. для меня')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ReviewTabLocators.REVIEW_ON_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.REVIEW_FOR_ME_ON_LINK)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Отслеживание изменений включено'))

    button = document_editor.find_element(ReviewTabLocators.STATUSBAR_REVIEW_ON_BTN)
    class_list = button.get_attribute('class').split()

    check.is_true('active' in class_list, "Кнопка отслеживания изменений нижнего statusbar не включена")
    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_REVIEW_FOR_ME_ON, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_view_source_doc(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка включения отображения исходного состояния')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это изменение исходного документа')
     .click_on_element(ReviewTabLocators.VIEW_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.VIEW_SOURCE_DOC_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_VIEW_SOURCE_DOC, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_change_accept(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка принятия изменения')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это изменение исходного документа')
     .click_on_element(ReviewTabLocators.CHANGE_ACCEPT_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CHANGE_ACCEPT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_current_change_accept(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка принятия текущего изменения')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это изменение исходного документа')
     .click_on_element(ReviewTabLocators.CHANGE_ACCEPT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.CURRENT_CHANGE_ACCEPT_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CURRENT_CHANGE_ACCEPT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_change_reject(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка отклонения изменения')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это изменение исходного документа')
     .click_on_element(ReviewTabLocators.CHANGE_REJECT_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CHANGE_REJECT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_current_change_reject(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Проверка отклонения текущего изменения')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это изменение исходного документа')
     .click_on_element(ReviewTabLocators.CHANGE_REJECT_DROPDOWN_MENU)
     .click_on_element_coord(ReviewTabLocators.CURRENT_CHANGE_REJECT_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_CURRENT_CHANGE_REJECT, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_move_to_previous_change(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это первое изменение')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это второе изменение')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это третье изменение')
     .click_on_element(ReviewTabLocators.MOVE_TO_PREVIOUS_CHANGE_BTN, 5))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_MOVE_TO_PREVIOUS_CHANGE, document_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.document
@pytest.mark.review_tab
def test_doc_move_to_next_change(document_editor):
    (document_editor.click_on_element(DocumentEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.REVIEW_ON_BTN)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это первое изменение')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это второе изменение')
     .send_keys_to_element(document_editor.TEXT_FIELD, Keys.ENTER)
     .send_keys_to_element(document_editor.TEXT_FIELD, 'Это третье изменение')
     .click_on_element(ReviewTabLocators.MOVE_TO_PREVIOUS_CHANGE_BTN, 5)
     .click_on_element(ReviewTabLocators.MOVE_TO_NEXT_CHANGE_BTN, 2))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        document_editor, ExpectedImages.TEST_DOC_MOVE_TO_NEXT_CHANGE, document_editor.CANVAS),'Скриншот не соответствует эталонному')
