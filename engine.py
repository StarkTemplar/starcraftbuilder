from unit import *
from unitclass import *
import error

class Engine():
    def __init__(self, race):
        self.race = race
        self.input = []
        self.queue = []
        self.chrono = []
        self.worker = Worker()
        # game starts
        if race == 'protoss':
            n = 'nexus'
            w = 'probe'
        elif race == 'terran':
            n = 'command center'
            w = 'scv'
        elif race == 'zerg':
            n = 'hatchery'
            w = 'drone'
        else:
            print("Wrong race : %s"%race)
            raise

        self.queue.append(Unit('building', n,0,state='end'))
        
        #start chronoboost on starting nexus
        if race == 'protoss':
            self.chrono.append(ChronoSchedule())
            #self.chrono[0].addSchedule(0, self.queue[-1]) #only use if you want starting nexus to start with chronoboost

        #create starting 12 workers
        for i in range(12):
            self.queue.append(Unit('unit',w,0,state='end'))

        #generate larva for zerg
        if race == "zerg":
            for i in range(3):
                self.queue.append(Unit('unit',"larva",0,state='end'))

        self.worker.addSchedule(0,8,0,0,0,0) #8 workers get to a mineral patch immediatly
        self.worker.addSchedule(3.825,4,0,0,0,0) #4 workers have to wait 3.825 seconds to start mining

# quick sort according to 'starttime'
    def SortQueue(self, x):
        if len(x)<=1:
            return x

        pivot = x[len(x) // 2]
        left = []
        right = []
        equal = []
        for i in x:
            if i.starttime < pivot.starttime:
                left.append(i)
            elif i.starttime > pivot.starttime:
                right.append(i)
            else:
                equal.append(i)

        return self.SortQueue(left) + equal + self.SortQueue(right)

    def AddItem(self, name, typ):
        self.input.append( (name,typ) )

    def DeleteItem(self, no):
        if no<-1 or no>=len(self.input):
            return error.WrongIndex
        elif no == -1:
            self.input.pop()
        else:
            self.input.pop(no)
        return self.Rearrange()

    def Rearrange (self):
        t = Engine(self.race)
        c = 0
        print("\n*** New Simulation ***")
        for i in range(len(self.input)):
            if self.input[i][1] == 'unit' or self.input[i][1] == 'upgrade':
                if i>0 and self.input[i-1][0] == "chronoboost":
                    c = t.BuildUnit(self.input[i][1], self.input[i][0], c, True)
                    if c<0:
                        return c
                    target = unit_dict[self.input[i][1]][self.race][self.input[i][0]]['buildfrom']
                    c = t.Chronoboost(target , c)
                    if c<0:
                        return c
                c = t.BuildUnit(self.input[i][1], self.input[i][0], c, False, i)
                if c<0:
                    return c
            elif self.input[i][1] == "building":
                c = t.BuildUnit(self.input[i][1], self.input[i][0], c, inputno=i)
                if c<0:
                    return c
            elif self.input[i][1] == "gas":
                c = t.EarliestGasTime(c)
                test = t.gatherGas(c)
                if c<0:
                    return c
                if test<0:
                    return test
            elif self.input[i][1] == "mineral":
                test = t.gatherMineral(c)
                if test<0:
                    return test
            elif self.input[i][1] == "scout":
                test = t.gatherScout(c)
                if test<0:
                    return test
        self.queue = t.queue
        self.worker = t.worker
        self.chrono = t.chrono
        self.queue = self.SortQueue(self.queue)
        for i in range(len(self.chrono)):
            for j in range(len(self.chrono[i].time)):
                print("chrono[%d].time[%d]:"%(i,j),self.chrono[i].time[j], \
                    "    target:",self.chrono[i].target[j].name)
        return (self.queue[-1].starttime)

# add a new item in the queue
# and return real actual time it starts to build itself
    def BuildUnit (self, typ, unit, time, flag=False, inputno=-1):
        if time < 0:
            # inappropriate time
            return error.NegativeTime
        condition_time,condition_object = self.ConditionCheck(unit,typ,time)
        if condition_time == -1:
            # condition would never be satisfied
            return error.ConditionNotSatisfied
        elif condition_time < 0:
            # unknown error occured
            return condition_time
        elif condition_time > time:
            time = condition_time

        try:
            mineral = unit_dict[typ][self.race][unit]['mineral']
            gas = unit_dict[typ][self.race][unit]['gas']
            build_time = unit_dict[typ][self.race][unit]['buildtime']
        except:
            return error.WrongUnitName

        res_time = self.ResourceTime(mineral, gas, time)
        if res_time < 0:
            return res_time

        real_time, building = self.BuildableTimeAfter(typ, unit, res_time)
        if real_time < 0:
            return real_time

        if flag == True:
            return real_time

        if self.CheckUnique(typ,unit,real_time):
            return error.UniqueOnly

        build_time = unit_dict[typ][self.race][unit]['buildtime']
        boosted = 0
        if typ != 'building':
            for i in self.chrono:
                for j in range(len(i.time)-1):
                    if i.time[j] > real_time or i.time[j+1] < real_time:
                        break
                    if i.target[j] == building:
                        if i.time[j+1] < real_time + (build_time / 1.15):
                            boosted = 1
                            build_time = (int)((i.time[j+1] - real_time) / 1.15) + (build_time - i.time[j+1] + real_time)
                        else:
                            boosted = 2
                            build_time = (int)(build_time / 1.15)
                if len(i.time)>0 and i.time[-1] <= real_time and i.target[-1] == building:
                    chronoRemaining = (20 - (real_time - i.time[-1])) #only look for chronoboost within the past 20 seconds.
                    if chronoRemaining > 0: 
                        if build_time <= chronoRemaining: #if full build is under chrono
                            boosted = 3
                            build_time = (int)(build_time / 1.50) #probe would go from 12 to 8 seconds
                        else: #build time is larger than chronoboost duration
                            boosted = 1
                            build_time = (int)(build_time - chronoRemaining + (chronoRemaining / 1.50)) #chronoboostRemaining is subtractd from the build and is replaced with chronoRemaining / 1.5

        self.queue.append(Unit(typ,unit, real_time, real_time+build_time))
        self.queue.append(Unit(typ,unit, real_time+build_time, state='end'))
        self.queue[-1].setLinked(self.queue[-2])
        if self.queue[-1].name == "queen":
            self.queue[-1].startingEnergy = 25
        self.queue[-2].setBuildingLink(building)
        self.queue[-2].setInputLink(inputno)
        self.queue[-2].boosted = boosted

        # in case of build a worker, it needs to be added to worker mineral schedule
        count, max_count = self.countMineralWorkers(self.queue[-1].starttime)
        if self.queue[-1].name in ["probe","drone","scv"]:
            if count<max_count:
                self.worker.addSchedule(self.queue[-1].starttime, 1, 0, 0, 0, 0)
            else:
                self.worker.addSchedule(self.queue[-1].starttime, 0, 0, 1, 0, 0)

        # handles morphing/merging units, set the endtime to make them disappear
        # building variable refers to the prerequisite unit(s). This is typically a building but ocassionally a unit IE archon
        if type(building) == Unit and building.type == 'unit':#units that morph from a single unit IE baneling
            building.endtime = real_time
            if building.name == "larva": #if larva is used call addLarva function
                if self.queue[-1].name == "zergling": # spawn extra zergling because 2 zergling are created from 1 larva
                    self.queue.append(Unit('unit',"zergling",real_time + build_time,state='end'))
                larvaResult = self.addLarva(real_time, 1, 11) #add 1 larva with 11 second delay
        elif type(building) == list and self.queue[-1].name == "archon": #units that morph from multiple units IE archon
            for i in building:
                i.endtime = real_time

         #check if building is an addon. Addons don't remove the previous building
        try: 
            buildingAddon = unit_dict[typ][self.race][unit]["addon"]
        except KeyError:
            buildingAddon = "none"

        # if it's an unit or upgrade, push this item into its building's queue
        if type(building) == Unit and typ != 'building': #zerg unit morphing
            building.add(self.queue[-2])
        elif type(building) == list: #archon unit morphing from multiple templars
            for i in building:
                i.add(self.queue[-2])
        elif (typ == "building" and buildingAddon != "none"):
            building.add(self.queue[-2])
        
        #output to engine window
        print("inputno:",inputno," build starttime:",real_time," buildtime:",build_time," build endtime:", real_time + build_time, " unit:",unit," boosted:",boosted)

        
        
        #check if building morphs from another building ie zerg buildings or protoss warp gate
        #buildings that morph are warp gates or lair etc.
        try: 
            buildingMorphed = unit_dict[typ][self.race][unit]["buildfrom"]
        except KeyError:
            buildingMorphed = "none"

        # in case of building a building, subtract a mineral worker for x time depending on race
        # protoss 2 seconds, terran whole build time, zerg loses a worker
        if typ == 'building':
            if self.race == 'protoss':
                self.worker.addSchedule(real_time, -1, 0, 0, 0, 1) #remove worker from minerals to start building
                self.worker.addSchedule(real_time + 2, 1, 0, 0, 0, -1) #add worker to minerals 2 seconds later
            elif self.race == 'terran':
                if buildingMorphed == "none":
                    self.worker.addSchedule(real_time, -1, 0, 0, 0, 1)#remove worker from minerals to start building
                    self.worker.addSchedule(real_time + build_time + 2, 1, 0, 0, 0, -1) #add worker to minerals when building is done building + 2 seconds
            else: #zerg
                if buildingMorphed == "drone":
                    self.worker.addSchedule(real_time, -1, 0, 0, 0, 1)#remove worker from minerals to start building
                    self.worker.addSchedule(real_time + build_time, 0, 0, 0, 0, -1) #remove worker from building stats. do not add back to minerals since drone is gone
                if self.queue[-1].name == "hatchery":
                    larvaResult2 = self.addLarva(real_time + build_time, 3, 0) #add 3 larva when hatchery is done building with 0 delay
            if buildingMorphed != "none": # if this building morphs from a different building.
                if buildingAddon == "none": # if the building is not an addon
                    building.endtime = real_time #Set the endtime of morphing building so it is removed


        # for the case of protoss nexus, you get one more possible chrono schedule
        if self.queue[-1].name == "nexus":
            self.chrono.append(ChronoSchedule())
            self.chrono[-1].addSchedule(self.queue[-1].starttime, self.queue[-1])

        self.queue = self.SortQueue(self.queue)
        return real_time

    def addLarva(self, time, amount, delay):
        hatch = self.buildingCount("hatchery", time, False)
        lair = self.buildingCount("lair", time, True)
        hive = self.buildingCount("hive", time, True)
        count = 0
        for i in range(amount):
            if self.unitCount("larva", time) < (3 * (hatch + lair + hive)): #only add larva if there are less than 3 larva per hatch/lair/hive
                self.queue.append(Unit('unit',"larva",time + delay,state='end'))
                count += 1
        return count
# returns the earliest time in the whole game and corresponding object(s)
# (e.g. ConditionCheck("stalker","unit") will return the completion time of the first cybernetics core)
# if the required condition can never be satisfied, return error.ConditionNotSatisfied
# (e.g. you don't try to construct a cybernetics core in the queue)
    def ConditionCheck(self, unit, typ, time):
        try:
            t = unit_dict[typ][self.race][unit]["required"]
        except KeyError:
            t = "none"
        except:
            # unknown error
            return error.UnknownError, 0

        # case 1 : if no condition is required, return 0
        if t == "none":
            return 0, 0

        # case 2 : if there is only one required condition, return the first time when it satisfies
        if type(t) == type(""):
            for i in self.queue:
                if i.state =="end" and i.name == t and time<i.endtime:
                    return i.starttime, i

        # case 3 : if there are multiple conditions, return when all the conditions are satisfied
        elif type(t) == type([]):
            count = 0
            ans = 0
            ans2 = []
            for j in t:
                for i in self.queue:
                    if i.state == "end" and i.name == j and time<i.endtime:
                        if ans < i.starttime:
                            ans = i.starttime
                        ans2.append(i)
                        count += 1
                        break
            if count == len(t):
                return ans, ans2

        return error.ConditionNotSatisfied, 0

# returns the earliest time after given time, due to waiting queue.
# if there is no waiting queue, return now (given 'time')
# if not availabe for anytime, returns negative integer (supply or building condition may be the problem)
# this function must be called before BeforeUnit returns,
# otherwise some paradox might happen
    def BuildableTimeAfter (self, typ, unit, time):
        if typ == 'unit':
            # check supply first
            try:
                a = unit_dict[typ][self.race][unit]['supply']
            # the given unit doesn't exist
            except:
                return error.WrongUnitName, 0

            required_supply,max_supply = self.CurrentSupply(time)
            required_supply += a
            i = 0
            while required_supply > max_supply and i < len(self.queue):
                if self.queue[i].type == "building" and self.queue[i].state == "end":
                    if self.queue[i].starttime < time:
                        i += 1
                        continue
                    max_supply += unit_dict['building'][self.race][self.queue[i].name]['supplyoffer']
                    time = self.queue[i].starttime
                elif self.queue[i].type == "unit" and self.queue[i].state == "start":
                    if self.queue[i].starttime < time:
                        i += 1
                        continue
                    required_supply += unit_dict['unit'][self.race][self.queue[i].name]['supply']
                    time = self.queue[i].starttime
                i += 1

            # no available time due to supply problem
            if required_supply > max_supply:
                return error.SupplyBlocked, 0
        
        #retrieve build from property
        #all units should have at least one of these
        #only morphed buildings will have this
        try:
            target = unit_dict[typ][self.race][unit]['buildfrom']
        except KeyError:
            target = "none"

        if typ == "building" and target == "none":
            return time,0 #if buildfrom is empty, this is a building that is
                            #built from scratch IE pylon, gateway. A building that morphs like a warp gate or lair will have a build from property

        # for the case of archon that consumes two units
        if type(target) == list:
            building = []
            for t in target:
                for i in self.queue:
                    #if len(building) >= 2: #len(target):
                        #   break
                    if i in building:
                        continue # if i is already in building list skip this iteration
                    if i.state == "end" and i.name == t and i.endtime == maxtime:
                        building.append(i)
            ans = 0
            for i in building:
                if ans<i.starttime:
                    ans = i.starttime
            
            if len(building) < 2 and unit == 'archon': #archon needs 2 units to build from
                return error.NoBarrackExists, 0 
            elif unit == 'archon':
                return ans,building
            else:
                #checks if target building is in build queue
                available = 0
                ans = maxtime
                for i in building:
                    #if i.state == "end" and i.name == target and i.endtime>time:
                    if i.starttime <= time:
                        if len(i.queue) == 0 or i.queue[-1].endtime<=time:
                            return time, i
                        else:
                            if ans > i.queue[-1].endtime:
                                ans = i.queue[-1].endtime
                                building = i
                                available += 1
                    else:
                        if len(i.queue) == 0:
                            if ans > i.starttime:
                                ans = i.starttime
                                building = i
                                available += 1
                        else:
                            if ans > i.queue[-1].endtime:
                                ans = i.queue[-1].endtime
                                building = i
                                available = 1
                return ans,building #other units can be built from any single item in the list.



        available = 0
        building = 0
        ans = maxtime # suppose the game ends before 10000 seconds (2hrs 46mins 40secs)

        #checks if target building is in build queue
        for i in self.queue:
            if i.state == "end" and i.name == target and i.endtime>time:
                if i.starttime <= time:
                    if len(i.queue) == 0 or i.queue[-1].endtime<=time:
                        return time, i
                    else:
                        if ans > i.queue[-1].endtime:
                            ans = i.queue[-1].endtime
                            building = i
                            available += 1
                else:
                    if len(i.queue) == 0:
                        if ans > i.starttime:
                            ans = i.starttime
                            building = i
                            available += 1
                    else:
                        if ans > i.queue[-1].endtime:
                            ans = i.queue[-1].endtime
                            building = i
                            available = 1

        # no available time because no corresponding barrack exists
        if available <= 0 or building.endtime <= ans:
            return error.NoBarrackExists, 0
        return ans, building

# return True if the given upgrade or epic unit is already built
    def CheckUnique(self, typ, unit, time):
        if typ == "upgrade":
            for i in self.queue:
                if i.state == 'end' and i.name == unit and i.starttime<=time:
                    return True
        if unit == "mothership core" or unit == "mothership":
            for i in self.queue:
                if i.state == 'end' and i.name == unit and i.starttime<=time:
                    return True
        return False

# returns current supply and maximum limit
    def CurrentSupply (self, time):
        current_supply = 12
        for i in self.queue:
            if i.type != 'unit' or i.state != "start":
                continue
            if i.starttime <= time:
                current_supply += unit_dict['unit'][self.race][i.name]['supply']

        max_supply = 0
        for i in self.queue:
            if i.type != 'building' or i.state != "end":
                continue
            if i.starttime <= time:
                max_supply += unit_dict['building'][self.race][i.name]['supplyoffer']

        return current_supply, max_supply

# this returns the earliest time from given aftertime, which is the time when minerals and gases are ready.
# if you already have them, returns now - 'aftertime'
# if no available time exists, return error.NoOneGathersGasOrMineral
    def ResourceTime(self, mineral, gas, aftertime):
        # if this func approaches here, worker doesn't exist who gathers minerals or gases
        if aftertime >= 1000: #default value of 10000 was causing integer error
            return error.NoOneGathersGasOrMineral
        a,b = self.AccResources(aftertime)
        if a>=mineral and b>=gas:
            return aftertime
        return self.ResourceTime(mineral, gas, (int)(aftertime+1))
    
# accumulated minerals and gases at given time (seconds)
# this supposes that a worker returns 5 minerals for every 5.4 sec. One worker on one mineral field gathers 55-60 minerals per minute (80-85 for gold minerals), depending on distance.
# and a worker returns 4 gases for every 3.9 sec. One worker on a geyser gathers 61 gas per minute.
    def AccResources(self, time):
        mineral = 50 #starting minerals
        gas = 0 #starting gas
        #tmp = Worker()
        #tmp.time = self.worker.time.copy()

        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            mineral += 5 * self.worker.mineral[i] * (int) ((time - self.worker.time[i]) / 5.4)
            gas += 4 * self.worker.gas[i] * (int) ((time - self.worker.time[i]) / 3.9)

        for i in self.queue:
            if i.starttime > time:
                continue
            if i.state == "end":
                continue
            if i.type == "unit":
                mineral -= unit_dict['unit'][self.race][i.name]['mineral']
                gas -= unit_dict['unit'][self.race][i.name]['gas']
            elif i.type == "building":
                mineral -= unit_dict['building'][self.race][i.name]['mineral']
                gas -= unit_dict['building'][self.race][i.name]['gas']
            elif i.type == "upgrade":
                mineral -= unit_dict['upgrade'][self.race][i.name]['mineral']
                gas -= unit_dict['upgrade'][self.race][i.name]['gas']

        return mineral, gas

# return the number of workers gathering minerals and the maximum
    def countMineralWorkers(self, time):
        count = 0
        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            count += self.worker.mineral[i]

        max_count = 0
        for i in self.queue:
            if i.state == "end" and (i.name in ["nexus","command center","hatchery"]) and i.starttime <= time:
                max_count += 16
        return count, max_count

# return the number of workers gathering gases and the maximum
    def countGasWorkers(self, time):
        count = 0
        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            count += self.worker.gas[i]

        max_count = 0
        for i in self.queue:
            if i.state == "end" and i.name in ["assimilator","refinery","extractor"] and i.starttime <= time:
                max_count += 3
        return count, max_count
# return the number of workers doing nothing workers
    def countDoingNothingWorkers(self, time):
        count = 0
        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            count += self.worker.donothing[i]
        return count
# return the number of workers scouting
    def countScoutingWorkers(self, time):
        count = 0
        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            count += self.worker.scouting[i]
        return count

# return the number of workers building
    def countBuildingWorkers(self, time):
        count = 0
        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            count += self.worker.building[i]
        return count

    def gatherMineral(self, time):
        mineral_count, mineral_max_count = self.countMineralWorkers(time)
        gas_count, gas_max_count = self.countGasWorkers(time)
        idle_count = self.countDoingNothingWorkers(time)

        if mineral_count >= mineral_max_count:
            # you can't allocate more workers on mineral fields
            return error.MineralFieldsAreFull

        if idle_count > 0:
            self.worker.addSchedule(time, 1, 0, -1, 0, 0)
        elif gas_count <= 0:
            return error.NoOneGathersGas
        else:
            self.worker.addSchedule(time, 1, -1, 0, 0, 0)

        return 0

    def gatherGas(self, time):
        mineral_count, mineral_max_count = self.countMineralWorkers(time)
        gas_count, gas_max_count = self.countGasWorkers(time)
        idle_count = self.countDoingNothingWorkers(time)

        if gas_count >= gas_max_count:
            # you can't allocate more workers on gas layers
            return error.GasLayersAreFull


        if idle_count > 0:
            self.worker.addSchedule(time, 0, 1, -1, 0, 0)
        elif mineral_count > 0:
            self.worker.addSchedule(time, -1, 1, 0, 0, 0)
        else:
            # no workers available
            return error.NotEnoughWorkers
        return 0

    def gatherScout(self, time):
        mineral_count, mineral_max_count = self.countMineralWorkers(time)
        
        if mineral_count > 0:
            self.worker.addSchedule(time, -1, 0, 0, 1, 0)
        else:
            # no workers available
            return error.NotEnoughWorkers
        return 0

# returns the time of assimilator completion as fastest as you can use
    def EarliestGasTime(self, time):
        count, max_count = self.countGasWorkers(time)
        if count < max_count:
            return time
        for i in self.queue:
            if i.state == "end" and i.starttime > time and i.name in ["assimilator","refinery","extractor"]:
                return i.starttime
        return error.NoRefineryExists

# returns the number of given units at the given time
    def unitCount(self, unit, time):
        count = 0
        for i in self.queue:
            if i.type != 'unit' or i.state != 'end':
                continue
            if i.name == unit and i.starttime <= time < i.endtime:
                count += 1
        return count

# returns the number of given buildings at the given time
    def buildingCount(self, building, time, morphing):
        count = 0
        for i in self.queue:
            if i.type != 'building' or i.state != 'end':
                continue
            if i.name == building:
               if i.starttime <= time < i.endtime:
                    count +=1
               elif morphing == True and i.starttime > time and i.name in ["lair","hive"]:
                   # if morphing is true and the starttime is in the future
                   # and the name is lair or hive. count this so larva will still be produced
                   count += 1
            
        return count

# returns the earliest time to use targetEnergy
    def earliestEnergyUse(self, unit, targetEnergy):
        usedEnergy = len(unit.usedEnergy) * targetEnergy

        # if never used energy return the units endtime
        if usedEnergy == 0:
            return unit.endtime
        
        generatedEnergy = (unit.usedEnergy[-1] - unit.endtime) * 0.5625
        if generatedEnergy + unit.startingEnergy - usedEnergy >= 200:
            generatedEnergy = 200 #maximum energy
        else:
            generatedEnergy = generatedEnergy + unit.startingEnergy

        latestEnergyValue = generatedEnergy - usedEnergy
        # if most recent energy used time still has enough energy, return last used energy time
        if latestEnergyValue >= targetEnergy:
            return unit.usedEnergy[-1]
        else: # find time where there is enough energy
            energyDeficit = targetEnergy - latestEnergyValue
            futureTime = (energyDeficit / 0.5625) + unit.usedEnergy[-1]
            return futureTime


# add chronoboost schedule
# if all nexuses are in their cooldown, return error.ChronoCooldown
# if all available target objects are already boosted, return error.AlreadyBoosted
    def Chronoboost(self, target, time):
        available_target_list = ['nexus', 'gateway', 'warp gate', 'forge',
            'cybernetics core', 'twilight council', 'templar archives', 'dark shrine',
            'stargate', 'fleet beacon', 'robotics facility', 'robotics bay']
        if target not in available_target_list:
            return error.UnboostableBuilding

        # try to find a target object from the queue
        target_object = 0
        for i in self.queue:
            if i.name == target and i.state == 'end' and i.starttime <= time <= i.endtime:
                test = False
                for j in self.chrono:
                    test = j.checkTargetIsBoosted(i, time)
                    if test == True:
                        break
                if test == False:
                    target_object = i

        if target_object == 0:
            return error.AlreadyBoosted

        test = error.ChronoNotAvailable
        for i in self.chrono:
            test = i.addSchedule(time, target_object)
            if test == 0:
                chrono_schedule = i
                break

        if test == error.ChronoNotAvailable or test == error.ChronoCooldown:
            return test

        # try to modify unit/upgrade build time due to changed chronoboosting schedule
        # (for the case of changing boosting duration)
        
        #doesn't seem to be in use for unit chronoboosting
        for i in self.queue:
            if i.state == "start" and i.endtime > time and i.starttime<time:
                link = i.linked
                if link == 0:
                    continue
                if i.type == "unit":
                    build_time = unit_dict['unit'][self.race][i.name]['buildtime']
                elif i.type == "upgrade":
                    build_time = unit_dict['upgrade'][self.race][i.name]['buildtime']
                else:
                    continue
                building = i.buildlinked

                for j in range(len(chrono_schedule.time)-1):
                    if chrono_schedule.time[j] > i.starttime or chrono_schedule.time[j+1] < i.starttime:
                        break
                    if chrono_schedule.target[j] == building:
                        if chrono_schedule.time[j+1] < i.starttime + (build_time / 1.15):
                            i.boosted = 1
                            build_time = (int)((chrono_schedule.time[j+1] - i.starttime) / 1.15) \
                                + (build_time - chrono_schedule.time[j+1] + i.starttime)
                            print("no:",i.inputlink,"time:",i.starttime,i.name,":",build_time)
                i.endtime = i.starttime + build_time
                link.starttime = i.endtime

        return test
