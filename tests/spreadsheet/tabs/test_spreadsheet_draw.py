import pytest
from editors.base_editor import Editor
from editors.spreadsheet_editor import DrawTabLocators, CommonLocators
from utils.screenshot_comparsion import smart_canvas_comparison
from resources.spreadsheet import ExpectedImages
import pytest_check as check


@pytest.mark.spreadsheet
@pytest.mark.draw_tab
def test_sp_select_tool(spreadsheet_editor):
    spreadsheet_editor.click_on_element(Editor.DRAW_TAB)
    spreadsheet_editor.click_on_element(DrawTabLocators.PEN_GREEN)
    spreadsheet_editor.click_on_element(DrawTabLocators.SELECT)
    spreadsheet_editor.click_on_element_coord(Editor.TEXT_FIELD)
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_SELECT_TOOL, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.draw_tab
def test_sp_pen_green(spreadsheet_editor):
    spreadsheet_editor.click_on_element(Editor.DRAW_TAB)
    spreadsheet_editor.click_on_element(DrawTabLocators.PEN_GREEN)
    element = spreadsheet_editor.find_element(CommonLocators.WORKSHEET_EDITOR_SDK)
    (
        spreadsheet_editor.action.move_to_element(element)
        .click_and_hold()
        .move_by_offset(0, 100)
        .release()
        .click_and_hold()
        .move_by_offset(100, 0)
        .release()
        .click_and_hold()
        .move_by_offset(0, -100)
        .release()
        .click_and_hold()
        .move_by_offset(-100, 0)
        .release()
        .perform()
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_PEN_GREEN, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.draw_tab
def test_sp_pen_red(spreadsheet_editor):
    spreadsheet_editor.click_on_element(Editor.DRAW_TAB)
    spreadsheet_editor.click_on_element(DrawTabLocators.PEN_RED)
    element = spreadsheet_editor.find_element(CommonLocators.WORKSHEET_EDITOR_SDK)
    (
        spreadsheet_editor.action.move_to_element(element)
        .click_and_hold()
        .move_by_offset(0, 100)
        .release()
        .click_and_hold()
        .move_by_offset(100, 0)
        .release()
        .click_and_hold()
        .move_by_offset(0, -100)
        .release()
        .click_and_hold()
        .move_by_offset(-100, 0)
        .release()
        .perform()
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_PEN_RED, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.draw_tab
def test_sp_pen_yellow(spreadsheet_editor):
    spreadsheet_editor.click_on_element(Editor.DRAW_TAB)
    spreadsheet_editor.click_on_element(DrawTabLocators.PEN_YELLOW)
    element = spreadsheet_editor.find_element(CommonLocators.WORKSHEET_EDITOR_SDK)
    (
        spreadsheet_editor.action.move_to_element(element)
        .click_and_hold()
        .move_by_offset(0, 100)
        .release()
        .click_and_hold()
        .move_by_offset(100, 0)
        .release()
        .click_and_hold()
        .move_by_offset(0, -100)
        .release()
        .click_and_hold()
        .move_by_offset(-100, 0)
        .release()
        .perform()
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_PEN_YELLOW, spreadsheet_editor.SP_CANVAS))


@pytest.mark.spreadsheet
@pytest.mark.draw_tab
def test_sp_eraser(spreadsheet_editor):
    spreadsheet_editor.click_on_element(Editor.DRAW_TAB)
    spreadsheet_editor.click_on_element(DrawTabLocators.PEN_GREEN)
    element = spreadsheet_editor.find_element(CommonLocators.WORKSHEET_EDITOR_SDK)

    (
        spreadsheet_editor.action.move_to_element(element)
        .click_and_hold()
        .move_by_offset(0, 100)
        .release()
        .click_and_hold()
        .move_by_offset(100, 0)
        .release()
        .click_and_hold()
        .move_by_offset(0, -100)
        .release()
        .click_and_hold()
        .move_by_offset(-100, 0)
        .release()
        .perform()
    )
    check.is_true(smart_canvas_comparison(spreadsheet_editor, ExpectedImages.TEST_SP_ERASER, spreadsheet_editor.SP_CANVAS))
