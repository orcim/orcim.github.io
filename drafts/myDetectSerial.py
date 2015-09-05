#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Search Port serial
    The scan function of this module tries to open each port number
    from 0 to 255 and try comunications.

    - scan

    140302 init
    140304 clean code & platform support
    140310 passaggio port
"""
myRev = "(rev.140310)"

import sys
#-----------------------------------------------------------------------------
# Module
#-----------------------------------------------------------------------------
from serial import Serial, SerialException

#-----------------------------------------------------------------------------
# myDefine
#-----------------------------------------------------------------------------
def scan(dev="/dev/ttyS", sta=1, end=256):
    """ scanner serial port
     --> None
     <-- list port available
    """
    mLis = []

    # if sys.platform == 'win32':
    #     # winzoz
    #     por = "COM"
    # else:
    #     # Unix
    #     por = "/dev/ttyS"
    #     #por = "/dev/ttyUSB"
    #     #por = "/dev/ttymxc"

    print "try with:", dev
    for ind in range(sta,end):
        try:
            ser = Serial("%s%d" %(dev, ind))
            por = ser.portstr.find(dev)
            print ser.portstr, por
            mLis.append( (ind, ser.portstr[sta:]))
            ser.close()
        except SerialException:
            pass
    print "found it:"
    return mLis

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__=='__main__':

    if 1:
        for ind, por in scan(dev="/dev/ttyS", sta=1, end=4):
            print "- %s" %(por)
    else:
        for ind, por in scan(dev="/dev/ttyUSB", sta=0, end=4):
            print "- %s" %(por)
            