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

 ```
 Need to add:
 ```
 ESC ` :
 ESC ` 0
 ESC A 3 8
 ESC F message CR            Program and display computer message on status line
 ESC ENQ
 ESC A 1 0
 ESC A 1 4
 ESC A 3 :
 
```