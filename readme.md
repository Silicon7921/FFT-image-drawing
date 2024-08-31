## FFT-Image-Drawing
Use Discrete Fourier Transform to draw a svg image and display the result using pygame.

### About main.py
main.py use pyqt6 for gui and pygame for the demo.

### About tosvg.py
tosvg.py generates Scalable Vector Graphics from a bitmap image.
the output cannot be used directly because it contains useless xml things and multiple paths.
It should be used only as a reference when you draw.

### About fourier.py:
fourier.py parses path data and generate fourier data.
the svg parsing system is really simple so some commands are unsupported.

### About pathfile:
path.txt contains the path data of a svg file.

you can use the following pathfiles as input file in Demo.
provided pathfile:
path_basic.txt - just some lines and curves.
path_rikka_fixed - takanashi rikka from Love, Chunibyo & Other Delusions
path_tachibana - tachibana arisu from THE IDOLM@STER CINDERELLA GIRLS
path_yukimi - sajo yukimi from THE IDOLM@STER CINDERELLA GIRLS

or you can draw a svg and extract the path data in it.

only one closed path (like a circle) is supported.
supported svg command: HhVvLlMmCcSs.
use "," to seperate values. do not put spaces between digits and alphabets.
any illegal data will result in crash or weird display.

format example:
M521.76,615.83 means move cursor to (521.76,615.83).