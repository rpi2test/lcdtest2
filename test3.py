#!/usr/bin/env python3

# codes borrowed from 
# https://www.mikan-tech.net/entry/raspi-st7789-lcd

import st7789
from PIL import Image

# Create a display instance
disp = st7789.ST7789(port=0, cs=0, rst=5, dc=6, backlight=None, spi_speed_hz=80 * 1000 * 1000)

# Added: Change to SPI MODE 3
disp._spi.mode = 3
disp.reset()
disp._init()

# Open image file
image = Image.open("whosnext.jpg")

# Resize to screen size
image = image.resize((disp.width, disp.height), resample=Image.LANCZOS)

# Show it on display
disp.display(image)
# end of the list
