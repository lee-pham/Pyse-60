# -*- coding: utf-8 -*-
import curses
import time


def graphicsmode(raw):
    graphics = {'0': '┳',
                '1': '┗',
                '2': '┏',
                '3': '┓',
                '4': '┣',
                '5': '┛',
                '6': '┃',
                '8': '╋',
                '9': '┫',
                ':': '━',
                ' ': ' ',
                '␋': '␋',
                '\n': '\n'}

    box = []
    for i in raw:
        box.append(graphics[i])

    box = ''.join(box)
    return box


linecode = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',
            '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
            '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
            '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p']


def superparser(raw):
    esclist = raw.split('␛')
    if esclist[0] == '':
        del esclist[0]

    for i in range(0, len(esclist)):
        if esclist[i][0] == '=' and esclist[i][-1] == '\n':
            row = esclist[i][1]
            col = esclist[i][2]
            rownumber = linecode.index(row)
            esclistlist = list(esclist[i])[:-1]

            for j in range(0, len(esclistlist)):
                if esclistlist[j] == '\n':
                    rownumber += 1
                    esclistlist[j] = '=' + linecode[rownumber] + col

            esclist[i] = ''.join(esclistlist)

    return ''.join(esclist)


# setup curses window
stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Graphics mode
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Write-protect mode
color = 0
stdscr.resize(44, 82)
stdscr.border(0)


def wyprint(line):
    global color
    gmode = False
    cache = color

    for i in line:
        if i[0] == ')':
            cache = color
            color = 2

        elif i[0] == '(':
            color = cache

        elif i[0:2] == 'H␂':
            gmode = True
            cache = color
            color = 1

        elif i[0:2] == 'H␃':
            gmode = False
            color = cache

        elif i[0] == '=':
            if gmode:
                stdscr.addstr(linecode.index(i[1]), linecode.index(i[2]), i[3:], curses.color_pair(color))

                # stdscr.addstr(linecode.index(i[1]), linecode.index(i[2]), graphicsmode(i[3:]), curses.color_pair(color))

            else:
                stdscr.addstr(linecode.index(i[1]), linecode.index(i[2]), i[3:], curses.color_pair(color))

        stdscr.getch()
        stdscr.refresh()


data = """␛H␂␛=%`0
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
␛=%$0
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
4
4
4
4
8
␛=C%::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8␛=F$8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8␛=D$6
6
␛=D)6
6
␛=D.6
6
␛=D36
6
␛=D86
6
␛=D=6
6
␛=DB6
6
␛=DG6
6
␛=DL6
6
␛=DQ6
6
␛=DV6
6
␛=D[6
6
␛=D`6
6
␛=De6
6
␛=Dj6
6
␛=Do6
6
␛H␃␛)␛=EbUP␌␌␌DN␌␌␌SYS␛=D # UP␛=E # DN␛=#0HOURLY AVERAGE HALL CALL WAITING TIME␛=#bSYSTEM AVERAGE␛=. S

E

C

O

N

D

S

␛=%"60




50




40




30




20




10




0␛(␛H␂␛=A)6
6
␛=A)2::::3
6
␛=@.6
9␛=@.2::::3
6
6
␛=A34::::3
6
␛=@86
9␛=@82::::3
6
6
␛=?=6
9␛=?=2::::3
6
6
6
␛=AB4::::3
6
␛=BG4::::3
␛=?L6
6
6
9␛=?L2::::3
6
6
6
␛=AQ4::::3
6
␛=@a::::3
6
6
␛=@e0::::3
6
6
␛=@j0::::3
6
6
␛H␃␛)␛=I6DATA FOR WED MAR 08, 2017␛=I_6AM-6PM␛=B% 0.0␛=D% 0.0␛=@* 6.0␛=B* 0.0␛=?/ 6.0␛=A/ 7.0␛=@4 7.0␛=B4 0.0␛=?9 6.0␛=A9 4.0␛=>> 6.0␛=@> 8.0␛=@C 6.0␛=BC 0.0␛=AH 4.7␛=CH␛=>M 7.5␛=@M 8.0␛=@R 6.0␛=BR 1.0␛=BW 0.0␛=DW 0.0␛=B\ 0.0␛=D\ 0.0␛=?a␛=?a 6.2␛=Aa␛=?f 5.5␛=Af␛=?k 5.7␛=Ak␛=?p␛=D% 00 ␛=E% 00 ␛=D* 01 ␛=E* 00 ␛=D/ 01 ␛=E/ 01 ␛=D4 01 ␛=E4 00 ␛=D9 02 ␛=E9 02 ␛=D> 02 ␛=E> 01 ␛=DC 02 ␛=EC 00 ␛=DH 04 ␛=EH 00 ␛=DM 05 ␛=EM 02 ␛=DR 02 ␛=ER 01 ␛=DW 00 ␛=EW 00 ␛=D\ 00 ␛=E\ 00 ␛=Da 20 ␛=Df 07 ␛=G#6AM  7AM  8AM  9AM  10AM 11AM 12N  1PM  2PM  3PM  4PM  5PM  6PM ␛(␛A38␛F03/08/17 16:25:05        F4 = Main Menu

"""

cleaned = superparser(data)
print(cleaned)
wyprint(cleaned)

stdscr.getch()
curses.endwin()
