import sys
sys.path.append('/home/pi/Desktop/Final_code')
from Position_Orientation import *
import time


while True:
    a=gps_location()
    #b=magnetometer()
    #print("GPS Location:",a)
    #print("Heading:",b)
    #print('-'*50)
    
    if a[0] is not None:
        lat = round(a[0],5)
        
    else:
        lat = a[0]
    
    if a[1] is not None:
        long = round(a[1],5)
        
    else:
        long = a[1]    
    print(lat,long)
    
    '''
    with open('/home/pi/Desktop/gps_points.txt', mode='a') as f:
            f.write('{},'.format(lat))
            f.write('{}\n'.format(long))
            '''
    
    time.sleep(0.25)
