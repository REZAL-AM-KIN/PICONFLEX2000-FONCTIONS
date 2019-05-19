print("Demarrage 'CLAVIER.py'")
def CLAVIER_get():
    stdscr=curses.initscr()
    stdscr.nodelay(True)
    curses.cbreak()
    curses.flushinp()
    _touche=-1
    while (_touche==-1):
        _touche=int(str(stdscr.getch()))
    curses.flushinp()
    curses.endwin()
    return _touche
def CLAVIER_getRFID():
    stdscr = curses.initscr()
    stdscr.nodelay(True)
    curses.cbreak()
    curses.flushinp()
    _touche=-1
    while (_touche==-1):
        if not(RFID_carteCheck()):
            _touche=0
        else:
            _touche=int(str(stdscr.getch()))
    curses.flushinp()
    curses.endwin()
    return _touche
def CLAVIER_getNotRFID():
    stdscr = curses.initscr()
    stdscr.nodelay(True)
    curses.cbreak()
    curses.flushinp()
    _touche=-1
    while (_touche==-1):
        if (RFID_carteCheck()):
            _touche=0
        else:
            _touche=int(str(stdscr.getch()))
    curses.flushinp()
    curses.endwin()
    return _touche
def CLAVIER_confirmation():
    return CLAVIER_get()==10