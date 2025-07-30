# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/
# i had this error. 'Device is not busy, but the adapter queue is active...'
# because I was trying to run it from the terminal and not uploaded to the ESP32
# When the ESP32 enters deep sleep, which cuts off the serial connection. PyMakr then gets confused trying to interact with a device that’s temporarily offline, and it leaves "adapter queue" tasks pending — hence the error:
#deepsleep(10000) tells the ESP32 to:

# Enter deep sleep mode for 10 seconds
# Shut down most hardware including USB serial
# Then reboot as if freshly powered on
# VSCode’s PyMakr doesn’t expect the board to "disappear," so it keeps trying to interact with it.
'''How to Fix / Avoid This
🔹 1. Don't run this via the "Run" button in PyMakr

Instead of running it from the PyMakr interface, upload the script and let it run independently.

Steps:

Save your script as main.py
Use the Upload button in PyMakr (not Run)
The ESP32 will automatically execute main.py on boot
This avoids trying to talk to the board over serial after it enters sleep.

🔹 2. Add a delay before sleep (you already do this — good!)

Keep the sleep(5) before deep sleep so you can:

Open a REPL
Re-upload code
Interrupt before it sleeps
But for production code, you might remove or shorten this.

🔹 3. (Optional) Modify boot.py for control

If you want full control, you can add logic in boot.py to determine whether to enter sleep (e.g., based on a button press or serial connection).
✅ Clean PyMakr After Wake
After the ESP32 reboots, it should reconnect to PyMakr if:

It's still connected via USB
You haven't disabled main.py
You're not in a REPL lockout (which can happen)
If it doesn't, try:

Clicking the "Connect" icon in PyMakr
Or resetting the ESP32 with the EN button
'''



from machine import deepsleep
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)

#blink LED
led.value(1)
sleep(1)
led.value(0)
sleep(1)

# wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# you should remove this sleep line in your final script
sleep(5)

print('Im awake, but Im going to sleep')

#sleep for 10 seconds (10000 milliseconds)
deepsleep(10000)

'''To add a button press on your Pico W (or ESP32) for control in your MicroPython project, here’s how to set it up and what it can be used for — such as controlling upload, switching between modes, or initiating an action.
✅ Use Case Example
Let’s say you want the button to:

Send a special command to your client/server
Toggle between upload modes (e.g. local vs PyMakr)
Reboot or enter a config mode
🧠 1. Wire Up the Button
Connect a tactile push button between GPIO pin (e.g. GP14) and GND.
Use an internal pull-up resistor in code.
📜 2. MicroPython Code Example
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
'''
You can replace print(...) with:

Triggering a client/server message
Resetting a state
Switching an LED or motor state
Starting/stopping upload logic (with a flag)
🧭 3. Tip: Use boot.py for Startup Behavior
If you want the button to control upload behavior at boot, place this logic in boot.py'''
# boot.py
from machine import Pin
import os

button = Pin(14, Pin.IN, Pin.PULL_UP)

if not button.value():
    print("Button held at boot — enter safe mode or disable Wi-Fi")
    # os.remove('main.py') or start minimal mode
else:
    print("Normal boot")

