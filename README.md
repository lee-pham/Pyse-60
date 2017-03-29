# Pyse-60
## written for python3
A curses application written in Python that interprets a Wyse 60 output from a serial device.

Currently interprets:
```
ESC = line col              Address cursor in current 80-column page
ESC H STX (ESC H CTRL B)    Graphics mode on
ESC H ETX (ESC H CTRL C)    Graphics mode off
ESC +                       Clear page to spaces
ESC z ( text                Program/display unshifted label line
ESC F message CR            Program and display computer message on status line
ESC A field attr            Assign display attribute to message field
ESC A 1 0                   Function key label line, normal
ESC A 1 4                   Function key label line, reverse
ESC A 3 :                   Computer message, underline and blink
ESC A 3 8                   Computer message, underlined
```
Need to add:
```
ESC ` :
ESC ` 0
ESC )                       Write-protect mode on
ESC (                       Write-protect mode off
```
Arrow and [official] function keys are currently unsupported. The function keys have been mapped to QWERTYUI, F1-F8.