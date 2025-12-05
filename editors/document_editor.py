from selenium.webdriver.common.by import By
from editors.base_editor import Editor


class DocumentEditor(Editor):
    COPY = (By.ID, 'id-toolbar-btn-copy')
    RULERS_CANVAS = (By.ID, 'id_vert_ruler')

    def new_document(self):
        super().new_file(CommonLocators.NEW_DOCUMENT)


class CommonLocators:
    NEW_DOCUMENT = (By.XPATH, '//*[@id="placeholder"]/div[1]/div/li[1]/a')
    SAVE_DOCUMENT = (By.ID, 'slot-btn-dt-save')
    SHAPE_BACKGROUND_COLOR = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[5]/table/tbody/tr[3]/td/div[1]/div/div/button/span[1]')
    SHAPE_BACKGROUND_COLOR_RED = (
    By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[5]/table/tbody/tr[3]/td/div[1]/div/div/ul/li[1]/div/div[1]/a[63]/em/span')


class MainTabLocators:
    FONT_INPUT = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[1]/div[1]/div[1]/span[1]/div/input')
    FONTSIZE_INPUT = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[1]/div[1]/div[1]/span[2]/span/input')
    INCREASE_FONT = (By.ID, 'id-toolbar-btn-incfont')
    DECREASE_FONT = (By.ID, 'id-toolbar-btn-decfont')
    FONT_CASE = (By.ID, 'id-toolbar-btn-case')
    FONT_CASE_OPTION = (By.LINK_TEXT, 'ВЕРХНИЙ РЕГИСТР')

    BOLD_TEXT = (By.ID, 'id-toolbar-btn-bold')
    ITALIC_TEXT = (By.ID, 'id-toolbar-btn-italic')
    UNDERLINE_TEXT = (By.ID, 'id-toolbar-btn-underline')
    STRIKEOUT_TEXT = (By.ID, 'id-toolbar-btn-strikeout')
    SUPERSCRIPT_TEXT = (By.ID, 'id-toolbar-btn-superscript')
    SUBSCRIPT_TEXT = (By.ID, 'id-toolbar-btn-subscript')
    HIGHLIGHT = (By.CSS_SELECTOR, '#id-toolbar-btn-highlight > button.btn.btn-toolbar.dropdown-toggle')
    HIGHLIGHT_COLOR_GREEN = (By.CSS_SELECTOR, '#id-toolbar-menu-highlight > div.palette-inner > a.palette-color.color-00FF00')
    FONT_COLOR = (By.CSS_SELECTOR, '#id-toolbar-btn-fontcolor > button.btn.btn-toolbar.dropdown-toggle')
    FONT_COLOR_RED = (
    By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[1]/div[1]/div[2]/span[8]/div/ul/li[3]/div/div[1]/a[62]/em/span')

    MARKERS = (By.ID, 'id-toolbar-btn-markers')
    NUMBERING = (By.ID, 'id-toolbar-btn-numbering')
    MULTILEVELS = (By.ID, 'id-toolbar-btn-multilevels')
    MULTILEVELS_OPTION = (By.CSS_SELECTOR, '#menu-multilevels-group-lib > div.group-items-container > div:nth-child(4)')
    DECOFFSET = (By.ID, 'id-toolbar-btn-decoffset')
    INCOFFSET = (By.ID, 'id-toolbar-btn-incoffset')
    LINESPACE = (By.ID, 'id-toolbar-btn-linespace')
    LINESPACE_OPTION = (By.LINK_TEXT, '2.0')
    ALIGN_LEFT = (By.ID, 'slot-btn-align-left')
    ALIGN_CENTER = (By.ID, 'slot-btn-align-center')
    ALIGN_RIGHT = (By.ID, 'slot-btn-align-right')
    ALIGN_JUST = (By.ID, 'slot-btn-align-just')
    HIDENCHARS = (By.ID, 'slot-btn-hidenchars')
    PARACOLOR = (By.CSS_SELECTOR, '#id-toolbar-btn-paracolor > button.btn.btn-toolbar.dropdown-toggle')
    PARACOLOR_INDIGO = (
    By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[1]/div[3]/div[2]/span[6]/div/ul/li[1]/div/div[1]/a[5]/em/span')

    CLEARSTYLE = (By.ID, 'id-toolbar-btn-clearstyle')
    COLORSCHEMAS = (By.ID, 'id-toolbar-btn-colorschemas')
    COLORSCHEMAS_STREAM = (By.LINK_TEXT, 'Поток')
    COPYSTYLE = (By.ID, 'id-toolbar-btn-copystyle')
    TEXT_STYLE = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[1]/div[7]/div/div[1]/div/div[3]/div/div')


class InsertTabLocators:
    INSERT_BLANK_PAGE = (By.ID, 'id-toolbar-btn-blankpage')
    INSERT_PAGE_BREAK = (By.ID, 'id-toolbar-toolbar__icon btn-pagebreak0')
    INSERT_TABLE = (By.ID, 'slot-btn-instable')
    INSERT_IMAGE = (By.ID, 'tlbtn-insertimage')
    INSERT_IMAGE_BY_URL = (By.LINK_TEXT, 'Изображение по URL')
    INSERT_IMAGE_INPUT = (By.CSS_SELECTOR, '#id-dlg-url > div > input')
    INSERT_IMAGE_INPUT_OK = (By.XPATH, '/html/body/div[4]/div/div[2]/button[1]')
    INSERT_CHART = (By.ID, 'tlbtn-insertchart')
    INSERT_CHART_HISTOGRAM = (
    By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[2]/div[5]/span[2]/div/ul/li/div/div/div[1]/div[2]/div[1]/div')
    INSERT_CHART_APPLY = (By.ID, 'id-btn-editor-apply')
    INSERT_SHAPE = (By.ID, 'tlbtn-insertshape')
    INSERT_SHAPE_RIGHT_ARROW = (
    By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[2]/div[5]/span[3]/div/ul/li/div/div/div[1]/div[2]/div[3]')
    INSERT_SMART_ART = (By.ID, 'tlbtn-insertsmartart')
    INSERT_SMART_ART_LIST = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[2]/div[5]/span[4]/div/ul/li[1]/a')
    INSERT_SMART_ART_ARC_LAYOUT = (
    By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[2]/div[5]/span[4]/div/ul/li[1]/ul/li/div/div/div[1]')
    ADD_COMMENT = (By.ID, 'tlbtn-addcomment-0')
    ADD_COMMENT_INPUT = (By.CSS_SELECTOR, r'#-\31  > div.inner-edit-ct > textarea')
    ADD_COMMENT_APPLY = (By.ID, 'id-comments-change-popover')
    INSERT_HYPERLINK = (By.ID, 'id-toolbar-toolbar__icon btn-inserthyperlink0')
    INSERT_HYPERLINK_INPUT = (By.CSS_SELECTOR, '#id-dlg-hyperlink-url-input')
    INSERT_HYPERLINK_APPLY = (By.CSS_SELECTOR, '#window-hyperlink > div.body > div.footer.center > button.btn.normal.dlg-btn.primary')
    EDIT_HEADER = (By.ID, 'id-toolbar-btn-editheader')
    EDIT_HEADER_UPPER = (By.LINK_TEXT, 'Изменить верхний колонтитул')
    INSERT_DATETIME = (By.ID, 'id-toolbar-btn-datetime')
    INSERT_DATETIME_APPLY = (By.CSS_SELECTOR, '#window-date-time > div.body > div.footer.center > button.btn.normal.dlg-btn.primary')
    INSERT_TEXT = (By.ID, 'tlbtn-inserttext')
    INSERT_TEXTART = (By.ID, 'tlbtn-inserttextart')
    INSERT_TEXTART_FIRST = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[2]/div[11]/span[2]/div/ul/li/div/div/div[1]/div')
    INSERT_EQUATION = (By.ID, 'tlbtn-insertequation')
    INSERT_SYMBOL = (By.ID, 'tlbtn-insertsymbol')
    INSERT_SYMBOL_INPUT = (By.CSS_SELECTOR, '#symbol-table-text-code > div > input')
    INSERT_SYMBOL_INSERT = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/button[1]')
    INSERT_SYMBOL_CLOSE = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/button[2]')
    INSERT_DROPCAP = (By.ID, 'tlbtn-dropcap')
    INSERT_DROPCAP_IN_TEXT = (By.LINK_TEXT, 'В тексте')
    INSERT_CONTROLS = (By.ID, 'tlbtn-controls')
    INSERT_CONTROLS_SIMPLE_TEXT = (By.LINK_TEXT, 'Обычный текст')
    INSERT_EMBEDDED_DOCUMENT = (By.ID, 'slot-btn-add-embedded-document')


class DrawTabLocators:
    SELECT = (By.ID, 'slot-btn-draw-select')
    PEN_GREEN = (By.ID, 'slot-btn-draw-pen-0')
    PEN_RED = (By.ID, 'slot-btn-draw-pen-1')
    PEN_YELLOW = (By.ID, 'slot-btn-draw-pen-2')
    ERASER = (By.ID, 'slot-btn-draw-eraser')


class LayoutTabLocators:
    PAGE_MARGINS = (By.ID, 'tlbtn-pagemargins')
    PAGE_MARGINS_NARROW = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[4]/div[1]/span[1]/div/ul/li[4]/a')
    PAGE_ORIENT = (By.ID, 'slot-btn-pageorient')
    PAGE_ORIENT_LANDSCAPE = (By.LINK_TEXT, 'Альбомная')
    PAGESIZE = (By.ID, 'slot-btn-pagesize')
    PAGESIZE_A5 = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[4]/div[1]/span[3]/div/ul/li[4]/a')
    COLUMNS = (By.ID, 'slot-btn-columns')
    COLUMNS_TWO = (By.LINK_TEXT, 'Две')
    PAGE_BRAKE = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[4]/div[1]/span[5]/div/button[1]')
    LINE_NUMBERS = (By.ID, 'slot-btn-line-numbers')
    LINE_NUMBERS_CONTINUOUS = (By.LINK_TEXT, 'Непрерывная')
    HYPHENATION = (By.ID, 'slot-btn-hyphenation')
    HYPHENATION_AUTO = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[4]/div[1]/span[7]/div/ul/li[2]/a')
    WRAPPING = (By.ID, 'slot-img-wrapping')
    WRAPPING_FRAME = (By.LINK_TEXT, 'Вокруг рамки')
    MOVE_FWD = (By.ID, 'slot-img-movefrwd')
    MOVE_BWD = (By.ID, 'slot-img-movebkwd')
    ALIGN = (By.ID, 'slot-img-align')
    ALIGN_CENTER = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[4]/div[3]/span[4]/div/ul/li[2]/a')
    GROUP = (By.ID, 'slot-img-group')
    GROUP_DO = (By.LINK_TEXT, 'Сгруппировать')
    GROUP_UNDO = (By.LINK_TEXT, 'Разгруппировать')
    WATERMARK = (By.ID, 'slot-btn-watermark')
    WATERMARK_SET = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/section[2]/section[4]/div[5]/span/div/ul/li[1]/a')
    WATERMARK_TEXT = (By.ID, 'watermark-radio-text')
    WATERMARK_APPLY = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/button[1]')


class LinksTabLocators:
    CONTENTS = (By.CSS_SELECTOR, r'#id-toolbar-toolbar__icon\ btn-contents0')
    ADD_TEXT = (By.ID, 'slot-btn-add-text')
    ADD_TEXT_LVL1 = (By.LINK_TEXT, 'Уровень 1')
    ADD_TEXT_LVL2 = (By.LINK_TEXT, 'Уровень 2')
    ADD_TEXT_LVL3 = (By.LINK_TEXT, 'Уровень 3')
    CONTENTS_UPDATE = (By.ID, 'slot-btn-contents-update')
    NOTES = (By.CSS_SELECTOR, '#toolbar > div > section > section.box-panels > section.panel.active > div:nth-child(4) > span')
    INSERT_HYPERLINK = (By.CSS_SELECTOR, r'#id-toolbar-toolbar__icon\ btn-inserthyperlink1')
    BOOKMARKS = (By.CSS_SELECTOR, '#slot-btn-bookmarks')
    BOOKMARKS_INPUT = (By.CSS_SELECTOR, '#bookmarks-txt-name > div > input')
    BOOKMARKS_ADD = (By.ID, 'bookmarks-btn-add')
    BOOKMARKS_SELECT = (By.CSS_SELECTOR, '#bookmarks-list > div > div.item')
    BOOKMARKS_GOTO = (By.ID, 'bookmarks-btn-goto')
    BOOKMARKS_CLOSE = (By.CSS_SELECTOR, '#window-bookmarks > div.body > div.footer.center > button')
    CAPTION = (By.ID, 'slot-btn-caption')
    CAPTION_INPUT = (By.CSS_SELECTOR, '#caption-txt-caption > div > input')
    CAPTION_APPLY = (By.CSS_SELECTOR, '#window-caption > div.body > div.footer.center > button.btn.normal.dlg-btn.primary')
    CROSSREF = (By.ID, 'slot-btn-crossref')
    CROSSREF_INPUT = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/span')
    CROSSREF_HEADER = (By.LINK_TEXT, 'Заголовок')
    CROSSREF_INSERT = (By.CSS_SELECTOR, '#window-cross-ref > div.body > div.footer.center > button.btn.normal.dlg-btn.custom.primary')
    CROSSREF_CLOSE = (By.CSS_SELECTOR, '#window-cross-ref > div.body > div.footer.center > button:nth-child(2)')
    TOF = (By.ID, 'slot-btn-tof')
    TOF_UPDATE = (By.ID, 'slot-btn-tof-update')


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

    REVIEW_ON_BTN = (By.CSS_SELECTOR, '#btn-review-on button:nth-of-type(1)')
    REVIEW_ON_DROPDOWN_MENU = (By.CSS_SELECTOR, '#btn-review-on button:nth-of-type(2)')
    REVIEW_FOR_ME_ON_LINK = (By.XPATH, '(//span[@id="btn-review-on"]//a[contains(text(), "ВКЛ.")])[1]')
    STATUSBAR_REVIEW_ON_BTN = (By.CSS_SELECTOR, '#btn-doc-review button:nth-of-type(1)')
    VIEW_DROPDOWN_MENU = (By.CSS_SELECTOR, '#btn-review-view button')
    VIEW_SOURCE_DOC_LINK = (By.XPATH, '//span[@id="btn-review-view"]//div[contains(text(), "Исходный")]/parent::a')

    CHANGE_ACCEPT_BTN = (By.CSS_SELECTOR, '#btn-change-accept button:nth-of-type(1)')
    CHANGE_ACCEPT_DROPDOWN_MENU = (By.CSS_SELECTOR, '#btn-change-accept button:nth-of-type(2)')
    CURRENT_CHANGE_ACCEPT_LINK = (By.XPATH, '//span[@id="btn-change-accept"]//a[contains(text(), "текущее")]')
    CHANGE_REJECT_BTN = (By.CSS_SELECTOR, '#btn-change-reject button:nth-of-type(1)')
    CHANGE_REJECT_DROPDOWN_MENU = (By.CSS_SELECTOR, '#btn-change-reject button:nth-of-type(2)')
    CURRENT_CHANGE_REJECT_LINK = (By.XPATH, '//span[@id="btn-change-reject"]//a[contains(text(), "текущее")]')
    MOVE_TO_PREVIOUS_CHANGE_BTN = (By.CSS_SELECTOR, '#btn-change-prev button')
    MOVE_TO_NEXT_CHANGE_BTN = (By.CSS_SELECTOR, '#btn-change-next button')


class ViewTabLocators:
    """
    Сокращения в названиях:
    BTN - button (кнопка)
    CBX - checkbox (чекбокс)
    """
    VIEW_NAVIGATION_BTN = (By.CSS_SELECTOR, '#slot-btn-navigation button')
    NAVIGATION_PANEL = (By.ID, 'navigation-list')
    NAVIGATION_TEXT = (By.CSS_SELECTOR, '#navigation-list .name')
    INPUT_ZOOM_FIELD = (By.CSS_SELECTOR, '#slot-field-zoom input')
    INPUT_ZOOM_DROPDOWN_BTN = (By.CSS_SELECTOR, '#slot-field-zoom button')
    ZOOM_150 = (By.CSS_SELECTOR, '#slot-field-zoom [data-value="150"]')
    ZOOM_TO_PAGE_BTN = (By.CSS_SELECTOR, '#slot-btn-ftp button')
    ZOOM_TO_WIDTH_BTN = (By.CSS_SELECTOR, '#slot-btn-ftw button')
    INTERFACE_THEME_DROPDOWN_MENU = (By.CSS_SELECTOR, '#slot-btn-interface-theme button')
    CONTRAST_DARK_INTERFACE_LINK = (By.XPATH, '//span[@id="slot-btn-interface-theme"]//a[contains(text(),"Контрастная")]')
    SYSTEM_INTERFACE_LINK = (By.XPATH, '//span[@id="slot-btn-interface-theme"]//a[contains(text(),"Системная")]')
    DARK_DOCUMENT_BTN = (By.CSS_SELECTOR, '#slot-btn-dark-document button')

    TOOLBAR_CBX = (By.XPATH, '//span[@id="slot-chk-toolbar"]//span[contains(text(), "Всегда показывать")]/preceding-sibling::label')
    TOOLBAR_CHECK = (By.XPATH, '//span[@id="slot-chk-toolbar"]//span[contains(text(), "Всегда показывать")]/preceding-sibling::input')
    TOOLBAR_SECTION = (By.CLASS_NAME, 'box-controls')
    STATUSBAR_CBX = (By.XPATH, '//span[@id="slot-chk-statusbar"]//span[contains(text(), "Строка состояния")]/preceding-sibling::label')
    STATUSBAR_CHECK = (By.XPATH, '//span[@id="slot-chk-statusbar"]//span[contains(text(), "Строка состояния")]/preceding-sibling::input')
    STATUSBAR_BUTTON = (By.ID, 'btn-zoom-down')
    LEFT_MENU_CBX = (By.XPATH, '//span[@id="slot-chk-leftmenu"]//span[contains(text(), "Левая")]/preceding-sibling::label')
    LEFT_MENU_CHECK = (By.XPATH, '//span[@id="slot-chk-leftmenu"]//span[contains(text(), "Левая")]/preceding-sibling::input')
    LEFT_MENU_COMMENT_BUTTON = (By.ID, 'left-btn-comments')
    RIGHT_MENU_CBX = (By.XPATH, '//span[@id="slot-chk-rightmenu"]//span[contains(text(), "Правая")]/preceding-sibling::label')
    RIGHT_MENU_CHECK = (By.XPATH, '//span[@id="slot-chk-rightmenu"]//span[contains(text(), "Правая")]/preceding-sibling::input')
    RIGHT_MENU_TEXT_BUTTON = (By.ID, 'id-right-menu-text')
    RULERS_CBX = (By.CSS_SELECTOR, '#slot-chk-rulers label>label')
    RULERS_CHECK = (By.CSS_SELECTOR, '#slot-chk-rulers label>input')


class Samples:
    LOREM_IPSUM = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
                   'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                   'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
                   'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    WAR_AND_PEACE = (
        'Да, здесь, в этом лесу был этот дуб, с которым мы были согласны,- подумал князь Андрей. - Да где он»,- подумал опять князь Андрей, глядя на левую сторону дороги и, сам того не зная, не узнавая его, любовался тем дубом, которого он искал.'
        'Старый дуб, весь преображённый, раскинувшись шатром сочной, тёмной зелени, млел, чуть колыхаясь в лучах вечернего солнца. Ни корявых пальцев, ни болячек, ни старого недоверия и горя — ничего не было видно.'
        'Сквозь жёсткую, столетнюю кору пробились без сучков сочные, молодые листья, так что верить нельзя было, что этот старик произвёл их.'
        '"Да это тот самый дуб", - подумал князь Андрей, и на него вдруг нашло беспричинное весеннее чувство радости и обновления.'
        'Все лучшие минуты его жизни вдруг в одно и то же время вспомнились ему. И Аустерлиц с высоким небом, и мёртвое, укоризненное лицо жены, и Пьер на пароме, и девочка, взволнованная красотою ночи, и эта ночь, и луна — и всё это вдруг вспомнилось ему.')
    CAPYBARA_IMG = 'https://distribution.faceit-cdn.net/images/e45e9f66-5bb7-40a6-8c43-c2a075a5f3f9.jpeg'
    AT_SYMBOL_CODE = '00040'
    IMAGE_LINK = 'https://i.pinimg.com/originals/ea/b5/b1/eab5b1aa1fa0c7472465e53fd2a7905e.png'
