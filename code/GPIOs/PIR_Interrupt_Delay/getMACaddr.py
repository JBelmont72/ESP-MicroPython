'''


'''
# mac_formatter.py

# import network

# w = network.WLAN(network.STA_IF)
# w.active(True)

# mac = w.config('mac')
# print("Raw MAC bytes:", mac)

# # Print MAC formatted for MicroPython use
# formatted = ''.join(['\\x{:02x}'.format(b) for b in mac])
# print(f"Copy this for your sender script:\npeer_mac = b'{formatted}'")
###~~~~~~~~

import network
w = network.WLAN(network.STA_IF)
w.active(True)

mac = w.config('mac')

print("MAC:", mac)
formatted = ''.join(['\\x{:02x}'.format(b) for b in mac])
print("Use this in your sender code:")
print(f"peer_mac = b'{formatted}'")

import network
import espnow
import time
from machine import Pin

# Setup Wi-Fi in station mode
w0 = network.WLAN(network.STA_IF)
w0.active(True)

# Initialize ESP-NOW
e = espnow.ESPNow(w0)

# Copy this exactly from the formatter output
peer_mac = b'\xb0\xb2\x1c\xa9\x3a\x5c'  # ✅ Replace with correct MAC

e.add_peer(peer_mac)

led = Pin(2, Pin.OUT)

while True:
    try:
        print("Sending test message...")
        led.value(1)
        e.send(peer_mac, b"Hello from ESP32")
        led.value(0)
    except Exception as err:
        print("Send failed:", err)
    time.sleep(3)
