## FFT-Image-Drawing
Use Discrete Fourier Transform to draw a svg image and display the result using pygame.

### About main.py
main.py use pygame to show everything.
you may change some variables to adjust the window size, gamespeed, color and more.

### About tosvg.py
tosvg.py generates Scalable Vector Graphics from bitmap image.
the output cannot be used directly because it contains useless xml things and multiple paths.
the easiest way to use the output is just putting it into Adobe Illustrator and draw a svg with only one closed path by yourself.

### About fourier.py:
fourier.py handles path data parsing and wave data generation.
the svg parsing system is really simple so some commands are unsupported.

### About path.txt:
path.txt contains the path data of svg.
only one closed path (like a circle) is supported.
svg command supported: HhVvLlMmCcSs.
use "-" or "," to seperate values. do not put spaces between commands.
any illegal data will cause crash or weird result.

format example:
M521.76,615.83c-15.93-43.03-49.96-152.72-18.78-287.61

M521.76,615.83 means move cursor to (521.76,615.83).
c-15.93-43.03-49.96-152.72-18.78-287.61 means draw a curve using following arguments(seperated by "-" here). 