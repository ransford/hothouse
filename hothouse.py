#!/usr/bin/env python

import sys
import serial

if len(sys.argv) != 2:
    print >> sys.stderr, "Usage: %s /dev/tty.usbXXXX" % sys.argv[0]
    sys.exit(1)

logfilename = 'hothouse.log' # XXX use getopts

serport = sys.argv[1]

ser = serial.Serial(serport, 9600)

# discard a couple of readings
ser.readline()
ser.readline()

readings = ()

try:
    outfile = open(logfilename, 'a')
except IOError:
    print >> sys.stderr, "Unable to open %s for appending." % logfilename

try:
    while 1:
        reading = ser.readline().rstrip()
        readings.append(reading)
        outfile.write("%f,%s\n" % (time.time(), reading))
except StandardError:
    outfile.flush()
    outfile.close()
except:
    print >> sys.stderr, "Error."
