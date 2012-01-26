#!/usr/bin/env python

import optparse
import sys
import serial
import time
import collections 

usage = "Usage: %prog /dev/tty.usbXXXX"
parser = optparse.OptionParser(usage=usage)
parser.add_option("-l", action="store", type="string", dest="logfilename", default=None, help="Optional logfile timestamps and readings.")

if len(sys.argv) != 2:
    print usage
    sys.exit(1)

(options,args) = parser.parse_args()
logfilename = options.logfilename

serport = sys.argv[1]

ser = serial.Serial(serport, 9600)

# discard a couple of readings
ser.readline()
ser.readline()

if logfilename:
    try:
        outfile = open(logfilename, 'a')
    except IOError:
        print >> sys.stderr, "Unable to open %s for appending." % logfilename

# Python's awkward way of getting a circular buffer
timestamps = collections.deque([],maxlen=100)
readings = collections.deque([],maxlen=100)

def humanTime(curTime):
    return str(curTime.tm_hour).zfill(2) + ':' + str(curTime.tm_min).zfill(2)

try:
    while 1:
        reading = ser.readline().rstrip()
        readings.append(reading)
        timestamps.append(time.localtime())
        print humanTime(timestamps[0]), readings[0]
        if logfilename:
            outfile.write("%s,%s\n" % (timestamps[0], reading))
except StandardError:
    if logfilename:
        outfile.flush()
        outfile.close()
    print >> sys.stderr, "Error."
except:
    print >> sys.stderr, "Error."
