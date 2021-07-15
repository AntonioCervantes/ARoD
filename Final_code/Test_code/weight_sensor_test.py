import sys
sys.path.append('/home/pi/Desktop/Final_code')
from UART import send, receive, weight
import time

while True:
    weight1 = int(weight())
    print(weight1)
    time.sleep(5)
    weight2 = int(weight())
    print(weight2)
    while abs(weight1 - weight2) <= 500:
        print('Second weight: {}'.format(weight2))
        print('Weight Difference: {}'.format(abs(weight1 - weight2)))
        print('Nothing has been added or removed')
        weight2 = int(weight())
        time.sleep(0.5)
    print('weight Difference: {}'.format(abs(weight1 - weight2)))
    print('Something was added or removed \n')
    time.sleep(0.5)
    #close_door()
    print('Closing door \n')
