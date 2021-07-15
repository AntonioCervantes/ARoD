from time import sleep
from RFID import rfid
#from weight_sensor import check_weight

rfid_id = ['0xa2', '0x9a', '0x5c', '0x6f']

while True:
    rfidInput = rfid()
    if rfidInput is not None:
        rfidInput = [hex(i) for i in rfidInput]
    while rfidInput != rfid_id:
        rfidInput = rfid()
        if rfidInput is not None:
            rfidInput = [hex(i) for i in rfidInput]
        if rfidInput == rfid_id:
            print("return to weight sensor")
            sleep(1)
            break
    #else:
    print("incorrect")
        #sleep(1)