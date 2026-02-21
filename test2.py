#!/usr/bin/env python3
import st7789

display = st7789.ST7789(
    port=0,
    cs=0,
    dc=25,
    backlight=24,
    rst=8,
    spi_speed_hz=80 * 1000 * 1000,
    width=240,
    height=240,
    offset_left=0,
    offset_top=0
)

# Init and test
display.init()
display.fill(0x0000)  # Black
display.text("GMT130 OK!", 10, 10, 0xFFFF)  # White text
