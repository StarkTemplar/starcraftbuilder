from unit import *
from unitclass import *
import error

startingSupply = 0
lairBuildTime = ""
hiveBuildTime = ""
larvaGenerationTime = 0
injectionSpawnTime = 0
queenStartingEnergy = 0
muleLifespan = 0
orbitalStartingEnergy = 0
nexusStartingEnergy = 0
chronoBoostDuration = 0
energyRegenRate = 0.0
fullySaturatedBase = 0

class Engine():
    def __init__(self, race):
        self.race = race
        self.input = []
        self.queue = []
        self.chrono = []
        self.worker = Worker()

        #reference global variables
        global startingSupply
        global lairBuildTime
        global hiveBuildTime
        global larvaGenerationTime
        global injectionSpawnTime
        global queenStartingEnergy
        global muleLifespan
        global orbitalStartingEnergy
        global nexusStartingEnergy
        global chronoBoostDuration
        global energyRegenRate
        global fullySaturatedBase

        # game starts
        if race == 'protoss':
            n = 'nexus'
            w = 'probe'
            startingSupply = 12
            nexusStartingEnergy = unit_dict['building'][race]['nexus']["startingEnergy"]
            chronoBoostDuration = 20
        elif race == 'terran':
            n = 'command center'
            w = 'scv'
            startingSupply = 12
            muleLifespan = 90
            orbitalStartingEnergy = unit_dict['building'][race]['orbital command']["startingEnergy"]
        elif race == 'zerg':
            n = 'hatchery'
            w = 'drone'
            startingSupply = 12
            lairBuildTime = unit_dict['building'][race]['lair']["buildtime"]
            hiveBuildTime = unit_dict['building'][race]['hive']["buildtime"]
            larvaGenerationTime = 11
            injectionSpawnTime = 40
            queenStartingEnergy = unit_dict['unit'][race]['queen']["startingEnergy"]
        elif race == 'protossBW':
            n = 'nexus'
            w = 'probe'
            startingSupply = 4
        elif race == 'terranBW':
            n = 'command center'
            w = 'scv'
            startingSupply = 4
        elif race == 'zergBW':
            n = 'hatchery'
            w = 'drone'
            startingSupply = 4
            lairBuildTime = unit_dict['building'][race]['lair']["buildtime"]
            hiveBuildTime = unit_dict['building'][race]['hive']["buildtime"]
            larvaGenerationTime = 11
        else:
            print("Wrong race : %s"%race)
            raise

        #creating starting base
        self.queue.append(Unit('building', n,0,state='end'))
        #create starting X workers
        for i in range(startingSupply):
            self.queue.append(Unit('unit',w,0,state='end'))
        
        #add energy to nexus. SC2 only
        if race == 'protoss':
            self.queue[0].startingEnergy = nexusStartingEnergy            

        #generate larva and overlord for zerg and zergBW
        if race in ["zerg","zergBW"]:
            self.queue.append(Unit('building',"overlord",0,state='end'))
            for i in range(3):
                self.queue.append(Unit('unit',"larva",0,state='end'))
        
        # Starcraft2
        if race in ["protoss","terran","zerg"]:
            self.worker.addSchedule(0,8,0,0,0,0) #8 workers get to a mineral patch immediatly
            self.worker.addSchedule(3.825,4,0,0,0,0) #4 workers have to wait 3.825 seconds to start mining
            energyRegenRate = 0.7875
            fullySaturatedBase = 24

        # Starcraft BW
        if race in ["protossBW","terranBW","zergBW"]:
            self.worker.addSchedule(0,4,0,0,0,0) #4 workers get to a mineral patch immediatly            
            energyRegenRate = 0.744
            fullySaturatedBase = 27

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

# add unit, building, upgrade to input queue
    def AddItem(self, name, typ):
        self.input.append( (name,typ) )

# remove item from input queue
    def DeleteItem(self, no):
        if no<-1 or no>=len(self.input):
            return error.WrongIndex, 0
        elif no == -1:
            self.input.pop()
        else:
            self.input.pop(no)
        return self.Rearrange()

#process input queue
    def Rearrange (self):
        t = Engine(self.race)
        c = 0
        print("\n*** New Simulation ***")
        for i in range(len(self.input)):
            if self.input[i][1] == 'unit' or self.input[i][1] == 'upgrade':
                if i>0 and self.input[i-1][0] == "chronoboost":
                    c, missingpreReq = t.BuildUnit(self.input[i][1], self.input[i][0], c, True, True)
                    if c<0:
                        return c, missingpreReq
                else:
                    c, missingpreReq = t.BuildUnit(self.input[i][1], self.input[i][0], c, False, False, i)
                    if c<0:
                        return c, missingpreReq
            elif self.input[i][1] == "building":
                c, missingpreReq = t.BuildUnit(self.input[i][1], self.input[i][0], c, False, inputno=i)
                if c<0:
                    return c, missingpreReq
            elif self.input[i][1] == "gas":
                c = t.EarliestGasTime(c)
                test = t.gatherGas(c)
                if c<0:
                    return c, 0
                if test<0:
                    return test, 0
            elif self.input[i][1] == "mineral":
                test = t.gatherMineral(c)
                if test<0:
                    return test, 0
            elif self.input[i][1] == "scout":
                test = t.gatherScout(c)
                if test<0:
                    return test, 0
            elif self.input[i][0] == "spawnlarva":
                test = t.spawnLarva(c)
                if test<0:
                    return test, 0
            elif self.input[i][0] == "mule":
                test = t.callMule(c)
                if test<0:
                    return test, 0
        self.queue = t.queue
        self.worker = t.worker
        self.chrono = t.chrono
        self.queue = self.SortQueue(self.queue)
        return self.queue[-1].starttime, 0

# add a new item in the queue
# and return real actual time it starts to build itself
    def BuildUnit (self, typ, unit, time, chrono, flag=False, inputno=-1):
        if time < 0:
            # inappropriate time
            return error.NegativeTime, 0
        condition_time,condition_object = self.ConditionCheck(unit,typ,time)
        if condition_time == -1:
            # condition would never be satisfied
            return error.ConditionNotSatisfied, condition_object
        elif condition_time < 0:
            # unknown error occured
            return condition_time, condition_object
        elif condition_time > time:
            time = condition_time

        try:
            mineral = unit_dict[typ][self.race][unit]['mineral']
            gas = unit_dict[typ][self.race][unit]['gas']
            build_time = unit_dict[typ][self.race][unit]['buildtime']
        except:
            return error.WrongUnitName, 0

        res_time = self.ResourceTime(mineral, gas, time)
        if res_time < 0:
            return res_time, 0

        real_time, building = self.BuildableTimeAfter(typ, unit, res_time)
        if real_time < 0:
            return real_time, building

        #if flag == True:
         #   return real_time, building

        if self.CheckUnique(typ,unit,real_time): #check for unique units like a mothership
            return error.UniqueOnly, 0

        build_time = unit_dict[typ][self.race][unit]['buildtime']
        boosted = 0

        if chrono == True:
            if typ in ['unit','upgrade']:
                build_time, boosted = self.callChronoboost(building, real_time, build_time)
                if build_time < 0:
                    return error.NotEnoughNexusEnergy, 0
            else:
                return error.InvalidChronoboost
        elif self.race == "protoss" and typ in ['unit','upgrade']:
            build_time, boosted = self.chronoBuildtime(building, real_time, build_time)
            
        self.queue.append(Unit(typ,unit, real_time, real_time+build_time))
        self.queue.append(Unit(typ,unit, real_time+build_time, state='end'))
        self.queue[-1].setLinked(self.queue[-2])
        if self.queue[-1].name == "queen":
            self.queue[-1].startingEnergy = queenStartingEnergy
        if self.queue[-1].name == "orbital command":
            self.queue[-1].startingEnergy = orbitalStartingEnergy
        if self.queue[-1].name == "nexus":
            self.queue[-1].startingEnergy = nexusStartingEnergy
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
                elif self.queue[-1].name == "scourge": # spawn extra scourge because 2 scourge are created from 1 larva
                    self.queue.append(Unit('unit',"scourge",real_time + build_time,state='end'))
                larvaResult = self.addLarva(real_time, 1, larvaGenerationTime, False) #add 1 larva with 11 second delay
        elif type(building) == list and self.queue[-1].name in ['archon','dark archon']: #units that morph from multiple units IE archon
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
            building.add(self.queue[-2]) #add item to building queue
            if self.queue[-1].name in ["orbital command","planetary fortress"]:
                building.endtime = real_time + build_time - 1 #set end time for morphing command center
            if "with tech lab" in self.queue[-1].name:
                building.endtime = real_time + build_time - 1 #set end time for morphing building
                if "barracks" in self.queue[-1].name:
                    self.queue.append(Unit('building',"barracks tech lab",real_time + build_time,state='end'))
                elif "factory" in self.queue[-1].name:
                    self.queue.append(Unit('building',"factory tech lab",real_time + build_time,state='end'))
                elif "starport" in self.queue[-1].name:
                    self.queue.append(Unit('building',"starport tech lab",real_time + build_time,state='end'))
            elif "factory with machine shop" in self.queue[-1].name:
                building.endtime = real_time + build_time - 1 #set end time for morphing building
                self.queue.append(Unit('building',"factory machine shop",real_time + build_time,state='end'))
            elif "starport with control tower" in self.queue[-1].name:
                building.endtime = real_time + build_time - 1 #set end time for morphing building
                self.queue.append(Unit('building',"starport control tower",real_time + build_time,state='end'))
            elif "cc with comsat station" in self.queue[-1].name:
                building.endtime = real_time + build_time - 1 #set end time for morphing building
                self.queue.append(Unit('building',"cc comsat station",real_time + build_time,state='end'))
            elif "cc with nuclear silo" in self.queue[-1].name:
                building.endtime = real_time + build_time - 1 #set end time for morphing building
                self.queue.append(Unit('building',"cc nuclear silo",real_time + build_time,state='end'))
            
        
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
            if self.race in ['protoss','protossBW']:
                self.worker.addSchedule(real_time, -1, 0, 0, 0, 1) #remove worker from minerals to start building
                self.worker.addSchedule(real_time + 2, 1, 0, 0, 0, -1) #add worker to minerals 2 seconds later
            elif self.race in ['terran','terranBW']:
                if buildingMorphed == "none":
                    self.worker.addSchedule(real_time, -1, 0, 0, 0, 1)#remove worker from minerals to start building
                    self.worker.addSchedule(real_time + build_time + 2, 1, 0, 0, 0, -1) #add worker to minerals when building is done building + 2 seconds
            else: #zerg or zergBW
                if buildingMorphed == "drone":
                    self.worker.addSchedule(real_time, -1, 0, 0, 0, 1)#remove worker from minerals to start building
                    self.worker.addSchedule(real_time + build_time, 0, 0, 0, 0, -1) #remove worker from building stats. do not add back to minerals since drone is gone
                if self.queue[-1].name == "hatchery":
                    larvaResult2 = self.addLarva(real_time + build_time, 3, 0, False) #add 3 larva when hatchery is done building with 0 delay
                if self.queue[-1].name in ["lair","hive"]: #copy over a buildings secondary and tertiary queue. used by lair and hive for larva injection and larva generation
                    self.queue[-1].secondaryQueue = building.secondaryQueue 
                    building.secondaryQueue = []
                    self.queue[-1].tertiaryQueue = building.tertiaryQueue 
                    building.tertiaryQueue = []
            if buildingMorphed != "none": # if this building morphs from a different building.
                if buildingAddon == "none": # if the building is not an addon
                    building.endtime = real_time #Set the endtime of morphing building so it is removed

        self.queue = self.SortQueue(self.queue)
        return real_time, 0

#addLarva function. Takes into account morphing lair or hive
#use tertiaryQueue array to schedule larva generation as quickly as possible
    def addLarva(self, time, amount, delay, injection):
        zergBases = []
        larvaGenerated = 0
        tempBase = maxtime
        ans = maxtime
        earliestBase = Unit

        # find all zerg bases
        for i in self.queue:
           if i.name in ["hatchery","lair","hive"]:
               if i.state != "end":
                   continue
               if i.starttime <= time < i.endtime:
                    zergBases.append(i)
               elif i.starttime - lairBuildTime <= time < i.endtime and i.name in ["lair"]:
                   # if starttime minus build time
                   # and name is lair or hive. count this so larva will still be produced
                   zergBases.append(i)
               elif i.starttime - hiveBuildTime <= time < i.endtime and i.name in ["hive"]:
                   # if starttime minus build time
                   # and name is lair or hive. count this so larva will still be produced
                   zergBases.append(i)
        
        totalBasesCount = len(zergBases)
        larvaCount = self.unitCount("larva", time)
        larvaQueue = 0

        if injection == False and delay > 0: #only try to generate larva if there are less than 3 larva per hatch/lair/hive
            #find zergBase that can generate larva the soonest
            for i in zergBases:
                for j in i.secondaryQueue: #find all larva injections already in base's queue
                    if j.endtime <= time + larvaGenerationTime:
                        larvaQueue += 3
                for j in i.tertiaryQueue: #find all larva already in base's queue
                    if j.endtime > time:
                        larvaQueue += 1
                if larvaQueue + larvaCount < 3: # only add larva if queued larva and larva count is less than 3
                    if i.starttime <= time:
                        if len(i.tertiaryQueue) == 0 or i.tertiaryQueue[-1].endtime<=time:
                            ans = time
                        else:
                            #if ans > i.queue[-1].endtime:
                            ans = i.tertiaryQueue[-1].endtime
                    else:
                        if len(i.tertiaryQueue) == 0:
                            #if ans > i.starttime:
                            ans = i.starttime
                        else:
                            #if ans > i.queue[-1].endtime:
                                ans = i.tertiaryQueue[-1].endtime
                    if ans < tempBase:
                        tempBase = ans
                        earliestBase = i
            
            if ans < maxtime:
                #add larva in tertiary queue of base
                earliestBase.tertiaryQueue.append(Unit('unit','larva', tempBase, tempBase + delay))

                #add larva to overall queue
                self.queue.append(Unit('unit',"larva",tempBase + delay,state='end'))
                larvaGenerated += 1
        elif delay == 0 and amount == 3: #creating 3 larva when hatchery is done building
            for i in range(amount):
                self.queue.append(Unit('unit',"larva",time,state='end'))
                larvaGenerated += 1
        elif injection == True: #if this is from queen larva injection
            for i in zergBases:
                for j in i.secondaryQueue: #find all larva injections already in base's queue
                    if j.starttime < time < j.endtime:
                        larvaQueue += 3
            for i in range(amount):
                if ((larvaCount + larvaQueue + larvaGenerated) < (19 * totalBasesCount)): #each injected base can only support 19 larva
                    self.queue.append(Unit('unit',"larva",time + delay,state='end'))
                    larvaGenerated += 1

        return larvaGenerated

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
            if typ in ["unit","upgrade"]:
                count = 0
                ans = 0
                ans2 = []
                for j in t:
                    for i in self.queue:
                        if i.state == "end" and i.name == j and time<i.endtime:
                            if ans < i.starttime: #find highest time to meet all requirements
                                ans = i.starttime
                            ans2.append(i)
                            count += 1
                            break
                if count == len(t): #must meet all requirements
                    return ans, ans2
            else: #buildings can satisfy any of the requirements instead of all
                count = 0
                ans = maxtime
                ans2 = []
                for j in t:
                    for i in self.queue:
                        if i.state == "end" and i.name == j and time<i.endtime:
                            if ans > i.starttime: #find lowest time
                                ans = i.starttime
                            ans2.append(i)
                            count += 1
                            break
                if count > 0: #can meet any requirement for buildings
                    return ans, ans2

        return error.ConditionNotSatisfied, t

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
        
        #retrieve buildFrom property
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
            
            # if building is empty, there are no available units or buildings to morph/build unit
            if len(building) == 0:
                return error.NoBarrackExists, target
            #find the highest startTime in building array
            ans = 0
            for i in building:
                if ans<i.starttime:
                    ans = i.starttime
            
            if len(building) < 2 and unit in ['archon','dark archon']: #archon needs 2 units to build from
                return error.NoBarrackExists, 0 #not enough templars to build archon
            elif unit in ['archon','dark archon']:
                return ans,building #enough templars to build archon
            else:
                #for all other units that only need 1 item from their list of many IE queen can be built from hatchery, lair, or hive
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
                return ans,building #other units can be built from any single item in the list


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

        # no available time because no corresponding building in buildFrom property exists
        if available <= 0 or building.endtime <= ans:
            return error.NoBarrackExists, target
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
        current_supply = startingSupply
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

        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            #normal mineral workers
            mineral += int(5 * self.worker.mineral[i] * ((time - self.worker.time[i]) / 5.4))
            #MULE on minerals
            mineral += int(25 * self.worker.mule[i] * ((time - self.worker.time[i]) / 6.9))
            gas += int(4 * self.worker.gas[i] * ((time - self.worker.time[i]) / 3.9))

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
            if i.state == "end" and (i.name in ["nexus","command center","orbital command","planetary fortress","hatchery"]) and i.starttime <= time <= i.endtime:
                max_count += fullySaturatedBase
            elif i.state == "end" and (i.name in ["lair"]) and (i.starttime - lairBuildTime) <= time <= i.endtime:
                max_count += fullySaturatedBase
            elif i.state == "end" and (i.name in ["hive"]) and (i.starttime - hiveBuildTime) <= time <= i.endtime:
                max_count += fullySaturatedBase
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

# return the number of Mules
    def countMules(self, time):
        count = 0
        for i in range(len(self.worker.time)):
            if self.worker.time[i] > time:
                continue
            count += self.worker.mule[i]
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
            return unit.starttime
        
        generatedEnergy = (unit.usedEnergy[-1] - unit.starttime) * energyRegenRate
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
            futureTime = (energyDeficit / energyRegenRate) + unit.usedEnergy[-1]
            return (int(futureTime + 1))

#returns earliest time spawn larva function can be used
    def spawnLarva(self, time):
        
        #find all queens
        earliestQueenEnergy = maxtime
        tempEnergy = maxtime
        earliestQueen = Unit
        for i in self.queue:
            if i.name == 'queen' and i.state == 'end':
                tempEnergy = self.earliestEnergyUse(i,queenStartingEnergy)
                if tempEnergy < earliestQueenEnergy:
                    earliestQueen = i
                    earliestQueenEnergy = tempEnergy
        
        if earliestQueenEnergy == 10000:
            return error.NoQueens
        else:
            #find all hatcheries, lairs, and hives
            earliestBase = Unit
            zergBases = []
            tempBase = maxtime
            ans = maxtime
            for i in self.queue:
                if i.name in ["hatchery"] and i.state == 'end':
                    if i.starttime <= earliestQueenEnergy < i.endtime:
                        zergBases.append(i)
                elif i.name in ["lair"] and i.state == 'end':
                    if i.starttime - lairBuildTime <= earliestQueenEnergy < i.endtime:
                        zergBases.append(i)
                elif i.name in ["hive"] and i.state == 'end':
                    if i.starttime - hiveBuildTime <= earliestQueenEnergy < i.endtime:
                        zergBases.append(i)

            for i in zergBases:
                if (i.starttime <= earliestQueenEnergy) or (i.name == "lair" and ((i.starttime - lairBuildTime) <= earliestQueenEnergy)) \
                or (i.name == "hive" and ((i.starttime - hiveBuildTime) <= earliestQueenEnergy)):
                    if len(i.secondaryQueue) == 0 or i.secondaryQueue[-1].endtime<=earliestQueenEnergy:
                        ans = earliestQueenEnergy
                    else:
                        #if ans > i.queue[-1].endtime:
                        ans = i.secondaryQueue[-1].endtime
                else:
                    if len(i.secondaryQueue) == 0:
                        #if ans > i.starttime:
                        ans = i.starttime
                    else:
                        #if ans > i.queue[-1].endtime:
                         ans = i.secondaryQueue[-1].endtime
                if ans < tempBase:
                    tempBase = ans
                    earliestBase = i

            #put in injection in secondary queue of hatchery
            earliestBase.secondaryQueue.append(Unit('skill','injection', tempBase, tempBase+injectionSpawnTime))

            #create 3 larva 40 seconds from now
            self.addLarva(tempBase, 3, injectionSpawnTime, True) #add 3 larva with 40 second delay

            #queen objects seemed to be linked based on energyuse
            #earliestQueen
            earliestQueen.useEnergy(tempBase)
        return tempBase

#returns earliest time a mule can be called down
    def callMule(self, time):
        
        #find all Orbital Commands
        earliestOrbitalEnergy = maxtime
        tempEnergy = maxtime
        earliestOrbital = Unit
        for i in self.queue:
            if i.name == 'orbital command' and i.state == 'end':
                tempEnergy = self.earliestEnergyUse(i,50)
                if tempEnergy < earliestOrbitalEnergy:
                    earliestOrbital = i
                    earliestOrbitalEnergy = tempEnergy
        
        if earliestOrbitalEnergy == 10000:
            return error.NoOrbitalCommands
        else:
            # use energy on orbital command
            earliestOrbital.useEnergy(earliestOrbitalEnergy)

            #put in injection in secondary queue of hatchery
            earliestOrbital.secondaryQueue.append(Unit('skill','mule', earliestOrbitalEnergy, earliestOrbitalEnergy+muleLifespan))


            #schedule MULE addition in worker object
            self.worker.muleSchedule(earliestOrbitalEnergy,1)
            #schedule MULE to disappear 64 seconds later
            self.worker.muleSchedule(earliestOrbitalEnergy + muleLifespan,-1)

        return earliestOrbitalEnergy

#returns earliest time a chronoboost can be used to build target unit
    def callChronoboost(self, target, targetTime, build_time):
        #verify target building is chronoboostable
        available_target_list = ['nexus', 'gateway', 'warp gate', 'forge',
            'cybernetics core', 'twilight council', 'templar archives', 'dark shrine',
            'stargate', 'fleet beacon', 'robotics facility', 'robotics bay']
        if target.name not in available_target_list:
            return error.UnboostableBuilding, 0

        #find all Nexuses
        earliestNexusEnergy = maxtime
        tempEnergy = maxtime
        earliestNexus = Unit
        for i in self.queue:
            if i.name == 'nexus' and i.state == 'end':
                tempEnergy = self.earliestEnergyUse(i,50)
                if tempEnergy < earliestNexusEnergy:
                    earliestNexus = i
                    earliestNexusEnergy = tempEnergy
        
        #reset earliestNexusEnergy to target build time
        if earliestNexusEnergy < targetTime:
            earliestNexusEnergy = targetTime

        if earliestNexusEnergy == 10000:
            return error.NotEnoughNexusEnergy, 0
        elif earliestNexusEnergy >= (targetTime + build_time):
            return error.NotEnoughNexusEnergy, 0
        else:
            #find all target buildings
            earliestTarget = Unit
            chronoStart = maxtime
            ans = maxtime
            
            #for i in allTargets:
            if (target.starttime <= earliestNexusEnergy):
                if len(target.secondaryQueue) == 0 or target.secondaryQueue[-1].endtime<=earliestNexusEnergy:
                    ans = earliestNexusEnergy
                else:
                    #if ans > target.queue[-1].endtime:
                    ans = target.secondaryQueue[-1].endtime
            else:
                if len(target.secondaryQueue) == 0:
                    #if ans > target.starttime:
                    ans = target.starttime
                else:
                    #if ans > target.queue[-1].endtime:
                        ans = target.secondaryQueue[-1].endtime
           
            chronoStart = ans

            #check if this chrono can affect this build
            if targetTime + build_time <= chronoStart:
                error.NotEnoughNexusEnergy, 0

            #put in chronoboost in secondary queue of target
            target.secondaryQueue.append(Unit('skill','chronoboost', chronoStart, chronoStart+chronoBoostDuration))
            # use energy on nexus
            earliestNexus.useEnergy(earliestNexusEnergy)
            
            #call chronoBuildTime function to calculate new build time
            build_time, boosted = self.chronoBuildtime(target, targetTime, build_time)

        return build_time, boosted

#calculate new build time from chronoboost
    def chronoBuildtime(self, target, targetTime, build_time):
        boostedSeconds = 0
        for i in target.secondaryQueue:
            chronoStart = i.starttime
            chronoEnd = i.endtime
            if chronoEnd <= targetTime or chronoStart >= (targetTime + build_time):
                continue
            elif chronoStart <= targetTime and (targetTime + build_time) <= chronoEnd:
                boostedSeconds += (chronoEnd - chronoStart) - (targetTime - chronoStart) - (chronoEnd - (targetTime + build_time))
            elif chronoStart > targetTime and targetTime + build_time > chronoEnd:
                boostedSeconds += (chronoEnd - chronoStart)
            elif chronoStart > targetTime and (targetTime + build_time) > chronoStart and (targetTime + build_time) < chronoEnd:
                boostedSeconds += (chronoEnd - chronoStart) - (chronoEnd - (targetTime + build_time))
            elif targetTime > chronoStart and targetTime + build_time > chronoEnd:
                boostedSeconds += (chronoEnd - chronoStart) - (targetTime - chronoStart)
            else:
                boostedSeconds += (chronoEnd - chronoStart)
        
        if boostedSeconds == 0: #no chronoboost applied
            return build_time, 0
        elif boostedSeconds >= build_time: #whole build time is under chronoboost
            build_time = (int)(build_time / 1.50) #probe would go from 12 to 8 seconds
            boosted = 3
        else: #partial chronoboost
            boosted = 1
            build_time = (int)(build_time - boostedSeconds + (boostedSeconds / 1.50)) #boostedSeconds is subtractd from the build and is replaced with boostedSeconds / 1.5

        return build_time, boosted

