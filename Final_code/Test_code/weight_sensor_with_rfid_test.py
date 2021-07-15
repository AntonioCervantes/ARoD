import sys
sys.path.append('/home/pi/Desktop/Final_code')
from UART import send, receive, weight,open_door,close_door
import time
from RFID import rfid

rfid_id = ['0xa2', '0x9a', '0x5c', '0x6f']

while True:
    weight1 = int(weight())
    print(weight1)
    rfidInput = rfid()
    if rfidInput is not None:
        rfidInput = [hex(i) for i in rfidInput]
    while rfidInput != rfid_id:
        print("incorrect rfid")
        
        rfidInput = rfid()
        if rfidInput is not None:
            rfidInput = [hex(i) for i in rfidInput]
        if rfidInput == rfid_id:
            print("correct rfid")
            time.sleep(1)
            break
            #time.sleep(10)
    open_door()
    print("door open")
    time.sleep(25)
    try:
        weight2 = int(weight())
    except ValueError:
        weight2 = int(weight())
        pass
    while abs(weight1 - weight2) <= 1000:
        print('Second weight: {}'.format(weight2))
        print('Weight Difference: {}'.format(abs(weight1 - weight2)))
        print('Nothing has been added or removed')
        weight2 = int(weight())
        time.sleep(0.5)
    print('weight Difference: {}'.format(abs(weight1 - weight2)))
    print('Something was added or removed \n')
    time.sleep(5)
    close_door()
    print('Closing door \n')
    time.sleep(25)
    print("drive forward")
    
    