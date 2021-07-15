####### This is the Obstacle Avoidance Module #######
from UART import avoidance_steering
#from eyes import expression
import time

ultrasonic_sensor = 'r'
ultrasonic_distance = 4000
rplidar_distance = 4000
rplidar_angle = 180
    
def get_rplidar_info():
    with open("/home/pi/Desktop/rplidar_info.txt", "r") as a:
        b = a.read()
        c = b.split(",")
        rplidar_distance = float(c[0])
        rplidar_angle = float(c[1])
        min_data = [rplidar_distance, rplidar_angle]
        return min_data
    time.sleep(0.0001) ### This is probably something that can be removed ###

def get_ultrasonic_info():
    with open("/home/pi/Desktop/ultrasonic_info.txt", "r") as a:
        b = a.read()
        c = b.split(",")
        sensor = c[0]
        ultrasonic_sensor = sensor
        minimum_cm = c[1]
        minimum_mm = float(minimum_cm)*10
        ultrasonic_distance = minimum_mm
        #print(ultrasonic_sensor, ",", ultrasonic_distance)
        
        return ultrasonic_sensor, ultrasonic_distance
    time.sleep(0.001) ### This is probably something that can be removed ###

def update_data():
    global ultrasonic_sensor
    global ultrasonic_distance
    global rplidar_distance
    global rplidar_angle
    try:
        #global ultrasonic_sensor
        #global ultrasonic_distance
        
        rplidar = get_rplidar_info()          #Returns a list for distance and angle of rplidar
        ultrasonic_sensor, ultrasonic_distance = get_ultrasonic_info()
        
        #global rplidar_distance
        #global rplidar_angle
        
        rplidar_distance = rplidar[0]           #Grabs the rpLiDAR distance from list
        rplidar_angle = rplidar[1]              #Grabs the rpLiDAR angle from list

    except ValueError:
        pass
    except IndexError:
        pass

    return rplidar_distance
    return rplidar_angle
    return ultrasonic_sensor, ultrasonic_distance

def obstacle_avoidance():
    #### distance variables (In Millimeters) #####
    rplidar_long_range_trigger = 2000
    rplidar_short_range_trigger = 1000
    ultrasonic_trigger_distance = 2500

    #### LiDAR Angle Range (In Degrees) ####
    left_zone = [60, 140]
    center_zone = [140, 220]
    right_zone = [220, 300]
    center_angle = 180

    #### eye commands ####
    stare = 1
    blink = 2
    look_left = 3
    look_right = 4
    look_down = 5
    look_down_left = 6
    look_down_right = 7
    look_up_left = 8
    look_up_right = 9

    update_data()

    if ultrasonic_distance < rplidar_distance:
        if ultrasonic_distance < ultrasonic_trigger_distance:
            if ultrasonic_sensor == "l":
                avoidance_steering("right")
                print("turn right")
                obstacle = True
                return obstacle
                time.sleep(0.0001)
            elif ultrasonic_sensor == "f":
                avoidance_steering("right")
                print("its in the front")
                obstacle = True
                return obstacle
                time.sleep(0.0001)
            elif ultrasonic_sensor == "r":
                avoidance_steering("left")
                print("turn left")
                obstacle = True
                return obstacle 
                time.sleep(0.0001)
        else:
            pass
        
    elif rplidar_distance < ultrasonic_distance:
        if rplidar_angle < left_zone[1]:
            if rplidar_distance <= rplidar_short_range_trigger:
                avoidance_steering('right')
                #print('turning right')
                #expression(look_right)
                obstacle = True
                return obstacle

            elif rplidar_distance > rplidar_short_range_trigger:
                pass

        elif center_zone[0] <= rplidar_angle <= center_zone[1]:
            if rplidar_distance <= rplidar_long_range_trigger and rplidar_angle < center_angle:
                avoidance_steering('right')
                #print('turning right')
                #expression(look_right)
                obstacle = True
                return obstacle

            elif rplidar_distance <= rplidar_long_range_trigger and rplidar_angle >= center_angle:
                avoidance_steering('left')
                #print('turning left')
                #expression(look_left)
                obstacle = True
                return obstacle

            elif rplidar_distance > rplidar_long_range_trigger:
                pass

        elif right_zone[0] < rplidar_angle <= right_zone[1]:
            if rplidar_distance <= rplidar_short_range_trigger:
                #print("lidar turn left")
                avoidance_steering('left')
                #print('turning left')
                #expression(look_left)
                obstacle = True
                return obstacle

            elif rplidar_distance > rplidar_short_range_trigger:
                pass
        else:
            obstacle = False
            return obstacle
    else:
        obstacle = False
        return obstacle

