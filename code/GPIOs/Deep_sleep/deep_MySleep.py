'''

a copy from /Users/judsonbelmont/Documents/RandomNerd/ESP-MicroPython/code/GPIOs/Deep_sleep/deep_sleep_esp32.py
'''
from machine import Pin
import time

# Set up the button on GP14
button = Pin(14, Pin.IN, Pin.PULL_UP)

def button_pressed():
    return not button.value()  # Button is active-low

# Example loop: act on press
while True:
    if button_pressed():
        print("Button pressed — take action!")
        # Add any function you want here
        time.sleep(0.3)  # debounce delay