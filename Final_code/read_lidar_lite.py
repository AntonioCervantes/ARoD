import serial, time


arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
arduino.flush()

def lidar_lite():
    while True:
        distance = arduino.readline().decode('utf-8').rstrip()
        #print(distance)
        with open("/home/pi/Desktop/lidar_lite_info.txt", "w") as output:
            output.write(distance)

