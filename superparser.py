# -*- coding: utf-8 -*-

linecode = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',
            '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
            '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
            '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p']

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
split = data.split('␛')

if split[0] == '':
    del split[0]

keep = []
for i in split:
    if i[-1] == '\n':
        keep.append(i)

print(keep)
subject = list(keep[0])
print(subject)


def newline(x):
    if x[0] == '=':
        row = x[1]
        col = x[2]
        rownumber = linecode.index(row)
        print(rownumber)
        for j in range(0, len(x)):
            if x[j] == '\n':
                rownumber += 1
                x[j] = '␛=' + linecode[rownumber] + col

    return ''.join(x)

aaa = newline(subject)
print(aaa)


def superparser(raw):
    raw = raw.split('␛')
    if raw[0] == '':
        del raw[0]

    for index in raw:
