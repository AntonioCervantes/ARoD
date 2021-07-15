import sys
sys.path.append('/home/pi/Desktop/Final_code')
#from UART import *
from stanley_control_law import *
import time
from Position_Orientation import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

waypoints = [[37.1243,-121.64105],
             [37.1243,-121.64127]]
'''
waypoints_tolerance = [[37.3362,-121.8819],
                     [37.3354,-121.8813]]
                     '''

gps_location()
max_left = 50
max_right = 130

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
'''
#####################################################
################### Data Plotting ###################
#####################################################
lat = []
long = []
Alat = []
Along = []
Blat = []
Blong = []

mag = []
t = []
des = []

x_track_error = []
x_track_zero = []

steering = []

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax1.set_ylabel('Latitude')
ax1.set_xlabel('Longitude')
ax2 = fig.add_subplot(2,2,2)
ax2.set_ylabel('Heading [deg]')
ax2.set_xlabel('Time [sec]')
ax3 = fig.add_subplot(2,2,3)
ax3.set_ylabel('Crosstrack Error [m]')
ax3.set_xlabel('Time [sec]')
ax4 = fig.add_subplot(2,2,4)
ax4.set_ylabel('Steering Angle [deg]')
ax4.set_xlabel('Time [sec]')

def update_data(i):
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()

    ###################################
    ############### GPS ###############
    ###################################
    A_lat = waypoints[0][0]
    A_long = waypoints[0][1]
    B_lat = waypoints[1][0]
    B_long =waypoints[1][1]
    deg_LatC, deg_LongC, v, sat, qual = gps_location()
    lat.append(deg_LatC)
    long.append(deg_LongC)
    Alat.append(A_lat)
    Along.append(A_long)
    Blat.append(B_lat)
    Blong.append(B_long)
    ax1.plot(long,lat, label='GPS Points')
    ax1.plot([Along,Blong],[Alat,Blat],label='Waypoint A-B')
    #ax1.legend()

    ##################################
    ########## Magnetometer ##########
    ##################################
    angle = magnetometer()
    t_sec = time.monotonic()
    mag.append(angle)
    des.append(desired_angle)
    t.append(t_sec)
    ax2.plot(t,mag, label='Heading')
    ax2.plot(t,des, label='Desired Heading')
    ax2.legend()

    ######################################
    ########## Crosstrack Error ##########
    ######################################
    x_zero = 0
    x_track_error.append(crosstrack_error)
    x_track_zero.append(x_zero)
    ax3.plot(t,x_track_error, label='Crosstrack Error')
    ax3.plot(t,x_track_zero, label='Zero')
    ax3.legend()

    ######################################
    ########### Steering Angle ###########
    ######################################
    steering.append(steering_angle)
    ax4.plot(t,steering, label='Steering Angle')
    ax4.legend()
'''
while True:
    gps_data = gps_location()
    current_location = gps_data[0:2]

    while current_location != waypoints[1]:
        # Calling GPS Location Function
        # and setting variables equal to new data
        gps_data = gps_location()
        current_location = gps_data[0:2]
        lat = current_location[0] 
        long = current_location[1]
        
        if lat is not None:
            lat = round(lat,5)
        
        else:
            lat = lat
        
        if long is not None:
            long = round(long,5)
            
        else:
            long = long
        
        speed = gps_data[2]
        sat = gps_data[3]
        qual = gps_data[4]
        if speed is not None:
            speed = round((speed / 1.944),2) # m/s
        else:
            speed = 1.5 # m/s SPEED OF ARoD
            
        # Calling Magnetometer Function
        current_angle = magnetometer()
        
        # Checking the current time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
        
        # if its not the desired end point
        # set up current waypoints and
        # run the steering function
        waypointA_lat = waypoints[0][0]
        waypointA_long = waypoints[0][1]

        waypointB_lat = waypoints[1][0]
        waypointB_long =waypoints[1][1]

        
        steering_angle,desired_angle,crosstrack_error, heading_error = stanley(waypointA_lat,
        waypointA_long, waypointB_lat, waypointB_long, lat, long, speed, current_angle)
        
        
        #print('Steering Angle (Uncorrected)',steering_angle)

        ##################################################
        ##### Printing the Corrected Steering Angle ######
        ##################################################

        
        if steering_angle > 0: # Turn left (Robot is on right side of line)
            steering_angle = 90 - math.fabs(steering_angle)
            if steering_angle < max_left:
                steering_angle = max_left
                print('Turning Left (Corrected):', steering_angle)
            else:
                print('Turning Left (Corrected):', steering_angle)
                
        elif steering_angle < 0: # Turn Right (Robot is on left side of line)
            steering_angle = 90 + math.fabs(steering_angle)
            if steering_angle > max_right:
                steering_angle = max_right
                print('Turning Right (Corrected):', steering_angle)
            else:
                print('Turning Right (Corrected):', steering_angle)
        
        
        
        #ani = FuncAnimation(fig, update_data, interval=100)
        #plt.tight_layout()
        #plt.show()
        
        # Print Statements
        #print('Not there yet')
        #print('Time/Date: ',dt_string)
        #print('dTheta: ',dtheta)
        #print("Initial angle:",desired_angle)
        #print('WaypointA: ',waypointA_Lat,', ', waypointA_Long)
        #print('WaypointB: ',waypointB_Lat,', ', waypointB_Long)
        #print("Distance between waypoints:",D, "m")
        #print("Desired Angle: ",desired_angle)
        #print('Speed:',speed,'m/s')
        #print('Quality: ', qual,' Satellites: ', sat)
        print('Current Point:',lat,long)
        print('Current Angle: ',current_angle)
        print('Cross-track Error: ',crosstrack_error,'m')
        #print('Heading Error',heading_error)
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
        time.sleep(1)
