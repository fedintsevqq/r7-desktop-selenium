from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from editors.base_editor import Editor


class PresentationEditor(Editor):

    LEFT_CANVAS = (By.ID, 'id_thumbnails_background')
    NOTES_CANVAS = (By.ID, 'id_notes')
    RULERS_CANVAS = (By.ID, 'id_vert_ruler')
    TRANSIT = (By.XPATH, '//a[@data-tab="transit"]')
    FULL_WINDOW = (By.ID, 'viewport')
    STATUSBAR = (By.ID, 'statusbar')
    RIGHT_MENU = (By.ID, 'right-menu')
    TOOLBAR = (By.ID, 'toolbar')
    SELECT_ALL = (By.ID, 'id-toolbar-btn-select-all')
    COPY = (By.ID, 'id-toolbar-btn-copy')

    def new_presentation(self):
        super().new_file(CommonLocators.NEW_PRESENTATION)


class CommonLocators:
    NEW_PRESENTATION = (By.XPATH, '//a[@action="new:pptx"]')


class MainTabLocators:
    """
    Сокращения в названиях:
    BTN - button (кнопка)
    CBX - checkbox (чекбокс)
    """
    ADD_SLIDE_BTN = (By.CSS_SELECTOR, '#tlbtn-addslide-0 button:nth-of-type(1)')
    ADD_SLIDE_DROPDOWN_BTN = (By.CSS_SELECTOR, '#tlbtn-addslide-0 button:nth-of-type(2)')
    ADD_ONLY_HEADER_SLIDE = (By.XPATH, '//div[@id="tlbtn-addslide-0"]//div[contains(text(), "Только заголовок")]')
    CHANGE_SLIDE_LAYOUT = (By.CSS_SELECTOR, '#id-toolbar-button-change-slide button')
    TWO_OBJECTS_SLIDE_LAYOUT = (By.XPATH, '//div[@id="id-toolbar-button-change-slide"]//div[contains(text(), "Два объекта")]')
    PREVIEW_BTN = (By.CSS_SELECTOR, '#id-toolbar-button-preview button')

    FONT_INPUT = (By.CSS_SELECTOR, '#slot-field-fontname input')
    FONT_SIZE_INPUT = (By.CSS_SELECTOR, '#slot-field-fontsize input')
    INCREASE_FONT = (By.ID, 'id-toolbar-btn-incfont')
    DECREASE_FONT = (By.ID, 'id-toolbar-btn-decfont')
    FONT_CASE = (By.ID, 'id-toolbar-btn-case')
    FONT_CASE_OPTION = (By.XPATH, '//div[@id="id-toolbar-btn-case"]//a[contains(text(), "ВЕРХНИЙ РЕГИСТР")]')

    BOLD_TEXT = (By.ID, 'id-toolbar-btn-bold')
    ITALIC_TEXT = (By.ID, 'id-toolbar-btn-italic')
    UNDERLINE_TEXT = (By.ID, 'id-toolbar-btn-underline')
    STRIKEOUT_TEXT = (By.ID, 'id-toolbar-btn-strikeout')
    SUPERSCRIPT_TEXT = (By.ID, 'id-toolbar-btn-superscript')
    SUBSCRIPT_TEXT = (By.ID, 'id-toolbar-btn-subscript')
    HIGHLIGHT = (By.CSS_SELECTOR, '#id-toolbar-btn-highlight button.dropdown-toggle')
    HIGHLIGHT_COLOR_GREEN = (By.CSS_SELECTOR, '#id-toolbar-menu-highlight a.color-00FF00')
    FONT_COLOR = (By.CSS_SELECTOR, '#id-toolbar-btn-fontcolor button.dropdown-toggle')
    FONT_COLOR_RED = (By.XPATH, '//div[@id="id-toolbar-btn-fontcolor"]//a[@color-name="Красный"]')

    MARKERS = (By.ID, 'id-toolbar-btn-markers')
    NUMBERING = (By.ID, 'id-toolbar-btn-numbering')
    INCOFFSET = (By.ID, 'id-toolbar-btn-incoffset')
    DECOFFSET = (By.ID, 'id-toolbar-btn-decoffset')
    ALIGN_BTN = (By.CSS_SELECTOR, '#id-toolbar-btn-halign button')
    ALIGN_LEFT_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-halign li:nth-of-type(1) a')
    ALIGN_CENTER_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-halign li:nth-of-type(2) a')
    ALIGN_RIGHT_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-halign li:nth-of-type(3) a')
    ALIGN_JUST_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-halign li:nth-of-type(4) a')
    LINESPACE_BTN = (By.CSS_SELECTOR, '#id-toolbar-btn-linespace button')
    LINESPACE_OPTION = (By.XPATH, '//div[@id="id-toolbar-btn-linespace"]//a[contains(text(), "2.0")]')
    VERTICAL_ALIGN_BTN = (By.CSS_SELECTOR, '#id-toolbar-btn-valign button')
    ALIGN_TOP_LINK = (By.CSS_SELECTOR,'#id-toolbar-btn-valign li:nth-of-type(1) a')
    ALIGN_MIDDLE_LINK = (By.CSS_SELECTOR,'#id-toolbar-btn-valign li:nth-of-type(2) a')
    ALIGN_BOTTOM_LINK = (By.CSS_SELECTOR,'#id-toolbar-btn-valign li:nth-of-type(3) a')
    COLUMNS_BTN = (By.CSS_SELECTOR, '#id-toolbar-btn-columns button')
    ONE_COLUMN_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-columns li:nth-of-type(1) a')
    TWO_COLUMN_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-columns li:nth-of-type(2) a')
    THREE_COLUMN_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-columns li:nth-of-type(3) a')

    INSERT_HORIZONTAL_TEXT_BTN = (By.CSS_SELECTOR, '#tlbtn-inserttext-0 button:nth-child(1)')
    INSERT_TEXT_BTN = (By.CSS_SELECTOR, '#tlbtn-inserttext-0 button:nth-child(2)')
    INSERT_HORIZONTAL_TEXT = (By.CSS_SELECTOR, '#tlbtn-inserttext-0 li:nth-of-type(1) a')
    INSERT_VERTICAL_TEXT = (By.CSS_SELECTOR, '#tlbtn-inserttext-0 li:nth-of-type(2) a')

    INSERT_IMAGE_BTN = (By.CSS_SELECTOR, '#tlbtn-insertimage-0 button')
    INSERT_IMAGE_BY_URL = (By.XPATH, '//div[@id="tlbtn-insertimage-0"]//a[contains(text(),"Изображение по URL")]')
    INSERT_IMAGE_INPUT_FIELD = (By.CSS_SELECTOR, '#id-dlg-url input')
    INSERT_IMAGE_OK_BTN = (By.CSS_SELECTOR, '.footer.center button')
    IMAGE_LINK = 'https://natworld.info/wp-content/uploads/2018/02/vodosvinka-ili-kapibara.jpg'

    INSERT_SHAPE_BTN =(By.CSS_SELECTOR, '#tlbtn-insertshape-0 button')
    INSERT_RECTANGLE = (By.XPATH, '//div[@id="tlbtn-insertshape-0"]//div[@data-index="0"]')
    INSERT_ELLIPSE = (By.XPATH, '//div[@id="tlbtn-insertshape-0"]//div[@data-index="1"]')
    SHAPE_ARRANGE_BTN = (By.CSS_SELECTOR, '#id-toolbar-btn-shape-arrange button')
    SHAPE_ARRANGE_BACK_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-shape-arrange li:nth-of-type(2) a')
    SHAPE_ALIGN_BTN = (By.CSS_SELECTOR, '#id-toolbar-btn-shape-align button')
    SHAPE_ALIGN_LEFT_LINK = (By.CSS_SELECTOR, '#id-toolbar-btn-shape-align li:nth-of-type(1) a')

    CLEAR_STYLE = (By.CSS_SELECTOR, '#slot-btn-clearstyle button')
    COPY_STYLE = (By.ID, 'id-toolbar-btn-copystyle')
    COLOR_SCHEMAS = (By.CSS_SELECTOR, '#id-toolbar-btn-colorschemas button')
    COLOR_SCHEMAS_STREAM = (By.XPATH, '//div[@id="id-toolbar-btn-colorschemas"]//span[contains(text(),"Поток")]/ancestor::a[1]')
    SLIDE_SIZE = (By.CSS_SELECTOR, '#id-toolbar-btn-slide-size button')
    SLIDE_SIZE_STANDARD = (By.XPATH, '//div[@id="id-toolbar-btn-slide-size"]//a[contains(text(), "Стандартный")]')
    FIELD_STYLES = (By.ID, 'slot-field-styles')
    SLIDE_STYLE_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-field-styles button')
    POINT_STYLE = (By.CSS_SELECTOR, '#slot-field-styles li .item:nth-of-type(9)')


class InsertTabLocators:
    """
        Сокращения в названиях:
        BTN - button (кнопка)
        CBX - checkbox (чекбокс)
        """
    ADD_SLIDE_BTN = (By.CSS_SELECTOR, '#tlbtn-addslide-1 button:nth-of-type(1)')
    ADD_SLIDE_DROPDOWN_BTN = (By.CSS_SELECTOR, '#tlbtn-addslide-1 button:nth-of-type(2)')
    ADD_ONLY_HEADER_SLIDE = (By.XPATH, '//div[@id="tlbtn-addslide-1"]//div[contains(text(), "Только заголовок")]')

    INSERT_TABLE_BTN = (By.CSS_SELECTOR, '#tlbtn-inserttable button')
    INSERT_TABLE_MOUSECATCHER = (By.CLASS_NAME, 'dimension-picker-mousecatcher')
    INSERT_USER_TABLE = (By.XPATH, '//div[@id="tlbtn-inserttable"]//a[contains(text(), "Пользовательская таблица")]')
    INSERT_TABLE_CELLS = (By.XPATH, '//label[contains(text(), "Количество столбцов")]/following-sibling::div//input')
    INSERT_TABLE_ROWS = (By.XPATH, '//label[contains(text(), "Количество строк")]/following-sibling::div//input')
    CELLS_SPINNER_UP_BTN = (By.CSS_SELECTOR, '#window-insert-table .input-row:first-of-type .spinner-buttons>button:nth-of-type(1)')
    ROWS_SPINNER_DOWN_BTN = (By.CSS_SELECTOR, '#window-insert-table .input-row:nth-of-type(2) .spinner-buttons>button:nth-of-type(2)')
    INSERT_TABLE_OK_BTN = (By.XPATH, '//div[@id="window-insert-table"]//button[contains(text(), "OK")]')
    INSERT_TABLE_FORM = (By.XPATH, '//div[@id="tlbtn-inserttable"]//a[contains(text(), "Вставить таблицу")]')
    INSERT_TABLE_FRAME = (By.XPATH, '//div[contains(text(), "Редактор таблиц")]//following::iframe[1]')
    INSERT_TABLE_SAVE_AND_EXIT_BTN = (By.ID, 'id-btn-editor-apply')

    INSERT_HORIZONTAL_TEXT_BTN = (By.CSS_SELECTOR, '#tlbtn-inserttext-1 button:nth-child(1)')
    INSERT_TEXT_BTN = (By.CSS_SELECTOR, '#tlbtn-inserttext-1 button:nth-child(2)')
    INSERT_HORIZONTAL_TEXT = (By.CSS_SELECTOR, '#tlbtn-inserttext-1 li:nth-of-type(1) a')
    INSERT_VERTICAL_TEXT = (By.CSS_SELECTOR, '#tlbtn-inserttext-1 li:nth-of-type(2) a')

    INSERT_TEXT_ART_BTM = (By.CSS_SELECTOR, '#tlbtn-inserttextart button')
    INSERT_TEXT_ART = (By.CSS_SELECTOR, '#tlbtn-inserttextart .item:nth-of-type(7)')

    INSERT_IMAGE_BTN = (By.CSS_SELECTOR, '#tlbtn-insertimage-1 button')
    INSERT_LINKED_IMAGE = (By.XPATH, '//div[@id="tlbtn-insertimage-1"]//a[contains(text(),"Связать изображение по URL")]')
    INSERT_IMAGE_INPUT_FIELD = (By.CSS_SELECTOR, '#id-dlg-url input')
    INSERT_IMAGE_OK_BTN = (By.CSS_SELECTOR, '.footer.center button')
    IMAGE_LINK = 'https://i.pinimg.com/originals/ea/b5/b1/eab5b1aa1fa0c7472465e53fd2a7905e.png'

    INSERT_CHART_BTN = (By.CSS_SELECTOR, '#tlbtn-insertchart button')
    INSERT_PIE_CHART = (By.CSS_SELECTOR, '#menu-chart-group-pie .group-items-container div:nth-of-type(3)')
    INSERT_CHART_FRAME = (By.XPATH, '//div[contains(text(), "Редактор диаграмм")]//following::iframe[1]')
    INSERT_CHART_SAVE_AND_EXIT_BTN = (By.ID, 'id-btn-editor-apply')

    INSERT_SMART_ART_BTN = (By.CSS_SELECTOR, '#tlbtn-insertsmartart button')
    INSERT_SMART_ART_PROCESS_LINK = (By.XPATH, '//div[@id="tlbtn-insertsmartart"]//ul//li[2]/a')
    INSERT_SMART_GEAR_ART = (By.XPATH, '//div[@id="tlbtn-insertsmartart"]//ul//li[2]//ul//div[@class="item"][5]')

    INSERT_SHAPE = (By.CSS_SELECTOR, '#slot-combo-insertshape .item:nth-of-type(8)')
    INSERT_SHAPE_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-combo-insertshape button')
    INSERT_SHAPE_FROM_DROPDOWN_BTN = (By.XPATH, '//span[contains(text(), "Основные фигуры")]/following::div[1]/div[31]')
    INSERT_COMMENT_BTN = (By.XPATH, '//span[contains(text(), "Комментарий")]/ancestor::button')
    INSERT_COMMENT_FIELD = (By.CSS_SELECTOR, '.inner-edit-ct textarea')
    INSERT_COMMENT_ADD_BTN = (By.ID, 'id-comments-change-popover')

    INSERT_HYPERLINK_BTN = (By.ID, 'tlbtn-insertlink')
    INSERT_HYPERLINK_FIELD = (By.CSS_SELECTOR, '#id-dlg-hyperlink-url input')
    HYPERLINK = ('https://r7-office.ru')
    INSERT_HYPERLINK_OK_BTN = (By.XPATH, '//div[@id="window-hyperlink-settings"]//button[contains(text(), "OK")]')
    INSERT_EDITHEADER_BTN = (By.ID, 'id-toolbar-btn-editheader')
    INSERT_DATE_AND_TIME_EDITHEADER_CBX = (By.XPATH, '//span[contains(text(), "Дата и время")]/preceding-sibling::label')
    DATE_AND_TIME_FORMAT = (By.CSS_SELECTOR, '#datetime-dlg-format>div div:nth-of-type(1)')
    DATE_AND_TIME_WINDOW_OK_BTN = (By.XPATH, '//div[@id="window-date-time"]//button[contains(text(), "OK")]')
    INSERT_SLIDE_NUMBER_EDITHEADER_CBX = (By.XPATH,'//span[contains(text(), "Номер слайда")]/preceding-sibling::label')
    INSERT_DOWNTEXT_EDITHEADER_CBX =  (By.XPATH, '//span[contains(text(), "Текст в нижнем колонтитуле")]/preceding-sibling::label')
    INSERT_DOWNTEXT_EDITHEADER_FIELD =  (By.CSS_SELECTOR, '#hf-dlg-text input')
    INSERT_EDITHEADER_APPLY_BTN = (By.XPATH, '//div[@id="window-header-footer"]//button[(text()="Применить")]')
    INSERT_DATE_AND_TIME_BTN = (By.ID, 'id-toolbar-btn-datetime')
    INSERT_FORMAT_DATE_DROPDOWN_BTN = (By.CSS_SELECTOR, '#hf-dlg-combo-format button')
    FORMAT_DATE = (By.CSS_SELECTOR, '#hf-dlg-combo-format li:nth-of-type(2) a')
    INSERT_SLIDE_NUMBER_BTN = (By.ID, 'id-toolbar-btn-slidenum')

    INSERT_EQUATION_BTN = (By.CSS_SELECTOR, '#tlbtn-insertequation button:nth-of-type(1)')
    INSERT_EQUATION_DROPDOWN_BTN = (By.CSS_SELECTOR, '#tlbtn-insertequation button:nth-of-type(2)')
    INSERT_RADICAL_EQUATION = (By.CSS_SELECTOR, '#equation-container>span:nth-of-type(4) button')
    INSERT_QUADRATIC_EQUATION = (By.CSS_SELECTOR, '#id-document-holder-btn-equation-menu-3 .item:nth-of-type(5)')
    INSERT_LOGARITHM_EQUATION_LINK = (By.CSS_SELECTOR, '#tlbtn-insertequation .dropdown-submenu:nth-of-type(10)>a')
    INSERT_LIMIT_EQUATION = (By.CSS_SELECTOR, '#id-toolbar-menu-equationgroup9 .item:nth-of-type(7)')

    INSERT_SYMBOL_BTN = (By.ID, 'tlbtn-insertsymbol')
    INSERT_SPECIAL_SYMBOLS_BTN = (By.ID, 'symbol-table-special')
    INSERT_TRADEMARK_SYMBOL = (By.XPATH, '//div[@id="symbol-table-special-list"]//div[contains(text(), "товарный знак")]')
    INSERT_BTN = (By.XPATH, '//button[contains(text(), "Вставить")]')
    INSERT_SYMBOL_WINDOW_CLOSE_BTN = (By.XPATH, '//button[contains(text(), "Закрыть")]')


class DrawTabLocators:
    SELECT = (By.ID, 'slot-btn-draw-select')
    PEN_GREEN = (By.ID, 'slot-btn-draw-pen-0')
    PEN_RED = (By.ID, 'slot-btn-draw-pen-1')
    PEN_YELLOW = (By.ID, 'slot-btn-draw-pen-2')
    ERASER = (By.ID, 'slot-btn-draw-eraser')


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
    REMOVE_COMMENT_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-comment-remove [data-toggle="dropdown"]')
    REMOVE_CURRENT_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-remove"]//a[contains(text(), "Удалить текущие")]')
    REMOVE_MY_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-remove"]//a[contains(text(), "Удалить мои")]')
    REMOVE_ALL_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-remove"]//a[contains(text(), "Удалить все")]')

    RESOLVE_COMMENT_BTN = (By.CSS_SELECTOR, '#slot-comment-resolve button:nth-of-type(1)')
    RESOLVE_COMMENT_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-comment-resolve [data-toggle="dropdown"]')
    RESOLVE_CURRENT_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-resolve"]//a[contains(text(), "Решить текущие")]')
    RESOLVE_MY_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-resolve"]//a[contains(text(), "Решить мои")]')
    RESOLVE_ALL_COMMENTS_LINK = (By.XPATH, '//span[@id="slot-comment-resolve"]//a[contains(text(), "Решить все")]')


class ViewTabLocators:
    """
            Сокращения в названиях:
            BTN - button (кнопка)
            CBX - checkbox (чекбокс)
    """
    INPUT_ZOOM_FIELD = (By.CSS_SELECTOR, '#slot-field-zoom input')
    INPUT_ZOOM_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-field-zoom button')
    ZOOM_150 = (By.CSS_SELECTOR, '#slot-field-zoom [data-value="150"]')
    ZOOM_TO_SLIDE_BTN = (By.CSS_SELECTOR, '#slot-btn-fts button')
    ZOOM_TO_WIDTH_BTN = (By.CSS_SELECTOR, '#slot-btn-ftw button')
    INTERFACE_THEME_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-btn-interface-theme button')
    CONTRAST_DARK_INTERFACE_LINK = (By.XPATH, '//span[@id="slot-btn-interface-theme"]//a[contains(text(),"Контрастная")]')
    CLASSIC_LIGHT_INTERFACE_LINK = (By.XPATH, '//span[@id="slot-btn-interface-theme"]//a[contains(text(),"Классическая")]')

    NOTES_CBX = (By.CSS_SELECTOR, '#slot-chk-notes label>label')
    NOTES_CHECK = (By.CSS_SELECTOR, '#slot-chk-notes label>input')
    RULERS_CBX = (By.CSS_SELECTOR, '#slot-chk-rulers label>label')
    RULERS_CHECK = (By.CSS_SELECTOR, '#slot-chk-rulers label>input')
    GUIDES_BTN = (By.CSS_SELECTOR, '#slot-btn-guides button:nth-of-type(1)')
    GUIDES_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-btn-guides button:nth-of-type(2)')
    SHOW_GUIDES_LINK = (By.XPATH, '//span[@id="slot-btn-guides"]//a[contains(text(), "Показать направляющие")]')
    SHOW_VERTICAL_GUIDES_LINK = (By.CSS_SELECTOR, '#slot-btn-guides li:nth-of-type(3) a')
    SHOW_HORIZONTAL_GUIDES_LINK = (By.CSS_SELECTOR, '#slot-btn-guides li:nth-of-type(4) a')
    SHOW_SMART_GUIDES_LINK = (By.CSS_SELECTOR, '#slot-btn-guides li:nth-of-type(6) a')
    DELETE_GUIDES_LINK = (By.CSS_SELECTOR, '#slot-btn-guides li:nth-of-type(7) a')
    GRID_LINES_BTN = (By.CSS_SELECTOR, '#slot-btn-gridlines button:nth-of-type(1)')
    GRID_LINES_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-btn-gridlines button:nth-of-type(2)')
    SHOW_GRID_LINES = (By.XPATH, '//span[@id="slot-btn-gridlines"]//a[contains(text(), "Показать")]')
    BIND_GRID_LINES = (By.XPATH, '//span[@id="slot-btn-gridlines"]//a[contains(text(), "Привязать")]')
    GRID_LINES_1_PER_5 = (By.XPATH, '//span[@id="slot-btn-gridlines"]//a[contains(text(), "1/5")]')
    GRID_LINES_1_PER_8 = (By.XPATH, '//span[@id="slot-btn-gridlines"]//a[contains(text(), "1/8")]')
    USER_GRID_LINES = (By.XPATH, '//span[@id="slot-btn-gridlines"]//a[contains(text(), "Пользовательские")]')
    GRID_SPACING_COMBO_DROPDOWN_BTN = (By.CSS_SELECTOR, '#grid-spacing-combo button')
    GRID_LINES_1_PER_8_LINK = (By.XPATH, '//div[@id="grid-spacing-combo"]//a[contains(text(), "1/8")]')
    USER_GRID_LINES_LINK = (By.XPATH, '//div[@id="grid-spacing-combo"]//a[contains(text(), "Пользовательские")]')
    USER_GRID_LINES_SPINNER_UP = (By.CSS_SELECTOR, '#grid-spacing-spin .spinner-up')
    USER_GRID_LINES_SPINNER_DOWN = (By.CSS_SELECTOR, '#grid-spacing-spin .spinner-down')
    WINDOW_GRID_SETTINGS_OK_BTN = (By.XPATH, '//div[@id="window-grid-settings"]//button[contains(text(), "OK")]')

    TOOLBAR_CBX = (By.XPATH, '//span[@id="slot-chk-toolbar"]//span[contains(text(), "Всегда показывать")]/preceding-sibling::label')
    TOOLBAR_CHECK = (By.XPATH, '//span[@id="slot-chk-toolbar"]//span[contains(text(), "Всегда показывать")]/preceding-sibling::input')
    TOOLBAR_SECTION = (By.CLASS_NAME, 'box-controls')
    STATUSBAR_CBX = (By.XPATH, '//span[@id="slot-chk-statusbar"]//span[contains(text(), "Строка состояния")]/preceding-sibling::label')
    STATUSBAR_CHECK = (By.XPATH, '//span[@id="slot-chk-statusbar"]//span[contains(text(), "Строка состояния")]/preceding-sibling::input')
    STATUSBAR_BTN = (By.ID, 'btn-zoom-down')
    LEFT_MENU_CBX = (By.XPATH, '//span[@id="slot-chk-leftmenu"]//span[contains(text(), "Левая")]/preceding-sibling::label')
    LEFT_MENU_CHECK = (By.XPATH, '//span[@id="slot-chk-leftmenu"]//span[contains(text(), "Левая")]/preceding-sibling::input')
    LEFT_MENU_COMMENT_BTN = (By.ID, 'left-btn-comments')
    LEFT_MENU_FIELD_BTN = (By.ID, 'left-btn-thumbs')
    RIGHT_MENU_CBX = (By.XPATH, '//span[@id="slot-chk-rightmenu"]//span[contains(text(), "Правая")]/preceding-sibling::label')
    RIGHT_MENU_CHECK = (By.XPATH, '//span[@id="slot-chk-rightmenu"]//span[contains(text(), "Правая")]/preceding-sibling::input')
    RIGHT_MENU_PARAMS_BTN = (By.ID, 'id-right-menu-slide')


class Samples:
    LOREM_IPSUM = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
               'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
               'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
               'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    WAR_AND_PEACE = ('Да, здесь, в этом лесу был этот дуб, с которым мы были согласны,- подумал князь Андрей. - Да где он»,- подумал опять князь Андрей, глядя на левую сторону дороги и, сам того не зная, не узнавая его, любовался тем дубом, которого он искал.'
                'Старый дуб, весь преображённый, раскинувшись шатром сочной, тёмной зелени, млел, чуть колыхаясь в лучах вечернего солнца. Ни корявых пальцев, ни болячек, ни старого недоверия и горя — ничего не было видно.'
                'Сквозь жёсткую, столетнюю кору пробились без сучков сочные, молодые листья, так что верить нельзя было, что этот старик произвёл их.'
                '"Да это тот самый дуб", - подумал князь Андрей, и на него вдруг нашло беспричинное весеннее чувство радости и обновления.'
                'Все лучшие минуты его жизни вдруг в одно и то же время вспомнились ему. И Аустерлиц с высоким небом, и мёртвое, укоризненное лицо жены, и Пьер на пароме, и девочка, взволнованная красотою ночи, и эта ночь, и луна — и всё это вдруг вспомнилось ему.')
    CAPYBARA_IMG = 'https://distribution.faceit-cdn.net/images/e45e9f66-5bb7-40a6-8c43-c2a075a5f3f9.jpeg'
