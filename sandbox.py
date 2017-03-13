import curses

stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Graphics mode
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Write-protect mode
color = 0
stdscr.resize(44, 82)
stdscr.border(0)
stdscr.addstr(0, 0, "123456", curses.color_pair(2))
stdscr.getch()
stdscr.addstr(5, 60, "\n", curses.color_pair(2))
stdscr.getch()
a = """h"""
stdscr.addstr(5, 61, a)
stdscr.getch()
curses.endwin()
