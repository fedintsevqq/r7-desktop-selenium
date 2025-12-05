import pytest
import pytest_check as check
from editors.presentation_editor import PresentationEditor, Samples, ReviewTabLocators, ViewTabLocators
from resources.presentation import ExpectedImages
from utils import screenshot_comparsion
from configs import config


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_add_comment(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .pause_in_test(config.general_pause))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_COMMENT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_remove_comment(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
         presentation_editor, ExpectedImages.TEST_REVIEW_ADD_COMMENT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    presentation_editor.click_on_element(ReviewTabLocators.REMOVE_COMMENT_BTN)

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_REMOVE_COMMENT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_remove_current_comments(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_THREE_COMMENTS, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')

    (presentation_editor
     .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_BTN)
     .click_on_element_coord(ReviewTabLocators.REMOVE_CURRENT_COMMENTS_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_REMOVE_CURRENT_COMMENTS, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_remove_my_comments(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_THREE_COMMENTS, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')

    (presentation_editor
     .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_BTN)
     .click_on_element_coord(ReviewTabLocators.REMOVE_MY_COMMENTS_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_REMOVE_MY_COMMENTS, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_remove_all_comments(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_THREE_COMMENTS, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')

    (presentation_editor
     .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_BTN)
     .click_on_element_coord(ReviewTabLocators.REMOVE_ALL_COMMENTS_LINK))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_REMOVE_ALL_COMMENTS, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_resolve_comment(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_COMMENT, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')

    presentation_editor.click_on_element(ReviewTabLocators.RESOLVE_COMMENT_BTN)

    element = presentation_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = presentation_editor.driver.execute_script("""
                        const element = arguments[0];
                        return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                    """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_RESOLVE_COMMENT, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_resolve_current_comments(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_COMMENT, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')

    (presentation_editor
    .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_BTN)
    .click_on_element_coord(ReviewTabLocators.RESOLVE_CURRENT_COMMENTS_LINK))

    element = presentation_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = presentation_editor.driver.execute_script("""
                            const element = arguments[0];
                            return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                        """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_RESOLVE_CURRENT_COMMENTS, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_resolve_my_comments(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_COMMENT, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')

    (presentation_editor
     .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_BTN)
     .click_on_element_coord(ReviewTabLocators.RESOLVE_MY_COMMENTS_LINK))

    element = presentation_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = presentation_editor.driver.execute_script("""
                                const element = arguments[0];
                                return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                            """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_RESOLVE_MY_COMMENTS, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_popover_resolve_all_comments(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_COMMENT, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')

    (presentation_editor
     .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_BTN)
     .click_on_element_coord(ReviewTabLocators.RESOLVE_ALL_COMMENTS_LINK))

    element = presentation_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = presentation_editor.driver.execute_script("""
                                   const element = arguments[0];
                                   return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                               """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_RESOLVE_ALL_COMMENTS, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.review_tab
def test_presentation_review_popover_resolve_comment(presentation_editor):
    (presentation_editor.click_on_element(PresentationEditor.REVIEW_TAB)
     .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
     .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
     .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN))

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_ADD_COMMENT, presentation_editor.CANVAS),'Скриншот не соответствует эталонному')

    (presentation_editor
     .click_on_element_coord(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
     .click_on_element(ViewTabLocators.LEFT_MENU_COMMENT_BTN))

    element = presentation_editor.find_element(ReviewTabLocators.POPOVER_RESOLVE_COMMENT_BTN)
    color_after_click = presentation_editor.driver.execute_script("""
                                       const element = arguments[0];
                                       return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                                   """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_REVIEW_POPOVER_RESOLVE_COMMENT, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')
