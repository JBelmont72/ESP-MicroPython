'''
time exercises
/Users/judsonbelmont/Documents/RandomNerd/ESP-MicroPython/code/Blink_LED/Time_NTP..py
https://pytutorial.com/python-timelocaltime-getting-local-time-in-python/
note strftime works in python but not micropython

To get the correct local time in MicroPython, you can use the ntptime module to synchronize with an NTP server and then adjust for your local timezone. For example, after setting the time with ntptime.settime(), you can add your timezone offset in seconds to the UTC time obtained from time.gmtime().
 forum.core-electronics.com.au forums.pimoroni.com
Understanding Local Time in MicroPython
Setting Up Local Time
To get the correct local time in MicroPython, you need to adjust the UTC time returned by the time module. The time.localtime() function may not provide the expected results if the timezone is not set correctly.
Using NTP for Time Synchronization
Fetch UTC Time: Use an NTP server to get the current UTC time. This can be done with the ntptime module.
python
Copy Code
import ntptime
ntptime.settime()
Adjust for Timezone: After fetching the UTC time, you can adjust it for your local timezone. For example, if you are in UTC+10, you can add the offset in seconds.
python
Copy Code
import time
tz_offset = 10 * 3600  # 10 hours in seconds
local_time = time.localtime(time.time() + tz_offset)
Example Code
Here’s a simple example to set and display the local time:
python
Copy Code
import ntptime
import time

# Set the time from NTP
ntptime.settime()

# Define your timezone offset (e.g., UTC+10)
tz_offset = 10 * 3600

# Get local time
local_time = time.localtime(time.time() + tz_offset)

# Print formatted local time
print("Local Time: {:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(
    local_time[0], local_time[1], local_time[2],
    local_time[3], local_time[4], local_time[5]
))
Important Notes
Ensure your device is connected to the internet to access the NTP server.
If you are using a Real Time Clock (RTC), you may need to set it manually or maintain it with a backup battery.
Adjust the timezone offset according to your local time zone, considering Daylight Saving Time if applicable.
https://duckduckgo.com/?q=how+to+get+the+local+time+for+use+in+the+time+module+of+micrpython.+time.localtime()+is+incorrect&t=osx&ia=web
https://docs.micropython.org/en/latest/library/time.html Has all micropython modules

'''

# import time

# # Connect to Wi-Fi before using ntptime
# import network

# ssid = 'NETGEAR48'
# password = 'waterypanda901'

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# if not wlan.isconnected():
# 	print('Connecting to network...')
# 	wlan.connect(ssid, password)
# 	while not wlan.isconnected():
# 		pass
# print('Network config:', wlan.ifconfig())

# try:
# 	import ntptime
# 	ntptime.settime()
# except Exception as e:
# 	print("Failed to set time via ntptime:", e)

# a = time.time()
# local_time = time.localtime()
# c = time.ticks_ms()
# print(a, '   ', local_time, '  ', c)

# # Set the correct timestamp for August 1, 2025 11:00:00 AM UTC
# # timestamp = 1754046000
# # timestamp = 1672531199  # Example timestamp
# # local_time = time.localtime(timestamp)
# local_time = time.localtime()
# # MicroPython does not support time.strftime, so format manually:(I substracted 4 hours to correct for time zone)
# def format_time(t):
# 	return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
# 		t[0], t[1], t[2], t[3]-4, t[4], t[5]
# 	)

# print("Local time from timestamp:", format_time(local_time))
### second work scripts
import time
from machine import Pin

led_pin = 18
led = Pin(led_pin, Pin.OUT)
interval = 5000  # milliseconds
last_toggle = time.ticks_ms()
state = False

while True:
	if time.ticks_diff(time.ticks_ms(), last_toggle) > interval:
		state = not state
		led.value(state)
		print(led.value())
		last_toggle = time.ticks_ms()
	time.sleep_ms(10)  # Small sleep to reduce CPU usage
    
    
    
# import time 
# from machine import Pin
# import sys

# ledPin = 18
# RLed =Pin(ledPin,Pin.OUT)
# interval=5000
# timeStart = time.ticks_ms()
# active =True
# try:
#     while True:
#         timeNow=time.ticks_ms()
#         if time.ticks_diff(timeNow,timeStart) >interval:
#             RLed.value( 1 if active else 0)
#             print(RLed.value())
#             timeStart=time.ticks_ms()
#             active = not active
#         else:
#             continue
        
# except KeyboardInterrupt:
#     print('Exit')
#     sys.exit()
    

