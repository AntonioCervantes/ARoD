import smbus
import time
import sys

lidar_distance = 1

class Lidar_Lite():
    def __init__(self):
        self.address = 0x62
        self.distWriteReg = 0x00
        self.distWriteVal = 0x04
        self.distReadReg1 = 0x8f
        self.distReadReg2 = 0x10
        self.velWriteReg = 0x04
        self.velWriteVal = 0x08
        self.velReadReg = 0x09

    def connect(self, bus):
        try:
            self.bus = smbus.SMBus(bus)
            time.sleep(0.5)
            return 0
        except:
            return -1

    def writeAndWait(self, register, value):
        self.bus.write_byte_data(self.address, register, value);
        time.sleep(0.02)

    def readAndWait(self, register):
        res = self.bus.read_byte_data(self.address, register)
        time.sleep(0.02)
        return res

    def getDistance(self):
        self.writeAndWait(self.distWriteReg, self.distWriteVal)
        dist1 = self.readAndWait(self.distReadReg1)
        dist2 = self.readAndWait(self.distReadReg2)
        #print(type(dist1))
        #print(dist2)
        return (dist1 << 8) + (dist2<< 8)

    def getVelocity(self):
        self.writeAndWait(self.distWriteReg, self.distWriteVal)
        self.writeAndWait(self.velWriteReg, self.velWriteVal)
        vel = self.readAndWait(self.velReadReg)
        return self.signedInt(vel)

    def signedInt(self, value):
        if value > 127:
            return (256-value) * (-1)
        else:
            return value

lidar = Lidar_Lite()
connected = lidar.connect(1)

if connected < -1:
    print("Not Connected")

while True:
    try:
        lidar_distance = lidar.getDistance()
        lidar_vel = lidar.getVelocity()
        print('Lidar Distance: ',lidar_distance)
        #print('Lidar velocity: ',lidar_vel)
    except:
        print("ERROR")
        time.sleep(0.1)
