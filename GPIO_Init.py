import RPi.GPIO as GPIO

import time

import Adafruit_GPIO.SPI as SPI
import SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Input pins:
L_pin, R_pin, C_pin, U_pin, D_pin = 27, 23, 4, 17, 22
A_pin, B_pin = 5, 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up

# Raspberry Pi pin configuration:
RST = 24

# 128x64 display with hardware I2C:
disp = SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)


# Initialize library.
disp.begin()


# Clear display.
# disp.clear()
# disp.display()

def getLargeFont():
    return ImageFont.truetype("Fonts/Georgia Bold.ttf", 12)


def getFont():
    return ImageFont.truetype("Fonts/Georgia Bold.ttf", 10)


def getSmallFont():
    return ImageFont.truetype("Fonts/Georgia Bold.ttf", 8)


def clearDisplay():
    disp.clear()


def displayImage(img):
    disp.clear()
    disp.image(img)
    disp.display()


def getKeyStroke():
    try:
        while 1:
            if not GPIO.input(U_pin):
                return "UP"
            if not GPIO.input(L_pin):
                return "LEFT"
            if not GPIO.input(R_pin):
                return "RIGHT"
            if not GPIO.input(D_pin):
                return "DOWN"
            if not GPIO.input(C_pin):
                return "CENTER"
            if not GPIO.input(A_pin):
                return "A"
            if not GPIO.input(B_pin):
                return "B"
    except KeyboardInterrupt:
        GPIO.cleanup()


def getAnyKeyEvent():
    if getKeyStroke() != "":
        return True
