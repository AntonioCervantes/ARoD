''' AR-o-D
    ME195

    last updated: 3/17/2021

    This is the Position & Orientation Module.'''

import time, math, board, digitalio, adafruit_gps, serial, adafruit_lsm9ds1, busio

############################# GPS #############################

# GPS Setup
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
FIX = digitalio.DigitalInOut(board.D11)
FIX.direction = digitalio.Direction.OUTPUT

def gps_location():
    with open("/home/pi/Desktop/gps.txt", "r") as data:
        read_data = data.read()
        split_data = read_data.split(",")
        try:
            global lat
            global long
            global speed
            global sat
            global qual
            lat = float(split_data[0])
            long = float(split_data[1])
            speed = float(split_data[2])
            sat = float(split_data[3])
            qual = float(split_data[4])
            gps_data = [lat, long, speed, sat, qual]
        except ValueError:
            pass
        gps_data = [lat, long, speed, sat, qual]
        return gps_data

'''
def gps_location():
    while True:
        gps.update()
        # Every second print out current location details if there's a fix.
        if not gps.has_fix:
            FIX.value = False
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            time.sleep(0.1)
            continue
        gps.update()
        break
    gps.update()
    lat = gps.latitude 
    long = gps.longitude
    speed = gps.speed_knots
    
    # Rounds value to 5 decimal places
    if lat is not None:
        lat = round(lat,5)
    else:
        lat = lat

    if long is not None:
        long = round(long,5)
    else:
        long = long
        
    if speed is not None:
        speed = round((speed / 1.944),2) # m/s
    else:
        speed = 1.5 # m/s SPEED OF ARoD
        
    sat = gps.satellites
    qual = gps.fix_quality
    gps_data = [lat, long, speed, sat, qual]
    return gps_data
''' 
############################# Magnetometer #############################

# Magnetometer Setup
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

# Offsets for ARoD (UPDATED: 4/30/21)
offset_x = 0.1110
offset_y = 0.2406
offset_z = -0.0126
'''
# Offsets for Breadboard (UPDATED: 4/3/21)
offset_x = 0.233
offset_y = 0.4235
offset_z = 0.1835
'''
def magnetometer():
    mag_x, mag_y, mag_z = sensor.magnetic
    cal_x = mag_x - offset_x
    cal_y = mag_y - offset_y
    cal_z = mag_z - offset_z

    angle = math.atan2( cal_y , cal_x ) * ( 180 / math.pi )

    if angle > 0:
        angle = angle + 180
    elif angle < 0:
        angle = angle + 180
    return angle