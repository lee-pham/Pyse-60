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
    line = line.split('␛')
    if line[0] == '':
        del line[0]

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

                stdscr.addstr(linecode.index(i[1]), linecode.index(i[2]), graphicsmode(i[3:]), curses.color_pair(color))

            else:
                stdscr.addstr(linecode.index(i[1]), linecode.index(i[2]), i[3:], curses.color_pair(color))

        stdscr.getch()
        stdscr.refresh()


data = """␛H␂␛=%`0␛=&`4␛='`4␛=(`4␛=)`4␛=*`8␛=+`4␛=,`4␛=-`4␛=.`4␛=/`8␛=0`4␛=1`4␛=2`4␛=3`4␛=4`8␛=5`4␛=6`4␛=7`4␛=8`4␛=9`8␛=:`4␛=;`4␛=<`4␛==`4␛=>`8␛=?`4␛=@`4␛=A`4␛=B`4␛=C`8␛=%$0␛=&$4␛='$4␛=($4␛=)$4␛=*$8␛=+$4␛=,$4␛=-$4␛=.$4␛=/$8␛=0$4␛=1$4␛=2$4␛=3$4␛=4$8␛=5$4␛=6$4␛=7$4␛=8$4␛=9$8␛=:$4␛=;$4␛=<$4␛==$4␛=>$8␛=?$4␛=@$4␛=A$4␛=B$4␛=C$8␛=C%::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8␛=F$8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8::::8␛=D$6␛=E$6␛=D)6␛=E)6␛=D.6␛=E.6␛=D36␛=E36␛=D86␛=E86␛=D=6␛=E=6␛=DB6␛=EB6␛=DG6␛=EG6␛=DL6␛=EL6␛=DQ6␛=EQ6␛=DV6␛=EV6␛=D[6␛=E[6␛=D`6␛=E`6␛=De6␛=Ee6␛=Dj6␛=Ej6␛=Do6␛=Eo6␛H␃␛)␛=EbUP␌␌␌DN␌␌␌SYS␛=D # UP␛=E # DN␛=#0HOURLY AVERAGE HALL CALL WAITING TIME␛=#bSYSTEM AVERAGE␛=. S␛=/ ␛=0 E␛=1 ␛=2 C␛=3 ␛=4 O␛=5 ␛=6 N␛=7 ␛=8 D␛=9 ␛=: S␛=; ␛=%"60␛=&"␛='"␛=("␛=)"␛=*"50␛=+"␛=,"␛=-"␛=."␛=/"40␛=0"␛=1"␛=2"␛=3"␛=4"30␛=5"␛=6"␛=7"␛=8"␛=9"20␛=:"␛=;"␛=<"␛=="␛=>"10␛=?"␛=@"␛=A"␛=B"␛=C"0␛(␛H␂␛=A)6␛=B)6␛=A)2::::3␛=B)6␛=@.6␛=A.9␛=@.2::::3␛=A.6␛=B.6␛=A34::::3␛=B36␛=@86␛=A89␛=@82::::3␛=A86␛=B86␛=?=6␛=@=9␛=?=2::::3␛=@=6␛=A=6␛=B=6␛=AB4::::3␛=BB6␛=BG4::::3␛=?L6␛=@L6␛=AL6␛=BL9␛=?L2::::3␛=@L6␛=AL6␛=BL6␛=AQ4::::3␛=BQ6␛=@a::::3␛=Aa6␛=Ba6␛=@e0::::3␛=Ae6␛=Be6␛=@j0::::3␛=Aj6␛=Bj6␛H␃"""

wyprint(data)

stdscr.getch()
curses.endwin()
