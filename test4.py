#!/usr/bin/env python3

# codes borrowed from 
# https://www.mikan-tech.net/entry/raspi-st7789-lcd

import st7789
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont

def do_nothing(obj):
    pass  # No-op to prevent clearing

# Create a display instance
disp = st7789.ST7789(port=0, cs=0, rst=5, dc=6, rotation=90, backlight=None,
                        spi_speed_hz=80 * 1000 * 1000)

# Added: Change to SPI MODE 3
disp._spi.mode = 3
disp.reset()
disp._init()

# I2C interface (change address if needed)
serial = i2c(port=1, address=0x3C)
# 128x32 SSD1306 device
device = ssd1306(serial, width=128, height=32)
device.cleanup = do_nothing  # Override cleanup

# Show texts on oled display
with canvas(device) as draw:
    # draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((0, 0), "The Who - Who's Next", fill="white")
    draw.text((0, 16), "We Won't Get Fool Again Test 123", fill="white")

# Open image file
image = Image.open("whosnext.jpg")
# Resize to screen size
image = image.resize((disp.width, disp.height), resample=Image.LANCZOS)
# Show it on square display
disp.display(image)
