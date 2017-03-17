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


def gigaparse(data):
    datasplit = data.split('␛')
    if datasplit[0] == '':
        del datasplit[0]

    for i, string in enumerate(datasplit):
        if string[-1] == '\n' and string[1] == '=':
            datasplit[i] = string[:-1]
        datasplit[i] = '␛' + datasplit[i]

    for j, string1 in enumerate(datasplit):
        if string1[1] == '=':
            row = linecode.index(string1[2])
            col = string1[3]
            temp = list(string1)
            for k, string2 in enumerate(temp):
                if string2 == '\n':
                    row += 1
                    temp[k] = '␛=' + linecode[row] + col

            datasplit[j] = ''.join(temp)

    return ''.join(datasplit)


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
    global gmode, llattr, slattr
    line = line.split('␛')
    if line[0] == '':
        del line[0]

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

        time.sleep(.003)


data3 = """␛`:␛`0␛=$8Performance Reports Menu (F2)␛)␛=*21  -  System Performance Graph␛=-22  -  Hall Call Distribution Table␛=023  -  Clear Reports␛=31␛(␛H␂␛=',2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3␛=(*2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3 6␛=)*6␛=)e6 6␛=**6␛=*e6 6␛=+*6␛=+e6 6␛=,*6␛=,e6 6␛=-*6␛=-e6 6␛=.*6␛=.e6 6␛=/*6␛=/e6 6␛=0*6␛=0e6 6␛=1*6␛=1e6 6␛=2*6␛=2e6 6␛=3*6␛=3e6 6␛=4*1::::::::::::::::::::::::::::::::::::::::::::::::::::::::::5␋:5␛H␃␛A38␛F03/08/17 16:25:02        F4 = Main Menu
␛A38␛F03/08/17 16:25:03        F4 = Main Menu
␅␛A38␛F03/08/17 16:25:04        F4 = Main Menu
1␛A10␛z(
␛`0␛+␛`:␛`0␛A14␛z(                      Up = Next Day     Down = Previous Day
␛A3:␛FPLEASE WAIT.... PROCESSING
␛=!9MCE SYSTEM PERFORMANCE GRAPH␛H␂␛=%`0
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
␛H␃␛)␛=I6DATA FOR WED MAR 08, 2017␛=I_6AM-6PM␛=B% 0.0␛=D% 0.0␛=@* 6.0␛=B* 0.0␛=?/ 6.0␛=A/ 7.0␛=@4 7.0␛=B4 0.0␛=?9 6.0␛=A9 4.0␛=>> 6.0␛=@> 8.0␛=@C 6.0␛=BC 0.0␛=AH 4.7␛=CH␛=>M 7.5␛=@M 8.0␛=@R 6.0␛=BR 1.0␛=BW 0.0␛=DW 0.0␛=B\ 0.0␛=D\ 0.0␛=?a␛=?a 6.2␛=Aa␛=?f 5.5␛=Af␛=?k 5.7␛=Ak␛=?p␛=D% 00 ␛=E% 00 ␛=D* 01 ␛=E* 00 ␛=D/ 01 ␛=E/ 01 ␛=D4 01 ␛=E4 00 ␛=D9 02 ␛=E9 02 ␛=D> 02 ␛=E> 01 ␛=DC 02 ␛=EC 00 ␛=DH 04 ␛=EH 00 ␛=DM 05 ␛=EM 02 ␛=DR 02 ␛=ER 01 ␛=DW 00 ␛=EW 00 ␛=D\ 00 ␛=E\ 00 ␛=Da 20 ␛=Df 07 ␛=G#6AM  7AM  8AM  9AM  10AM 11AM 12N  1PM  2PM  3PM  4PM  5PM  6PM ␛(␛A38␛F03/08/17 16:25:05        F4 = Main Menu"""

wyprint(gigaparse(data3))

data2 = """␛A38␛F03/08/17 16:38:13        F4 = Main Menu
␅␛A10␛z(
␛`0␛+␛`:␛`0␛A3:␛FPLEASE WAIT.... PROCESSING
␛="<MCE CRT Display Option␛=$BMain Menu␛)␛=*4F1  -  Job Configuration Parameters␛=,4F2  -  Performance Reports Menu␛=.4F3  -  Graphic Display of Elevator Status␛=04F4  -  Main Menu␛=24F5  -  CRT Terminal Initialization␛=44F6  -  Computer Parameters␛=64F7  -  Special Event Calendar Menu␛=84F8  -  Car  A  Inputs and Outputs␛=8? A ␛=:.Shift F2  -  System Performance Counters␛=<.Shift F5  -  Security Menu␛=>.Shift F6  -  CMS Parameters␛(␛H␂␛=',2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3␛=(*2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3 6␛=)*6␛=)e6 6␛=**6␛=*e6 6␛=+*6␛=+e6 6␛=,*6␛=,e6 6␛=-*6␛=-e6 6␛=.*6␛=.e6 6␛=/*6␛=/e6 6␛=0*6␛=0e6 6␛=1*6␛=1e6 6␛=2*6␛=2e6 6␛=3*6␛=3e6 6␛=4*6␛=4e6 6␛=5*6␛=5e6 6␛=6*6␛=6e6 6␛=7*6␛=7e6 6␛=8*6␛=8e6 6␛=9*6␛=9e6 6␛=:*6␛=:e6 6␛=;*6␛=;e6 6␛=<*6␛=<e6 6␛==*6␛==e6 6␛=>*6␛=>e6 6␛=?*6␛=?e6 6␛=@*1::::::::::::::::::::::::::::::::::::::::::::::::::::::::::5␋:5␛H␃␛=@+ Ver 3.64 EMI A-2K␛G|␛A38␛F03/08/17 16:38:14        F4 = Main Menu
"""
wyprint(gigaparse(data2))

dataarea.getch()
curses.endwin()
