
# from machine import Pin
# from time import sleep

# led = Pin(2, Pin.OUT)

# while True:
#   led.value(not led.value())
#   sleep(0.5)

from machine import Pin
from time import sleep
led=Pin(2,Pin.OUT)
name = "Sara"
age = 30
height = 160.521
# Format a string with placeholders
message = f"Hello, my name is {name}. I am {age} years old and I'm {height:.1f} cm tall."
# Print the formatted message
print(message)
def Blink_LED():
  
  while True:
    led.value(not led.value())
    sleep(0.5)
    
if __name__=='__main__':
  Blink_LED()
  
  


'''


from machine import Pin
from time import sleep
import sys
from Blink_LED import Blink_LED  # Import only the function you need

BUTTON_PIN = 4
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

try:
    print("Waiting 1 second for button press...")
    sleep(1.0)
    if not button.value():  # Button pressed (active low)
        print("Button pressed — running Blink_LED.")
        Blink_LED()
    else:
        print("Button not pressed — exiting.")
        sys.exit()

except KeyboardInterrupt:
    print("KeyboardInterrupt — exiting.")
    sys.exit()


'''