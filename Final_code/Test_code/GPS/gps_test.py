import sys
sys.path.append('/home/pi/Desktop/Final_code')
from Position_Orientation import *


while True:
    a=gps_location()
    
    print(a)
#magnetometer()