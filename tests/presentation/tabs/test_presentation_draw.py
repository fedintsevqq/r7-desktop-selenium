import pytest
import pytest_check as check
from editors.presentation_editor import DrawTabLocators
from resources.presentation import ExpectedImages
from utils import screenshot_comparsion


@pytest.mark.presentation
@pytest.mark.draw_tab
def test_presentation_pen_green(presentation_editor):
    (presentation_editor.click_on_element(presentation_editor.DRAW_TAB)
    .click_on_element(DrawTabLocators.PEN_GREEN))
    element = (presentation_editor.find_element(DrawTabLocators.PEN_GREEN))

    (presentation_editor.action.move_to_element_with_offset(element, 300, 150)
     .click_and_hold().move_by_offset(0, 100).release()
     .click_and_hold().move_by_offset(100, 0).release()
     .click_and_hold().move_by_offset(0, -100).release()
     .click_and_hold().move_by_offset(-100, 0).release().perform())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_DRAW_PEN_GREEN, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.draw_tab
def test_presentation_pen_red(presentation_editor):
    (presentation_editor.click_on_element(presentation_editor.DRAW_TAB)
    .click_on_element(DrawTabLocators.PEN_RED))
    element = (presentation_editor.find_element(DrawTabLocators.PEN_GREEN))

    (presentation_editor.action.move_to_element_with_offset(element, 300, 150)
     .click_and_hold().move_by_offset(0, 100).release()
     .click_and_hold().move_by_offset(100, 0).release()
     .click_and_hold().move_by_offset(0, -100).release()
     .click_and_hold().move_by_offset(-100, 0).release().perform())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_DRAW_PEN_RED, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.draw_tab
def test_presentation_pen_yellow(presentation_editor):
    (presentation_editor.click_on_element(presentation_editor.DRAW_TAB)
    .click_on_element(DrawTabLocators.PEN_YELLOW))
    element = (presentation_editor.find_element(DrawTabLocators.PEN_GREEN))

    (presentation_editor.action.move_to_element_with_offset(element, 300, 150)
     .click_and_hold().move_by_offset(0, 100).release()
     .click_and_hold().move_by_offset(100, 0).release()
     .click_and_hold().move_by_offset(0, -100).release()
     .click_and_hold().move_by_offset(-100, 0).release().perform())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_DRAW_PEN_YELLOW, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.draw_tab
def test_presentation_eraser(presentation_editor):
    (presentation_editor.click_on_element(presentation_editor.DRAW_TAB)
    .click_on_element(DrawTabLocators.PEN_GREEN))
    element = (presentation_editor.find_element(DrawTabLocators.PEN_GREEN))

    (presentation_editor.action.move_to_element_with_offset(element, 300, 150)
     .click_and_hold().move_by_offset(0, 100).release()
     .click_and_hold().move_by_offset(100, 0).release()
     .click_and_hold().move_by_offset(0, -100).release()
     .click_and_hold().move_by_offset(-100, 0).release().perform())

    (presentation_editor.click_on_element(DrawTabLocators.ERASER)
     .action.move_to_element_with_offset(element, 400, 200).click().perform())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_DRAW_ERASER, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')


@pytest.mark.presentation
@pytest.mark.draw_tab
def test_presentation_select_tool(presentation_editor):
    (presentation_editor.click_on_element(presentation_editor.DRAW_TAB)
    .click_on_element(DrawTabLocators.PEN_GREEN))
    element = (presentation_editor.find_element(DrawTabLocators.PEN_GREEN))

    (presentation_editor.action.move_to_element_with_offset(element, 300, 150)
     .click_and_hold().move_by_offset(0, 100).release()
     .click_and_hold().move_by_offset(100, 50).release()
     .click_and_hold().move_by_offset(0, -100).release()
     .click_and_hold().move_by_offset(-100, -50).release().perform())

    (presentation_editor.click_on_element(DrawTabLocators.SELECT)
     .action.move_to_element_with_offset(element, 400, 200).click().perform())

    check.is_true(screenshot_comparsion.smart_canvas_comparison(
        presentation_editor, ExpectedImages.TEST_DRAW_SELECT_TOOL, presentation_editor.CANVAS), 'Скриншот не соответствует эталонному')
