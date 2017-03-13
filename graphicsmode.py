# -*- coding: utf-8 -*-


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
                ' ': ' '}

    box = []
    for i in raw:
        box.append(graphics[i])

    box = ''.join(box)
    return box

sample = '2::::::::3'
output = graphicsmode(sample)
print(output)
