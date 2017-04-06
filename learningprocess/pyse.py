# -*- coding: utf-8 -*-
# use python3
# pi version of pysev2.py
import curses
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=0)

try:
    duration = 0  # set delay to visually inspect cursor movement
    # setup curses
    statusline = curses.initscr()  # initialize curses
    curses.noecho()  # disable local echo

    # create three windows for the 3 sections of the terminal: status line, data area, label line
    statusline.resize(46, 82)
    statusline.resize(2, 81)
    dataarea = curses.newwin(142, 181, 2, 1)  # temporary oversized window to allow cursor to go off screen
    labelline = curses.newwin(2, 81, 44, 1)
    dataarea.nodelay(1)  # allows dataarea.getch() to be non blocking (returns -1 if no key is pressed)

    # initialize attributes
    llattr = curses.A_NORMAL  # label line attribute (label line is the bottom row of the terminal)
    slattr = curses.A_NORMAL  # status line attribute (status line is the top row of the terminal)

    # control character codes in hex
    ESC = '\x1b'  # Escape
    BS = '\x08'   # Backspace
    NL = '\n'     # new line/linefeed
    STX = '\x02'  # Start of Text
    ETX = '\x03'  # End of Text
    VT = '\x0b'   # vertical tab
    FF = '\x0c'   # form feed
    ENQ = '\x05'  # Enquire
    ACK = '\x06'  # Acknowledge

    # defines the corresponding row/column values found after ESC =
    # ESC=!" would mean move the cursor to row 1, column 2
    linecode = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',
                '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
                '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
                '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p']

    curses.start_color()  # required to enable color
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # assign color pairs to numbers (you can't change 0)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    color = 0
    wrpt = False   # write-protect mode is initially off
    gmode = False  # flag for the graphicsmode() function

    def graphicsmode(raw):  # replaces the text with box drawing characters if gmode is True
        if gmode:
            graphics = {'0': '┬',
                        '1': '└',
                        '2': '┌',
                        '3': '┐',
                        '4': '├',
                        '5': '┘',
                        '6': '│',
                        '7': '█',
                        '8': '┼',
                        '9': '┤',
                        ':': '─',
                        ';': '▒',
                        '<': '═',
                        '=': '┴',
                        '>': '║',
                        '?': '░',
                        ' ': ' ',
                        NL: '',
                        BS: '',
                        VT: '',
                        FF: ''}

            box = []
            for i in raw:
                box.append(graphics[i])

            box = ''.join(box)
            return box

        else:
            return raw


    def getmessage():
        line = []
        while True:
            for c in ser.read():
                line.append(chr(c))
                if chr(c) == '\r':
                    return ''.join(line)[:-1]  # return message without the final carriage return character


    def wyprint(message):
        global gmode, llattr, slattr, wrpt, color

        split = message.split(ESC)
        if split[0] == '':  # remove empty string generated from the split function
            del split[0]    # empty strings occur when the string starts with '␛'

        for escape in split:
            # move cursor, print characters
            if escape[0] == '=':
                row, col = linecode.index(escape[1]), linecode.index(escape[2])  # get coordinates
                dataarea.move(row, col)  # move cursor to coordinates
                for char in escape[3:]:
                    if char == BS:  # move the cursor to the left one position
                        y, x = dataarea.getyx()
                        dataarea.move(y, x - 1)

                    elif char == NL:  # move the cursor down one position
                        y, x = dataarea.getyx()
                        dataarea.move(y + 1, x)

                    elif char == FF:  # I believe form feed adds one space...just a guess.
                        y, x = dataarea.getyx()
                        dataarea.move(y, x + 1)

                    elif char == VT:  # appears to move the cursor up one position
                        y, x = dataarea.getyx()
                        dataarea.move(y - 1, x)

                    elif char == ENQ:
                        pass

                    else:
                        dataarea.addstr(graphicsmode(char), curses.color_pair(color))
                        # after printing a character, the cursor moves right 1 spot

                    time.sleep(duration)
                    dataarea.refresh()

            # enable/disable graphicsmode
            elif escape[0] == 'H':
                if escape[1] == STX:
                    gmode = True

                else:
                    gmode = False

                for char in escape[2:]:
                    if char == BS:  # move the cursor to the left one position
                        y, x = dataarea.getyx()
                        dataarea.move(y, x - 1)

                    elif char == NL:  # move the cursor down one position
                        y, x = dataarea.getyx()
                        dataarea.move(y + 1, x)

                    elif char == FF:  # I believe form feed adds one space...just a guess.
                        y, x = dataarea.getyx()
                        dataarea.move(y, x + 1)

                    elif char == VT:  # appears to move the cursor up one position
                        y, x = dataarea.getyx()
                        dataarea.move(y - 1, x)

                    elif char == ENQ:
                        pass

                    else:
                        dataarea.addstr(graphicsmode(char), curses.color_pair(color))
                        # after printing a character, the cursor moves right 1 spot

                    time.sleep(duration)
                    dataarea.refresh()

            # enable/disable write-protect mode
            elif escape[0] == '(':
                wrpt = False
                color = 0

            elif escape[0] == ')':
                wrpt = True
                color = 1

            # program status line
            elif escape[0] == 'F':
                statusline.clear()
                statusline.addstr(1, 1, escape[1:], slattr)
                statusline.refresh()

            # program label line
            elif escape[0:2] == 'z(':
                if len(escape) == 2:
                    labelline.clear()

                else:
                    labelline.addstr(0, 0, escape[2:], llattr)

                labelline.chgat(0, 0, llattr)  # change attribute
                labelline.refresh()

            # clear screen
            elif escape[0] == '+':
                dataarea.clear()
                dataarea.refresh()

            elif escape[0] == 'A':  # adjust Attributes of the status line and label line
                # regards label line
                if escape[1] == '1':
                    if escape[2] == '4':
                        llattr = curses.A_REVERSE

                    elif escape[2] == '0':
                        llattr = curses.A_NORMAL

                    labelline.chgat(0, 0, llattr)
                    labelline.refresh()

                # regards status line
                elif escape[1] == '3':
                    if escape[2] == ':':
                        slattr = curses.A_UNDERLINE | curses.A_BLINK

                    elif escape[2] == '8':
                        slattr = curses.A_UNDERLINE

                    statusline.chgat(1, 1, slattr)
                    statusline.refresh()

        dataarea.refresh()


    def sendkey():
        char = dataarea.getch()
        if char != -1:
            # using the row of keys below the numbers to correspond to the function keys as a temporary measure...
            if chr(char) == 'q':
                ser.write(b'\x01@')  # F1

            elif chr(char) == 'w':
                ser.write(b'\x01A')  # F2

            elif chr(char) == 'e':
                ser.write(b'\x01B')  # F3

            elif chr(char) == 'r':
                ser.write(b'\x01C')  # F4

            elif chr(char) == 't':
                ser.write(b'\x01D')  # F5

            elif chr(char) == 'y':
                ser.write(b'\x01E')  # F6

            elif chr(char) == 'u':
                ser.write(b'\x01F')  # F7

            elif chr(char) == 'i':
                ser.write(b'\x01G')  # F8

            else:
                ser.write(str.encode(chr(char)))

    # main loop
    while True:
        msg = getmessage()
        wyprint(msg)
        sendkey()

finally:
    curses.endwin()
    ser.close()
