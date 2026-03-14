#!/usr/bin/env python3

# codes borrowed from 
# https://www.mikan-tech.net/entry/raspi-st7789-lcd

import st7789
from PIL import Image, ImageDraw, ImageFont

# Create a display instance
disp = st7789.ST7789(port=0, cs=0, rst=5, dc=6, backlight=None, spi_speed_hz=80 * 1000 * 1000)

# Added: Change to SPI MODE 3
disp._spi.mode = 3
disp.reset()
disp._init()

# Define fonts
FONT_ROBOTO = ImageFont.truetype("Roboto-Medium.ttf", 24)
FONT_NOTO = ImageFont.truetype("NotoSansCJK-Regular.ttc", 48)

# Define colors
COLOR_ORANGE = (255, 167, 38)

# Open image file
image = Image.open("whosnext.jpg")

# Resize to screen size
image = image.resize((disp.width, disp.height), resample=Image.LANCZOS)

###
# Create an image with black background
# image = Image.new("RGB", (disp.width, disp.height), (0, 50, 0))
# Draw some text
draw = ImageDraw.Draw(image)
draw.text((0, 180), "The Who - Who's Next", font=FONT_ROBOTO, fill=COLOR_ORANGE)
draw.text((0, 200), "We Won't Get Fool Again", font=FONT_ROBOTO, fill=COLOR_ORANGE)

# Show it on display
disp.display(image)
