# Pyse-60
###### written for python3
A curses application written in Python that interprets a Wyse 60 output from a serial device.

---

Currently interprets:
---
Command                    | Description
---------------------------| ---
ESC = *line* *col*         | Address cursor in current 80-column page
ESC H `STX` (ESC H CTRL B) | Graphics mode on
ESC H `ETX` (ESC H CTRL C) | Graphics mode off
ESC +                      | Clear page to spaces
ESC z ( *text*             | Program/display unshifted label line
ESC F message `CR`         | Program and display computer message on status line
ESC A *field* *attr*       | Assign display attribute to message field
ESC A 1 0                  | Function key label line, normal
ESC A 1 4                  | Function key label line, reverse
ESC A 3 :                  | Computer message, underline and blink
ESC A 3 8                  | Computer message, underlined
ECS G *attr*               | change character attribute
ESC R                      | Delete cursor line
ESC E                      | Insert line of spaces

Need to add:
------------
Command        | Description                              | Flag
---------------|------------------------------------------|---
ESC ` :        | Select 80-column display
ESC ` 0        | Cursor display off
ESC )          | Write-protect mode on
ESC (          | Write-protect mode off
ESC '          | Protect mode off
ESC &          | Protect mode on
ESC ;          | Clear unprotected page to spaces
ESC e 1        | Character attribute mode. on
ESC e 3        | Line attribute mode on
ESC e 7 `\x14` | ACK mode on
ESC r          | Insert mode off, replace mode on
ESC d (space)  | Secondary receive mode off               | *
ESC X          | Monitor mode off                         | ?
ESC c 10001    |
ESC ~ (space)  | Turn enhance mode off                    | *
ESC C ESC D F  | Full-duplex mode on
ESC l          | Duplex edit mode on, local edit mode off | ?
ESC ` b        | Standard status line on
ESC ` A        |
ESC d /        | End-of-line wrap mode on
ESC N          | Autoscrolling mode off
ESC ^ 0        | Restore normal screen
ESC z `\x7f`   | Shifted label line off                   | ?
ESC c ? 0      | Clear font bank                          | *
ESC c @ 0 `    | Load font bank                           | *
ESC c B 0      | Define primary character set             | *
ESC c D        | Select primary character set
ESC c A        | Define and load character

> Where `*` denotes *"considering ignoring"*
>
>and `?` denotes *"I'm not 100% sure what the description means"*

Ignoring:

Command | Description                                                       | Reason
--------|-------------------------------------------------------------------|---
ESC e 8 | Select MODEM port for data communications, AUX port as printer port
ESC e % | Turn keyclick on (default)
ESC e P | Turn screen saver off
ESC e F | Economy 80-column mode off
ESC e * | Display 42 data lines
