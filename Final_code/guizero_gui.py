from guizero import App, Box, Text, PushButton, Slider
import time
import random


import sys
sys.path.append('/home/pi/Desktop/Final_code')
from UART import *

def cal():
    drive_cal()
    print('ESC Calibrating.....')
def on():
    drive_on()
    print("Starting Motor")
def off():
    drive_off()
    print("Stopping Motor")
def display_data():
    a = random.randint(0,100)
    treading_text.value = "{0:.2f}".format(a)
def turn_left():
    avoidance_steering("left")
    print("Turning Left")
def turn_right():
    avoidance_steering("right")
    print("Turning Right")
def turn_straight():
    avoidance_steering("straight")
    print("Turning Straight")
def openDoor():
    open_door()
    print("Opening Door")  
def closeDoor():
    close_door()
    print("Closing Door")
def openDoorAdjust():
    open_door_adjust()
    print("Opening Door")  
def closeDoorAdjust():
    close_door_adjust()
    print("Closing Door") 

windowHeight = 500
windowWidth = 700
buttonHeight = 2
buttonWidth = 10
text_Size = 20

app = App(title="Servo GUI", width=windowWidth, height=windowHeight, layout="auto")
app.bg = "black"
title_text = Text(app, text="ARoD GUI",align="top")
title_text.text_color = "white"
title_text.text_size = 30

everything_box = Box(app,width="fill",align="top",layout="auto")

buttons_box_B = Box(everything_box,width="fill",align="right",layout="auto")
Commands_title = Text(buttons_box_B, text="Drive Commands",align="top")
Commands_title.text_color = "white"
Commands_title.text_size = 20
on_button = PushButton(buttons_box_B, on, text="Motor On", align="top",width = buttonWidth, height = buttonHeight)
on_button.text_size = text_Size
on_button.text_color = "white"
on_button.bg = "green"
off_button = PushButton(buttons_box_B, off, text="Motor Off", align="top",width = buttonWidth, height = buttonHeight)
off_button.text_size = text_Size
off_button.bg = "red"
off_button.text_color = "white"
cal_button = PushButton(buttons_box_B, cal, text="ESC Cal", align="top",width = buttonWidth, height = buttonHeight)
cal_button.text_size = text_Size
cal_button.text_color = "white"
#cal_button.bg = "#E0E0E0"



door_box = Box(everything_box,width="fill",align="left",layout="auto")
door_title = Text(door_box, text="Door Commands",align="top")
door_title.text_color = "white"
door_title.text_size = 20
openDoor_button = PushButton(door_box, openDoor, text="Open Door", align="top",width = buttonWidth, height = buttonHeight)
openDoor_button.text_size = text_Size
openDoor_button.text_color = "white"
openDoor_button.bg = "green"
closeDoor_button = PushButton(door_box, closeDoor, text="Close Door", align="top",width = buttonWidth, height = buttonHeight)
closeDoor_button.text_size = text_Size
closeDoor_button.text_color = "white"
closeDoor_button.bg = "red"
openDoorAdjust_button = PushButton(door_box, openDoorAdjust, text="Open Adjust", align="top",width = buttonWidth, height = buttonHeight)
openDoorAdjust_button.text_size = text_Size
openDoorAdjust_button.text_color = "white"
closeDoorAdjust_button = PushButton(door_box, closeDoorAdjust, text="Close Adjust", align="top",width = buttonWidth, height = buttonHeight)
closeDoorAdjust_button.text_size = text_Size
closeDoorAdjust_button.text_color = "white"

buttons_box_A = Box(everything_box,width="fill",align="top",layout="grid")
steering_title = Text(buttons_box_A, text="Steering",grid=[1,0])
steering_title.text_color = "white"
steering_title.text_size = 20
left_button = PushButton(buttons_box_A, turn_left, text="<", grid=[0,2])
left_button.text_size = 30
left_button.text_color = "white"
left_button.bg = "gray"
right_button = PushButton(buttons_box_A, turn_right, text=">", grid=[2,2])
right_button.text_size = 30
right_button.text_color = "white"
right_button.bg = "gray"
straight_button = PushButton(buttons_box_A, turn_straight, text="^", grid=[1,1])
straight_button.text_size = 30
straight_button.text_color = "white"
straight_button.bg = "gray"

app.display()


