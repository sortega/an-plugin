from aqt import mw
from aqt.qt import *
from anki.hooks import addHook, wrap

TEXTS = {
    'An': 'A<span class="front-only">(</span>n<span class="front-only">)</span>',
    'A': 'A<span class="front-only">(n)</span>',
    'an': 'a<span class="front-only">(</span>n<span class="front-only">)</span>',
    'a': 'a<span class="front-only">(n)</span>',
}


def on_menu_button(editor):
    main = QMenu(mw)

    for key in TEXTS.keys():
        an_action = main.addAction(key)
        an_action.triggered.connect(write(editor, key))

    main.exec_(QCursor.pos())


def write(editor, key):
    return lambda: editor.web.eval("wrap('%s', '');" % TEXTS[key])


def setup_buttons(buttons, editor):
    b = editor.addButton(None, 'a(n)', on_menu_button, tip="Inserts an a(n) that resolved to a or an for the back card")
    buttons.append(b)
    return buttons


addHook("setupEditorButtons", setup_buttons)
