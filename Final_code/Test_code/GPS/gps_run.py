import time, math, board, digitalio, adafruit_gps, serial, busio

# GPS Setup
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
FIX = digitalio.DigitalInOut(board.D11)
FIX.direction = digitalio.Direction.OUTPUT

while True:
#while True:
    gps.update()
    # Every second print out current location details if there's a fix.
    while not gps.has_fix:
        FIX.value = False
        # Try again if we don't have a fix yet.
        print("Waiting for fix...")
        time.sleep(0.1)
        break
    gps.update()
    #break
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
    lat = str(lat)
    long = str(long)
    speed = str(speed)
    sat = str(sat)
    qual = str(qual)
    gps_data = lat + ',' + long + ',' + speed+ ',' + sat+ ',' + qual


    print(gps_data)

    with open("/home/pi/Desktop/gps.txt", "w") as output:
        output.write(gps_data)
    time.sleep(0.01)

