# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example shows connecting to the PN532 with I2C (requires clock
stretching support), SPI, or UART. SPI is best, it uses the most pins but
is the most reliable and universally supported.
After initialization, try waving various 13.56MHz RFID cards over it!
"""

import board, time
import busio
from digitalio import DigitalInOut

#
# NOTE: pick the import that matches the interface being used
#
from adafruit_pn532.i2c import PN532_I2C

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)

# Non-hardware
# pn532 = PN532_I2C(i2c, debug=False)

# With I2C, we recommend connecting RSTPD_N (reset) to a digital pin for manual
# harware reset
reset_pin = DigitalInOut(board.D6)
# On Raspberry Pi, you must also connect a pin to P32 "H_Request" for hardware
# wakeup! this means we don't need to do the I2C clock-stretch thing
req_pin = DigitalInOut(board.D12)
pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

def rfid():
    ic, ver, rev, support = pn532.firmware_version
    #print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

    # Configure PN532 to communicate with MiFare cards
    pn532.SAM_configuration()

    #print("Waiting for RFID/NFC card...")

    # Check if a card is available to read
    #while True:
    uid = pn532.read_passive_target(timeout=0.5)
        #print(".", end="")
        # Try again if no card is available.
        #if uid is None:
            #continue
        #print("Found card with UID:", [hex(i) for i in uid])
        #break
    return uid

#while True:
    #uid = rfid()
    #print(uid)
    #time.sleep(0.1)