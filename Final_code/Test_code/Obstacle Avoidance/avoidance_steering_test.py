import sys
sys.path.append('/home/pi/Desktop/Final_code')
from UART import *
from stanley_control_law import *
import time
from obstacle_avoidance import *
from Position_Orientation import *
#from Ultrasonic import *
while True:
    avoidance_steering('left')
    print('Steering Left')
    time.sleep(3)

    avoidance_steering('right')
    print('Steering Right')
    time.sleep(3)

    avoidance_steering('straight')
    print('Steering Straight')
    time.sleep(3)
