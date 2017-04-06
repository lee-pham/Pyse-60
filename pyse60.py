# -*- coding: utf-8 -*-
# use python3
import curses
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=0)

try:
    duration = 0  # set delay to visually inspect cursor movement
    # setup curses
    statusline = curses.initscr()  # initialize curses
    curses.noecho()  # disable local echo
    curses.curs_set(0)  # turn off cursor

    # create three windows for the 3 sections of the terminal: status line, data area, label line
    statusline.resize(46, 82)
    statusline.resize(2, 81)
    dataarea = curses.newwin(142, 181, 2, 1)  # temporary oversized window to allow cursor to go off screen
    labelline = curses.newwin(2, 81, 44, 1)
    dataarea.nodelay(1)  # allows dataarea.getch() to be non blocking (returns -1 if no key is pressed)

    # initialize attributes
    llattr = curses.A_NORMAL  # label line attribute (label line is the bottom row of the terminal)
    slattr = curses.A_NORMAL  # status line attribute (status line is the top row of the terminal)
    charattr = curses.A_NORMAL

    wrpt = False   # write-protect mode is initially off
    gmode = False  # flag for the graphicsmode() function
    start = 0

    # control character codes in hex
    ESC = '\x1b'  # ESCape
    NL = '\n'     # New Line/LiNefeed
    STX = '\x02'  # Start of TeXt
    ETX = '\x03'  # End of TeXt
    ENQ = '\x05'  # ENQuire
    ACK = '\x06'  # ACKnowledge
    BS = '\x08'   # BackSpace
    VT = '\x0b'   # Vertical Tab
    FF = '\x0c'   # Form Feed
    CR = '\x0D'   # Carriage Return

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

    # graphics replacement characters
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


    def setattribute(num):  # sets attribute based off of the attribute number
        if num == '0':
            return curses.A_NORMAL

        elif num == '2':
            return curses.A_BLINK

        elif num == '4':
            return curses.A_REVERSE

        elif num == '8':
            return curses.A_UNDERLINE

        elif num == ':':
            return curses.A_UNDERLINE | curses.A_BLINK

        elif num == '|':
            return curses.A_NORMAL
            # '|' is supposed to return dim, underline, and reverse
            # however, the terminal emulator appears to NOT do the above case


    def graphicsmode(raw):  # replaces the text with box drawing characters if gmode is True
        if gmode:
            return graphics[raw]

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
        global gmode, llattr, slattr, wrpt, charattr, start

        split = message.split(ESC)
        if split[0] == '':  # remove empty string generated from the split function
            del split[0]  # empty strings occur when the string starts with '␛'

        for escape in split:
            onward = False
            # move cursor, print characters
            if escape[0] == '=':
                row, col = linecode.index(escape[1]), linecode.index(escape[2])  # get coordinates
                dataarea.move(row, col)  # move cursor to coordinates
                start = 3
                onward = True

            # enable/disable graphicsmode
            elif escape[0] == 'H':
                if escape[1] == STX:
                    gmode = True

                else:
                    gmode = False

                start = 2
                onward = True

            elif escape[0] == 'G':
                charattr = setattribute(escape[1])
                start = 2
                onward = True

            # enable/disable write-protect mode
            elif escape[0] == '(':
                wrpt = False
                start = 1

            elif escape[0] == ')':
                wrpt = True
                start = 1

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

                labelline.refresh()

            # clear screen
            elif escape[0] == '+':
                dataarea.clear()
                dataarea.refresh()
                start = 1

            # adjust Attributes of the status line and label line
            elif escape[0] == 'A':
                # regards label line
                if escape[1] == '1':
                    llattr = setattribute(escape[2])
                    labelline.chgat(0, 0, llattr)
                    labelline.refresh()

                # regards status line
                elif escape[1] == '3':
                    slattr = setattribute(escape[2])
                    statusline.chgat(1, 1, slattr)
                    statusline.refresh()

            elif escape[0] == 'R':
                dataarea.deleteln()

            elif escape[0] == 'E':
                dataarea.insertln()

            elif escape[0] == NL:
                start = 0
                onward = True

            if onward:
                for char in escape[start:]:
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
                        ser.write(str.encode(ACK))

                    else:
                        dataarea.addstr(graphicsmode(char), charattr)
                        # after printing a character, the cursor moves right 1 spot

                    time.sleep(duration)
                    dataarea.refresh()

                dataarea.getch()


    def sendkey():
        char = dataarea.getch()
        if char != -1:
            if chr(char) == NL:
                ser.write(str.encode(CR))   # enter key is interpreted as NL but sends out a CR

            elif chr(char) == ESC:
                two = dataarea.getch()  # get second character
                if two == -1:
                    ser.write(str.encode(ESC))  # send the escape key if the next key is detected as a pass (-1)

                elif chr(two) == '[':
                    thirdc = chr(dataarea.getch())  # finally, checks for the value of the third Character
                    if thirdc == 'A':
                        ser.write(str.encode(VT))   # up arrow

                    elif thirdc == 'B':
                        ser.write(str.encode(NL))   # down arrow

                    elif thirdc == 'C':
                        ser.write(str.encode(FF))   # right arrow

                    elif thirdc == 'D':
                        ser.write(str.encode(BS))   # left arrow

                    elif thirdc == '1':
                        fourthc = chr(dataarea.getch())
                        if fourthc == '5':
                            ser.write(b'\x01D')  # F5

                        elif fourthc == '7':
                            ser.write(b'\x01E')  # F6

                        elif fourthc == '8':
                            ser.write(b'\x01F')  # F7

                        elif fourthc == '9':
                            ser.write(b'\x01G')  # F8

                elif chr(two) == 'O':
                    thirdc = chr(dataarea.getch())  # finally, checks for the value of the third Character
                    if thirdc == 'P':
                        ser.write(b'\x01@')  # F1

                    elif thirdc == 'Q':
                        ser.write(b'\x01A')  # F2

                    elif thirdc == 'R':
                        ser.write(b'\x01B')  # F3

                    elif thirdc == 'S':
                        ser.write(b'\x01C')  # F4

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
