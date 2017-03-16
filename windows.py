import curses

statusline = curses.initscr()

statusline = curses.newwin(1, 81, 1, 1)
dataarea = curses.newwin(42, 81, 2, 1)
labelline = curses.newwin(1, 81, 44, 1)

statusline.addstr(0, 0, 'status here')
statusline.refresh()

for i in range(0, 42):
    dataarea.addstr(i, 0, str(i))

dataarea.refresh()

labelline.addstr(0, 0, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
labelline.refresh()
statusline.addstr(0, 0, 'hello')
statusline.addstr(0, 10, 'hello')

statusline.refresh()
dataarea.getch()
curses.endwin()
