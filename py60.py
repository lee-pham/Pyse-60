# -*- coding: utf-8 -*-
import curses

number = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',
          '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
          '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
          '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
          'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
          '\\', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f',
          'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

stdscr = curses.initscr()
stdscr.resize(44, 82)
stdscr.border(0)

data = """␛="<MCE CRT Display Option␛=$BMain Menu␛)␛=*4F1  -  Job Configuration Parameters␛=,4F2  -  Performance Reports Menu␛=.4F3  -  Graphic Display of Elevator Status␛=04F4  -  Main Menu␛=24F5  -  CRT Terminal Initialization␛=44F6  -  Computer Parameters␛=64F7  -  Special Event Calendar Menu␛=84F8  -  Car  A  Inputs and Outputs␛=8? A ␛=:.Shift F2  -  System Performance Counters␛=<.Shift F5  -  Security Menu␛=>.Shift F6  -  CMS Parameters␛(␛H␂␛=',2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3␛=(*2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3 6␛=)*6␛=)e6 6␛=**6␛=*e6 6␛=+*6␛=+e6 6␛=,*6␛=,e6 6␛=-*6␛=-e6 6␛=.*6␛=.e6 6␛=/*6␛=/e6 6␛=0*6␛=0e6 6␛=1*6␛=1e6 6␛=2*6␛=2e6 6␛=3*6␛=3e6 6␛=4*6␛=4e6 6␛=5*6␛=5e6 6␛=6*6␛=6e6 6␛=7*6␛=7e6 6␛=8*6␛=8e6 6␛=9*6␛=9e6 6␛=:*6␛=:e6 6␛=;*6␛=;e6 6␛=<*6␛=<e6 6␛==*6␛==e6 6␛=>*6␛=>e6 6␛=?*6␛=?e6 6␛=@*1::::::::::::::::::::::::::::::::::::::::::::::::::::::::::5␋:5␛H␃␛=@+ Ver 3.64 EMI A-2K␛G|␛A38␛F03/08/17 16:38:14        F4 = Main Menu"""
parsed = data.split("␛=")

for i in range(1, len(parsed)):
    stdscr.addstr(number.index(parsed[i][0]), number.index(parsed[i][1]), parsed[i][2:])
    stdscr.refresh()

stdscr.getch()
curses.endwin()

