# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

# from machine import Pin
# from time import sleep,time

# led = Pin(18, Pin.OUT)
# button = Pin(4, Pin.IN)
# while True:
#   led.value(button.value())
#   NewButVal=button.value()
#   print(f'New button val: {NewButVal}')
#   sleep(0.5)
### work on debouncing
# from machine import Pin ##this works but runs contiously (that is why need interrup)
# import time

# button = Pin(4, Pin.IN, Pin.PULL_UP)  # Button connected to pin 4
# led = Pin(18, Pin.OUT)  # LED connected to pin 18
# last_state = button.value()  # Initial button state

# while True:
#     current_state = button.value()
#     print(f'current state: {current_state}')
#     if current_state != last_state:  # State change detected
#         time.sleep(0.02)  # Wait for 20ms for debounce
#         current_state = button.value()  # Read the state again
#         if current_state == 0:  # Button pressed
#             led.value(not led.value())  # Toggle LED
#     last_state = current_state

  
'''
PW lesson 84 Pico button debouncing, works fine

important:
# tUp=time.ticks_ms() ## time button from 1 to zero, when the button comes up (though the value goes to zero)
# tDown=time.ticks_ms() ### time button  down. is when the button is pushed down(and becomes zero)   the t Diff will be the time between the button coming up minus time down
# ## the real tDown when value goes to one from zero after a long interval of time.
# ## thus want tDown - tUP  to be greater than what we want as a debounee time ( maybe 25 ms)

Using separate up down counters with manipulation of the leds separately in each just provided confused logic.
Much better to have the press value from the up and down counter passed to a third function using bitwise logic(% worked okay as well)
(bitwise practice at bottom)
the first sketch below works fine and uses a third function
'''
# import sys
# from machine import Pin, Timer
# import time

# # Button and LED pin definitions
# butPin = 15
# butPin2 = 14
# gPin = 19
# rPin = 17
# bPin = 16
# yPin = 18

# # Button setup
# watchButton = Pin(butPin, Pin.IN, Pin.PULL_DOWN)
# Button = Pin(butPin2, Pin.IN, Pin.PULL_DOWN)

# # LED setup
# rLed = Pin(rPin, Pin.OUT)
# gLed = Pin(gPin, Pin.OUT)
# bLed = Pin(bPin, Pin.OUT)
# yLed = Pin(yPin, Pin.OUT)

# # Initial states
# butStateOld = 0
# butStateOld2 = 0
# tUp    = time.ticks_ms()
# tDown  = time.ticks_ms()
# press  = 0
# tUp2   = time.ticks_ms()
# tDown2 = time.ticks_ms()

# # Update LED states based on binary representation
# def update_leds(press):
#     bLed.value(press & 0b0001)  # LSB (1st bit)
#     rLed.value((press >> 1) & 0b0001)  # 2nd bit
#     yLed.value((press >> 2) & 0b0001)  # 3rd bit
#     gLed.value((press >> 3) & 0b0001)  # 4th bit

# # Button 1: Increase counter
# def button_press(pin):
#     global press, butStateOld, tUp, tDown
#     ButtonState = watchButton.value()
#     if ButtonState == 0:
#         tUp = time.ticks_ms()
#     if ButtonState == 1:
#         tDown = time.ticks_ms()
#     timeDiff = time.ticks_diff(tDown, tUp)
#     if ButtonState == 1 and butStateOld == 0 and timeDiff > 25:
#         press += 1
#         print('Button #1 count:', press)
#         update_leds(press)
#     butStateOld = ButtonState

# # Button 2: Decrease counter
# def button_press2(pin):
#     global press, tUp2, tDown2, butStateOld2
#     ButtonState2 = Button.value()
#     if ButtonState2 == 0:
#         tUp2 = time.ticks_ms()
#     if ButtonState2 == 1:
#         tDown2 = time.ticks_ms()
#     timeDiff = time.ticks_diff(tDown2, tUp2)
#     if ButtonState2 == 1 and butStateOld2 == 0 and timeDiff > 25:
#         if press > 0:  # This Prevents negative values. If value is one, then it goes to zero but stops there 
#             press -= 1
#             print('Button #2 count:', press)
#             update_leds(press)
#     butStateOld2 = ButtonState2

# # Interrupt setup
# watchButton.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_press)
# Button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_press2)

# # Main loop
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     yLed.value(0)
#     sys.exit()



# from machine import Pin,Timer
# import time
# butPin=15
# butPin2=14
# gPin=17
# rPin=16
# bPin=18
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# Button=Pin(butPin2,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# press=0     ## # if tune bu
# tUp=time.ticks_ms() ## time button from 1 to zero, when the button comes up (though the value goes to zero)
# tDown=time.ticks_ms() ### time button  down. is when the button is pushed down(and becomes zero)   the t Diff will be the time between the button coming up minus time down
# ## the real tDown when value goes to one from zero after a long interval of time.
# ## thus want tDown - tUP  to be greater than what we want as a debounee time ( maybe 25 ms)

# butStateOld=0


# def button_pressed(pin):
#     global tUp, tDown,butStateOld, press
#     ButState=watchButton.value()
#     if  ButState==1:
#         tDown=time.ticks_ms()
#     if ButState==0:
#         tUp=time.ticks_ms()
#     tDiff=tDown-tUp
#     if butStateOld==0 and ButState==1 and tDiff>=25:
#         press +=1
#         print('button has been pressed',press)
#         print(tDiff)
#         bLed.toggle()
#     butStateOld=ButState  

# watchButton.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler=button_pressed)

# try:
#     while True:
  
#         for i in range(50):
#             print(i)
#             if i %2 ==0:
#                 gLed.toggle()
#         time.sleep(1.5)           


# except KeyboardInterrupt:
#     print('All done')
#     gLed.value(0)
#     bLed.value(0)
#     rLed.value(0)
###~~~~~~~~~~~~~
# i can substitute the PIR and it works fine as well as with a Pushbutton
# next i can try to include a timer to turn on another led (r Led)or a buzzer etc
# from machine import Pin,Timer
# import time
# butPin=15
# butPin2=14
# gPin=17
# rPin=16
# bPin=18
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# Button=Pin(butPin2,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# butStateOld=0
# tUp=time.ticks_ms()
# tDown=time.ticks_ms()
# press =0
# def button_press(pin):
  
#     if  butState==1 and butStateOld==0 and (tDown-tUp>25):
#         press+=1
#         gLed.toggle()
#         print('Hi')
#         print('TRIGGER: ',press)
#         # for i in range(10):
#         #     rLed.toggle()
#         #     time.sleep(.2)
        
#     butStateOld=butState


# Button.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler =button_press)

# try:
#     while True:
  
#         for i in range(50):
#             print(i)
#             time.sleep(.3)
#             if i %2 ==0:
#                 bLed.toggle()
#         time.sleep(1.4)           


# except KeyboardInterrupt:
#     print('All done')
#     gLed.value(0)
#     bLed.value(0)
#     rLed.value(0)   
 #### create a binary up down counter with an interrupt ann debouncing
# import sys
# from machine import Pin,Timer
# import time
# butPin=15
# butPin2=14
# gPin=19
# rPin=17
# bPin=16
# yPin =18
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# Button=Pin(butPin2,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# yLed=Pin(yPin,Pin.OUT)
# butStateOld=0
# tUp=time.ticks_ms()
# tDown=time.ticks_ms()
# press =0
# # def update_leds(press):
# #     print(f'Binary: {bin(press)[2:].zfill(4)}')  # Show 4-bit binary
# #     bLed.value(press & 0b0001)  # 1st bit
# #     rLed.value((press >> 1) & 0b0001)  # 2nd bit
# #     yLed.value((press >> 2) & 0b0001)  # 3rd bit
# #     gLed.value((press >> 3) & 0b0001)  # 4th bit


# def binaryCounter(press):
#     print(' counter',press)
     
#     print(f'Binary: {bin(press)[2:]}')  # Show 4-bit binary 
#     # bLed.toggle()
#     bLed.value(press &0b0001)
#     rLed.value((press>>1) & 0b0001)
#     yLed.value((press >>2 & 0b0001))
#     gLed.value(press>> 3 & 0b0001)

#     # if press % 2 == 0:
#     #     rLed.toggle()
#     # if press % 4 == 0:
#     #     yLed.toggle()
#     # if press % 8 == 0:
#     #     gLed.toggle()


# def button_press(pin):
#     global press,butStateOld,tUp,tDown
#     ButtonState=watchButton.value()
#     if ButtonState ==0:
#         tUp=time.ticks_ms() ## tUp is tghe time the button is UP
#     if ButtonState == 1:
#         tDown = time.ticks_ms()
#     timeDiff =time.ticks_diff(tDown,tUp)## tUp is when the buttonState is back  up 0
#     if ButtonState == 1 and butStateOld == 0 and timeDiff >25:
#         press +=1
#         print('Trigger:  ',press)
#         binaryCounter(press)
#     butStateOld=ButtonState      
# watchButton.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler=button_press)
# # Button.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler=button_press)
# try:
#     while True:
#         pass       
# except KeyboardInterrupt:
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     yLed.value(0)
#     sys.exit()
    
### ~~ bitwise practice

# print(5 & 0b0101)
# 5 in binary: 0101
# 1 in binary: 0001
# Result:      0001 -> 1
# if (5 & 0b0101):
#     print('hi')
# else:
#     print('bye')
# if (5 & 0b010):
#     print('hi')
# else:
#     print('bye')
# print(8 >>1)
# print(8 >>2)
# print(8 >>3)

### from PW 83 and 84 in Micropython_Programs Paul McWhorter

''' At bottom is SHillehs debouncing function for a PIR
works well , very similar to PW 84 but no irq
https://shillehtek.com/blogs/news/how-to-connect-and-use-the-hcsr501-pir-sensor-with-a-raspberry-pi-pico-pico-w?utm_source=youtube&utm_medium=product_shelf
page 160 Random Nerds Micropython
debounce_timer=None
button.irg trigger is the button press.Rising   and the handler is the def button_pressed

def button_pressed(pin):
    global counter,debounce_timer
    counter +=1
    
    led.toggle or some short function
    debounce_timer =Timer()
    debounce_timer=init(period  200 ms,  mode timer.One_Shot callback=debounce_callback)
def debounce_callback(pin):
    global debounce_timer
    debounce_timer=None
'''
# from machine import Pin    ### program 1 of lesson 83
# import time
# butPin=15
# rPin=17
# gPin=16
# bPin=18
# pTime=0
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# press =0
# def IntSwitch(pin):
#     global press
#     pTIme=time.ticks_ms()
#     press =press +1
#     gLed.toggle()
#     print('Triggered: ',press)
#     pTImeOld=pTime


# watchButton.irq(trigger=Pin.IRQ_RISING,handler=IntSwitch)

# try:
#     while True:
#         pass
  
# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#######~~~~~~~~
####does  work  this is from the Random Nerds interupt/tiomer lesson section p 160
from machine import Pin,Timer
import time
butPin=15
gPin=17
rPin=16
bPin=18
yPin=19
Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
rLed=Pin(rPin,Pin.OUT)
gLed=Pin(gPin,Pin.OUT)
bLed=Pin(bPin,Pin.OUT)
yLed=Pin(yPin,Pin.OUT)
x=0
press=0
downTime=time.ticks_ms()
upTime=time.ticks_ms()
OldButState=0
def button_pressed(pin):
    global press,upTime,downTime,OldButState
    ButState=Button.value()
    # upTime=time.ticks_ms()
    
    # if NewButState==1:##Pressed, record the time the button was pressed 
    #     downTime=time.ticks_us()
    # if OldButState==0:
    #     upTime=time.ticks_us()  
    # if NewButState==1 and OldButState==0 and (time.ticks_diff(downTime,upTime)<25):
    # # if NewButState==1 and OldButState==0 :
    #     time_diff=time.ticks_diff(downTime,upTime)
    #     print(time_diff)
    #     print(f'{downTime}  {upTime}')
    #     rLed.toggle
    #     OldButState=NewButState
 
    #     print('Trigger: ',press)
    #     press +=1
    # # upTime=downTime
    # OldButState=NewButState
    # downTime=time.ticks_us()
    
    if ButState==1:##Pressed, record the time the button was pressed 
        downTime=time.ticks_ms()
    
    
    if ButState==0:
        upTime=time.ticks_ms() 
    # if ButState==1:##Pressed, record the time the button was pressed 
    #     downTime=time.ticks_ms()  
    if ButState==1 and OldButState==0 and (time.ticks_diff(downTime,upTime)>25):
    # if ButState==1 and OldButState==0 and (downTime-upTime<25):
    # if NewButState==1 and OldButState==0 :
        time_diff=time.ticks_diff(downTime,upTime)
        print('time_diff',time_diff)
        print(f'{downTime}   time  {upTime}')
        press+=1
        if press>16:
            press =press-16
        if press%2==0:
            gLed.toggle()
        if press%4==0:
            bLed.toggle()
        if press%8==0:
            yLed.toggle()
        rLed.toggle()
        print('Trigger: ',press)    
    # upTime=downTime
    OldButState=ButState
    # print("old but state ",OldButState)
    
    
    
    
Button.irq(trigger=Button.IRQ_RISING|Button.IRQ_FALLING,handler = button_pressed)
try:
    while True:
        # ButVal=Button.value()
        # print(ButVal)
        print(x)
        # if ButVal==1:
        #     rLed.value(1)
        # else:
        #     rLed.value(0)
        time.sleep(1)
        x+=1
except KeyboardInterrupt:
    print('all done')
    rLed.value(0)
    gLed.value(0)
    bLed.value(0)
### debouncing from the keith lohmeyer version of homework for lesson 83 PW
### this works fine SORT OF - not really
# from machine import Pin,Timer
# import time
# butPin=15
# rPin=17
# gPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# counter=0
# myTimer=Timer()
# def myCallback(pin):
#     global counter
    
#     if Button.value()==1:
#         counter+=1
#         gLed.toggle()
#         print('Button Pressed: ',counter)
#     Button.irq(handler=HandFx)

# def HandFx(pin):
#     Button.irq(handler=None)
#     myTimer.init(period=1500,mode=Timer.ONE_SHOT,callback=myCallback)
    

# Button.irq(trigger=Button.IRQ_RISING,handler = HandFx)
# try:
#     while True:
#         # ButVal=Button.value()
#         # print(ButVal)
#         print(x)
#         # if ButVal==1:
#         #     rLed.value(1)
#         # else:
#         #     rLed.value(0)
#         time.sleep(1)
#         x+=1
# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     myTimer.deinit()
#############my THIS WORKS 
# from machine import Pin,Timer
# import time
# butPin=15
# rPin=17
# gPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# counter=0
# myTimer=Timer()
# oldTime=time.ticks_ms()
# oldButVal=0
# def myCallback(pin):
#     global counter
#     if Button.value()==1:
#         gLed.value(1)
#         counter+=1
#         print('Trigger= ',counter)
#     Button.irq(handler=myHand)

# def myHand(pin):
#     Button.irq(handler=None)
#     myTimer.init(mode=Timer.ONE_SHOT,period=1000,callback=myCallback)     
# Button.irq(trigger=Button.IRQ_RISING,handler=myHand)
# try:
#     while True:
#         newTime=time.ticks_ms()
#         for x in range(20):
#         # print(newButVal)
#             print(x)
#             time.sleep(.1)

# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#########oct6 2024 attempt at debouncing with interrrupt and timer- WORKS

# from machine import Pin,Timer
# import time
# butPin=14
# rPin=17
# gPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# counter=0
# myTimer=Timer()
# oldTime=time.ticks_ms()
# oldButVal=0
# counter=0
# def myCallback(pin):
#     global counter
#     if Button.value()==1:
#         counter+=1
#         rLed.toggle()
#         print('Button Pressed: ',counter)
    
#     # print('myCallback and Counter= ',counter)
#     print('')
#     Button.irq(handler=myHand)   
    
    


# def myHand(pin):
#     Button.irq(handler=None)
#     myTimer.init(period=1000,mode=Timer.ONE_SHOT,callback=myCallback)        
# Button.irq(trigger=Button.IRQ_RISING,handler=myHand)
# try:
#     while True:
#         # for i in range(20):
#         #     print(i)
#         #     time.sleep(.1)
            
#         print(Button.value())
        
#         newTime=time.ticks_ms()
#         print(newTime)
#         # ButVal=Button.value()
#         # if ButVal ==1:
#         #     print('ButVal: ',ButVal)
#         time.sleep(.1)
 
# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
########  PW lesson 84  uses an interrupt but no Timer
# from machine import Pin,Timer
# import time
# butPin=15
# gPin=17
# rPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# press=0
# myTimer=Timer()
# oldTime=time.ticks_us() ## same as tUp which is when button is 0
# newTime=time.ticks_us() ## same as tDown which is whne button is 1 and pressed down
# oldButVal=0
# butStateOld =0
# def myHand(pin):
#     global oldTime,newTime,butStateOld,press
#     newTime=time.ticks_ms()
#     butStateNew=Button.value() 
#     if butStateNew==1:
#         newTime=time.ticks_us()
#     if butStateOld==0:
#         oldTime=time.ticks_us()           
#     # if butStateOld ==0 and butStateNew==1 :
#     if butStateOld ==0 and butStateNew==1 and (newTime-oldTime)  <25:
        
#         press +=1
#         print('TRIGGER: ',press) 
#         rLed.toggle()
#         # deltaTime=time.ticks_diff(newTime,oldTime)
#         deltaTime=newTime-oldTime
#         print('deltatime: ',deltaTime)
#     butStateOld=butStateNew
# Button.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING ,handler=myHand)
# try:
#     while True:
#         newTime=time.ticks_ms()
#         for x in range(30):
#         # print(newButVal)
#             print(x)
#             time.sleep(.1)

# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)


# from machine import Pin,Timer
# import time
# butPin=15
# gPin=17
# rPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# But_state=False
# last_time=0
# debounce_time =5
# stop_state=False
# def button_pressed(pin):
#     global But_state, debounce_time,last_time ,stop_state      
#     current_time=time.time()
#     Button.irq(handler = None)
#     stop_state=False
#     if But_state==False and (current_time-last_time>debounce_time):
#         print('hi, button pressed')
#         print('Duration = ',current_time-last_time)
#         last_time=current_time
#         stop_state=True
#         reset(stop_state)
#     else:
#         stop_state=False    
# def reset(stop_state):
#     global But_state, debounce_time,last_time 
#     print('bye')
#     Button.irq(handler=button_pressed)
     
# Button.irq(trigger=Pin.IRQ_RISING,handler=button_pressed)
# while True:
#     reset(stop_state)
#     if stop_state==True:
#         gLed.value(1)
#         time.sleep(.5)
#         gLed.value(0)
#         time.sleep(.1)
#     else:
#         gLed.value(0)
#         print('resting')
#         time.sleep(2)



# from machine import Pin,Timer
# import time
# butPin=15
# gPin=17
# rPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# last_time=0
# debounce_time =5
# stop_state=False
# def button_pressed(pin):
#     global  debounce_time,last_time ,stop_state      
#     current_time=time.time()
#     Button.irq(handler = None)
#     stop_state=False
#     if stop_state==False and (current_time-last_time>debounce_time):
#         print('hi, button pressed')
#         print('Duration = ',current_time-last_time)
#         last_time=current_time
#         stop_state=True
#         reset(stop_state)
#     else:
#         stop_state=False    
# def reset(stop_state):
#     global debounce_time,last_time 
#     print('bye')
#     Button.irq(handler=button_pressed)
#     stop_state=False
     
# Button.irq(trigger=Pin.IRQ_RISING,handler=button_pressed)
# while True:
#     reset(stop_state)
#     if stop_state==True:
#         gLed.value(1)
#         time.sleep(.5)
#         gLed.value(0)
#         time.sleep(.1)
#     else:
#         gLed.value(0)
#         print('resting')
#         time.sleep(2)
# ## shilleh    https://shillehtek.com/blogs/news/how-to-connect-and-use-the-hcsr501-pir-sensor-with-a-raspberry-pi-pico-pico-w?utm_source=youtube&utm_medium=product_shelf

# from machine import Pin
# import time

# # Initialize PIR sensor on GPIO 0
# pir = Pin(0, Pin.IN, Pin.PULL_DOWN)
# led = Pin(16, Pin.OUT)  # Initialize LED on GPIO 2
# pir_state = False  # Start assuming no motion detected
# last_motion_time = 0  # Timestamp of the last motion detected
# debounce_time = 3  # Debounce period in seconds

# print("PIR Module Initialized")
# time.sleep(1)  # Allow the sensor to stabilize
# print("Ready")

# while True:
#     val = pir.value()  # Read input value from PIR sensor
#     current_time = time.time()

#     if val == 1:  # Motion detected
#         if not pir_state and (current_time - last_motion_time >= debounce_time):
#             print(current_time - last_motion_time)
#             print("Motion detected!")
#             pir_state = True
#             led.on()  # Turn on LED
#             last_motion_time = current_time  # Update the last motion timestamp

#     elif val == 0: 
#         if pir_state and (current_time - last_motion_time >= debounce_time):
#             pir_state = False
#             led.off()
#             last_motion_time = current_time  # Update the last motion timestamp

#     time.sleep(0.1)  # Small delay to prevent spamming
    
