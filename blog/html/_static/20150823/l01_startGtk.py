#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

    - 
"""

myRev = "(rev.150823)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from myApp import MyApp

#-----------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# myClass
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def myTry01():
    """ + window (self)                                                   
    "conf                                       .------------------------.
    "0001 - aBox            (h application)     | application            |
    "0002   - gBox            (h global)        |   .--------------------.
    "0004   - mBox            (v main)          |   | g | m | menu       |
    "0008     - uBox            (h menu)        |   | l | a .------------.
    "0010     - bBox            (v body)        |   | o | i | body       |
    "0020     - sBox            (h status)      |   | b | n |            |
    "                                           |   | a |   .------------.
    "                                           |   | l |   | status     |
    "                                           .---.---.----------------.
    """ 
    # istanza l'applicazione 
    self = MyApp(width=400, height=400, title="myApp", 
                    center=True, color="#bbb", conf=0x003f, show=1)

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    # test arguments
    if len(sys.argv) == 1:
        # no arguments (scelgo io)
        choi = 1
    else:
        # get first argument (scelta esterna)
        choi = int(sys.argv[1])

    if choi == 1:
        # draw Applications (MyApp)
        myTry01()
    elif choi == 2:
        # draw Applications (MyApp)
        myTry01()

    # avvia applicazione
    Gtk.main()