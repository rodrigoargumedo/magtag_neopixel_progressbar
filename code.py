import board
import digitalio
import neopixel

# Import MagTag libraries
from adafruit_magtag.magtag import MagTag

# Use Sparkle from the NeoPixel library
from adafruit_led_animation.animation.sparkle import Sparkle
# If you going to use the colors other than the ones here,
# please see the docs about the available colors here:
# https://s.rodrigoargumedo.me/neopxl_color
from adafruit_led_animation.color import GOLD

# Import the Animation groups and sequences
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup

# Import Progress Bar to calculate the year progress
from adafruit_progressbar import ProgressBar

# The Basics

# The Customization of the NeoPixel
# ---------------------------------
# 1. The pin interface that you are connecting to.
# 2. The D10 uses the JST port to comminucate from the MagTag
# to the NeoPixel strip interface.
strip_pin = board.D10

# Number of NeoPixel strips that you are going to use.
# This requires the NeoPixel LED strips from Adafruit here.
# https://www.adafruit.com/product/4801
strip_num = 30

# You can adjust the brightness of the MagTag LED strips
pixel_brightness = 0.5
# You can adjust the brightness of the NeoPixel LED strips
strip_brightness = 1

# The color of the sparkle.
sparkle_color = GOLD
# Sparkle speed. It is measured in seconds.
sparkle_speed = 0.1

def days_in_year(date_obj):
	# Check whether if the day count is a leap year.
	if (date_obj.tm_year % 100 != 0 or date_obj.tm_year % 400 == 0) and date_obj.tm_year % 4 == 0:
		return 366
	return 365


# Initialize the MagTag.
magtag = MagTag();

# Connect the MagTag to ESP32 WiFi interface.
magtag.network.connect();

# Setup the pixel interface.
pixels = magtag.peripherals.neopixels
pixels.brightness = pixel_brightness
magtag.peripherals.neopixel_disable = False
strip = neopixel.NeoPixel(strip_pin, strip_num, brightness = strip_brightness, auto_write = False)

