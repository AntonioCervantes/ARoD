       
def RPLiDAR():
    
    from math import cos, sin, pi, floor
    from adafruit_rplidar import RPLidar
    import time

    PORT_NAME = '/dev/ttyUSB2'
    rplidar = RPLidar(None, PORT_NAME)

    def process_data(data):
        for angle in range(360):
            distance = data[angle]
            if distance > 0:
                radians = angle * pi / 180.0
                x = distance * cos(radians)
                y = distance * sin(radians)
    while True:
        scan_data = [0]*360
        rplidar.connect()
        for scan in rplidar.iter_scans():
            for (_, angle, distance) in scan:
                scan_data[min([359, floor(angle)])] = distance
            process_data(scan_data)
            rplidar_distance = 999999999
            for piece in scan:
                if piece[2] < rplidar_distance:
                    rplidar_distance = piece[2]
                    rplidar_angle = piece[1]
            rplidar_distance = str(rplidar_distance)
            rplidar_angle = str(rplidar_angle)

            min_data = rplidar_distance + "," + rplidar_angle

            #print(min_data)
            with open("/home/pi/Desktop/rplidar_info.txt", "w") as output:
                output.write(min_data)
            time.sleep(0.0001)