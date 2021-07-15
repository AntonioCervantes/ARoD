import sys
sys.path.append('/home/pi/Desktop/Final_code')
import time
from Position_Orientation import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
#import pandas as pd

waypoints = [[37.12475,-121.64192],
             [37.12364,-121.64119]]

#plt.style.use('fivethirtyeight')
# X - Long
# Y - Lat
deg_LatC, deg_LongC, v, sat, qual = gps_location()
angle = magnetometer()
i = count()

lat = []
long = []
Alat = []
Along = []
Blat = []
Blong = []
A = []
B = []

mag = []
t = []
des = []

fig = plt.figure(1)
ax1 = fig.add_subplot(2,1,1)
ax1.set_ylabel('Latitude')
ax1.set_xlabel('Longitude')
ax2 = fig.add_subplot(2,1,2)
ax2.set_ylabel('Heading [Deg]')
ax2.set_xlabel('Time [sec]')



def update_data(i):
    ax1.cla()
    ax2.cla()

    ###################################
    ############### GPS ###############
    ###################################
    waypointA_lat = waypoints[0][0]
    waypointA_long = waypoints[0][1]
    waypointB_lat = waypoints[1][0]
    waypointB_long =waypoints[1][1]
    deg_LatC, deg_LongC, v, sat, qual = gps_location()
    lat.append(deg_LatC)
    long.append(deg_LongC)
    Alat.append(waypointA_lat)
    Along.append(waypointA_long)
    Blat.append(waypointB_lat)
    Blong.append(waypointB_long)
    A = [Alat,Blat]
    B = [Along,Blong]
    ax1.plot(long,lat, label='GPS Points')
    ax1.plot([Along,Blong],[Alat,Blat],label='Waypoint A-B')
    #ax1.legend()

    ##################################
    ########## Magnetometer ##########
    ##################################
    angle = magnetometer()
    t_sec = time.monotonic()
    desired = 25
    mag.append(angle)
    des.append(desired)
    t.append(t_sec)
    ax2.plot(t,mag, label='Heading')
    ax2.plot(t,des, label='Desired Heading')
    ax2.legend()


gps_ani = FuncAnimation(fig, update_data, interval=100)
plt.tight_layout()
plt.show()