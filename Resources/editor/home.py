import os

from game.files import GameFiles

f = GameFiles()

def setFileRoot(root):
    # Just a quick and dirty check to see if we're valid
    if os.path.exists(os.path.join(root, 'graphics.ini')):
        f.GAME_DIR = root
        return True
    else:
        return False

window.editor.files = f
window.editor.setRoot = setFileRoot
window.editor.playGame = lambda: f.launch_towns()