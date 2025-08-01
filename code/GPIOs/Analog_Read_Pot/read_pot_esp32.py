# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/
# /Users/judsonbelmont/Documents/RandomNerd/ESP-MicroPython/code/GPIOs/Analog_Read_Pot/read_pot_esp32.py
'''
I added PWM and OLED at bottom
https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/
THis web site has very good explanations of Attn bits and width etc https://alselectro.wordpress.com/2020/03/29/esp32-micropython-adc-with-analog-sensors/
The ADC resolution by default is 12 bits
2 power 12 is 4096.
We can convert the reading to voltage by multiplying with 0.000805
2 power 12 is 4096
Voltage is 3.3v ,   3.3/4096 = 0.000805

As per documentation of ESP32 the maximum ADC volt can be set using attenuation.
ADC.atten(attenuation)
This method allows for the setting of the amount of attenuation on the input of the ADC.
This allows for a wider possible input voltage range, at the cost of accuracy
(the same number of bits now represents a wider range). The possible attenuation options are:
ADC.ATTN_0DB: 0dB attenuation, gives a maximum input voltage of 1.00v – this is the default configuration  (but while testing it shows 3.3v)
ADC.ATTN_2_5DB: 2.5dB attenuation, gives a maximum input voltage of approximately 1.34v
ADC.ATTN_6DB: 6dB attenuation, gives a maximum input voltage of approximately 2.00v
ADC.ATTN_11DB: 11dB attenuation, gives a maximum input voltage of approximately 3.6v
 
Setting the attenuation to 11DB gives value of 1.72 volt ( but the document says 3.3v)
So leave it to default 0DB which practically gives 3.3v

https://alselectro.wordpress.com/wp-content/uploads/2020/03/ad4.jpg
The resolution can be changed to 10 bit by setting width to 10BIT.
Default is 12 BIT.
 
ADC.width(width)
so write ADC.width(ADC.WIDTH_12BIT)
print(ADC.read())
This method allows for the setting of the number of bits to be utilised and returned during ADC reads. Possible width options are:
ADC.WIDTH_9BIT: 9 bit data
ADC.WIDTH_10BIT: 10 bit data
ADC.WIDTH_11BIT: 11 bit data
ADC.WIDTH_12BIT: 12 bit data – this is the default configuration


'''
# from machine import Pin, ADC
# from time import sleep

# pot = ADC(Pin(34))
# pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

# while True:
#   pot_value = pot.read()
#   print(pot_value)
#   sleep(0.1)


from machine import Pin, ADC
from time import sleep

class LED_Pot:
  def __init__(self, potPin, green, red):
    self.potPin = potPin
    self.green = green
    self.red = red

  def main(self):
    print('Running Main')
    pot = ADC(Pin(self.potPin))
    pot.atten(ADC.ATTN_11DB)  # Full range: 3.3v
    greenLed = Pin(self.green, Pin.OUT)
    redLed = Pin(self.red, Pin.OUT)
    try:
      while True:
        potVal = pot.read()
        # Map potVal (0-4095) to LED control (0 or 1)
        if potVal > 2047:
          greenLed.value(1)
          redLed.value(0)
        else:
          greenLed.value(0)
          redLed.value(1)
        print(f'PotVal: {potVal}')
        sleep(0.3)
    except KeyboardInterrupt:
      pass

if __name__ == '__main__':
  LED_Pot(34, 18, 19).main()


'''
Consider using GPIOs 32, 33, 34, 35, or 36
These are safe for ADC. GPIO 36 and 39 sometimes behave erratically on some ESP32 variants.

'''


from machine import Pin, ADC
from time import sleep
import sys

class LED_Pot:
  def __init__(self, potPin, green, red):
    self.potPin = potPin
    self.green = green
    self.red = red

  def main(self):
    print('Running Main')
    pot = ADC(Pin(self.potPin))
    pot.atten(ADC.ATTN_11DB)  # Full range: 3.3v
    greenLed = Pin(self.green, Pin.OUT)
    redLed = Pin(self.red, Pin.OUT)
    try:
      while True:
        potVal = pot.read()
        # Map potVal (0-4095) to LED control (0 or 1)
        if potVal > 2047:
          greenLed.value(1)
          redLed.value(0)
        else:
          greenLed.value(0)
          redLed.value(1)
        print(f'PotVal: {potVal}')
        sleep(0.3)
    except KeyboardInterrupt:
      sys.exit()

if __name__ == '__main__':
  LED_Pot(34, 18, 19).main()
  
'''
from machine import ADC, Pin
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)

while True:
    val = pot.read()
    print("Potentiometer value:", val)
    sleep(0.2)
'''
## auto I2C address determination and PWM and OLED display
## https://chatgpt.com/c/688ac55d-9274-800f-9e96-bcf5256e7c4a

'''
Notes
led_pwm.duty(x) expects 0–1023 on ESP32.
You can scale the pot_val to any desired range.
If you have multiple I2C OLEDs, you could add an option to select the address manually or cycle through them.
🔄 Future Expansions You Can Try
Add a second potentiometer to control a second LED.
Display graphs or bars on the OLED.
Send values over MQTT or WebSocket.
Add button input for modes or settings
This script:
Reads the potentiometer via ADC.
Controls PWM brightness of an LED based on pot value.
Displays the ADC value and brightness % on an OLED (SSD1306).
Automatically detects the I2C address of your OLED.
Works with I2C-connected components (flexible for future expansion).
'''

# Users/judsonbelmont/Documents/RandomNerd/ESP-MicroPython/code/GPIOs/Analog_Read_Pot/read_pot_esp32.py
from machine import Pin, ADC, PWM, I2C
from time import sleep
import ssd1306

# === Constants ===
POT_PIN = 34
LED_PIN = 18
I2C_SDA = 21
I2C_SCL = 22
PWM_FREQ = 1000

# === Setup I2C and Scan for OLED ===
i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
oled_addr_list = i2c.scan()

if not oled_addr_list:
    raise Exception("No I2C devices found. Check wiring.")
else:
    print(f"I2C device(s) found: {oled_addr_list}")
    oled_addr = oled_addr_list[0]  # Assume first one is OLED

# === Setup OLED ===
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=oled_addr)

# === Setup ADC ===
pot = ADC(Pin(POT_PIN))
pot.atten(ADC.ATTN_11DB)  # Full range 0–3.3V
pot.width(ADC.WIDTH_12BIT)

# === Setup PWM ===
led_pwm = PWM(Pin(LED_PIN), freq=PWM_FREQ)
led_pwm.duty(0)

# === Main Loop ===
while True:
    pot_val = pot.read()  # 0–4095
    duty = int((pot_val / 4095) * 1023)  # Scale to 0–1023 for PWM
    led_pwm.duty(duty)

    brightness_pct = int((duty / 1023) * 100)

    # Update OLED display
    oled.fill(0)
    oled.text("Potentiometer:", 0, 0)
    oled.text(f"ADC: {pot_val}", 0, 16)
    oled.text(f"PWM: {brightness_pct}%", 0, 32)
    oled.show()

    print(f"ADC: {pot_val}, PWM duty: {duty}, Brightness: {brightness_pct}%")
    sleep(0.2)


