from time import sleep
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

# I2C interface (change address if needed)
serial = i2c(port=1, address=0x3C)

# 128x32 SSD1306 device
device = ssd1306(serial, width=128, height=32)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((5, 10), "Hello 128x32!", fill="white")

sleep(10)
