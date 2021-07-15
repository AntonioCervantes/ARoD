# This code is for the Raspberry Pi
# This module contain the functions for sending and recieving data with UART

import serial
import math, time

# For USB to Serial Cable
feather = serial.Serial('/dev/ttyUSB1', 9600, timeout = 1)
#feather = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) #####testing line only


# For RX/TX Pins
#feather = serial.Serial('/dev/ttyS0', 9600, timeout = 1)

# clears the buffer before sending data through UART
feather.flush()

max_left = 50
max_right = 130

########################## Send Function ##########################

def send(data):

    # formats the given steering angle to make sure that
    # it is 3 bytes long (nessesary for the angle decode on the feather)
    data = '%3d' % data

    # Writes number to UART lines
    feather.write(data.encode())
    feather.flush()
    #print('sending data')

########################## Receive Function ##########################

def receive():

    # formats the given steering angle to make sure that
    # it is 3 bytes long (nessisary for the angle decode on the feather)
    #value = '%3d' % value

    # Writes number to UART lines
    val = feather.read(5)
    msg = val.decode('utf-8').rstrip()

    return msg
    print('I got a {}'.format(msg))

########################## Weight Function ##############################

def weight():
    trigger = 1
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))
    time.sleep(1)
    msg = receive()
    #msg = 10
    return msg

########################## Open Door Function ###########################

def open_door():
    trigger = 2
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))

########################## Close Door Function ##########################

def close_door():
    trigger = 3
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))

########################## Open Door Adjust Function ###########################

def open_door_adjust():
    trigger = 7
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))

########################## Close Door Adjust Function ##########################

def close_door_adjust():
    trigger = 8
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))

########################## Drive On Function ############################

def drive_on():
    trigger = 4
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))


########################## Drive Off Function ###########################

def drive_off():
    trigger = 5
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))

########################## Drive Calibrate ###########################
def drive_cal():
    trigger = 6
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))

########################## Backup Function ##############################
def backup():
    trigger = 7
    send(trigger)
    print('I sent a {}, waiting for reply'.format(trigger))

########################## Steering Function ############################

def stanley_steering(steering_angle):

    # drive angle convertion
    if steering_angle < 0: # Turn Right (Robot is on left side of line)
        steering_angle = 90 + math.fabs(steering_angle)
        if steering_angle > max_right:
            steering_angle = max_right
            send(steering_angle)
            print('Turning Right:', steering_angle)
        else:
            send(steering_angle)
            print('Turning Right:', steering_angle)


    elif steering_angle > 0: # Turn left (Robot is on right side of line)
        steering_angle = 90 - math.fabs(steering_angle)
        if steering_angle < max_left:
            steering_angle = max_left
            send(steering_angle)
            print('Turning Left:', steering_angle)
        else:
            send(steering_angle)
            print('Turning Left:', steering_angle)


def avoidance_steering(direction):
    max_left = 50
    max_right = 130
    straight_angle = 90
    
    if direction == 'left':
        send(max_left)

    elif direction == 'right':
        send(max_right)
    
    elif direction == 'straight':
        send(straight_angle)
