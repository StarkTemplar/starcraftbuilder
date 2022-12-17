from ast import Try
import error
from unit import *

maxtime = 10000

class Unit():
    def __init__(self, typ, unit, time, time2=maxtime, state='start'):
        self.type = typ
        self.state = state
        self.name = unit
        self.starttime = time
        self.endtime = time2
        self.linked = 0
        self.buildlinked = 0
        self.inputlink = 0
        self.boosted = 0
        self.queue = []

    def setLinked(self, link):
        if type(link) != Unit or link.type != 'unit':
            return error.NotUnitType
        self.linked = link
        link.linked = self
        return 0

    def setBuildingLink(self, link):
        if type(link) != Unit or link.type != 'building':
            return error.NotBuildingType
        self.buildinglinked = link
        if self.linked != 0:
            self.linked.buildinglinked = link
        return 0

    def setInputLink(self, link):
        if type(link) != int or link<0:
            return error.WrongIndex
        self.inputlink = link
        if self.linked != 0:
            self.linked.inputlink = link

    def add(self, u):
        if type(u) != Unit:
            return error.NotUnitType
        self.queue.append(u)

# mineral[i] = no of workers gathering minerals from time[i] to time[i+1] (or forever)
# gas[i] = nothing different with mineral[i] but only gases
class Worker():
    def __init__(self):
        self.time = []
        self.mineral = []
        self.gas = []
        self.donothing = [] #doing nothing or building
        self.scouting = []
    # if m is negative, mineral schedule preserves
    # same as others
    def addSchedule(self, t, m, g, n, s):
        self.time.append(t)
        self.mineral.append(m)
        self.gas.append(g)
        self.donothing.append(n)
        self.scouting.append(s)

class ChronoSchedule():
    def __init__(self):
        self.time = []
        self.target = []

    def addSchedule(self, t, b):
        if len(self.time)>0 and self.time[-1] + 88 > t: #default of 4 seconds. changed to 88 seconds to mimic energy generation rate of 0.5625 energy gained per second.
            return error.ChronoCooldown
        self.time.append(t)
        self.target.append(b)
        return 0

    def checkTargetIsBoosted(self, t, time):
        if len(self.target)>0: #starting nexus target array will be empty
            if self.target[-1] == t: #check if target and item in queue are the same
                if len(self.time)>0 and time - self.time[-1] > 20: #verify chronoboost is at least 20 seconds after previous chronoboost
                    return 0
                else:
                    return error.AlreadyBoosted
            return 0
        else:
            return 0
