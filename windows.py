import curses

statusline = curses.initscr()

statusline.resize(46, 82)
statusline.resize(2, 81)
dataarea = curses.newwin(42, 81, 2, 1)
labelline = curses.newwin(1, 81, 44, 1)

statusline.addstr(1, 1, 'status here')
statusline.refresh()
statusline.getch()

attr = curses.A_BLINK | curses.A_UNDERLINE
statusline.chgat(1, 1, attr)
statusline.refresh()
statusline.getch()


for i in range(0, 42):
    dataarea.addstr(i, 0, str(i + 1))

dataarea.refresh()
dataarea.getch()


labelline.addstr(0, 0, 'label line is here')
labelline.getch()
labelline.chgat(0, 0, curses.A_REVERSE)

labelline.refresh()
labelline.getch()

curses.endwin()
