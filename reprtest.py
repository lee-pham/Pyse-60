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
␛=%$0"""

aaa = data.split('␛')

if aaa[0] == '':
    del aaa[0]

# escsplit = ['H\xe2\x90\x82', '=%`0\n4\n4\n', '=%$0']


def megaparse(escsplit):
    for i, string in enumerate(escsplit):

        if string[0] == '=' and string[-1] == '\n':
            templist = list(string[:-1])
            rowint = linecode.index(string[1])
            col = string[2]

            for j, char in enumerate(templist):
                if char == '\n':
                    rowint += 1
                    templist[j] = '=' + linecode[rowint] + col

            escsplit[i] = ''.join(templist)

    return escsplit


def gigaparse(data):
    datasplit = data.split('␛')
    if datasplit[0] == '':
        del datasplit[0]

    for i, string in enumerate(datasplit):
        if string[-1] == '\n':
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

data2 = """␛H␂␛=%`0
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
␛H␃"""

print(gigaparse(data2))
