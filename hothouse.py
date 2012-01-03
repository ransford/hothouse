#!/usr/bin/env python

import sys
import serial

if len(sys.argv) != 2:
    print >> sys.stderr, "Usage: %s /dev/tty.usbXXXX" % sys.argv[0]
    sys.exit(1)

serport = sys.argv[1]

ser = serial.Serial(serport, 9600)

# discard a couple of readings
ser.readline()
ser.readline()

while 1:
    print ser.readline().rstrip()
