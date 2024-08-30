## FFT-Image-Drawing
Use Discrete Fourier Transform to draw a svg image and display the result using pygame.

### About main.py
main.py use pyqt6 for gui and pygame for the demo.

### About tosvg.py
tosvg.py generates Scalable Vector Graphics from a bitmap image.
the output cannot be used directly because it contains useless xml things and multiple paths.
the easiest way to use the output is to put it into Adobe Illustrator and draw a svg with only one closed path.

### About fourier.py:
fourier.py handles parsing path data and generating fourier data .
the svg parsing system is really simple and some commands are unsupported.

### About path.txt:
path.txt contains the path data of a svg file.
only one closed path (like a circle) is supported.
supported svg command: HhVvLlMmCcSs.
use "," to seperate values. do not put spaces between digits and alphabets.
any illegal data will result in crash or weird display.

format example:
M521.76,615.83 means move cursor to (521.76,615.83).
