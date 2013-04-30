#!/usr/bin/env python
# /* -*-  indent-tabs-mode:t; tab-width: 8; c-basic-offset: 8  -*- */
# /*
# Copyright (c) 2013, Daniel M. Lofaro
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# */

import sys
import time
from ctypes import *
import commands as c
import curses
import time
import hubo_walking as hw
import ach



stdscr = curses.initscr()
curses.cbreak()

sIndent = 11
sLine = 9




# Open Ach Channels and create variables
wch = ach.Channel(hw.HUBO_CHAN_WALKING_NAME)
wch.flush()
wcmd = hw.HUBO_WALKING()



stdscr.refresh()


stdscr.addstr(2, 2, "Hubo Walking: Daniel M. Lofaro <dan@danLofaro.com>")
stdscr.addstr(3, 2, "-------------------------------------------------")
stdscr.addstr(4, 2, "Inputs: Ach (UP, LEFT, RIGHT)")
stdscr.addstr(7,2,"Hit 'q' to quit")

stdscr.addstr(sLine,2,"Status:")

stdscr.addstr(sLine, sIndent,"Going to WALK READY       ")
stdscr.refresh()
c.getoutput('./walk.sh walkready')
time.sleep(2.0)



key = ''
while True:
  try:
    stdscr.addstr(sLine, sIndent,"Give Command                         ")
    stdscr.refresh()
    [statusw, framesizew] = wch.get(wcmd, wait=False, last=False)
#    [statusw, framesizew] = wch.get(wcmd, wait=True, last=False)
    if wcmd.cmd == hw.forward: 
        stdscr.addstr(sLine, sIndent, "Going Forward                   ")
        stdscr.refresh()
        c.getoutput('./walk.sh forward')
    elif wcmd.cmd == hw.forward5: 
        stdscr.addstr(sLine, sIndent, "Going Forward                   ")
        stdscr.refresh()
        c.getoutput('./walk.sh forward5')
    elif wcmd.cmd == hw.turn: 
        stdscr.addstr(sLine, sIndent, "Turning "+str(wcmd.angle)+" rad          ")
        stdscr.refresh()
        c.getoutput('./walk.sh turn '+str(wcmd.angle))
    elif wcmd.cmd == hw.home: 
        break
    else: 
        stdscr.addstr(sLine, sIndent, "Bad Command                    ")
        stdscr.refresh()
    time.sleep(5.0)
    wch.flush()
  except KeyboardInterrupt:
    break




stdscr.addstr(sLine, sIndent,"Going to HOME         ")
stdscr.refresh()
c.getoutput('./walk.sh home')
curses.endwin()

#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -n walking_traj/walkReady.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -n walking_traj/walkReadyOneSecWait.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -n walking_traj/walkFiveSteps0p2m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -w 0.3 -n walking_traj/walk1sTurnBase0m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -w 0.3 -n walking_traj/walk1sTurnBase0m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -w 0.3 -n walking_traj/walk1sTurnBase0m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -w 0.3 -n walking_traj/walk1sTurnBase0m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -n walking_traj/walkFiveSteps0p2m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -w -0.3 -n walking_traj/walk1sTurnBase0m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -w -0.3 -n walking_traj/walk1sTurnBase0m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -w -0.3 -n walking_traj/walk1sTurnBase0m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -n walking_traj/walkFiveSteps0p2m.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -n walking_traj/walkReadyOneSecWait.traj')
#c.getoutput('sudo ./hubo-read-trajectory -s -f 200 -n walking_traj/home.traj')
