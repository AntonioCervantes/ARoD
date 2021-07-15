# Write your code here :-)
import serial, time


arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
arduino.flush()

while True:
    try:
        line = arduino.readline().decode('utf-8').rstrip()
        dist = int(line)*10
        print(dist)
    except ValueError:
        pass
