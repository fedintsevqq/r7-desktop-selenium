import pytest_check as check
import pytest
from selenium.webdriver.common.keys import Keys
from editors.spreadsheet_editor import SpreadsheetEditor, ReviewTabLocators, CommonLocators, Samples, ViewTabLocators
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_add_comment(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .pause_in_test()
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_ADD_COMMENT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_remove_comment(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .click_on_element(ReviewTabLocators.REMOVE_COMMENT_BTN)
        .pause_in_test()
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_REMOVE_COMMENT, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_remove_current_comments(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_MENU)
        .click_on_element_coord(ReviewTabLocators.REMOVE_CURRENT_COMMENTS_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_REMOVE_CURRENT_COMMENTS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_remove_my_comments(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_MENU)
        .click_on_element_coord(ReviewTabLocators.REMOVE_MY_COMMENTS_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_REMOVE_MY_COMMENTS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_remove_all_comments(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Другой комментарий')
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, 'Еще один комментарий')
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .send_keys_to_element(CommonLocators.WORKSHEET_TEXT_AREA, Keys.RIGHT)
        .click_on_element(ReviewTabLocators.REMOVE_COMMENT_DROPDOWN_MENU)
        .click_on_element_coord(ReviewTabLocators.REMOVE_ALL_COMMENTS_LINK)
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_REMOVE_ALL_COMMENTS, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_resolve_comment(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .click_on_element(ViewTabLocators.LEFT_MENU_COMMENT_BUTTON)
        .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_BTN)
        .pause_in_test()
    )

    element = spreadsheet_editor.find_element(ReviewTabLocators.LEFT_MENU_RESOLVE_COMMENT_BTN)
    color_after_click = spreadsheet_editor.driver.execute_script("""
                            const element = arguments[0];
                            return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                        """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_RESOLVE_COMMENT, spreadsheet_editor.LEFT_MENU))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_resolve_current_comments(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .click_on_element(ViewTabLocators.LEFT_MENU_COMMENT_BUTTON)
        .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_MENU)
        .click_on_element_coord(ReviewTabLocators.RESOLVE_CURRENT_COMMENTS_LINK)
        .pause_in_test()
    )

    element = spreadsheet_editor.find_element(ReviewTabLocators.LEFT_MENU_RESOLVE_COMMENT_BTN)
    color_after_click = spreadsheet_editor.driver.execute_script("""
                                const element = arguments[0];
                                return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                            """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_RESOLVE_CURRENT_COMMENTS, spreadsheet_editor.LEFT_MENU))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_resolve_my_comments(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .click_on_element(ViewTabLocators.LEFT_MENU_COMMENT_BUTTON)
        .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_MENU)
        .click_on_element_coord(ReviewTabLocators.RESOLVE_MY_COMMENTS_LINK)
        .pause_in_test()
    )

    element = spreadsheet_editor.find_element(ReviewTabLocators.LEFT_MENU_RESOLVE_COMMENT_BTN)
    color_after_click = spreadsheet_editor.driver.execute_script("""
                                const element = arguments[0];
                                return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                            """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_RESOLVE_MY_COMMENTS, spreadsheet_editor.LEFT_MENU))


@pytest.mark.spreadsheet
@pytest.mark.review_tab
def test_spreadsheet_review_resolve_all_comments(spreadsheet_editor):
    (
        spreadsheet_editor.click_on_element(SpreadsheetEditor.REVIEW_TAB)
        .click_on_element(ReviewTabLocators.ADD_COMMENT_BTN)
        .send_keys_to_element(ReviewTabLocators.ADD_COMMENT_FIELD, Samples.WAR_AND_PEACE)
        .click_on_element_coord(ReviewTabLocators.POPOVER_ADD_COMMENT_OK_BTN)
        .click_on_element(ViewTabLocators.LEFT_MENU_COMMENT_BUTTON)
        .click_on_element(ReviewTabLocators.RESOLVE_COMMENT_DROPDOWN_MENU)
        .click_on_element_coord(ReviewTabLocators.RESOLVE_ALL_COMMENTS_LINK)
        .pause_in_test()
    )

    element = spreadsheet_editor.find_element(ReviewTabLocators.LEFT_MENU_RESOLVE_COMMENT_BTN)
    color_after_click = spreadsheet_editor.driver.execute_script("""
                                const element = arguments[0];
                                return window.getComputedStyle(element, '::after').getPropertyValue('border-color');
                            """, element)
    check.is_false(color_after_click == 'rgb(132, 132, 132)', "Не изменился цвет галочки Решения комментария")
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SPREADSHEET_REVIEW_RESOLVE_ALL_COMMENTS, spreadsheet_editor.LEFT_MENU))
