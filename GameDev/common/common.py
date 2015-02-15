import sfml as sf


def init(width, height, name):
    videoMode = sf.VideoMode(width, height)
    window = sf.RenderWindow(videoMode, name)
    window.framerate_limit = 60
    return window  
    
    
def isQuitRequested(e):
    """ 
    Checks if event e is a request to quit 
    """
    if type(e) is sf.CloseEvent:
        return True
    if type(e) is sf.KeyEvent and e.code is sf.Keyboard.ESCAPE:
        return True
    return False
    