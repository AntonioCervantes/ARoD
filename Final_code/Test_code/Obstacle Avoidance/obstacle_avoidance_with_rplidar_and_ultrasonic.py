import sys
sys.path.append('/home/pi/Desktop/Final_code')
import time

def get_ultrasonic_info():
    with open("/home/pi/Desktop/ultrasonic_info.txt", "r") as a:
        b = a.read()
        print(b)
        c = b.split(",")
        print(c)
        sensor = c[0]
        ultrasonic_sensor = sensor
        minimum = c[1]
        ultrasonic_distance = float(minimum)
        
        return ultrasonic_sensor, ultrasonic_distance
    time.sleep(0.001) ### This is probably something that can be removed ###

def update_data():
    try:
        global ultrasonic_sensor
        global ultrasonic_distance
        
        ultrasonic_sensor, ultrasonic_distance = get_ultrasonic_info()                 #Returns lidar_lite distance
    except ValueError:
        pass
    except IndexError:
        pass

    return ultrasonic_sensor, ultrasonic_distance

while True:
    update_data()
    if ultrasonic_distance < 1000:
        if ultrasonic_sensor == "l":
            print("turn right")
            time.sleep(0.0001)
        elif ultrasonic_sensor == "f":
            print("its in the front")
            time.sleep(0.0001)
        elif ultrasonic_sensor == "r":
            print("turn left")
            time.sleep(0.0001)

    
    