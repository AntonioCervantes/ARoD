import sys
sys.path.append('/home/pi/Desktop/Final_code')
from obstacle_avoidance import obstacle_avoidance
from obstacle_avoidance import update_data
from Ultrasonic import ultrasonic
from UART import *
import time

#drive_cal()
#time.sleep(30)
#print('ESC Calibrating.....')
#drive_on()

while True:
    obstacle_avoidance()
    '''
    while obstacle_avoidance() is True:
        print('I see something')
    else:
        avoidance_steering('straight')
    '''
    time.sleep(0.1)