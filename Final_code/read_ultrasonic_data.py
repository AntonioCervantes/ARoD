import serial
import time


arduino = serial.Serial('/dev/ttyUSB3', 9600, timeout=1)
arduino.flush()

def ultrasonic():
    while True:
        data = arduino.readline().decode('utf-8').rstrip()
        with open("/home/pi/Desktop/ultrasonic_info.txt", "w") as output:
            output.write(data)
        time.sleep(0.01)
