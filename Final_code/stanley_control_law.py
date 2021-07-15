''' AR-o-D
    ME195

    last updated: 3/17/2021

    This is the Stanley Control Law Module.'''

from Position_Orientation import gps_location,magnetometer
import math
import time
from datetime import datetime

##########################################################
####################### Assumptions ######################
##########################################################
# X - Long
# Y - Lat

# deg_LatA/deg_LatB Latitude/Longtitude coordinates in degrees
# LatA/LongA Latitude/Longtitude coordinates in radians

# Each time this module is called, it is set to follow an incremental pathline
# consisting of a start and end (waypointA/waypointB). As is travel along its
# delivery it will need to update these waypoints as it reeaches them in order
# to change direction and follow the specified path.




def stanley(waypointA_Lat, waypointA_Long, waypointB_Lat, waypointB_Long,deg_LatC,deg_LongC,speed,mag_angle):

    ##########################################################
    ################## Path Following Setup ##################
    ##########################################################
    
     # Waypoint A: first point of the incremental path line (where the robot starts)
    xA = math.radians(waypointA_Long)   # radians (x-axis)
    yA = math.radians(waypointA_Lat)    # radians (y-axis)

    # Waypoint B: second point of the incremental path line (where the robot is going)
    xB = math.radians(waypointB_Long)   # radians (x-axis)
    yB = math.radians(waypointB_Lat)    # radians (y-axis)

    # Latitude/Longitude Difference Calculations
    dx_AB = xB - xA   # radians (x-axis)
    dy_AB = yB - yA   # radians (y-axis)
    
    # Current Position
    xC = math.radians(deg_LongC)  # radians (x-axis)
    yC = math.radians(deg_LatC)   # radians (y-axis)

    dx_CB = xB - xC  # radians
    dy_CB = yB - yC  # radians
    
    # Correcting Desired Angle Calculation
    if dx_AB == 0:
        angle_div = 0
    else:
        angle_div = (dy_AB) / (dx_AB)

    # Desired Angle Calculation
    desired_angle = math.degrees( math.atan( angle_div ) )    # degrees

    declination = 13
    
    # Correcting Desired Angle Calculation in clockwise degree format
    if dx_AB < 0 and dy_AB > 0:
        desired_angle = desired_angle + 360+10
        #print("Quadrant 4")
    elif dx_AB < 0 and dy_AB < 0:
        desired_angle = desired_angle + 180+20
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
        #print("Quadrant 1 or 0 deg axis")
    desired_angle = desired_angle + declination
    # Stanley Control Gains
    k = 1      # Proportional Constant
    ks = 1     # Softening Constant

    # Linear Velocity
    v = speed

    ##########################################################
    ###################### Magnetometer ######################
    ##########################################################

    # Calculating Current angle of robot
    current_angle = mag_angle


    ##########################################################
    ################## Stanley Control Law ###################
    ##########################################################

    ################## Cross-track Error #####################

    # Waypoint A: first point of the incremental path line (where the robot starts)
    xA = math.radians(waypointA_Long)   # radians (x-axis)
    yA = math.radians(waypointA_Lat)    # radians (y-axis)

    # Waypoint B: second point of the incremental path line (where the robot is going)
    xB = math.radians(waypointB_Long)   # radians (x-axis)
    yB = math.radians(waypointB_Lat)    # radians (y-axis)

    # Latitude/Longitude Difference Calculations
    dx_AB = xB - xA   # radians (x-axis)
    dy_AB = yB - yA   # radians (y-axis)
    
    # Current Position
    xC = math.radians(deg_LongC)  # radians (x-axis)
    yC = math.radians(deg_LatC)   # radians (y-axis)

    dx_CB = xB - xC  # radians
    dy_CB = yB - yC  # radians

    R = 6371000.0 # meters, Earths Radius
    havAngle = (math.sin(dy_AB/2.0)**2)
    + math.cos(yA)*math.cos(yB)*math.sin(dx_AB/2.0)**2
    c = 2.0*math.atan2(math.sqrt(havAngle),math.sqrt(1-havAngle))
    D = R*c # Distance between point A and B
    
    # Angle between line AC and AB
    dtheta = math.atan2(dy_CB,dx_CB) - math.atan2(dy_AB,dx_AB)

    e = math.sin(dtheta)*D
    crosstrack_error = round(e,2)

    # Heading Error
    heading_error = current_angle - desired_angle   # degrees

    # Stanley Control Law
    steering_angle = heading_error + math.degrees((math.atan( (k*e) / (v+ks) ) ))


    return steering_angle, desired_angle, crosstrack_error, heading_error