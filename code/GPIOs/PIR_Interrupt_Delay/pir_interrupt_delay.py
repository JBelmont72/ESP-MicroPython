''' to get mac address of esp32 module
import network
sta_if = network.WLAN(network.STA_IF)
print('MAC address:', sta_if.config('mac'))
'''

# import network        ##33 to get mac address
# sta_if = network.WLAN(network.STA_IF)
# print('MAC address:', sta_if.config('mac'))
# mac = w.config('mac')
# print('Formatted MAC:', ['\\x{:02x}'.format(b) for b in mac])



import os
os.uname()
print(os.uname())


import network
import espnow
from machine import Pin
import time

# Setup Wi-Fi in station mode
w0 = network.WLAN(network.STA_IF)
w0.active(True)

# Initialize ESP-NOW with the Wi-Fi interface
e = espnow.ESPNow(w0)

# Replace this with the MAC address of your receiver board
# peer_mac = b'\xb0\xb2\x1c\xa9'  # <-- CHANGE THIS
peer_mac =  b'\xb0\xb2\x1c\xa9\x3a\x5c'  
e.add_peer(peer_mac)

# Optional: test sending a message every few seconds
led = Pin(2, Pin.OUT)

while True:
    print("Sending test message...")
    led.value(1)
    e.send(peer_mac, b"Hello from ESP32")
    led.value(0)
    time.sleep(3)

## this tells us the version of the esp32 board. older boards may need additional configuration to use espNow
# my output with first board :  (sysname='esp32', nodename='esp32', release='1.21.0', version='v1.21.0 on 2023-10-05', machine='Generic ESP32 module with ESP32')


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
# import sys

# try:
#     from machine import Pin
#     import time
# except ImportError:
#     print("Error: This script must run on a MicroPython device like ESP32 or Pico W.")
#     sys.exit(1)

# # Motion detection flags and timers
# motion1 = False
# motion2 = False
# motion1_timer = 0
# motion2_timer = 0
# MOTION_DURATION = 10000  # 10 seconds in milliseconds

# # LED pin (GPIO 18 works on both ESP32 and Pico W, adjust if needed)
# led = Pin(18, Pin.OUT)

# # PIR sensor pins
# pir1 = Pin(13, Pin.IN)
# pir2 = Pin(12, Pin.IN)

# # Interrupt service routines
# def handle_interrupt1(pin):
#     global motion1, motion1_timer
#     motion1 = True
#     motion1_timer = time.ticks_ms()
#     print("PIR #1 Activated")

# def handle_interrupt2(pin):
#     global motion2, motion2_timer
#     motion2 = True
#     motion2_timer = time.ticks_ms()
#     print("PIR #2 Activated")

# # Attach interrupts
# pir1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt1)
# pir2.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt2)

# # Main loop
# while True:
#     now = time.ticks_ms()
#     active = False

#     if motion1:
#         print("Motion detected on PIR #1")
#         active = True
#         if time.ticks_diff(now, motion1_timer) > MOTION_DURATION:
#             motion1 = False
#             print("Motion expired (PIR #1)")

#     if motion2:
#         print("Motion detected on PIR #2")
#         active = True
#         if time.ticks_diff(now, motion2_timer) > MOTION_DURATION:
#             motion2 = False
#             print("Motion expired (PIR #2)")

#     # Turn LED on if either sensor was triggered
#     led.value(1 if active else 0)

#     time.sleep_ms(100)
    
## ✅ ESP32 PIR Motion Sensor with Dual PIRs Sending Alerts via ESP-NOW
##  https://chatgpt.com/c/688c1551-f750-800f-a22a-b0bab8b39023
## initally I receved this error from the e.init().    AttributeError: 'ESPNow' object has no attribute 'init'
## learned that there has been an update to ESPNOW
# that error means you're likely using MicroPython v1.21+, where the espnow.ESPNow() class was revised, and you don’t need to call .init() anymore.

# Let me provide a clean and updated ESP-NOW program for ESP32, compatible with MicroPython 1.21 and newer (2024+), using the new espnow API.
# import network
# import espnow
# from machine import Pin
# import time

# # === Setup Wi-Fi in station mode ===
# w0 = network.WLAN(network.STA_IF)
# w0.active(True)

# # === Initialize ESP-NOW ===
# e = espnow.ESPNow()
# # e.init()

# # === Add peer MAC address (change to your receiver's MAC address) ===
# peer_mac = b'\xb0\xb2\x1c\xa9:\\'  # <--- CHANGE THIS to your receiver's MAC
# # peer_mac = b'\x24\x6f\x28\xaa\xbb\xcc'  # <--- CHANGE THIS to your receiver's MAC
# e.add_peer(peer_mac)

# # === Motion tracking ===
# motion1 = False
# motion2 = False
# motion1_timer = 0
# motion2_timer = 0
# MOTION_DURATION = 10000  # ms

# # === PIR & LED ===
# led = Pin(18, Pin.OUT)
# pir1 = Pin(13, Pin.IN)
# pir2 = Pin(12, Pin.IN)

# def send_motion_alert(pir_number):
#     msg = "MOTION{}".format(pir_number)
#     print(f"Sending: {msg}")
#     try:
#         e.send(peer_mac, msg)
#     except Exception as ex:
#         print("ESP-NOW send failed:", ex)

# # === Interrupt handlers ===
# def handle_interrupt1(pin):
#     global motion1, motion1_timer
#     if not motion1:
#         motion1 = True
#         motion1_timer = time.ticks_ms()
#         print("PIR #1 Activated")
#         send_motion_alert(1)

# def handle_interrupt2(pin):
#     global motion2, motion2_timer
#     if not motion2:
#         motion2 = True
#         motion2_timer = time.ticks_ms()
#         print("PIR #2 Activated")
#         send_motion_alert(2)

# pir1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt1)
# pir2.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt2)

# # === Main loop ===
# while True:
#     now = time.ticks_ms()
#     active = False

#     if motion1:
#         active = True
#         if time.ticks_diff(now, motion1_timer) > MOTION_DURATION:
#             motion1 = False
#             print("PIR #1 motion timeout")

#     if motion2:
#         active = True
#         if time.ticks_diff(now, motion2_timer) > MOTION_DURATION:
#             motion2 = False
#             print("PIR #2 motion timeout")

#     led.value(1 if active else 0)
#     time.sleep_ms(100)



import network
import espnow
from machine import Pin
import time

# === Enable Wi-Fi in STA mode (ESP-NOW requires this) ===
w0 = network.WLAN(network.STA_IF)
w0.active(True)

# === Setup ESP-NOW ===
e = espnow.ESPNow(w0)
# e.add_peer(b'\x24\x6f\x28\xaa\xbb\xcc')  # <-- REPLACE with your RECEIVER's MAC
e.add_peer( b'\xb0\xb2\x1c\xa9\x3a\x5c' )  

# === State Variables ===
motion1 = False
motion2 = False
motion1_timer = 0
motion2_timer = 0
MOTION_DURATION = 10000  # 10 sec

# === GPIO Setup ===
led = Pin(18, Pin.OUT)
pir1 = Pin(13, Pin.IN)
pir2 = Pin(12, Pin.IN)

# === Send alert via ESP-NOW ===
def send_motion_alert(n):
    try:
        msg = f"MOTION{n}"
        print(f"Sending: {msg}")
        e.send(b'\x24\x6f\x28\xaa\xbb\xcc', msg)  # same MAC here
    except Exception as ex:
        print("Send failed:", ex)

# === Interrupt handlers ===
def handle_interrupt1(pin):
    global motion1, motion1_timer
    if not motion1:
        motion1 = True
        motion1_timer = time.ticks_ms()
        print("PIR #1 Triggered")
        send_motion_alert(1)

def handle_interrupt2(pin):
    global motion2, motion2_timer
    if not motion2:
        motion2 = True
        motion2_timer = time.ticks_ms()
        print("PIR #2 Triggered")
        send_motion_alert(2)

# Attach interrupts
pir1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt1)
pir2.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt2)

# === Main loop ===
while True:
    now = time.ticks_ms()
    active = False

    if motion1:
        active = True
        if time.ticks_diff(now, motion1_timer) > MOTION_DURATION:
            motion1 = False
            print("PIR #1 motion expired")

    if motion2:
        active = True
        if time.ticks_diff(now, motion2_timer) > MOTION_DURATION:
            motion2 = False
            print("PIR #2 motion expired")

    led.value(1 if active else 0)
    time.sleep_ms(100)

