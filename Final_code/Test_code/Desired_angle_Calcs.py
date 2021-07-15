import math

waypoints = []
with open("/home/pi/Desktop/Final_code/Waypoints/SU_Dorms.txt", "r") as data:
    read_data = data.read()
    split_data = read_data.split("\n")
    
    for waypoint in split_data:
        new_split = waypoint.split(",")
        lat = float(new_split[0])
        long = float(new_split[1])
        lat_long_list = [lat,long]
        waypoints.append(lat_long_list)
    #print(waypoints)
    
for location in range(len(waypoints)-1):
    
    declination = 13
    
    waypointA_Lat = waypoints[location][0]
    waypointA_Long = waypoints[location][1]

    waypointB_Lat = waypoints[location+1][0]
    waypointB_Long =waypoints[location+1][1]
    
    # Waypoint A: first point of the incremental path line (where the robot starts)
    xA = math.radians(waypointA_Long)   # radians (x-axis)
    yA = math.radians(waypointA_Lat)    # radians (y-axis)

    # Waypoint B: second point of the incremental path line (where the robot is going)
    xB = math.radians(waypointB_Long)   # radians (x-axis)
    yB = math.radians(waypointB_Lat)    # radians (y-axis)

    # Latitude/Longitude Difference Calculations
    dx_AB = xB - xA   # radians (x-axis)
    dy_AB = yB - yA   # radians (y-axis)
    
    # Correcting Desired Angle Calculation
    if dx_AB == 0:
        angle_div = 0
    else:
        angle_div = (dy_AB) / (dx_AB)

    # Desired Angle Calculation
    desired_angle = math.degrees( math.atan( angle_div ) )    # degrees

    # Correcting Desired Angle Calculation in clockwise degree format
    if dx_AB < 0 and dy_AB > 0:
        desired_angle = desired_angle + 360
        #print("Quadrant 4")
    elif dx_AB < 0 and dy_AB < 0:
        desired_angle = desired_angle + 180
        #print("Quadrant 3")
    elif dx_AB > 0 and dy_AB < 0:
        desired_angle = desired_angle + 180
        #print("Quadrant 2")

    elif dx_AB > 0 and dy_AB == 0:
        desired_angle = desired_angle + 90
        #print("90 deg axis")
    elif dx_AB == 0 and dy_AB < 0:
        desired_angle = desired_angle + 180
        #print("180 deg axis")
    elif dx_AB < 0 and dy_AB == 0:
        desired_angle = desired_angle + 270 - declination*3
        #print("270 deg axis")
    else:
        desired_angle = desired_angle
        #print("else")
    desired_angle = desired_angle + declination
    
    print("Waypoint Seg: ",location," Angle: ",desired_angle)
    
waypoints = waypoints[::-1]
print("#"*20,"List Flip","#"*20)

for location in range(len(waypoints)-1):
    
    declination = 13
    
    waypointA_Lat = waypoints[location][0]
    waypointA_Long = waypoints[location][1]

    waypointB_Lat = waypoints[location+1][0]
    waypointB_Long =waypoints[location+1][1]
    
    # Waypoint A: first point of the incremental path line (where the robot starts)
    xA = math.radians(waypointA_Long)   # radians (x-axis)
    yA = math.radians(waypointA_Lat)    # radians (y-axis)

    # Waypoint B: second point of the incremental path line (where the robot is going)
    xB = math.radians(waypointB_Long)   # radians (x-axis)
    yB = math.radians(waypointB_Lat)    # radians (y-axis)

    # Latitude/Longitude Difference Calculations
    dx_AB = xB - xA   # radians (x-axis)
    dy_AB = yB - yA   # radians (y-axis)
    
    # Correcting Desired Angle Calculation
    if dx_AB == 0:
        angle_div = 0
    else:
        angle_div = (dy_AB) / (dx_AB)

    # Desired Angle Calculation
    desired_angle = math.degrees( math.atan( angle_div ) )    # degrees


    # Correcting Desired Angle Calculation in clockwise degree format
    if dx_AB < 0 and dy_AB > 0:
        desired_angle = desired_angle + 360
        #print("Quadrant 4")
    elif dx_AB < 0 and dy_AB < 0:
        desired_angle = desired_angle + 180
        #print("Quadrant 3")
    elif dx_AB > 0 and dy_AB < 0:
        desired_angle = desired_angle + 180
        #print("Quadrant 2")


    elif dx_AB > 0 and dy_AB == 0:
        desired_angle = desired_angle + 90
        #print("90 deg axis")
    elif dx_AB == 0 and dy_AB < 0:
        desired_angle = desired_angle + 180
        #print("180 deg axis")
    elif dx_AB < 0 and dy_AB == 0:
        desired_angle = desired_angle + 270
        #print("270 deg axis")
    else:
        desired_angle = desired_angle
        #print("else")
    desired_angle = desired_angle + declination
    
    print("Waypoint Seg: ",location," Angle: ",desired_angle)
    