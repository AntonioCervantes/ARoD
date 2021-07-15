import sys
from threading import Thread
sys.path.append('/home/pi/Desktop/Final_code')
from UART import send, receive, weight, open_door, close_door, drive_on, drive_off, drive_cal, backup, stanley_steering, avoidance_steering
from obstacle_avoidance import obstacle_avoidance
from stanley_control_law import stanley
from distance_calc import distance_CB
from LiDAR import RPLiDAR
from GPS import gps
from read_ultrasonic_data import ultrasonic
from RFID import rfid

import time,math
from Position_Orientation import gps_location,magnetometer
from datetime import datetime
#import pandas as pd

import sys
sys.path.append('/home/pi/Desktop/Final_code/Test_code/Stanely Control Test')
from steer_correct import steering_correct


waypoints = []
with open("/home/pi/Desktop/Final_code/Waypoints/SU_Library_longway_short.txt", "r") as data:
    read_data = data.read()
    split_data = read_data.split("\n")
    
    for waypoint in split_data:
        new_split = waypoint.split(",")
        lat = float(new_split[0])
        long = float(new_split[1])
        lat_long_list = [lat,long]
        waypoints.append(lat_long_list)
    print(waypoints)

'''
waypoints = [[37.33589, -121.88171],
             [37.33608, -121.88183],
             [37.33591, -121.88217],
             [37.33584, -121.88229],
             [37.33582, -121.88244],
             [37.33578, -121.88259]]

waypoints = [[37.33563, -121.88295],
             [37.33552, -121.8832],
             [37.3355,-121.88331],
             [37.3355, -121.88353]]
'''
stop_points = [waypoints[0],waypoints[-1]]

gps_location()
max_left = 50
max_right = 130
rfid_id = ['0xa2', '0x9a', '0x5c', '0x6f']


####################################################
################### Data Logging ###################
####################################################
with open('/home/pi/Desktop/data.txt', mode='a') as f:
    f.write('Date/Time,')
    f.write('Quality,')
    f.write('Satellites,')
    f.write('LatC,')
    f.write('LongC,')
    f.write('LatA,')
    f.write('LongA,')
    f.write('LatB,')
    f.write('LongB,')
    f.write('Desired Angle,')
    f.write('Current Angle,')
    f.write('Crosstrack Error,')
    f.write('Heading Error,')
    f.write('Steering Angle \n')
    f.flush()
        #f.close()

###### start threads for rplidar, gps, and ultrasonic ########

rplidar_thread = Thread(target = RPLiDAR)
gps_thread = Thread(target = gps)
ultrasonic_thread = Thread(target = ultrasonic)

rplidar_thread.start()
print('rplidar thread initiated')
gps_thread.start()
print('gps thread initiated')
ultrasonic_thread.start()
print('ultrasonic thread initiated')
    
##############################################################

#drive_cal()
#print('ESC Calibrating.....')
#time.sleep(30)
drive_on()
print('Drive On')
time.sleep(2)

while True:
    gps_data = gps_location()
    current_location = gps_data[0:2]

    for location in range(0, len(waypoints)):

        if waypoints[location] == stop_points[1]:
            stop_points = stop_points[::-1]
            print(stop_points)
            waypoints = waypoints[::-1]
            print(waypoints, '\n')
            drive_off()
            time.sleep(5)
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
                    ##open_door()
            print("door open")
            time.sleep(7)
            weight2 = int(weight())
            while abs(weight1 - weight2) <= 800:
                print('Second weight: {}'.format(weight2))
                print('Weight Difference: {}'.format(abs(weight1 - weight2)))
                print('Nothing has been added or removed')
                weight2 = int(weight())
                time.sleep(0.5)
            print('weight Difference: {}'.format(abs(weight1 - weight2)))
            print('Something was added or removed \n')
            time.sleep(5)
            ##close_door()
            print('Closing door \n')
            print("drive forward")
            
            drive_on()
            break
        else:
            gps_data = gps_location()
            current_location = gps_data[0:2]
            lat = current_location[0]
            long = current_location[1]

            waypointB_lat = waypoints[location+1][0]
            waypointB_long =waypoints[location+1][1]

            dLongC = math.radians(waypointB_long) - math.radians(long)
            dLatC = math.radians(waypointB_lat) - math.radians(lat)

            # Distance between point C and B
            D = distance_CB(dLatC,dLongC,waypointB_lat,lat)

            while D > 4:

                # Calling GPS Location Function
                # and setting variables equal to new data
                gps_data = gps_location()
                current_location = gps_data[0:2]
                lat = current_location[0]
                long = current_location[1]

                #speed = gps_data[2]
                speed = 1.0
                sat = gps_data[3]
                qual = gps_data[4]

                # Calling Magnetometer Function
                current_angle = magnetometer()

                # Checking the current time
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                waypointA_lat = waypoints[location][0]
                waypointA_long = waypoints[location][1]

                waypointB_lat = waypoints[location+1][0]
                waypointB_long =waypoints[location+1][1]

                steering_angle,desired_angle,crosstrack_error, heading_error = stanley(waypointA_lat,
                waypointA_long, waypointB_lat, waypointB_long, lat, long, speed, current_angle)

                stanley_steering(steering_angle)

                steering_angle = steering_correct(steering_angle)

                # as long as there is something in the way
                # keep runing obstical avoidance
                
                while obstacle_avoidance() is True:
                    print('I see something')
                    time.sleep(0.05)
                
                dLongC = math.radians(waypointB_long) - math.radians(long)
                dLatC = math.radians(waypointB_lat) - math.radians(lat)

                D = distance_CB(dLatC,dLongC,waypointB_lat,lat)

                # Print Statements
                if steering_angle < 80:
                    direction = 'left'
                elif steering_angle >= 80 and steering_angle <= 100:
                    direction = 'straight'
                else:
                    direction = 'right'
                print('Going to waypoint #',location+1)
                #print('Time/Date: ',dt_string)
                #print('dTheta: ',dtheta)
                #print("Initial angle:",desired_angle)
                #print('WaypointA: ',waypointA_lat,', ', waypointA_long)
                #print('WaypointB: ',waypointB_lat,', ', waypointB_long)
                print("Distance to waypoint B:",D,'m')
                #print('Speed:',speed,'m/s')
                #print('Quality: ', qual,' Satellites: ', sat)
                print('Current Point:',lat,long)
                print("Desired Angle: ",desired_angle)
                print('Current Angle: ',current_angle)
                #print('Heading Error',heading_error)
                print('Cross-track Error: ',crosstrack_error,'m')
                print('Steering angle: ',steering_angle,direction)
                print('-'*50,'\n')
                
                
                # Log Data
                with open('/home/pi/Desktop/data.txt', mode='a') as f:
                    f.write('{},'.format(dt_string))
                    f.write('{},'.format(qual))
                    f.write('{},'.format(sat))
                    f.write('{},'.format(lat))
                    f.write('{},'.format(long))
                    f.write('{},'.format(waypointA_lat))
                    f.write('{},'.format(waypointA_long))
                    f.write('{},'.format(waypointB_lat))
                    f.write('{},'.format(waypointB_long))
                    f.write('{},'.format(desired_angle))
                    f.write('{},'.format(current_angle))
                    f.write('{},'.format(crosstrack_error))
                    f.write('{},'.format(heading_error))
                    f.write('{}\n'.format(steering_angle))
                    f.flush()

                gps_data = gps_location()
                current_location = gps_data[0:2]
                time.sleep(0.1)

            print('#'*50,'\n'*15)
            print('Next waypoint segment','\n'*15)
            print('#'*50,'\n')
t