import curses
import time
stdscr = curses.initscr()
stdscr.resize(44, 82)
stdscr.border(0)

for i in range(1, 81):
    stdscr.addstr(1, i, "X")
    time.sleep(.01)
    stdscr.refresh()

for i in range(1, 43):
    stdscr.addstr(i, 1, "Y")
    time.sleep(.01)
    stdscr.refresh()

for i in range(1, 43):
    for j in range(1, 81):
        stdscr.addstr(i, j, "Z")
        stdscr.refresh()

stdscr.getch()
curses.endwin()

