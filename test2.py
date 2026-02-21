#!/usr/bin/env python3
import sys

from PIL import Image
import st7789

disp = st7789.ST7789(
    height=240,
    rotation=90,
    port=0,
    cs=st7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,  # Breakout Garden: 18 for back slot, 19 for front slot.
                    # NOTE: Change this to 13 for Pirate Audio boards
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=0,
    offset_top=0,
)
