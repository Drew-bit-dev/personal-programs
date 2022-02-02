import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

time.sleep(2)

layout.write(' ')
time.sleep(3)
layout.write('INPUT PASSWORD / TEXT HERE')
time.sleep(1)
layout.write('\n')

#to run this you will have to 
#copy this code into Thonny
#as well as download the 
#microcontroller library from Adafruit