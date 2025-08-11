# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/
# /Users/judsonbelmont/Documents/RandomNerd/ESP-MicroPython/.git
# Donsky has a very good tutorial on getting started with VSCode and PyMaker https://www.youtube.com/watch?v=YOeV14SESls
# # very complete website with EVERYTHING ESP32 and Micropython and links to a plethora of resources http://esp32.net/ page 28 pf RandomNerds esp32
# my boards ESP32 DOIT DEVKIT V1 Board
# # opening workspaces
# https://code.visualstudio.com/docs/editing/workspaces/workspaces#_multiroot-workspaces
'''
JBelmont72: walkthrough

GitHub Copilot: Could you clarify what you’d like a walkthrough of?  
For example:
- A specific file or code in your workspace  
- Setting up MicroPython on ESP devices  
- Running code in VS Code  
Let me know your focus, and I’ll guide you step by step.

JBelmont72: i want to open the 'walkthrough' for PyMakr'. the release notes for pyMaker state 'We've added a small walkthrough. To open it:

Click ctrl/cmd + shift + p
Type walkthrough
Select Get Started: Open Walkthrough... will show a list of walkthroughs.
Click Pymakr 2 - Getting Started.' but i cannot find the 'walkthrough'

VS Code: To open a walkthrough in Visual Studio Code, use the **Welcome: Open Walkthrough...** command. This will show a list of available walkthroughs, including any provided by extensions like PyMakr.

1. Open the Command Palette with ``cmd + shift + p``.
2. Type "walkthrough".
3. Select **Welcome: Open Walkthrough...**.
4. Look for "Pymakr 2 - Getting Started" in the list.

If you do not see the PyMakr walkthrough, make sure the PyMakr extension is installed and enabled.

You can also search for the PyMakr extension in the marketplace to ensure it's installed.



Show in Command Palette

JBelmont72: i have opened a folder of my micropython programs.  and my serial port is showing in 'DEVICES' I want to use all of my folder. Do i 'Create Project' or 'open Workspace' or skip these options?

GitHub Copilot: If you have already opened your folder in VS Code and see your serial port in "DEVICES," you do **not** need to "Create Project" or "Open Workspace" again.  
You can work directly with your folder as-is.

**Summary:**
- If your folder is open and you see your files and devices, you’re ready to use PyMakr and run your MicroPython programs.
- "Create Project" or "Open Workspace" are only needed if you want to organize multiple folders or start a new project structure.

You can now upload, run, and manage your scripts with PyMakr.

JBelmont72: what is 'restart in safe mode' 

GitHub Copilot: **Restart in Safe Mode** (in the context of MicroPython and ESP devices) means rebooting your board with minimal features enabled.  
This disables user scripts and some hardware features, allowing you to recover from crashes or errors caused by faulty code.

**Use cases:**
- Your board is stuck in a boot loop due to a problematic script.
- You need to troubleshoot or erase problematic files.

**How to use:**  
Most boards enter safe mode by holding down a specific button (like BOOT or RESET) during power-up, or by sending a command via PyMakr/serial.

**Result:**  
You get a clean environment to fix issues or upload new code.

JBelmont72: should a 'pymaker.json' file have been created?

GitHub Copilot: A `pymakr.json` file is **optional** but recommended when using PyMakr.  
It stores project-specific settings, such as your device address, sync folders, and files to ignore during upload.

**PyMakr will automatically create `pymakr.json`** when you use the "Create Project" command or configure settings via the PyMakr sidebar.  
If you just open a folder, it may not be created until you change a setting or explicitly create a project.

**Summary:**  
- Not strictly required, but useful for managing uploads and settings.
- You can create or edit it manually if needed.

Let me know if you want an example `pymakr.json` for your project!

JBelmont72: I want to run my blink.py file.  what sequence of steps do i need to follow. I have the pymaker extension, I have my folder loaded in VSCode, and 'Devices' is showing my usbserial port.

GitHub Copilot: Here’s a step-by-step guide to run your Blink_LED.py file on your ESP board using PyMakr in VS Code:

### 1. Connect Your Board
- Make sure your ESP board is plugged in and showing under **DEVICES** in PyMakr.

### 2. Select the Correct Serial Port
- In the PyMakr sidebar, confirm your device (e.g., `/dev/tty.usbserial...`) is selected.

### 3. Open Your Script
- Open Blink_LED.py in the editor.

### 4. Upload and Run the Script
- Click the **Upload** button (up arrow) in the PyMakr sidebar, or  
- Right-click the file and select **Upload to device**, or  
- Use the PyMakr toolbar at the bottom of VS Code and click **Run** (play icon).

### 5. Monitor Output
- Open the **PyMakr Terminal** (usually at the bottom of VS Code) to see logs or errors.

### 6. Stop the Script (if needed)
- Press **Ctrl+C** in the PyMakr Terminal to interrupt the running script.

---

**Tip:**  
If you want the script to run automatically on boot, rename it to `main.py` and upload it.

Let me know if you need troubleshooting help!


JBelmont72: walkthrough

GitHub Copilot: Could you clarify what you’d like a walkthrough of?  
For example:
- A specific file or code in your workspace  
- Setting up MicroPython on ESP devices  
- Running code in VS Code  
Let me know your focus, and I’ll guide you step by step.

JBelmont72: i want to open the 'walkthrough' for PyMakr'. the release notes for pyMaker state 'We've added a small walkthrough. To open it:

Click ctrl/cmd + shift + p
Type walkthrough
Select Get Started: Open Walkthrough... will show a list of walkthroughs.
Click Pymakr 2 - Getting Started.' but i cannot find the 'walkthrough'

VS Code: To open a walkthrough in Visual Studio Code, use the **Welcome: Open Walkthrough...** command. This will show a list of available walkthroughs, including any provided by extensions like PyMakr.

1. Open the Command Palette with ``cmd + shift + p``.
2. Type "walkthrough".
3. Select **Welcome: Open Walkthrough...**.
4. Look for "Pymakr 2 - Getting Started" in the list.

If you do not see the PyMakr walkthrough, make sure the PyMakr extension is installed and enabled.

You can also search for the PyMakr extension in the marketplace to ensure it's installed.



Show in Command Palette

JBelmont72: i have opened a folder of my micropython programs.  and my serial port is showing in 'DEVICES' I want to use all of my folder. Do i 'Create Project' or 'open Workspace' or skip these options?

GitHub Copilot: If you have already opened your folder in VS Code and see your serial port in "DEVICES," you do **not** need to "Create Project" or "Open Workspace" again.  
You can work directly with your folder as-is.

**Summary:**
- If your folder is open and you see your files and devices, you’re ready to use PyMakr and run your MicroPython programs.
- "Create Project" or "Open Workspace" are only needed if you want to organize multiple folders or start a new project structure.

You can now upload, run, and manage your scripts with PyMakr.

JBelmont72: what is 'restart in safe mode' 

GitHub Copilot: **Restart in Safe Mode** (in the context of MicroPython and ESP devices) means rebooting your board with minimal features enabled.  
This disables user scripts and some hardware features, allowing you to recover from crashes or errors caused by faulty code.

**Use cases:**
- Your board is stuck in a boot loop due to a problematic script.
- You need to troubleshoot or erase problematic files.

**How to use:**  
Most boards enter safe mode by holding down a specific button (like BOOT or RESET) during power-up, or by sending a command via PyMakr/serial.

**Result:**  
You get a clean environment to fix issues or upload new code.

JBelmont72: should a 'pymaker.json' file have been created?

GitHub Copilot: A `pymakr.json` file is **optional** but recommended when using PyMakr.  
It stores project-specific settings, such as your device address, sync folders, and files to ignore during upload.

**PyMakr will automatically create `pymakr.json`** when you use the "Create Project" command or configure settings via the PyMakr sidebar.  
If you just open a folder, it may not be created until you change a setting or explicitly create a project.

**Summary:**  
- Not strictly required, but useful for managing uploads and settings.
- You can create or edit it manually if needed.

Let me know if you want an example `pymakr.json` for your project!

JBelmont72: I want to run my blink.py file.  what sequence of steps do i need to follow. I have the pymaker extension, I have my folder loaded in VSCode, and 'Devices' is showing my usbserial port.

GitHub Copilot: Here’s a step-by-step guide to run your Blink_LED.py file on your ESP board using PyMakr in VS Code:

### 1. Connect Your Board
- Make sure your ESP board is plugged in and showing under **DEVICES** in PyMakr.

### 2. Select the Correct Serial Port
- In the PyMakr sidebar, confirm your device (e.g., `/dev/tty.usbserial...`) is selected.

### 3. Open Your Script
- Open Blink_LED.py in the editor.

### 4. Upload and Run the Script
- Click the **Upload** button (up arrow) in the PyMakr sidebar, or  
- Right-click the file and select **Upload to device**, or  
- Use the PyMakr toolbar at the bottom of VS Code and click **Run** (play icon).

### 5. Monitor Output
- Open the **PyMakr Terminal** (usually at the bottom of VS Code) to see logs or errors.

### 6. Stop the Script (if needed)
- Press **Ctrl+C** in the PyMakr Terminal to interrupt the running script.

---

**Tip:**  
If you want the script to run automatically on boot, rename it to `main.py` and upload it.

Let me know if you need troubleshooting help!

JBelmont72: i see my tty.usbserial-0001 ' under 'Devices' but I do not see a mention of my ESP32 board. SHould I see that?

GitHub Copilot: No, you will typically only see the serial port name (e.g., `tty.usbserial-0001`) under **Devices** in PyMakr, not the specific board model (like ESP32).  
PyMakr detects and lists available serial ports, not board types.

As long as your ESP32 is connected and showing as a serial device, you are ready to upload and run your code.  
The board type is not shown in the PyMakr device list.

JBelmont72: i right clicked and selected 'upload to device'. i am getting this continuous message 'Uploading "Blink_LED.py" to "tty.usbserial-0001 / unknown?"...'

GitHub Copilot: If you see "Uploading 'Blink_LED.py' to 'tty.usbserial-0001 / unknown?'" continuously, it usually means PyMakr is having trouble communicating with your ESP32 board.

**Try these steps:**

1. **Check Board Connection**
   - Make sure your ESP32 is firmly plugged in.
   - Try a different USB cable or port if possible.

2. **Reset the Board**
   - Press the RESET or EN button on your ESP32.

3. **Close Other Serial Apps**
   - Make sure no other program (like Arduino IDE or a serial monitor) is using the port.

4. **Check PyMakr Settings**
   - In VS Code, open the PyMakr sidebar.
   - Confirm the correct serial port is selected (`tty.usbserial-0001`).

5. **Restart VS Code**
   - Close and reopen VS Code to reset the connection.

6. **Try Safe Mode**
   - Hold the BOOT button while pressing RESET on your ESP32, then try uploading again.

If it still doesn’t work, unplug and replug your board, then try uploading again.  
Let me know if you see any error messages in the PyMakr terminal!



JBelmont72: walkthrough

GitHub Copilot: Could you clarify what you’d like a walkthrough of?  
For example:
- A specific file or code in your workspace  
- Setting up MicroPython on ESP devices  
- Running code in VS Code  
Let me know your focus, and I’ll guide you step by step.

JBelmont72: i want to open the 'walkthrough' for PyMakr'. the release notes for pyMaker state 'We've added a small walkthrough. To open it:

Click ctrl/cmd + shift + p
Type walkthrough
Select Get Started: Open Walkthrough... will show a list of walkthroughs.
Click Pymakr 2 - Getting Started.' but i cannot find the 'walkthrough'

VS Code: To open a walkthrough in Visual Studio Code, use the **Welcome: Open Walkthrough...** command. This will show a list of available walkthroughs, including any provided by extensions like PyMakr.

1. Open the Command Palette with ``cmd + shift + p``.
2. Type "walkthrough".
3. Select **Welcome: Open Walkthrough...**.
4. Look for "Pymakr 2 - Getting Started" in the list.

If you do not see the PyMakr walkthrough, make sure the PyMakr extension is installed and enabled.

You can also search for the PyMakr extension in the marketplace to ensure it's installed.



Show in Command Palette

JBelmont72: i have opened a folder of my micropython programs.  and my serial port is showing in 'DEVICES' I want to use all of my folder. Do i 'Create Project' or 'open Workspace' or skip these options?

GitHub Copilot: If you have already opened your folder in VS Code and see your serial port in "DEVICES," you do **not** need to "Create Project" or "Open Workspace" again.  
You can work directly with your folder as-is.

**Summary:**
- If your folder is open and you see your files and devices, you’re ready to use PyMakr and run your MicroPython programs.
- "Create Project" or "Open Workspace" are only needed if you want to organize multiple folders or start a new project structure.

You can now upload, run, and manage your scripts with PyMakr.

JBelmont72: what is 'restart in safe mode' 

GitHub Copilot: **Restart in Safe Mode** (in the context of MicroPython and ESP devices) means rebooting your board with minimal features enabled.  
This disables user scripts and some hardware features, allowing you to recover from crashes or errors caused by faulty code.

**Use cases:**
- Your board is stuck in a boot loop due to a problematic script.
- You need to troubleshoot or erase problematic files.

**How to use:**  
Most boards enter safe mode by holding down a specific button (like BOOT or RESET) during power-up, or by sending a command via PyMakr/serial.

**Result:**  
You get a clean environment to fix issues or upload new code.

JBelmont72: should a 'pymaker.json' file have been created?

GitHub Copilot: A `pymakr.json` file is **optional** but recommended when using PyMakr.  
It stores project-specific settings, such as your device address, sync folders, and files to ignore during upload.

**PyMakr will automatically create `pymakr.json`** when you use the "Create Project" command or configure settings via the PyMakr sidebar.  
If you just open a folder, it may not be created until you change a setting or explicitly create a project.

**Summary:**  
- Not strictly required, but useful for managing uploads and settings.
- You can create or edit it manually if needed.

Let me know if you want an example `pymakr.json` for your project!

JBelmont72: I want to run my blink.py file.  what sequence of steps do i need to follow. I have the pymaker extension, I have my folder loaded in VSCode, and 'Devices' is showing my usbserial port.

GitHub Copilot: Here’s a step-by-step guide to run your Blink_LED.py file on your ESP board using PyMakr in VS Code:

### 1. Connect Your Board
- Make sure your ESP board is plugged in and showing under **DEVICES** in PyMakr.

### 2. Select the Correct Serial Port
- In the PyMakr sidebar, confirm your device (e.g., `/dev/tty.usbserial...`) is selected.

### 3. Open Your Script
- Open Blink_LED.py in the editor.

### 4. Upload and Run the Script
- Click the **Upload** button (up arrow) in the PyMakr sidebar, or  
- Right-click the file and select **Upload to device**, or  
- Use the PyMakr toolbar at the bottom of VS Code and click **Run** (play icon).

### 5. Monitor Output
- Open the **PyMakr Terminal** (usually at the bottom of VS Code) to see logs or errors.

### 6. Stop the Script (if needed)
- Press **Ctrl+C** in the PyMakr Terminal to interrupt the running script.

---

**Tip:**  
If you want the script to run automatically on boot, rename it to `main.py` and upload it.

Let me know if you need troubleshooting help!

JBelmont72: i see my tty.usbserial-0001 ' under 'Devices' but I do not see a mention of my ESP32 board. SHould I see that?

GitHub Copilot: No, you will typically only see the serial port name (e.g., `tty.usbserial-0001`) under **Devices** in PyMakr, not the specific board model (like ESP32).  
PyMakr detects and lists available serial ports, not board types.

As long as your ESP32 is connected and showing as a serial device, you are ready to upload and run your code.  
The board type is not shown in the PyMakr device list.

JBelmont72: i right clicked and selected 'upload to device'. i am getting this continuous message 'Uploading "Blink_LED.py" to "tty.usbserial-0001 / unknown?"...'

GitHub Copilot: If you see "Uploading 'Blink_LED.py' to 'tty.usbserial-0001 / unknown?'" continuously, it usually means PyMakr is having trouble communicating with your ESP32 board.

**Try these steps:**

1. **Check Board Connection**
   - Make sure your ESP32 is firmly plugged in.
   - Try a different USB cable or port if possible.

2. **Reset the Board**
   - Press the RESET or EN button on your ESP32.

3. **Close Other Serial Apps**
   - Make sure no other program (like Arduino IDE or a serial monitor) is using the port.

4. **Check PyMakr Settings**
   - In VS Code, open the PyMakr sidebar.
   - Confirm the correct serial port is selected (`tty.usbserial-0001`).

5. **Restart VS Code**
   - Close and reopen VS Code to reset the connection.

6. **Try Safe Mode**
   - Hold the BOOT button while pressing RESET on your ESP32, then try uploading again.

If it still doesn’t work, unplug and replug your board, then try uploading again.  
Let me know if you see any error messages in the PyMakr terminal!

JBelmont72: I am not seeing these options at the bottom of my terminal 'Pymakr Console: toggle board connection—connect/disconnect the board
Run: run currently open file on the board
Upload: upload project to your board
Download: download project from your board
All commands: list all available Pymakr commands
' and in the cammand palette I am not seeing pymaker options

VS Code: If you do not see PyMakr options in the terminal or Command Palette, the PyMakr extension may not be installed or enabled.

1. Search for "PyMakr" in the Extensions Marketplace to confirm it is installed and enabled.
2. If not installed, install the PyMakr extension.
3. Reload VS Code after installation.
4. Check the Command Palette (``cmd + shift + p``) for PyMakr commands.
5. Look for the PyMakr toolbar at the bottom of VS Code.

You can use the **Search marketplace** command to find PyMakr.



Search Extension Marketplace

JBelmont72: pymakr is installed but i do not have the toolbar

GitHub Copilot: If PyMakr is installed but you do not see the toolbar:

1. **Reload VS Code Window:**  
   Press `Cmd+Shift+P`, type `Reload Window`, and select it.

2. **Check Extension Activation:**  
   - Make sure your workspace folder is open (not just a single file).
   - Confirm your serial device is connected.

3. **Check for Errors:**  !!!!****!!!!!!!
   - Look for any error or warning icons in the bottom bar.
   - Open the "Output" panel (`Cmd+Shift+U`), select "PyMakr" from the dropdown, and check for error messages.

4. **Reinstall PyMakr:**  
   - Uninstall PyMakr from Extensions.
   - Reload VS Code.
   - Reinstall PyMakr.

5. **Check for Conflicting Extensions:**  
   - Disable other extensions that might use serial ports (like PlatformIO or Arduino).

If the toolbar still does not appear, let me know what you see in the "PyMakr" output panel.
'''

# from machine import Pin
# from time import sleep
# import sys

# led = Pin(2, Pin.OUT)
# try:
#    while True:
#       led.value(not led.value())
#       val=led.value() 
#       print('hi',val)          
#       sleep(0.5)
# except KeyboardInterrupt:
#    led.value(0)
#    print('signing off')
#    sys.exit()
# from machine import Pin
# from time import sleep

# led = Pin(2, Pin.OUT)

# while True:
#   led.value(not led.value())
#   val=led.value() 
#   print('hi',val)          
#   sleep(0.5)

## make into a function that can be called from the mainpy
from machine import Pin
from time import sleep
import sys

led = Pin(2, Pin.OUT)
def main():
   try:
      while True:
         led.value(not led.value())
         val=led.value() 
         print('hi',val)          
         sleep(0.5)
   except KeyboardInterrupt:
      led.value(0)
      print('signing off')
      sys.exit()
if __name__=='__main__':
   main()
## BELOW IS THE COMPLETE SETUP WITH THE MAIN.PY THAT WORKS WITH THE Blink_LED.main()
'''
Blink_LED.Blink_LED()

'''
from machine import Pin
from time import sleep
import sys

led = Pin(2, Pin.OUT)
try:
   while True:
      led.value(not led.value())
      val=led.value() 
      print('hi',val)          
      sleep(0.5)
except KeyboardInterrupt:
   led.value(0)
   print('Stopped Blinking')
   sys.exit()
   
'''
#Blink_LED.py  
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

def Blink_LED():
    print("Blinking LED. Press Ctrl+C to stop.")
    try:
        while True:
            #led.toggle()  # or: led.value(not led.value())
            led.value(not led.value())
            sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped blinking.")
'''
'''
# this main.py works with this Blink_LED.py
# main.py using button press on GPIO 4  

from machine import Pin
from time import sleep, ticks_ms, ticks_diff
import sys
import Blink_LED

# Configuration 
BUTTON_PIN = 4 #  to GROUND SO Pin.PULL_UP =1 when not pressed
TIMEOUT_MS = 1000  # 1 second

# Setup
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
ON_BOARD_PIN = 2
led_pin = Pin(ON_BOARD_PIN, Pin.OUT)

butVal=button.value()
print(f'butVal: {butVal}')
# Startup message
print("Waiting for button press...")
i=0
start = ticks_ms()
while ticks_diff(ticks_ms(), start) < TIMEOUT_MS:
    if not button.value():  # Active-low: pressed
        print("Button pressed — running Blink_LED")
        Blink_LED.main()
        for i in range(0,5,1):
            led_pin.value(not led_pin.value())
            sleep_ms(400)
            
        break
    sleep(0.05)

print("No button press — exiting safely")
sys.exit()
'''