import math

def distance_CB(dLatC,dLongC,waypointB_lat,lat):
    R = 6371000 # meters, Earths Radius
    havAngle = (math.sin(dLatC/2.0)**2) + math.cos(waypointB_lat)*math.cos(lat)*math.sin(dLongC/2.0)**2
    c = 2*math.atan2(math.sqrt(havAngle),math.sqrt(1-havAngle))
    D = R*c
    D = round(D,2)
    return D
