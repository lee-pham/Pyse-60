# Pyse-60
A curses application written in Python that interprets a Wyse 60 output from a serial device.

This application has yet to be tested on a real time device as text logs are currently being used to simulate the serial device output.
 
 Currently interprets:
 ```
 ESC = line col              Address cursor in current 80-column page
 ESC )                       Write-protect mode on  (only changes colors)
 ESC (                       Write-protect mode off (only changes colors)
 ESC H STX (ESC H CTRL B)    Graphics mode on
 ESC H ETX (ESC H CTRL B)    Graphics mode on
 ESC +                       Clear page to spaces
 ESC z ( text                Program/display unshifted label line
 ESC F message CR            Program and display computer message on status line


 ```
 Need to add:
 ```
 ESC ` :
 ESC ` 0
 ESC A field attr            Assign display attrivute to message field
 ESC A 3 8                   Computer message, underlined
 ESC ENQ
 ESC A 1 0                   Function key label line, normal
 ESC A 1 4                   Function key label line, reverse
 ESC A 3 :                   Computer message, underline and blink
```