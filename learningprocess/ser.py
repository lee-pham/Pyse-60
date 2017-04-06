# -*- coding: utf-8 -*-
import curses
import time

linecode = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',
            '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
            '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
            '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p']


def graphicsmode(raw):
    if gmode:
        graphics = {'0': '┬',
                    '1': '└',
                    '2': '┌',
                    '3': '┐',
                    '4': '├',
                    '5': '┘',
                    '6': '│',
                    '8': '┼',
                    '9': '┤',
                    ':': '─',
                    ' ': ' ',
                    '␋': '',  # ignores vertical tabs
                    '\n': ' '}

        box = []
        for i in raw:
            box.append(graphics[i])

        box = ''.join(box)
        return box

    else:
        return raw


# setup curses
statusline = curses.initscr()
curses.curs_set(0)

statusline.resize(46, 82)
statusline.resize(2, 81)
dataarea = curses.newwin(42, 81, 2, 1)
labelline = curses.newwin(2, 81, 44, 1)

# initialize attributes
llattr = curses.A_NORMAL
slattr = curses.A_NORMAL
gmode = False


def wyprint(line):
    line = line[:-1]
    global gmode, llattr, slattr
    line = line.split('␛')
    if line[0] == '':
        del line[0]

    y, x = curses.getsyx()
    dataarea.move(y + 1, x)

    for i in line:
        if i[0:2] == 'H␂':
            gmode = True

        elif i[0:2] == 'H␃':
            gmode = False

        elif i[0] == '=':
            dataarea.addstr(linecode.index(i[1]), linecode.index(i[2]), graphicsmode(i[3:]))
            dataarea.refresh()

        elif i[0] == '+':
            dataarea.clear()
            dataarea.refresh()

        # Computer message
        if i[0] == 'F':
            statusline.clear()
            statusline.addstr(1, 1, i[1:-2], slattr)
            statusline.refresh()

        # Function key label line
        if i[0:2] == 'z(':
            if i[2] == '\n':
                labelline.clear()
                labelline.chgat(0, 0, llattr)

            else:
                labelline.addstr(0, 0, i[2:-1], llattr)

            labelline.refresh()
            labelline.getch()

        if i[0] == 'A':
            # Function key label line
            if i[1] == '1':
                if i[2] == '4':
                    llattr = curses.A_REVERSE
                    labelline.chgat(0, 0, llattr)

                elif i[2] == '0':
                    llattr = curses.A_NORMAL
                    labelline.chgat(0, 0, llattr)

                labelline.refresh()
                labelline.getch()

            # Computer message
            elif i[1] == '3':
                if i[2] == ':':
                    slattr = curses.A_UNDERLINE | curses.A_BLINK
                    statusline.chgat(1, 1, slattr)

                elif i[2] == '8':
                    slattr = curses.A_UNDERLINE
                    statusline.chgat(1, 1, slattr)

                statusline.refresh()



        if i[-1] == '\n':
            y, x = curses.getsyx()
            dataarea.move(y + 1, x)


f = open('/Users/leepham/PycharmProjects/Pyse-60/hallcallEDIT.txt', 'r')
currentline = f.readline()


dataarea.getch()
curses.endwin()
