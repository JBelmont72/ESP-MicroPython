# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/
# /Users/judsonbelmont/Documents/RandomNerd/ESP-MicroPython/code/GPIOs/PIR_Interrupt_Delay/pir_interrupt_delay.py
# from machine import Pin
# from time import sleep

# motion = False

# def handle_interrupt(pin):
#   global motion
#   motion = True
#   global interrupt_pin
#   interrupt_pin = pin 

# led = Pin(18, Pin.OUT)
# pir = Pin(13, Pin.IN)

# pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

# while True:
#   if motion:
#     print('Motion detected! Interrupt caused by:', interrupt_pin)
#     led.value(1)
#     sleep(20)
#     led.value(0)
#     print('Motion stopped!')
#     motion = False

## add a second PIR 
# /Users/judsonbelmont/Documents/RandomNerd/ESP-MicroPython/code/GPIOs/PIR_Interrupt_Delay/pir_interrupt_delay.py
import sys

try:
    from machine import Pin
    import time
except ImportError:
    print("Error: This script must run on a MicroPython device like ESP32 or Pico W.")
    sys.exit(1)

# Motion detection flags and timers
motion1 = False
motion2 = False
motion1_timer = 0
motion2_timer = 0
MOTION_DURATION = 10000  # 10 seconds in milliseconds

# LED pin (GPIO 18 works on both ESP32 and Pico W, adjust if needed)
led = Pin(18, Pin.OUT)

# PIR sensor pins
pir1 = Pin(13, Pin.IN)
pir2 = Pin(12, Pin.IN)

# Interrupt service routines
def handle_interrupt1(pin):
    global motion1, motion1_timer
    motion1 = True
    motion1_timer = time.ticks_ms()
    print("PIR #1 Activated")

def handle_interrupt2(pin):
    global motion2, motion2_timer
    motion2 = True
    motion2_timer = time.ticks_ms()
    print("PIR #2 Activated")

# Attach interrupts
pir1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt1)
pir2.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt2)

# Main loop
while True:
    now = time.ticks_ms()
    active = False

    if motion1:
        print("Motion detected on PIR #1")
        active = True
        if time.ticks_diff(now, motion1_timer) > MOTION_DURATION:
            motion1 = False
            print("Motion expired (PIR #1)")

    if motion2:
        print("Motion detected on PIR #2")
        active = True
        if time.ticks_diff(now, motion2_timer) > MOTION_DURATION:
            motion2 = False
            print("Motion expired (PIR #2)")

    # Turn LED on if either sensor was triggered
    led.value(1 if active else 0)

    time.sleep_ms(100)
