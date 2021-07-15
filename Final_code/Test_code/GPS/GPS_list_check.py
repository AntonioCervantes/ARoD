import sys
sys.path.append('/home/pi/Desktop/Final_code')
from Position_Orientation import gps_location,magnetometer
from distance_calc import distance_CB
import math

waypoints = []
with open("/home/pi/Desktop/Final_code/Waypoints/SU_Library_longway.txt", "r") as data:
    read_data = data.read()
    split_data = read_data.split("\n")
    
    for waypoint in split_data:
        new_split = waypoint.split(",")
        lat = float(new_split[0])
        long = float(new_split[1])
        lat_long_list = [lat,long]
        waypoints.append(lat_long_list)
    #print(waypoints)


lat = 37.33482
long = -121.88258

#print(lat,long)
min_distance = 1000000000
for location in range(len(waypoints)):
    
    waypointA_lat = waypoints[location][0]
    waypointA_long = waypoints[location][1]

    dLongC = math.radians(waypointA_long) - math.radians(long)
    dLatC = math.radians(waypointA_lat) - math.radians(lat)

    # Distance between point C and B
    D = distance_CB(dLatC,dLongC,waypointA_lat,lat)
    
    if D < min_distance:
        min_distance = D
        i = location
    
    
    print(D)

print("Min Dist: ",min_distance)
print("Waypoint #",i)

for location in range(i, len(waypoints)):
    print(waypoints[location])
