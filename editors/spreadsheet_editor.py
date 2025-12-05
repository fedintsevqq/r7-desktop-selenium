from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from configs import config
from editors.base_editor import Editor
from configs import config


class SpreadsheetEditor(Editor):
    FORMULA_TAB = (By.XPATH, '//a[@data-tab="formula"]')
    DATA_TAB = (By.XPATH, '//a[@data-tab="data"]')
    PIVOT_TAB = (By.XPATH, '//a[@data-tab="pivot"]')
    CANVAS_PRINT_PREVIEW = (By.ID, 'print-preview')
    SP_CANVAS = (By.ID, 'ws-canvas')
    LEFT_MENU = (By.ID, 'left-menu')

    def new_spreadsheet(self):
        """Создание новой вкладки таблицы"""
        super().new_file(CommonLocators.NEW_SPREADSHEET)

    def click_on_element_with_offset_from_top_left(self, locator: WebElement | tuple[str, str], x, y, clicks=1, timeout=config.timeout):
        """Клик по элементу с отступом от верхнего левого угла"""
        element = locator
        if not isinstance(element, WebElement):
            element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        for click in range(clicks):
            self.action.move_to_element_with_offset(element, x - element.size['width'] / 2, y - element.size['height'] / 2).click().perform()
        return self

    def hold_key_down_and_press_key_count_times(self, key1: str, key2: str, count: int):
        """Держать нажатой клавишу (первый аргумент) и нажать несколько раз другую клавишу (второй аргумент)"""
        self.action.key_down(key1).perform()
        for i in range(count):
            self.action.key_down(key2).key_up(key2).perform()
        self.action.key_up(key1).perform()
        return self


class TopMenu:
    SAVE = (By.XPATH, '//*[@id="slot-btn-dt-save"]/button')
    PRINT = (By.XPATH, '//*[@id="slot-btn-dt-print"]/button')
    PRINT_QUICK = (By.XPATH, '//*[@id="slot-btn-dt-print-quick"]/button')
    UNDO = (By.XPATH, '//*[@id="slot-btn-dt-undo"]/button')
    REDO = (By.XPATH, '//*[@id="slot-btn-dt-redo"]/button')
    AUTOSAVE = (By.XPATH, '//*[@id="r7-slot-btn-dt-autosave"]/button')


class CommonLocators:
    NEW_SPREADSHEET = (By.XPATH, '//*[@id="placeholder"]/div[1]/div/li[2]/a')
    WORKSHEET_TEXT_AREA = (By.ID, 'area_id')
    WORKSHEET_MAIN_AREA = (By.ID, 'area_id_main')
    WORKSHEET_PARENT_AREA = (By.ID, 'area_id_parent')
    WORKSHEET_EDITOR_SDK = (By.ID, 'editor_sdk')
    CELL_ADDRESS_BAR_INPUT = (By.ID, 'ce-cell-name')
    CELL_ADDRESS_BAR_DROPDOWN = (By.XPATH, "//*[@id='ce-cell-name-menu']//button[contains(@class, 'dropdown-toggle')]")
    CELL_FORMULA_BAR_TEXTAREA = (By.ID, 'ce-cell-content')
    CELL_FORMULA_BAR_FUNCTION_BTN = (By.ID, 'ce-func-label')
    CELL_FORMULA_BAR_EXPAND_BTN = (By.ID, 'ce-btn-expand')


class MainTabLocators:
    FONT_NAME_SLOT = (By.ID, 'slot-field-font-name')
    FONT_NAME_INPUT = (By.XPATH, "//*[@id='slot-field-fontname']//input")
    FONT_NAME_DROPDOWN = (By.XPATH, "//*[@id='slot-field-fontname']//button[contains(@class, 'dropdown-toggle')]")
    FONT_NAME_DROPDOWN_OPEN_SANS = (By.XPATH, "//*[@id='slot-field-fontname']//ul[contains(@class, 'dropdown-menu')]/li[215]/a")
    FONT_NAME_DROPDOWN_ASANA = (By.XPATH, "//*[@id='slot-field-fontname']//ul[contains(@class, 'dropdown-menu')]/li[@class='divider']/following-sibling::li[7]")
    FONT_SIZE_INPUT = (By.XPATH, '//*[@id="slot-field-fontsize"]//input')
    INCREASE_FONT = (By.ID, 'id-toolbar-btn-incfont')
    DECREASE_FONT = (By.ID, 'id-toolbar-btn-decfont')
    CHANGE_FONT_CASE = (By.ID, 'id-toolbar-btn-case')
    CHANGE_FONT_CASE_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-changecase']//button[contains(@class, 'dropdown-toggle')]")
    CHANGE_FONT_CASE_UPPER_REGISTER = (By.XPATH, "//*[@id='slot-btn-changecase']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")

    BOLD_TEXT = (By.ID, 'id-toolbar-btn-bold')
    ITALIC_TEXT = (By.ID, 'id-toolbar-btn-italic')
    UNDERLINE_TEXT = (By.ID, 'id-toolbar-btn-underline')
    STRIKEOUT_TEXT = (By.ID, 'id-toolbar-btn-strikeout')
    SUBSCRIPT_TEXT = (By.ID, 'id-toolbar-btn-subscript')
    SUBSCRIPT_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-subscript']//button[contains(@class, 'dropdown-toggle')]")
    SUBSCRIPT_DROPDOWN_SUPERSCRIPT = (By.XPATH, "//*[@id='slot-btn-subscript']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    FONT_COLOR = (By.ID, 'slot-btn-fontcolor')
    FONT_COLOR_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-fontcolor']//button[contains(@class, 'dropdown-toggle')]")
    FONT_COLOR_DROPDOWN_RED = (By.XPATH, "//*[@id='slot-btn-fontcolor']//a[contains(@class, 'color-FF0000')]")
    HIGHLIGHT = (By.XPATH, "//*[@id='id-toolbar-btn-fillparag']/button")
    HIGHLIGHT_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-fillparag']//button[contains(@class, 'dropdown-toggle')]")
    HIGHLIGHT_DROPDOWN_COLOR_GREEN = (By.XPATH, "//*[@id='slot-btn-fillparag']//a[contains(@class, 'color-92D050')]")
    BORDERS = (By.ID, 'id-toolbar-btn-borders')
    BORDERS_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-borders']//button[contains(@class, 'dropdown-toggle')]")
    BORDERS_DROPDOWN_ALL_BORDERS = (By.XPATH, "//*[@id='slot-btn-borders']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")

    ALIGN_TOP = (By.ID, 'slot-btn-top')
    ALIGN_MIDDLE = (By.ID, 'slot-btn-middle')
    ALIGN_BOTTOM = (By.ID, 'slot-btn-bottom')
    ALIGN_LEFT = (By.ID, 'slot-btn-align-left')
    ALIGN_CENTER = (By.ID, 'slot-btn-align-center')
    ALIGN_RIGHT = (By.ID, 'slot-btn-align-right')
    ALIGN_JUST = (By.ID, 'slot-btn-align-just')

    HYPHENATION = (By.ID, 'slot-btn-wrap')
    TEXT_ORIENT = (By.ID, 'slot-btn-text-orient')
    TEXT_ORIENT_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-text-orient']//button[contains(@class, 'dropdown-toggle')]")
    TEXT_ORIENT_VERTICAL = (By.XPATH, "//*[@id='slot-btn-text-orient']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")
    MERGE_CELLS = (By.ID, 'slot-btn-merge')
    MERGE_CELLS_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-merge']//button[contains(@class, 'dropdown-toggle')]")
    MERGE_CELLS_MERGE_AND_CENTER_PLACE = (By.XPATH, "//*[@id='slot-btn-merge']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    MERGE_CELLS_CANCEL_MERGE = (By.XPATH, "//*[@id='slot-btn-merge']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")

    SUM_INSERT = (By.ID, 'slot-btn-formula')
    SUM_INSERT_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-formula']//button[contains(@class, 'dropdown-toggle')]")
    SUM_INSERT_SUM = (By.XPATH, "//*[@id='slot-btn-formula']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")

    NAMED_RANGE = (By.ID, 'slot-btn-named-range')
    NAMED_RANGE_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-named-range']//button[contains(@class, 'dropdown-toggle')]")
    NAMED_RANGE_DROPDOWN_ADD_NAME = (By.XPATH, "//*[@id='slot-btn-named-range']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    NAMED_RANGE_DROPDOWN_DISPATHER = (By.XPATH, "//*[@id='slot-btn-named-range']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    NAMED_RANGE_ADD_NAME_MODAL_NAME_INPUT = (By.XPATH, "//*[@id='named-range-txt-name']//input")
    NAMED_RANGE_ADD_NAME_MODAL_OK_BTN = (By.XPATH, "//*[@class='asc-window modal advanced-settings-dlg notransform']//button[@result='ok']")
    NAMED_RANGE_DISPATHER_MODAL_CANCEL_BTN = (By.XPATH, "//*[@id='window-name-manager']//button[@result='cancel']")

    SORT_DES = (By.XPATH, '//*[@id="id-toolbar-toolbar__icon btn-sort-down0"]')
    SORT_ASC = (By.XPATH, '//*[@id="id-toolbar-toolbar__icon btn-sort-up0"]')

    FILTER_INSERT_AUTO = (By.XPATH, '//*[@id="id-toolbar-toolbar__icon btn-autofilter0"]')
    FILTER_MODAL_SEARCH_INPUT = (By.XPATH, "//*[@id='id-sd-cell-search']//input")
    FILTER_MODAL_OK_BTN = (By.XPATH, "//*[@id='id-apply-filter']/button")
    FILTER_CLEAR = (By.XPATH, '//*[@id="id-toolbar-toolbar__icon btn-clear-filter0"]')

    DATA_FORMAT = (By.ID, 'slot-btn-format')
    DATA_FORMAT_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-format']//button[contains(@class, 'dropdown-toggle')]")
    DATA_FORMAT_DROPDOWN_NUMERIC = (By.XPATH, "//*[@id='slot-btn-format']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")

    DATA_FORMAT_PERCENTS = (By.ID, 'slot-btn-percents')
    DATA_FORMAT_CURRENCY = (By.ID, 'slot-btn-currency')
    DATA_FORMAT_CURRENCY_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-currency']//button[contains(@class, 'dropdown-toggle')]")
    DATA_FORMAT_CURRENCY_DROPDOWN_RUBLE = (By.XPATH, "//*[@id='slot-btn-currency']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")
    DATA_FORMAT_DIGIT_DEC = (By.ID, 'slot-btn-digit-dec')
    DATA_FORMAT_DIGIT_INC = (By.ID, 'slot-btn-digit-inc')

    INSERT_CELL = (By.ID, 'slot-btn-cell-ins')
    INSERT_CELL_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-cell-ins']//button[contains(@class, 'dropdown-toggle')]")
    INSERT_CELL_DROPDOWN_WITH_MOVE_RIGHT = (By.XPATH, "//*[@id='slot-btn-cell-ins']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    DELETE_CELL = (By.ID, 'slot-btn-cell-del')
    DELETE_CELL_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-cell-del']//button[contains(@class, 'dropdown-toggle')]")
    DELETE_CELL_DROPDOWN_WITH_MOVE_LEFT = (By.XPATH, "//*[@id='slot-btn-cell-del']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")

    CLEAR_STYLE = (By.ID, 'id-toolbar-btn-clear')
    CLEAR_STYLE_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-clear']//button[contains(@class, 'dropdown-toggle')]")
    CLEAR_STYLE_DROPDOWN_ALL = (By.XPATH, "//*[@id='slot-btn-clear']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    CLEAR_STYLE_DROPDOWN_FORMATING = (By.XPATH, "//*[@id='slot-btn-clear']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")
    CONDITION_FORMAT = (By.ID, 'slot-btn-condformat')
    CONDITION_FORMAT_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-condformat']//button[contains(@class, 'dropdown-toggle')]")
    CONDITION_FORMAT_DROPDOWN_EQUAL = (By.XPATH, "//*[@id='slot-btn-condformat']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    CONDITION_FORMAT_DROPDOWN_EQUAL_GRATE_OR_EQUAL = (By.XPATH, "//*[@id='slot-btn-condformat']//ul[contains(@class, 'dropdown-menu')]/li[1]/ul/li[2]/a")
    CONDITION_FORMAT_MODAL_VALUE_INPUT = (By.ID, 'range-input-field')
    CONDITION_FORMAT_MODAL_OK_BTN = (By.XPATH, "//*[@id='window-format-rules']//button[@result='ok']")

    COPY_STYLE = (By.ID, 'id-toolbar-btn-copystyle')
    TEMPLATE_TABLE = (By.ID, 'slot-btn-table-tpl')
    TEMPLATE_TABLE_DROPDOWN = (By.XPATH, "//*[@id='slot-btn-table-tpl']//button[contains(@class, 'dropdown-toggle')]")
    TEMPLATE_TABLE_DROPDOWN_LIGHT14 = (
        By.XPATH,
        "//*[@id='slot-btn-table-tpl']//*[@id='menu-table-group-light']/div[contains(@class, 'group-items-container')]/div[14]",
    )
    TEMPLATE_TABLE_MODAL_RANGE_INPUT = (By.XPATH, "//*[@id='id-dlg-tableoptions-range']//input")
    TEMPLATE_TABLE_MODAL_OK_BTN = (By.XPATH, "//*[@class='asc-window modal-dlg notransform']//button[@result='ok']")

    # Форматирование ячеек: хороший, плохой и т.п.
    FIELD_STYLES_NORMAL = (By.XPATH, "//*[@id='slot-field-styles']//div[@class='dataview inner field-picker canfocused']/div[1]")
    FIELD_STYLES_NEUTRAL = (By.XPATH, "//*[@id='slot-field-styles']//div[@class='dataview inner field-picker canfocused']/div[2]")
    FIELD_STYLES_DROPDOWN = (By.XPATH, "//*[@id='slot-field-styles']//button[contains(@class, 'dropdown-toggle')]")
    FIELD_STYLES_DROPDOWN_BAD = (By.XPATH, "//*[@id='menu-style-group-color']//div[@class='group-items-container']/div[3]")
    FIELD_STYLES_DROPDOWN_GOOD = (By.XPATH, "//*[@id='menu-style-group-color']//div[@class='group-items-container']/div[4]")


class InsertTabLocators:
    PIVOT_TABLE_BTN = (By.ID, 'id-toolbar-toolbar__icon btn-pivot-sum0')
    PIVOT_TABLE_MODAL_SOURCE_RANGE_INPUT = (By.XPATH, '//*[@id="create-pivot-input-source"]//input')
    PIVOT_TABLE_MODAL_EXIST_SHEET_RADIO_SPAN = (By.XPATH, '//*[@id="create-pivot-radio-exist"]//span')
    PIVOT_TABLE_MODAL_EXIST_SHEET_DEST_RANGE_INPUT = (By.XPATH, '//*[@id="create-pivot-input-dest"]//input')
    PIVOT_TABLE_MODAL_OK_BTN = (By.XPATH, '//*[@id="window-create-pivot"]//button[@result="ok"]')
    PIVOT_TABLE_RIGHT_MENU_BTN = (By.ID, 'id-right-menu-pivot')
    PIVOT_TABLE_LIST_FIELDS_CHK_LABEL = (By.XPATH, '//*[@id="pivot-list-fields"]//label[@class="checkbox__shape"]')

    INSERT_TABLE_BTN = (By.ID, 'slot-btn-instable')
    INSERT_TABLE_MODAL_INPUT = (By.XPATH, '//*[@id="id-dlg-tableoptions-range"]//input[@name="range"]')
    INSERT_TABLE_MODAL_TITLE_LABEL = (By.ID, 'id-dlg-tableoptions-title')
    INSERT_TABLE_MODAL_OK_BTN = (By.XPATH, '//div[@class="asc-window modal-dlg notransform"]//button[@result="ok"]')

    INSERT_IMAGE_BTN = (By.ID, 'slot-btn-insimage')
    INSERT_IMAGE_DROPDOWN_IMAGE_URL = (By.XPATH, '//*[@id="slot-btn-insimage"]//li[2]')
    INSERT_IMAGE_MODAL_INPUT_URL = (By.XPATH, '//*[@id="id-dlg-url"]//input')
    INSERT_IMAGE_MODAL_OK_BTN = (By.XPATH, '//div[@class="asc-window modal modal-dlg notransform"]//button[@result="ok"]')

    INSERT_SHAPE_BTN = (By.ID, 'slot-btn-insshape')
    INSERT_SHAPE_DROPDOWN_ARROW_RIGHT = (By.XPATH, '//*[@id="id-toolbar-menu-insertshape"]//div[@class="grouped-data  "][2]//div[@data-index=0]')

    INSERT_HORIZONTAL_TEXT_BTN = (By.ID, 'slot-btn-instext')
    INSERT_TEXT_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-instext']//button[contains(@class, 'dropdown-toggle')]")
    INSERT_TEXT_DROPDOWN_VERTICAL_TEXT = (By.XPATH, '//*[@id="slot-btn-instext"]//ul[@class="dropdown-menu "]/li[2]/a')

    INSERT_TEXT_ART_BTN = (By.ID, 'slot-btn-instextart')
    INSERT_TEXT_ART_DROPDOWN_FIRST_TEXT_ART = (By.XPATH, '//*[@id="id-toolbar-menu-insart"]//div[@class="item-art"]')

    INSERT_CHART_BTN = (By.ID, 'slot-btn-inschart')
    INSERT_CHART_DROPDOWN_CHART_COLUMN_NORMAL = (By.XPATH, '//*[@id="menu-chart-group-bar"]//div[@class="item"]')

    INSERT_SPARKLINE_BTN = (By.ID, 'slot-btn-inssparkline')
    INSERT_SPARKLINE_DROPDOWN_CHART_SPARK_COLUMN = (By.XPATH, '//*[@id="id-toolbar-menu-insertspark"]//div[@class="item"][1]')
    INSERT_SPARKLINE_DROPDOWN_CHART_SPARK_LINE = (By.XPATH, '//*[@id="id-toolbar-menu-insertspark"]//div[@class="item"][2]')
    INSERT_SPARKLINE_DROPDOWN_CHART_SPARK_WIN = (By.XPATH, '//*[@id="id-toolbar-menu-insertspark"]//div[@class="item"][3]')
    INSERT_SPARKLINE_MODAL_RANGE_INPUT = (By.ID, 'range-input-field')
    INSERT_SPARKLINE_MODAL_DEST_INPUT = (By.XPATH, '//*[@id="create-spark-input-dest"]//input')
    INSERT_SPARKLINE_MODAL_OK_BTN = (By.XPATH, "//*[@class='asc-window modal advanced-settings-dlg notransform']//button[@result='ok']")

    INSERT_SMART_ART_BTN = (By.ID, 'slot-btn-inssmartart')
    INSERT_SMART_ART_DROPDOWN_LIST_SUBMENU_BTN = (By.XPATH, '//*[@id="slot-btn-inssmartart"]//li[@class="dropdown-submenu"]/a')
    INSERT_SMART_ART_DROPDOWN_LIST_SUBMENU_ARC_MODEL = (By.XPATH, '//*[@id="menu-smart-art-group-list"]//div[@class="item"]')

    ADD_COMMENT_BTN = (By.ID, 'tlbtn-addcomment-0')
    ADD_COMMENT_POPOVER_TEXTAREA = (By.XPATH, '//*[@id="id-popover"]//textarea')
    ADD_COMMENT_POPOVER_ADD_BTN = (By.XPATH, '//*[@id="id-popover"]//button[@id="id-comments-change-popover"]')

    INSERT_HYPERLINK_BTN = (By.ID, 'slot-btn-inshyperlink')
    INSERT_HYPERLINK_MODAL_URL_INPUT = (By.ID, 'id-dlg-hyperlink-url-input')
    INSERT_HYPERLINK_MODAL_DISPLAY_INPUT = (By.ID, 'id-dlg-hyperlink-display-input')
    INSERT_HYPERLINK_MODAL_TIP_INPUT = (By.ID, 'id-dlg-hyperlink-tip-input')
    INSERT_HYPERLINK_MODAL_OK_BTN = (By.XPATH, '//*[@id="window-hyperlink"]//button[@result="ok"]')

    INSERT_HF_BTN = (By.ID, 'tlbtn-editheader-0')
    INSERT_HF_MODAL_HEADER_PRESET_BTN = (By.ID, 'id-dlg-h-presets')
    INSERT_HF_MODAL_HEADER_PRESET_DROPDOWN_PAGE_1_OF = (By.XPATH, '//*[@id="id-dlg-h-presets"]//ul/li[3]')
    INSERT_HF_MODAL_HEADER_INSERT_BTN = (By.ID, 'id-dlg-h-insert')
    INSERT_HF_MODAL_HEADER_INSERT_DROPDOWN_LIST_NAME = (By.XPATH, '//*[@id="id-dlg-h-insert"]//ul/li[6]')
    INSERT_HF_MODAL_FOOTER_PRESET_BTN = (By.ID, 'id-dlg-f-presets')
    INSERT_HF_MODAL_FOOTER_PRESET_DROPDOWN_PAGE_1_OF = (By.XPATH, '//*[@id="id-dlg-f-presets"]//ul/li[3]')
    INSERT_HF_MODAL_FOOTER_INSERT_BTN = (By.ID, 'id-dlg-f-insert')
    INSERT_HF_MODAL_FOOTER_INSERT_DROPDOWN_LIST_NAME = (By.XPATH, '//*[@id="id-dlg-f-insert"]//ul/li[6]')
    INSERT_HF_MODAL_OK_BTN = (By.XPATH, '//*[@id="window-header-footer"]//button[@result="ok"]')

    INSERT_EQUATION_BTN = (By.ID, 'slot-btn-insequation')
    INSERT_EQUATION_CONTAINER_EQUATION_6 = (By.ID, 'id-document-holder-btn-equation-6')
    INSERT_EQUATION_CONTAINER_EQUATION_6_DROPDOWN_ROUND_BRACKETS = (By.XPATH, '//*[@id="id-document-holder-btn-equation-6"]//div[@class="item"][1]')

    INSERT_SYMBOL_BTN = (By.ID, 'slot-btn-inssymbol')
    INSERT_SYMBOL_MODAL_EXCL_MARK = (By.XPATH, '//*[@id="id-preview-data"]//div[@class="cell"][1]')
    INSERT_SYMBOL_MODAL_OK_BTN = (By.XPATH, '//div[@class="asc-window modal modal-dlg notransform"]//button[@result="ok"]')
    INSERT_SYMBOL_MODAL_CLOSE_BTN = (By.XPATH, '//div[@class="asc-window modal modal-dlg notransform"]//button[@result="close"]')

    INSERT_SLICERS_BTN = (By.ID, 'slot-btn-insslicer')
    INSERT_SLICERS_MODAL_CHKBX_LABEL = (By.XPATH, '//*[@id="add-slicers-dlg-columns"]//label/label')
    INSERT_SLICERS_MODAL_OK_BTN = (By.XPATH, '//div[@class="asc-window modal modal-dlg notransform"]//button[@result="ok"]')


class DrawTabLocators:
    SELECT = (By.ID, 'slot-btn-draw-select')
    PEN_GREEN = (By.ID, 'slot-btn-draw-pen-0')
    PEN_RED = (By.ID, 'slot-btn-draw-pen-1')
    PEN_YELLOW = (By.ID, 'slot-btn-draw-pen-2')
    ERASER = (By.ID, 'slot-btn-draw-eraser')


class LayoutTabLocators:
    PAGE_MARGINS_BTN = (By.ID, 'slot-btn-pagemargins')
    PAGE_MARGINS_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-pagemargins']//button[contains(@class, 'dropdown-toggle')]")
    PAGE_MARGINS_DROPDOWN_NARROW = (By.XPATH, "//*[@id='slot-btn-pagemargins']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")

    PAGE_ORIENT_BTN = (By.ID, 'slot-btn-pageorient')
    PAGE_ORIENT_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-pageorient']//button[contains(@class, 'dropdown-toggle')]")
    PAGE_ORIENT_DROPDOWN_PORTRAIT = (By.XPATH, "//*[@id='slot-btn-pageorient']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    PAGE_ORIENT_DROPDOWN_LANDSCAPE = (By.XPATH, "//*[@id='slot-btn-pageorient']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")

    PAGE_SIZE_BTN = (By.ID, 'slot-btn-pagesize')
    PAGE_SIZE_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-pagesize']//button[contains(@class, 'dropdown-toggle')]")
    PAGE_SIZE_DROPDOWN_A4 = (By.XPATH, "//*[@id='slot-btn-pagesize']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")
    PAGE_SIZE_DROPDOWN_A5 = (By.XPATH, "//*[@id='slot-btn-pagesize']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")
    PAGE_SIZE_DROPDOWN_A3 = (By.XPATH, "//*[@id='slot-btn-pagesize']//ul[contains(@class, 'dropdown-menu')]/li[9]/a")

    PAGE_PRINT_AREA_BTN = (By.ID, 'slot-btn-printarea')
    PAGE_PRINT_AREA_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-printarea']//button[contains(@class, 'dropdown-toggle')]")
    PAGE_PRINT_AREA_DROPDOWN_SET_PRINT_AREA = (By.XPATH, "//*[@id='slot-btn-printarea']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    PAGE_PRINT_AREA_DROPDOWN_REMOVE_PRINT_AREA = (By.XPATH, "//*[@id='slot-btn-printarea']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")

    PAGE_BREAKS_BTN = (By.ID, 'slot-btn-pagebreaks')
    PAGE_BREAKS_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//button[contains(@class, 'dropdown-toggle')]")
    PAGE_BREAKS_DROPDOWN_INSERT_BREAK = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    PAGE_BREAKS_DROPDOWN_REMOVE_BREAK = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    PAGE_BREAKS_DROPDOWN_REMOVE_ALL_BREAKS = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")

    LAYOUT_HF_BTN = (By.ID, 'tlbtn-editheader-1')
    # Локаторы для модального окна вставки колонтитулов из класса InsertTabLocators

    PAGE_SCALE_BTN = (By.ID, 'slot-btn-scale')
    PAGE_SCALE_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//button[contains(@class, 'dropdown-toggle')]")
    PAGE_SCALE_DROPDOWN_WIDTH = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    PAGE_SCALE_DROPDOWN_WIDTH_SUBMENU_AUTO = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[1]//li[1]/a")
    PAGE_SCALE_DROPDOWN_WIDTH_SUBMENU_2_PAGES = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[1]//li[3")
    PAGE_SCALE_DROPDOWN_HEIGHT = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    PAGE_SCALE_DROPDOWN_HEIGHT_SUBMENU_AUTO = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[2]//li[1]/a")
    PAGE_SCALE_DROPDOWN_HEIGHT_SUBMENU_2_PAGES = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[2]//li[3]/a")
    PAGE_SCALE_DROPDOWN_CUSTOM_UP_BTN = (By.XPATH, "//*[@id='id-toolbar-scale-updownpicker']//button[1]")
    PAGE_SCALE_DROPDOWN_CUSTOM_DOWN_BTN = (By.XPATH, "//*[@id='id-toolbar-scale-updownpicker']//button[2]")
    PAGE_SCALE_DROPDOWN_SPECIAL = (By.XPATH, "//*[@id='slot-btn-pagebreaks']//ul[contains(@class, 'dropdown-menu')]/li[5]/a")

    PAGE_PRINT_TITLES_BTN = (By.ID, 'slot-btn-printtitles')
    PAGE_PRINT_MODAL_TOP_RANGE_INPUT = (By.XPATH, '//*[@id="window-page-margins"]//input[1]')
    # не работает, предположительно из-за одинаковых ид с первым инпутом
    # PAGE_PRINT_MODAL_LEFT_RANGE_INPUT = (By.XPATH, '//*[@id="window-page-margins"]//input[2]')
    PAGE_PRINT_MODAL_OK_BTN = (By.XPATH, '//*[@id="window-page-margins"]//button[@result="ok"]')

    PAGE_PRINT_GRID_LINES_CHK = (By.ID, 'slot-chk-print-gridlines')
    PAGE_PRINT_HEADINGS_CHK = (By.ID, 'slot-chk-print-headings')

    SHAPE_PANEL_COLOR_FILL_DROPDOWN_BTN = (By.XPATH, '//*[@id="shape-panel-color-fill"]//button')
    SHAPE_PANEL_COLOR_FILL_DROPDOWN_RED_FILL_COLOR = (By.XPATH, '//*[@id="shape-panel-color-fill"]//a[@class="palette-color color-FF0000"]')
    SHAPE_PANEL_COLOR_FILL_DROPDOWN_BLUE_GREEN_ACCENT_3_FILL_COLOR = (
        By.XPATH,
        '//*[@id="shape-panel-color-fill"]//a[@class="palette-color-effect color-0BD0D9"]',
    )

    MOVE_IMG_FWD_BTN = (By.ID, 'slot-img-movefrwd')
    MOVE_IMG_BWD_BTN = (By.ID, 'slot-img-movebkwd')

    ALIGN_IMG_BTN = (By.ID, 'slot-img-align')
    ALIGN_IMG_DROPDOWN_ALIGN_CENTER = (By.XPATH, '//*[@id="slot-img-align"]//ul[contains(@class, "dropdown-menu")]/li[2]/a')
    ALIGN_IMG_DROPDOWN_ALIGN_MIDDLE = (By.XPATH, '//*[@id="slot-img-align"]//ul[contains(@class, "dropdown-menu")]/li[5]/a')

    GROUP_IMG_BTN = (By.ID, 'slot-img-group')
    GROUP_IMG_DROPDOWN_GROUP = (By.XPATH, '//*[@id="slot-img-group"]//ul[contains(@class, "dropdown-menu")]/li[1]/a')
    GROUP_IMG_DROPDOWN_UNGROUP = (By.XPATH, '//*[@id="slot-img-group"]//ul[contains(@class, "dropdown-menu")]/li[2]/a')

    COLOR_SCHEMAS_BTN = (By.ID, 'slot-btn-colorschemas')
    COLOR_SCHEMAS_DROPDOWN_TORRENT = (By.XPATH, '//*[@id="slot-btn-colorschemas"]//ul[contains(@class, "dropdown-menu")]/li[9]/a')


class FormulaTabLocators:
    FORMULA_INSERT_MODAL_SEARCH_INPUT = (By.XPATH, '//*[@id="formula-dlg-search"]//input')
    FORMULA_INSERT_MODAL_OK_BTN = (By.XPATH, '//*[@class="asc-window modal formula-dlg notransform"]//button[@result="ok"]')

    FORMULA_WIZARD_MODAL_ARGUMENT_1_INPUT = (By.XPATH, '//*[@id="formula-wizard-txt-arg0"]//input')
    FORMULA_WIZARD_MODAL_ARGUMENT_2_INPUT = (By.XPATH, '//*[@id="formula-wizard-txt-arg1"]//input')
    FORMULA_WIZARD_MODAL_ARGUMENT_3_INPUT = (By.XPATH, '//*[@id="formula-wizard-txt-arg2"]//input')
    FORMULA_WIZARD_MODAL_OK_BTN = (By.XPATH, '//*[@class="asc-window modal advanced-settings-dlg notransform"]//button[@result="ok"]')

    ADDITIONAL_FORMULA_BTN = (By.ID, 'slot-btn-additional-formula')

    AUTO_SUM_FORMULA_BTN = (By.ID, 'slot-btn-autosum')
    AUTO_SUM_FORMULA_DROPDOWN_BTN = (By.XPATH, "//*[@id='slot-btn-autosum']//button[contains(@class, 'dropdown-toggle')]")
    AUTO_SUM_FORMULA_DROPDOWN_AVERAGE = (By.XPATH, '//*[@id="slot-btn-autosum"]//ul[contains(@class, "dropdown-menu")]/li[2]/a')

    RECENT_FORMULA_BTN = (By.ID, 'slot-btn-recent')
    RECENT_FORMULA_DROPDOWN_SUM = (By.XPATH, '//*[@id="slot-btn-recent"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "СУММ"]')

    FINANCIAL_FORMULA_BTN = (By.ID, 'slot-btn-financial')
    FINANCIAL_FORMULA_DROPDOWN_APL = (By.XPATH, '//*[@id="slot-btn-financial"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "АПЛ"]')

    LOGICAL_FORMULA_BTN = (By.ID, 'slot-btn-logical')
    LOGICAL_FORMULA_DROPDOWN_IF = (By.XPATH, '//*[@id="slot-btn-logical"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "ЕСЛИ"]')

    TEXT_FORMULA_BTN = (By.ID, 'slot-btn-text')
    TEXT_FORMULA_DROPDOWN_UNICODE = (By.XPATH, '//*[@id="slot-btn-text"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "UNICODE"]')

    DATE_TIME_FORMULA_BTN = (By.ID, 'slot-btn-datetime')
    DATE_TIME_FORMULA_DROPDOWN_DATE = (By.XPATH, '//*[@id="slot-btn-datetime"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "ДАТА"]')

    LOOKUP_FORMULA_BTN = (By.ID, 'slot-btn-lookup')
    LOOKUP_FORMULA_DROPDOWN_DVSSYL = (By.XPATH, '//*[@id="slot-btn-lookup"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "ДВССЫЛ"]')

    MATH_FORMULA_BTN = (By.ID, 'slot-btn-math')
    MATH_FORMULA_DROPDOWN_COS = (By.XPATH, '//*[@id="slot-btn-math"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "COS"]')

    MORE_FORMULA_BTN = (By.ID, 'slot-btn-more')
    MORE_FORMULA_DROPDOWN_ENGINEERING = (By.XPATH, '//*[@id="slot-btn-more"]//ul[contains(@class, "dropdown-menu")]/li[@class="dropdown-submenu"][2]/a')
    MORE_FORMULA_DROPDOWN_ENGINEERING_SUBMENU_BESSELI = (
        By.XPATH,
        '//*[@id="id-toolbar-formula-menu-Engineering"]//ul[contains(@class, "dropdown-menu")]//a[normalize-space(text()) = "БЕССЕЛЬ.I"]',
    )

    NAMED_RANGE_HUGE_BTN = (By.ID, 'slot-btn-named-range-huge')
    NAMED_RANGE_HUGE_DROPDOWN_ADD_NAME = (By.XPATH, "//*[@id='slot-btn-named-range-huge']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    NAMED_RANGE_HUGE_DROPDOWN_DISPATHER = (By.XPATH, "//*[@id='slot-btn-named-range-huge']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    # Локаторы модального окна взяты из класса MinaTabLocators

    WATCH_WINDOW_BTN = (By.ID, 'slot-btn-watch-window')
    WATCH_WINDOW_MODAL_ADD_CONTROL_VALUE_BTN = (By.ID, 'watch-dialog-btn-add')
    WATCH_WINDOW_MODAL_CLOSE_BTN = (By.XPATH, '//*[@class="asc-window advanced-settings-dlg notransform"]//buton[@result="cancel"]')
    WATCH_WINDOW_SUBMODAL_RANGE_INPUT = (By.ID, 'id-dlg-cell-range')
    WATCH_WINDOW_SUBMODAL_OK_BTN = (By.XPATH, '//div[@class="asc-window modal-dlg notransform"]//button[@result="ok"]')

    CALCULATE_FORMULAS_BTN = (By.ID, 'slot-btn-calculate')
    CALCULATE_FORMULAS_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-calculate"]//button[contains(@class, "dropdown-toggle")]')
    CALCULATE_FORMULAS_DROPDOWN_CALCULATE_BOOK = (By.XPATH, "//*[@id='slot-btn-calculate']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    CALCULATE_FORMULAS_DROPDOWN_CALCULATE_CURRENT_SHEET = (By.XPATH, "//*[@id='slot-btn-calculate']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")

    FORMULA_INFLUENCING_CELLS_BTN = (By.ID, 'slot-btn-trace-prec')
    FORMULA_DEPENDENT_CELLS_BTN = (By.ID, 'slot-btn-trace-dep')
    REMOVE_ARROWS_BTN = (By.ID, 'slot-btn-remove-arrows')
    REMOVE_ARROWS_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-remove-arrows"]//button[contains(@class, "dropdown-toggle")]')
    REMOVE_ARROWS_DROPDOWN_TO_INFLUENCING_CELLS = (By.XPATH, "//*[@id='slot-btn-remove-arrows']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    REMOVE_ARROWS_DROPDOWN_TO_DEPENDENT_CELLS = (By.XPATH, "//*[@id='slot-btn-remove-arrows']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    SHOW_FORMULAS_BTN = (By.ID, 'slot-btn-show-formulas')


class DataTabLocators:
    RECEIVE_DATA_FROM_TEXT_BTN = (By.ID, 'slot-btn-data-from-text')
    EXTERNAL_LINKS_BTN = (By.ID, 'slot-btn-data-external-links')

    GOAL_SEEK_BTN = (By.ID, 'slot-btn-goal-seek')
    GOAL_SEEK_MODAL_DEFINE_CELL_INPUT = (By.XPATH, '//*[@id="goal-seek-cell-with-formula"]//input')
    GOAL_SEEK_MODAL_EXPECTED_RESULT_INPUT = (By.XPATH, '//*[@id="goal-seek-expected-result"]//input')
    GOAL_SEEK_MODAL_VARIABLE_CELL_INPUT = (By.XPATH, '//*[@id="goal-seek-cell-for-change"]//input')
    GOAL_SEEK_MODAL_OK_BTN = (By.XPATH, '//*[@id="window-goal-seek"]//button[@result="ok"]')

    DATA_TABLE_BTN = (By.ID, 'slot-btn-data-table')
    DATA_TABLE_MODAL_VAR_ROW_INPUT = (By.ID, 'row-cell-input-field')
    DATA_TABLE_MODAL_VAR_COL_INPUT = (By.ID, 'col-cell-input-field')
    DATA_TABLE_MODAL_OK_BTN = (By.XPATH, '//*[@id="window-data-table-popup"]//button[@result="ok"]')

    ADD_AUTO_FILTER_BTN = (By.ID, 'id-toolbar-toolbar__icon btn-autofilter1')
    # Локаторы модального окна фильтра взяты из классы MainTabLocators
    CLEAR_FILTER_BTN = (By.ID, 'id-toolbar-toolbar__icon btn-clear-filter1')
    SORT_DESCENDING_BTN = (By.ID, 'id-toolbar-toolbar__icon btn-sort-down1')
    SORT_ASCENDING_BTN = (By.ID, 'id-toolbar-toolbar__icon btn-sort-up1')

    CUSTOM_SORT_BTN = (By.ID, 'slot-btn-custom-sort')

    TEXT_TO_COLUMN_BTN = (By.ID, 'slot-btn-text-column')
    REMOVE_DUPLICATES_BTN = (By.ID, 'slot-btn-rem-duplicates')

    DATA_VALIDATION_BTN = (By.ID, 'slot-btn-data-validation')
    DATA_VALIDATION_MODAL_CMB_ALLOW_DROPDOWN_BTN = (By.XPATH, '//*[@id="data-validation-cmb-allow"]//button')
    DATA_VALIDATION_MODAL_CMB_ALLOW_DROPDOWN_INTEGER = (By.XPATH, '//*[@id="data-validation-cmb-allow"]//ul[contains(@class, "dropdown-menu")]/li[2]/a')
    DATA_VALIDATION_MODAL_CMB_DATA_DROPDOWN_BTN = (By.XPATH, '//*[@id="data-validation-cmb-data"]//button')
    DATA_VALIDATION_MODAL_CMB_DATA_DROPDOWN_EQUAL = (By.XPATH, '//*[@id="data-validation-cmb-data"]//ul[contains(@class, "dropdown-menu")]/li[3]/a')
    DATA_VALIDATION_MODAL_TEXT_SOURCE_INPUT = (By.XPATH, '//*[@id="data-validation-txt-source"]//input')
    DATA_VALIDATION_MODAL_OK_BTN = (By.XPATH, '//*[@class="asc-window modal advanced-settings-dlg notransform"]//button[@result="ok"]')

    GROUP_BTN = (By.ID, 'slot-btn-group')
    GROUP_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-group"]//button[contains(@class, "dropdown-toggle")]')
    GROUP_DROPDOWN_GROUP_ROWS = (By.XPATH, "//*[@id='slot-btn-group']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    GROUP_DROPDOWN_GROUP_COLS = (By.XPATH, "//*[@id='slot-btn-group']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    GROUP_DROPDOWN_RESULT_IN_ROWS_CHK = (By.XPATH, "//*[@id='slot-btn-group']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")
    GROUP_DROPDOWN_RESULT_IN_COLS_CHK = (By.XPATH, "//*[@id='slot-btn-group']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")

    UNGROUP_BTN = (By.ID, 'slot-btn-ungroup')
    UNGROUP_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-ungroup"]//button[contains(@class, "dropdown-toggle")]')
    UNGROUP_DROPDOWN_UNGROUP_ROWS = (By.XPATH, "//*[@id='slot-btn-ungroup']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    UNGROUP_DROPDOWN_UNGROUP_COLS = (By.XPATH, "//*[@id='slot-btn-ungroup']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    UNGROUP_DROPDOWN_UNGROUP_ALL_STRUCTURE = (By.XPATH, "//*[@id='slot-btn-ungroup']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")


class PivotTableTabLocators:
    INSERT_PIVOT_TABLE_BTN = (By.XPATH, '//*[@id="pivot-table-panel"]//*[@id="id-toolbar-toolbar__icon btn-pivot-sum0"]')

    REPORT_LAYOUT_BTN = (By.ID, 'slot-btn-pivot-report-layout')
    REPORT_LAYOUT_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-pivot-report-layout"]//button[contains(@class, "dropdown-toggle")]')
    REPORT_LAYOUT_DROPDOWN_SHOW_IN_SHORT_FORM = (By.XPATH, "//*[@id='slot-btn-pivot-report-layout']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    REPORT_LAYOUT_DROPDOWN_SHOW_IN_STRUCTURE_FORM = (By.XPATH, "//*[@id='slot-btn-pivot-report-layout']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    REPORT_LAYOUT_DROPDOWN_SHOW_IN_TABLE_FORM = (By.XPATH, "//*[@id='slot-btn-pivot-report-layout']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")
    REPORT_LAYOUT_DROPDOWN_REPEAT_ALL_ELEMENT_MARKS = (By.XPATH, "//*[@id='slot-btn-pivot-report-layout']//ul[contains(@class, 'dropdown-menu')]/li[5]/a")
    REPORT_LAYOUT_DROPDOWN_DONT_REPEAT_ALL_ELEMENT_MARKS = (By.XPATH, "//*[@id='slot-btn-pivot-report-layout']//ul[contains(@class, 'dropdown-menu')]/li[6]/a")

    BLANK_ROWS_BNT = (By.ID, 'slot-btn-pivot-blank-rows')
    BLANK_ROWS_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-pivot-blank-rows"]//button[contains(@class, "dropdown-toggle")]')
    BLANK_ROWS_DROPDOWN_INSERT_BLANK_ROW_AFTER_EACH_ELEMENT = (By.XPATH, "//*[@id='slot-btn-pivot-blank-rows']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    BLANK_ROWS_DROPDOWN_REMOVE_BLANK_ROW_AFTER_EACH_ELEMENT = (By.XPATH, "//*[@id='slot-btn-pivot-blank-rows']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")

    SUBTOTALS_BNT = (By.ID, 'slot-btn-pivot-subtotals')
    SUBTOTALS_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-pivot-subtotals"]//button[contains(@class, "dropdown-toggle")]')
    SUBTOTALS_DROPDOWN_DONT_SHOW_SUBTOTALS = (By.XPATH, "//*[@id='slot-btn-pivot-subtotals']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    SUBTOTALS_DROPDOWN_SHOW_ALL_SUBTOTALS_IN_FOOTER = (By.XPATH, "//*[@id='slot-btn-pivot-subtotals']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    SUBTOTALS_DROPDOWN_SHOW_ALL_SUBTOTALS_IN_HEADER = (By.XPATH, "//*[@id='slot-btn-pivot-subtotals']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")

    GRAND_TOTALS_BTN = (By.ID, 'slot-btn-pivot-grand-totals')
    GRAND_TOTALS_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-pivot-grand-totals"]//button[contains(@class, "dropdown-toggle")]')
    GRAND_TOTALS_DROPDOWN_OFF_FOR_ROWS_AND_COLS = (By.XPATH, "//*[@id='slot-btn-pivot-grand-totals']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    GRAND_TOTALS_DROPDOWN_ON_FOR_ROWS_AND_COLS = (By.XPATH, "//*[@id='slot-btn-pivot-grand-totals']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    GRAND_TOTALS_DROPDOWN_ON_FOR_ROWS = (By.XPATH, "//*[@id='slot-btn-pivot-grand-totals']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")
    GRAND_TOTALS_DROPDOWN_ON_FOR_COLS = (By.XPATH, "//*[@id='slot-btn-pivot-grand-totals']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")

    REFRESH_PIVOT_BTN = (By.ID, 'slot-btn-refresh-pivot')
    REFRESH_PIVOT_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-refresh-pivot"]//button[contains(@class, "dropdown-toggle")]')
    REFRESH_PIVOT_DROPDOWN_REFRESH = (By.XPATH, "//*[@id='slot-btn-refresh-pivot']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    REFRESH_PIVOT_DROPDOWN_REFRESH_ALL = (By.XPATH, "//*[@id='slot-btn-refresh-pivot']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")

    PIVOT_CHART_BTN = (By.ID, 'slot-btn-pivot-chart')
    PIVOT_CHART_DROPDOWN_CHART_COLUMN_NORMAL = (By.XPATH, '//*[@id="menu-chart-group-bar"]//div[@class="item"]')
    PIVOT_TABLE_LIST_FIELDS_DROPDOWN = (By.XPATH, '//*[@id="pivot-list-fields"]//div[@class="listitem-icon img-commonctrl"]')
    PIVOT_TABLE_LIST_FIELDS_DROPDOWN_ADD_TO_VALUE = (By.XPATH, "//*[@id='menu-pivot-fields-container']//ul[contains(@class, 'dropdown-menu')]/li[4]/a")

    SELECT_ALL_PIVOT_TABLE_BTN = (By.ID, 'slot-btn-select-pivot')

    CALC_FIELD_BTN = (By.ID, 'slot-btn-calc-field')
    CALC_FIELD_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-btn-calc-field"]//button[contains(@class, "dropdown-toggle")]')
    CALC_FIELD_DROPDOWN_CALC_FIELD = (By.XPATH, "//*[@id='slot-btn-calc-field']//ul[contains(@class, 'dropdown-menu')]/li[1]/a")
    CALC_FIELD_DROPDOWN_CALC_OBJECT = (By.XPATH, "//*[@id='slot-btn-calc-field']//ul[contains(@class, 'dropdown-menu')]/li[2]/a")
    CALC_FIELD_DROPDOWN_SHOW_FORMULAS = (By.XPATH, "//*[@id='slot-btn-calc-field']//ul[contains(@class, 'dropdown-menu')]/li[3]/a")
    CALC_FIELD_MODAL_NAME_INPUT = (By.XPATH, '//*[@id="pcf-name"]//input')
    CALC_FIELD_MODAL_FORMULA_INPUT = (By.XPATH, '//*[@id="pcf-formula"]//input')
    CALC_FIELD_MODAL_FIELDS = (By.XPATH, '//*[@id="pcf-fields"]//div[contains(@class, "item")]')
    CALC_FIELD_MODAL_INSERT_FIELD_BTN = (By.XPATH, '//button[@id="pcf-insert-field"]')
    CALC_FIELD_MODAL_ADD_FIELD_BTN = (By.XPATH, '//button[@id="pcf-add"]')
    CALC_FIELD_MODAL_DELETE_FIELD_BTN = (By.XPATH, '//button[@id="pcf-delete"]')
    CALC_FIELD_MODAL_OK_BTN = (By.XPATH, '//div[@class="asc-window modal modal-dlg notransform"]//button[@result="ok"]')

    HEADER_ROW_CHK = (By.ID, 'slot-chk-header-row')
    HEADER_COL_CHK = (By.ID, 'slot-chk-header-column')
    BANDED_ROW_CHK = (By.ID, 'slot-chk-banded-row')
    BANDED_COL_CHK = (By.ID, 'slot-chk-banded-column')

    STYLE_PIVOT_TABLE_DROPDOWN_BTN = (By.XPATH, '//*[@id="slot-field-pivot-styles"]//button[contains(@class, "dropdown-toggle")]')
    STYLE_PIVOT_TABLE_DROPDOWN_LIGHT_8 = (By.XPATH, "//*[@id='slot-field-pivot-styles']//ul[contains(@class, 'dropdown-menu')]//div[@class='item'][8]")


class ReviewTabLocators:
    """
    Сокращения в названиях:
    BTN - button (кнопка)
    CBX - checkbox (чекбокс)
    """

    ADD_COMMENT_BTN = (By.ID, 'tlbtn-addcomment-1')
    ADD_COMMENT_FIELD = (By.CSS_SELECTOR, '#id-popover .inner-edit-ct textarea')
    POPOVER_EDIT_COMMENT_BTN = (By.CSS_SELECTOR, '#id-popover .edit-ct div:nth-of-type(1)')
    POPOVER_REMOVE_COMMENT_BTN = (By.CSS_SELECTOR, '#id-popover .edit-ct div:nth-of-type(2)')
    POPOVER_RESOLVE_COMMENT_BTN = (By.CSS_SELECTOR, '#id-popover .edit-ct div:nth-of-type(3)')
    POPOVER_ADD_REPLY = (By.CSS_SELECTOR, '#id-comments-popover label')
    POPOVER_ADD_REPLY_FIELD = (By.CSS_SELECTOR, '#id-comments-popover textarea')
    POPOVER_ADD_COMMENT_OK_BTN = (By.ID, 'id-comments-change-popover')
    LEFT_MENU_ADD_COMMENT_FIELD = (By.CSS_SELECTOR, '#left-panel-comments .inner-edit-ct textarea')
    LEFT_MENU_ADD_REPLY = (By.CSS_SELECTOR, '#left-panel-comments .user-reply')
    LEFT_MENU_ADD_REPLY_FIELD = (By.CSS_SELECTOR, '#left-panel-comments .reply-ct textarea')
    LEFT_MENU_ADD_COMMENT_BTN = (By.CSS_SELECTOR, '#left-panel-comments .reply-ct button')
    LEFT_MENU_EDIT_COMMENT_BTN = (By.CSS_SELECTOR, '#left-panel-comments .edit-ct div:nth-of-type(1)')
    LEFT_MENU_REMOVE_COMMENT_BTN = (By.CSS_SELECTOR, '#left-panel-comments .edit-ct div:nth-of-type(2)')
    LEFT_MENU_RESOLVE_COMMENT_BTN = (By.CSS_SELECTOR, '#left-panel-comments .edit-ct div:nth-of-type(3)')
    LEFT_MENU_ADD_COMMENT_OK_BTN = (By.ID, 'id-comments-change')
    REMOVE_COMMENT_BTN = (By.CSS_SELECTOR, '#slot-comment-remove button:nth-of-type(1)')
    REMOVE_COMMENT_DROPDOWN_MENU = (By.CSS_SELECTOR, '#slot-comment-remove [data-toggle="dropdown"]')
    REMOVE_CURRENT_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-remove"]//a[contains(text(), "Удалить текущие")]')
    REMOVE_MY_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-remove"]//a[contains(text(), "Удалить мои")]')
    REMOVE_ALL_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-remove"]//a[contains(text(), "Удалить все")]')

    RESOLVE_COMMENT_BTN = (By.CSS_SELECTOR, '#slot-comment-resolve button:nth-of-type(1)')
    RESOLVE_COMMENT_DROPDOWN_MENU = (By.CSS_SELECTOR, '#slot-comment-resolve [data-toggle="dropdown"]')
    RESOLVE_CURRENT_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-resolve"]//a[contains(text(), "Решить текущие")]')
    RESOLVE_MY_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-resolve"]//a[contains(text(), "Решить мои")]')
    RESOLVE_ALL_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-resolve"]//a[contains(text(), "Решить все")]')


class ViewTabLocators:
    """
    Сокращения в названиях:
    BTN - button (кнопка)
    CBX - checkbox (чекбокс)
    """

    SHEET_VIEW_BTN = (By.CSS_SELECTOR, '#slot-btn-sheet-view button')
    VIEW_MANAGER_LINK = (By.XPATH, '//span[@id="slot-btn-sheet-view"]//a[contains(text(), "Диспетчер")]')
    NEW_VIEW_MANAGER_BTN = (By.ID, 'view-manager-btn-new')
    GO_TO_VIEW_MANAGER_BTN = (By.XPATH, '//button[contains(text(), "Перейти к представлению")]')
    RENAME_VIEW_MANAGER_BTN = (By.ID, 'view-manager-btn-rename')
    RENAME_VIEW_MANAGER_FIELD = (By.CSS_SELECTOR, '#id-dlg-label-caption input')
    RENAME_VIEW_MANAGER_OK_BTN = (By.XPATH, '//button[contains(text(), "OK")]')
    RENAME_VIEW_MANAGER_CANCEL_BTN = (By.XPATH, '//button[contains(text(), "OK")]//following-sibling::button')
    NEW_VIEW_BTN = (By.ID, 'id-toolbar-btn-createview')
    CLOSE_VIEW_BTN = (By.ID, 'id-toolbar-btn-closeview')

    VIEW_PAGE_BRAKE_BTN = (By.CSS_SELECTOR, '#slot-btn-view-pagebreak button')
    VIEW_PAGE_LAYOUT_BTN = (By.CSS_SELECTOR, '#slot-btn-page-layout button')
    VIEW_PAGE_NORMAL_BTN = (By.CSS_SELECTOR, '#slot-btn-view-normal button')

    INPUT_ZOOM_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-field-zoom button')
    INPUT_ZOOM_FIELD = (By.CSS_SELECTOR, '#slot-field-zoom input')
    ZOOM_150_LINK = (By.XPATH, '//span[@id="slot-field-zoom"]//a[contains(text(), "150")]')
    INTERFACE_THEME_DROPDOWN_MENU = (By.CSS_SELECTOR, '#slot-btn-interface-theme button')
    SYSTEM_INTERFACE_LINK = (By.XPATH, '//span[@id="slot-btn-interface-theme"]//a[contains(text(), "Системная")]')
    CONTRAST_DARK_INTERFACE_LINK = (By.XPATH, '//span[@id="slot-btn-interface-theme"]//a[contains(text(), "Контрастная")]')

    FREEZE_FIELD_BTN = (By.CSS_SELECTOR, '#slot-btn-freeze button')
    FREEZE_AREA_LINK = (By.XPATH, '//span[@id="slot-btn-freeze"]//a[contains(text(), "области")]')
    FREEZE_ROW_LINK = (By.XPATH, '//span[@id="slot-btn-freeze"]//a[contains(text(), "строку")]')
    FREEZE_COLUMN_LINK = (By.XPATH, '//span[@id="slot-btn-freeze"]//a[contains(text(), "столбец")]')
    REMOVE_FREEZE_LINK = (By.XPATH, '//span[@id="slot-btn-freeze"]//a[contains(text(), "Снять закрепление")]')
    SHOW_SHADOW_LINK = (By.XPATH, '//span[@id="slot-btn-freeze"]//a[contains(text(), "Показывать")]')

    FORMULA_FIELD_CBX = (By.CSS_SELECTOR, '#slot-chk-formula label>label')
    FORMULA_FIELD_CHECK = (By.CSS_SELECTOR, '#slot-chk-formula label>input')
    FORMULA_FIELD_BTN = (By.CSS_SELECTOR, '#ce-cell-name-menu button')
    HEADING_CBX = (By.CSS_SELECTOR, '#slot-chk-heading label>label')
    HEADING_CHECK = (By.CSS_SELECTOR, '#slot-chk-heading label>input')
    GRID_LINES_CBX = (By.CSS_SELECTOR, '#slot-chk-gridlines label>label')
    GRID_LINES_CHECK = (By.CSS_SELECTOR, '#slot-chk-gridlines label>input')
    ZEROS_CBX = (By.CSS_SELECTOR, '#slot-chk-zeros label>label')
    ZEROS_CHECK = (By.CSS_SELECTOR, '#slot-chk-zeros label>input')
    RULERS_CBX = (By.CSS_SELECTOR, '#slot-chk-ruler label')
    RULERS_CHECK = (By.CSS_SELECTOR, '#slot-chk-ruler input')

    TOOLBAR_CBX = (By.XPATH, '//span[@id="slot-chk-toolbar"]//span[contains(text(), "Всегда показывать")]/preceding-sibling::label')
    TOOLBAR_CHECK = (By.XPATH, '//span[@id="slot-chk-toolbar"]//span[contains(text(), "Всегда показывать")]/preceding-sibling::input')
    TOOLBAR_SECTION = (By.CLASS_NAME, 'box-controls')
    STATUSBAR_CBX = (By.XPATH, '//span[@id="slot-chk-statusbar"]//span[contains(text(), "Объединить строки")]/preceding-sibling::label')
    STATUSBAR_CHECK = (By.XPATH, '//span[@id="slot-chk-statusbar"]//span[contains(text(), "Объединить строки")]/preceding-sibling::input')
    STATUSBAR_LABEL = (By.ID, 'label-sheets')
    LEFT_MENU_CBX = (By.XPATH, '//span[@id="slot-chk-leftmenu"]//span[contains(text(), "Левая")]/preceding-sibling::label')
    LEFT_MENU_CHECK = (By.XPATH, '//span[@id="slot-chk-leftmenu"]//span[contains(text(), "Левая")]/preceding-sibling::input')
    LEFT_MENU_COMMENT_BUTTON = (By.ID, 'left-btn-comments')
    RIGHT_MENU_CBX = (By.XPATH, '//span[@id="slot-chk-rightmenu"]//span[contains(text(), "Правая")]/preceding-sibling::label')
    RIGHT_MENU_CHECK = (By.XPATH, '//span[@id="slot-chk-rightmenu"]//span[contains(text(), "Правая")]/preceding-sibling::input')
    RIGHT_MENU_BUTTON = (By.ID, 'id-right-menu-cell')


# fmt: off
class Samples:
    LOREM_IPSUM = (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
        'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    )
    WAR_AND_PEACE = (
        'Да, здесь, в этом лесу был этот дуб, с которым мы были согласны,- подумал князь Андрей. - Да где он»,- подумал опять князь Андрей, глядя на левую сторону дороги и, сам того не зная, не узнавая его, любовался тем дубом, которого он искал.'
        'Старый дуб, весь преображённый, раскинувшись шатром сочной, тёмной зелени, млел, чуть колыхаясь в лучах вечернего солнца. Ни корявых пальцев, ни болячек, ни старого недоверия и горя — ничего не было видно.'
        'Сквозь жёсткую, столетнюю кору пробились без сучков сочные, молодые листья, так что верить нельзя было, что этот старик произвёл их.'
        '"Да это тот самый дуб", - подумал князь Андрей, и на него вдруг нашло беспричинное весеннее чувство радости и обновления.'
        'Все лучшие минуты его жизни вдруг в одно и то же время вспомнились ему. И Аустерлиц с высоким небом, и мёртвое, укоризненное лицо жены, и Пьер на пароме, и девочка, взволнованная красотою ночи, и эта ночь, и луна — и всё это вдруг вспомнилось ему.'
    )
    CAPYBARA_IMG = 'https://distribution.faceit-cdn.net/images/e45e9f66-5bb7-40a6-8c43-c2a075a5f3f9.jpeg'
    VODOSVINKA_IMG_URL = 'https://natworld.info/wp-content/uploads/2018/02/vodosvinka-ili-kapibara.jpg'
    CAPYBARA_IMG_URL = 'https://ic.pics.livejournal.com/ridolina/14796263/75392/75392_original.png'
    UNSORTED_DATA_SET = 'ЙQ1Ц2WУ3Eйq!цw@уe#'

    PIVOT_DATA_SET_RAW = (
        'Товар,Категория,Поставщик,Дата поставки,Регион продажи,Сумма,Количество,Прибыль.'
        'Манго спелый,Фрукты,ООО Рога и копытца,43354,Самара,53756,70,Да.'
        'Помидоры,Овощи,Иностранная компания,43357,Самара,7938,50,Да.'
        'Слива,Фрукты,ПродТрест,43357,Москва,71246,34,Да.'
        'Спагетти,Макароны,ЗАО Продукты,43359,Смоленск,4350,28,Нет.'
        'Огурцы,Овощи,ГлавМосСбытТрест,43362,Самара,18740,54,Да.'
        'Кабачки,Овощи,ООО Рога и копытца,43362,Тверь,4040,32,Да.'
        'Баранки,Выпечка,ГлавМосСбытТрест,43362,Санкт-Петербург,46096,14,Да.'
        'Манго,Фрукты,ЗАО Продукты,43365,Новосибирск,25986,15,Да.'
        'Слива,Фрукты,ООО Рога и копытца,43366,Самара,16632,61,Нет.'
    )
    CHART_DATA_METAL = (', Gold, Silver, Bronze.'
                        'USA, 46, 29, 29.'
                        'CHN, 38, 27, 23.'
                        'RUS, 24, 26, 32.'
                        'GBR, 29, 17, 19.'
                        'GER, 11, 19, 14.'
                        'JPN, 7, 14, 17.')

    DATES = ('1968.12.09',
             '1979.10.14',
             '1985.11.20',
             '1995.10.20')

    DATA_TABLE_COLUMN_VARIABLE = (
                        'Таблица данных с переменной столбца;;;;Продукты на чел/сут кг;Количество дней;.'
                        ';Кол-во человек;7;;;13;.'
                        ';Продукты на чел/сут кг;3;;3;;.'
                        ';Всего продуктов, кг;273;;2,9;;.'
                        ';;;;2,8;;.'
                        ';Количество дней;;;2,7;;.'
                        ';;;;2,6;;.'
                        ';;;;2,5;;.'
                        ';;;;2,4;;.'
                        ';;;;2,3;;.'
                        ';;;;2,2;;.'
                        ';;;;2,1;;.'
                        ';;;;2;;.'
                        )




# fmt:on
