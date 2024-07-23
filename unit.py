unit_dict = {
"unit":{
    "protoss":{
        "probe":{
            "no":0,
            "race":"protoss",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":12,
            "buildfrom":"nexus"
        },
        "zealot":{
            "no":1,
            "race":"protoss",
            "mineral":100,
            "gas":0,
            "supply":2,
            "buildtime":27,
            "buildfrom":"gateway"
        },
        "stalker":{
            "no":2,
            "race":"protoss",
            "mineral":125,
            "gas":50,
            "supply":2,
            "buildtime":30,
            "buildfrom":"gateway",
            "required":"cybernetics core"
        },
        "sentry":{
            "no":3,
            "race":"protoss",
            "mineral":50,
            "gas":100,
            "supply":2,
            "buildtime":26,
            "buildfrom":"gateway",
            "required":"cybernetics core"
        },
        "adept":{
            "no":4,
            "race":"protoss",
            "mineral":100,
            "gas":25,
            "supply":2,
            "buildtime":30,
            "buildfrom":"gateway",
            "required":"cybernetics core"
        },
        "high templar":{
            "no":5,
            "race":"protoss",
            "mineral":50,
            "gas":150,
            "supply":2,
            "buildtime":39,
            "buildfrom":"gateway",
            "required":"templar archives"
        },
        "dark templar":{
            "no":6,
            "race":"protoss",
            "mineral":125,
            "gas":125,
            "supply":2,
            "buildtime":39,
            "buildfrom":"gateway",
            "required":"dark shrine"
        },
        "observer":{
            "no":7,
            "race":"protoss",
            "mineral":25,
            "gas":75,
            "supply":1,
            "buildtime":18,
            "buildfrom":"robotics facility"
        },
        "immortal":{
            "no":8,
            "race":"protoss",
            "mineral":275,
            "gas":100,
            "supply":4,
            "buildtime":39,
            "buildfrom":"robotics facility"
        },
        "warp prism":{
            "no":9,
            "race":"protoss",
            "mineral":250,
            "gas":0,
            "supply":2,
            "buildtime":36,
            "buildfrom":"robotics facility"
        },
        "colossus":{
            "no":10,
            "race":"protoss",
            "mineral":300,
            "gas":200,
            "supply":6,
            "buildtime":54,
            "buildfrom":"robotics facility",
            "required":"robotics bay"
        },
        "disruptor":{
            "no":11,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "supply":4,
            "buildtime":36,
            "buildfrom":"robotics facility",
            "required":"robotics bay"
        },
        "phoenix":{
            "no":12,
            "race":"protoss",
            "mineral":150,
            "gas":100,
            "supply":2,
            "buildtime":25,
            "buildfrom":"stargate"
        },
        "void ray":{
            "no":13,
            "race":"protoss",
            "mineral":250,
            "gas":150,
            "supply":4,
            "buildtime":43,
            "buildfrom":"stargate"
        },
        "carrier":{
            "no":14,
            "race":"protoss",
            "mineral":350,
            "gas":250,
            "supply":6,
            "buildtime":64,
            "buildfrom":"stargate",
            "required":"fleet beacon"
        },
        "mothership":{
            "no":15,
            "race":"protoss",
            "mineral":300,
            "gas":300,
            "supply":6,
            "buildtime":79,
            "buildfrom":"nexus",
            "required":"fleet beacon"
        },
        "oracle":{
            "no":16,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "supply":3,
            "buildtime":37,
            "buildfrom":"stargate"
        },
        "tempest":{
            "no":17,
            "race":"protoss",
            "mineral":250,
            "gas":175,
            "supply":5,
            "buildtime":43,
            "buildfrom":"stargate",
            "required":"fleet beacon"
        },
        "archon":{
            "no":18,
            "race":"protoss",
            "mineral":0,
            "gas":0,
            "supply":4,
            "buildtime":9,
            "buildfrom":["high templar","high templar","warp high templar","warp high templar","warp dark templar","warp dark templar"]
        },
        
        "warp zealot":{
            "no":19,
            "race":"protoss",
            "mineral":100,
            "gas":0,
            "supply":2,
            "buildtime":20,
            "buildfrom":"warp gate"
        },
        "warp stalker":{
            "no":20,
            "race":"protoss",
            "mineral":125,
            "gas":50,
            "supply":2,
            "buildtime":23,
            "buildfrom":"warp gate",
            "required":"cybernetics core"
        },
        "warp sentry":{
            "no":21,
            "race":"protoss",
            "mineral":50,
            "gas":100,
            "supply":2,
            "buildtime":23,
            "buildfrom":"warp gate",
            "required":"cybernetics core"
        },
        "warp adept":{
            "no":22,
            "race":"protoss",
            "mineral":100,
            "gas":25,
            "supply":2,
            "buildtime":20,
            "buildfrom":"warp gate",
            "required":"cybernetics core"
        },
        "warp high templar":{
            "no":23,
            "race":"protoss",
            "mineral":50,
            "gas":150,
            "supply":2,
            "buildtime":32,
            "buildfrom":"warp gate",
            "required":"templar archives"
        },
        "warp dark templar":{
            "no":24,
            "race":"protoss",
            "mineral":125,
            "gas":125,
            "supply":2,
            "buildtime":32,
            "buildfrom":"warp gate",
            "required":"dark shrine"
        }
    },
    "terran":{
        "scv":{
            "no":0,
            "race":"terran",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":12,
            "buildfrom":["command center","orbital command","planetary fortress"]
        },
        "marine":{
            "no":1,
            "race":"terran",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":18,
            "buildfrom":["barracks","barracks reactor","barracks with tech lab"]
        },
        "marauder":{
            "no":2,
            "race":"terran",
            "mineral":100,
            "gas":25,
            "supply":2,
            "buildtime":21,
            "buildfrom":"barracks with tech lab",
            "required":"barracks tech lab"
        },
        "reaper":{
            "no":3,
            "race":"terran",
            "mineral":50,
            "gas":50,
            "supply":1,
            "buildtime":32,
            "buildfrom":["barracks","barracks reactor","barracks with tech lab"]
        },
        "ghost":{
            "no":4,
            "race":"terran",
            "mineral":150,
            "gas":125,
            "supply":2,
            "buildtime":29,
            "buildfrom":"barracks with tech lab",
            "required":"ghost academy"
        },
        "hellion":{
            "no":5,
            "race":"terran",
            "mineral":100,
            "gas":0,
            "supply":2,
            "buildtime":21,
            "buildfrom":["factory","factory reactor","factory with tech lab"]
        },
        "hellbat":{
            "no":6,
            "race":"terran",
            "mineral":100,
            "gas":0,
            "supply":2,
            "buildtime":21,
            "buildfrom":["factory","factory reactor", "factory with tech lab"],
            "required":"armory"
        },
        "siege tank":{
            "no":7,
            "race":"terran",
            "mineral":150,
            "gas":125,
            "supply":3,
            "buildtime":32,
            "buildfrom":"factory with tech lab",
            "required":"factory tech lab"
        },
        "cyclone":{
            "no":8,
            "race":"terran",
            "mineral":125,
            "gas":50,
            "supply":2,
            "buildtime":32,
            "buildfrom":["factory","factory reactor","factory with tech lab"]
        },
        "widow mine":{
            "no":9,
            "race":"terran",
            "mineral":75,
            "gas":25,
            "supply":2,
            "buildtime":21,
            "buildfrom":["factory","factory reactor","factory with tech lab"]
        },
        "thor":{
            "no":10,
            "race":"terran",
            "mineral":300,
            "gas":200,
            "supply":6,
            "buildtime":43,
            "buildfrom":"factory with tech lab",
            "required":"armory"
        },
        "viking":{
            "no":11,
            "race":"terran",
            "mineral":150,
            "gas":75,
            "supply":2,
            "buildtime":30,
            "buildfrom":["starport","starport reactor", "starport with tech lab"]
        },
        "medivac":{
            "no":12,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "supply":2,
            "buildtime":30,
            "buildfrom":["starport","starport reactor", "starport with tech lab"]
        },
        "liberator":{
            "no":13,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "supply":3,
            "buildtime":43,
            "buildfrom":["starport","starport reactor", "starport with tech lab"]
        },
        "raven":{
            "no":14,
            "race":"terran",
            "mineral":100,
            "gas":200,
            "supply":2,
            "buildtime":43,
            "buildfrom":"starport with tech lab",
        },
        "banshee":{
            "no":15,
            "race":"terran",
            "mineral":150,
            "gas":100,
            "supply":3,
            "buildtime":43,
            "buildfrom":"starport with tech lab",
        },
        "battle cruiser":{
            "no":16,
            "race":"terran",
            "mineral":400,
            "gas":300,
            "supply":6,
            "buildtime":64,
            "buildfrom":"starport with tech lab",
            "required":"fusion core"
        },
    },
    "zerg":{
        "drone":{
            "no":0,
            "race":"zerg",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":12,
            "buildfrom":"larva"
        },
        "zergling":{ # 50minerals and 1 supply morphs 2 zerglings from a single larva
            "no":1,
            "race":"zerg",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":17,
            "buildfrom":"larva",
            "required":"spawning pool"
        },
        "queen":{
            "no":2,
            "race":"zerg",
            "mineral":150,
            "gas":0,
            "supply":2,
            "buildtime":36,
            "buildfrom":["hatchery","lair","hive"],
            "required":"spawning pool",
            "startingEnergy":25
        },
        "baneling":{
            "no":3,
            "race":"zerg",
            "mineral":25,
            "gas":25,
            "supply":1,
            "buildtime":14,
            "buildfrom":"zergling",
            "required":"baneling nest"
        },
        "larva":{
            "no":4,
            "race":"zerg",
            "mineral":0,
            "gas":0,
            "supply":0,
            "buildtime":11,
            "buildfrom":"hatchery"
        },
        "roach":{
            "no":5,
            "race":"zerg",
            "mineral":75,
            "gas":25,
            "supply":2,
            "buildtime":19,
            "buildfrom":"larva",
            "required":"roach warren"
        },
        "ravager":{
            "no":6,
            "race":"zerg",
            "mineral":25,
            "gas":75,
            "supply":3,
            "buildtime":9,
            "buildfrom":"roach",
            "required":"roach warren"
        },
        "hydralisk":{
            "no":7,
            "race":"zerg",
            "mineral":100,
            "gas":50,
            "supply":2,
            "buildtime":24,
            "buildfrom":"larva",
            "required":"hydralisk den"
        },
		"lurker":{
            "no":8,
            "race":"zerg",
            "mineral":50,
            "gas":100,
            "supply":3,
            "buildtime":18,
            "buildfrom":"hydralisk",
            "required":"lurker den"
        },
		"infestor":{
            "no":9,
            "race":"zerg",
            "mineral":100,
            "gas":150,
            "supply":2,
            "buildtime":36,
            "buildfrom":"larva",
            "required":"infestation pit"
        },
		"swarm host":{
            "no":10,
            "race":"zerg",
            "mineral":100,
            "gas":75,
            "supply":3,
            "buildtime":29,
            "buildfrom":"larva",
            "required":"infestation pit"
        },
		"ultralisk":{
            "no":11,
            "race":"zerg",
            "mineral":275,
            "gas":200,
            "supply":6,
            "buildtime":39,
            "buildfrom":"larva",
            "required":"ultralisk cavern"
        },
		"mutalisk":{
            "no":12,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "supply":2,
            "buildtime":24,
            "buildfrom":"larva",
            "required":"spire"
        },
		"corruptor":{
            "no":13,
            "race":"zerg",
            "mineral":150,
            "gas":100,
            "supply":2,
            "buildtime":29,
            "buildfrom":"larva",
            "required":"spire"
        },
		"brood lord":{
            "no":14,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "supply":4,
            "buildtime":24,
            "buildfrom":"corruptor",
            "required":"greater spire"
        },
		"viper":{
            "no":15,
            "race":"zerg",
            "mineral":100,
            "gas":200,
            "supply":3,
            "buildtime":29,
            "buildfrom":"larva",
            "required":"hive"
        }
    },
    "protossBW":{
        "probe":{
            "no":0,
            "race":"protossBW",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":13,
            "buildfrom":"nexus"
        },
        "zealot":{
            "no":1,
            "race":"protossBW",
            "mineral":100,
            "gas":0,
            "supply":2,
            "buildtime":26,
            "buildfrom":"gateway"
        },
        "dragoon":{
            "no":2,
            "race":"protossBW",
            "mineral":125,
            "gas":50,
            "supply":2,
            "buildtime":32,
            "buildfrom":"gateway",
            "required":"cybernetics core"
        },
        "high templar":{
            "no":3,
            "race":"protossBW",
            "mineral":50,
            "gas":150,
            "supply":2,
            "buildtime":32,
            "buildfrom":"gateway",
            "required":"templar archives"
        },
        "dark templar":{
            "no":4,
            "race":"protossBW",
            "mineral":125,
            "gas":100,
            "supply":2,
            "buildtime":32,
            "buildfrom":"gateway",
            "required":"templar archives"
        },
        "observer":{
            "no":5,
            "race":"protossBW",
            "mineral":25,
            "gas":75,
            "supply":1,
            "buildtime":26,
            "buildfrom":"robotics facility",
            "required":"observatory"
        },
        "reaver":{
            "no":6,
            "race":"protossBW",
            "mineral":200,
            "gas":100,
            "supply":4,
            "buildtime":44,
            "buildfrom":"robotics facility",
            "required":"robotic support bay"
        },
        "shuttle":{
            "no":7,
            "race":"protossBW",
            "mineral":200,
            "gas":0,
            "supply":2,
            "buildtime":38,
            "buildfrom":"robotics facility"
        },
        "scout":{
            "no":8,
            "race":"protossBW",
            "mineral":275,
            "gas":125,
            "supply":3,
            "buildtime":50,
            "buildfrom":"stargate"
        },
        "carrier":{
            "no":9,
            "race":"protossBW",
            "mineral":350,
            "gas":250,
            "supply":6,
            "buildtime":88,
            "buildfrom":"stargate",
            "required":"fleet beacon"
        },
        "arbiter":{
            "no":10,
            "race":"protossBW",
            "mineral":100,
            "gas":350,
            "supply":4,
            "buildtime":101,
            "buildfrom":"stargate",
            "required":"arbiter tribunal"
        },
        "corsair":{
            "no":11,
            "race":"protossBW",
            "mineral":150,
            "gas":100,
            "supply":2,
            "buildtime":26,
            "buildfrom":"stargate"
        },
        "archon":{
            "no":12,
            "race":"protossBW",
            "mineral":0,
            "gas":0,
            "supply":4,
            "buildtime":13,
            "buildfrom":["high templar","high templar"]
        },
        "dark archon":{
            "no":13,
            "race":"protossBW",
            "mineral":0,
            "gas":0,
            "supply":4,
            "buildtime":13,
            "buildfrom":["dark templar","dark templar"]
        }
    },
    "terranBW":{
        "scv":{
            "no":0,
            "race":"terranBW",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":13,
            "buildfrom":"command center"
        },
        "marine":{
            "no":1,
            "race":"terranBW",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":16,
            "buildfrom":"barracks"
        },
        "firebat":{
            "no":2,
            "race":"terranBW",
            "mineral":50,
            "gas":25,
            "supply":1,
            "buildtime":16,
            "buildfrom":"barracks",
            "required":"academy"
        },
        "medic":{
            "no":3,
            "race":"terranBW",
            "mineral":50,
            "gas":25,
            "supply":1,
            "buildtime":19,
            "buildfrom":"barracks",
            "required":"academy"
        },
        "ghost":{
            "no":4,
            "race":"terranBW",
            "mineral":25,
            "gas":75,
            "supply":1,
            "buildtime":32,
            "buildfrom":"barracks",
            "required":["ghost academy","covert ops"]
        },
        "vulture":{
            "no":5,
            "race":"terranBW",
            "mineral":75,
            "gas":0,
            "supply":2,
            "buildtime":19,
            "buildfrom":["factory","factory with machine shop"]
        },
        "siege tank":{
            "no":6,
            "race":"terranBW",
            "mineral":150,
            "gas":100,
            "supply":2,
            "buildtime":32,
            "buildfrom":"factory with machine shop",
            "required":"factory machine shop"
        },
        "goliath":{
            "no":7,
            "race":"terranBW",
            "mineral":100,
            "gas":50,
            "supply":2,
            "buildtime":26,
            "buildfrom":"factory",
            "required":"armory"
        },
        "wraith":{
            "no":10,
            "race":"terranBW",
            "mineral":150,
            "gas":100,
            "supply":2,
            "buildtime":38,
            "buildfrom":["starport","starport with control tower"]
        },
        "dropship":{
            "no":11,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "supply":2,
            "buildtime":32,
            "buildfrom":"starport with control tower",
        },
        "science vessel":{
            "no":12,
            "race":"terranBW",
            "mineral":100,
            "gas":225,
            "supply":2,
            "buildtime":50,
            "buildfrom":"starport with control tower",
            "required":"science facility"
        },
        "battlecruiser":{
            "no":13,
            "race":"terranBW",
            "mineral":400,
            "gas":300,
            "supply":6,
            "buildtime":84,
            "buildfrom":"starport with control tower",
            "required":"physics lab"
        },
        "valkyrie":{
            "no":14,
            "race":"terranBW",
            "mineral":250,
            "gas":125,
            "supply":3,
            "buildtime":32,
            "buildfrom":"starport with control tower",
            "required":"armory"
        },
        "nuclear missile":{
            "no":14,
            "race":"terranBW",
            "mineral":200,
            "gas":200,
            "supply":8,
            "buildtime":63,
            "buildfrom":"cc nuclear silo"
        }
    },
    "zergBW":{
        "drone":{
            "no":0,
            "race":"zergBW",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":13,
            "buildfrom":"larva"
        },
        "zergling":{ # 50minerals and 1 supply morphs 2 zerglings from a single larva
            "no":1,
            "race":"zergBW",
            "mineral":50,
            "gas":0,
            "supply":1,
            "buildtime":18,
            "buildfrom":"larva",
            "required":"spawning pool"
        },
        "hydralisk":{
            "no":2,
            "race":"zergBW",
            "mineral":75,
            "gas":25,
            "supply":1,
            "buildtime":18,
            "buildfrom":"larva",
            "required":"hydralisk den"
        },
        "lurker":{
            "no":3,
            "race":"zergBW",
            "mineral":50,
            "gas":100,
            "supply":2,
            "buildtime":25,
            "buildfrom":"hydralisk",
            "required":"lurker aspect research"
        },
        "larva":{
            "no":4,
            "race":"zergBW",
            "mineral":0,
            "gas":0,
            "supply":0,
            "buildtime":11,
            "buildfrom":"hatchery"
        },
        "ultralisk":{
            "no":5,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "supply":4,
            "buildtime":38,
            "buildfrom":"larva",
            "required":"ultralisk cavern"
        },
        "defiler":{
            "no":6,
            "race":"zergBW",
            "mineral":50,
            "gas":150,
            "supply":2,
            "buildtime":32,
            "buildfrom":"larva",
            "required":"defiler mound"
        },
		"mutalisk":{
            "no":10,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "supply":2,
            "buildtime":25,
            "buildfrom":"larva",
            "required":"spire"
        },
		"scourge":{ # 25minerals, 75gas, and 1 supply morphs 2 scourge from a single larva
            "no":11,
            "race":"zergBW",
            "mineral":25,
            "gas":75,
            "supply":1,
            "buildtime":19,
            "buildfrom":"larva",
            "required":"spire"
        },
		"queen":{
            "no":12,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "supply":2,
            "buildtime":32,
            "buildfrom":"larva",
            "required":"queens nest"
        },
		"guardian":{
            "no":13,
            "race":"zergBW",
            "mineral":50,
            "gas":100,
            "supply":2,
            "buildtime":25,
            "buildfrom":"mutalisk",
            "required":"greater spire"
        },
		"devourer":{
            "no":14,
            "race":"zergBW",
            "mineral":150,
            "gas":50,
            "supply":2,
            "buildtime":25,
            "buildfrom":"mutalisk",
            "required":"greater spire"
        }
    }
},
"building":{
    "protoss":{
        "nexus":{
            "no":0,
            "race":"protoss",
            "mineral":400,
            "gas":0,
            "buildtime":71,
            "supplyoffer":15,
            "startingEnergy":50
        },
        "pylon":{
            "no":1,
            "race":"protoss",
            "mineral":100,
            "gas":0,
            "buildtime":18,
            "supplyoffer":8
        },
        "assimilator":{
            "no":2,
            "race":"protoss",
            "mineral":75,
            "gas":0,
            "buildtime":21,
            "supplyoffer":0
        },
        "forge":{
            "no":3,
            "race":"protoss",
            "mineral":150,
            "gas":0,
            "buildtime":32,
            "supplyoffer":0,
            "required":"pylon"
        },
        "cybernetics core":{
            "no":4,
            "race":"protoss",
            "mineral":150,
            "gas":0,
            "buildtime":36,
            "supplyoffer":0,
            "required":"gateway"
            },
        "photon cannon":{
            "no":5,
            "race":"protoss",
            "mineral":150,
            "gas":0,
            "buildtime":29,
            "supplyoffer":0,
            "required":"forge"
        },
        "templar archives":{
            "no":6,
            "race":"protoss",
            "mineral":150,
            "gas":200,
            "buildtime":36,
            "supplyoffer":0,
            "required":"twilight council"
        },
        "dark shrine":{
            "no":7,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildtime":71,
            "supplyoffer":0,
            "required":"twilight council"
        },
        "twilight council":{
            "no":8,
            "race":"protoss",
            "mineral":150,
            "gas":100,
            "buildtime":36,
            "supplyoffer":0,
            "required":"cybernetics core"
        },
        "fleet beacon":{
            "no":9,
            "race":"protoss",
            "mineral":300,
            "gas":200,
            "buildtime":43,
            "supplyoffer":0,
            "required":"stargate"
        },
        "robotics facility":{
            "no":10,
            "race":"protoss",
            "mineral":150,
            "gas":100,
            "buildtime":46,
            "supplyoffer":0,
            "required":"cybernetics core"
        },
        "robotics bay":{
            "no":11,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildtime":46,
            "supplyoffer":0,
            "required":"robotics facility"
        },
        "gateway":{
            "no":12,
            "race":"protoss",
            "mineral":150,
            "gas":0,
            "buildtime":46,
            "supplyoffer":0,
            "required":"pylon"
        },
        "warp gate":{
            "no":13,
            "race":"protoss",
            "mineral":0,
            "gas":0,
            "buildtime":7,
            "supplyoffer":0,
            "buildfrom":"gateway",
            "required":"warp gate research"
        },
        "stargate":{
            "no":14,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildtime":43,
            "supplyoffer":0,
            "required":"cybernetics core"
        },
        "shield battery":{
            "no":15,
            "race":"protoss",
            "mineral":100,
            "gas":0,
            "buildtime":29,
            "supplyoffer":0,
            "required":"cybernetics core"
        }
    },
    "terran":{
        "command center":{
            "no":0,
            "race":"terran",
            "mineral":400,
            "gas":0,
            "buildtime":71,
            "supplyoffer":15
        },
        "orbital command":{
            "no":1,
            "race":"terran",
            "mineral":150,
            "gas":0,
            "buildtime":25,
            "supplyoffer":15,
            "addon":"true",
            "buildfrom":"command center",
            "required":"barracks",
            "startingEnergy":50
        },
        "planetary fortress":{
            "no":2,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildtime":36,
            "supplyoffer":15,
            "addon":"true",
            "buildfrom":"command center",
            "required":"engineering bay"
        },
        "supply depot":{
            "no":3,
            "race":"terran",
            "mineral":100,
            "gas":0,
            "buildtime":21,
            "supplyoffer":8
        },
        "refinery":{
            "no":4,
            "race":"terran",
            "mineral":75,
            "gas":0,
            "buildtime":21,
            "supplyoffer":0
        },
        "barracks":{
            "no":5,
            "race":"terran",
            "mineral":150,
            "gas":0,
            "buildtime":46,
            "required":"supply depot",
            "supplyoffer":0
        },
        "factory":{
            "no":6,
            "race":"terran",
            "mineral":150,
            "gas":100,
            "buildtime":43,
            "required":"barracks",
            "supplyoffer":0
        },
        "starport":{
            "no":7,
            "race":"terran",
            "mineral":150,
            "gas":100,
            "buildtime":36,
            "required":"factory",
            "supplyoffer":0
        },
        "engineering bay":{
            "no":8,
            "race":"terran",
            "mineral":125,
            "gas":0,
            "buildtime":25,
            "supplyoffer":0
        },
        "missile turret":{
            "no":9,
            "race":"terran",
            "mineral":100,
            "gas":0,
            "buildtime":18,
            "required":"engineering bay",
            "supplyoffer":0
        },
        "barracks with tech lab":{
            "no":10,
            "race":"terran",
            "mineral":50,
            "gas":25,
            "buildtime":18,
            "buildfrom":"barracks",
            "addon":"true",
            "required":"barracks",
            "supplyoffer":0
        },
        "factory with tech lab":{
            "no":11,
            "race":"terran",
            "mineral":50,
            "gas":25,
            "buildtime":18,
            "buildfrom":"factory",
            "addon":"true",
            "required":"factory",
            "supplyoffer":0
        },
        "starport with tech lab":{
            "no":12,
            "race":"terran",
            "mineral":50,
            "gas":25,
            "buildtime":18,
            "buildfrom":"starport",
            "addon":"true",
            "required":"starport",
            "supplyoffer":0
        },
        "bunker":{
            "no":13,
            "race":"terran",
            "mineral":100,
            "gas":0,
            "buildtime":29,
            "required":"barracks",
            "supplyoffer":0
        },
        "sensor tower":{
            "no":14,
            "race":"terran",
            "mineral":125,
            "gas":100,
            "buildtime":18,
            "required":"engineering bay",
            "supplyoffer":0
        },
        "barracks reactor":{
            "no":15,
            "race":"terran",
            "mineral":50,
            "gas":50,
            "buildtime":36,
            "buildfrom":"barracks",
            "addon":"true",
            "required":"barracks",
            "supplyoffer":0
        },
        "factory reactor":{
            "no":16,
            "race":"terran",
            "mineral":50,
            "gas":50,
            "buildtime":36,
            "buildfrom":"factory",
            "addon":"true",
            "required":"factory",
            "supplyoffer":0
        },
        "starport reactor":{
            "no":17,
            "race":"terran",
            "mineral":50,
            "gas":50,
            "buildtime":36,
            "buildfrom":"starport",
            "addon":"true",
            "required":"starport",
            "supplyoffer":0
        },
        "armory":{
            "no":18,
            "race":"terran",
            "mineral":150,
            "gas":50,
            "buildtime":46,
            "required":["factory","factory reactor","factory with tech lab"],
            "supplyoffer":0
        },
        "ghost academy":{
            "no":19,
            "race":"terran",
            "mineral":150,
            "gas":50,
            "buildtime":29,
            "required":"barracks",
            "supplyoffer":0
        },
        "barracks tech lab":{
            "no":20,
            "race":"terran",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "factory tech lab":{
            "no":21,
            "race":"terran",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "starport tech lab":{
            "no":22,
            "race":"terran",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "fusion core":{
            "no":23,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildtime":46,
            "required":"starport",
            "supplyoffer":0
        }
    },
    "zerg":{
        "hatchery":{
            "no":0,
            "race":"zerg",
            "mineral":300,
            "gas":0,
            "buildtime":71,
			"buildfrom":"drone",
            "supplyoffer":6
        },
        "overlord":{
            "no":1,
            "race":"zerg",
            "mineral":100,
            "gas":0,
            "buildtime":18,
			"buildfrom":"larva",
            "supplyoffer":8
        },
        "extractor":{
            "no":2,
            "race":"zerg",
            "mineral":25,
            "gas":0,
            "buildtime":21,
			"buildfrom":"drone",
            "supplyoffer":0
        },
        "spawning pool":{
            "no":3,
            "race":"zerg",
            "mineral":200,
            "gas":0,
            "buildtime":46,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"hatchery"
        },
        "evolution chamber":{
            "no":4,
            "race":"zerg",
            "mineral":75,
            "gas":0,
            "buildtime":25,
            "supplyoffer":0,
			"buildfrom":"drone"
            },
        "lair":{
            "no":5,
            "race":"zerg",
            "mineral":150,
            "gas":100,
            "buildtime":57,
            "supplyoffer":15,
			"buildfrom":"hatchery",
            "required":"spawning pool"
        },
        "roach warren":{
            "no":6,
            "race":"zerg",
            "mineral":150,
            "gas":0,
            "buildtime":39,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"spawning pool"
        },
        "baneling nest":{
            "no":7,
            "race":"zerg",
            "mineral":100,
            "gas":50,
            "buildtime":43,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"spawning pool"
        },
        "hydralisk den":{
            "no":8,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildtime":29,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"lair"
        },
		"lurker den":{
            "no":9,
            "race":"zerg",
            "mineral":100,
            "gas":150,
            "buildtime":57,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"hydralisk den"
        },
        "hive":{
            "no":10,
            "race":"zerg",
            "mineral":200,
            "gas":150,
            "buildtime":71,
            "supplyoffer":15,
			"buildfrom":"lair",
            "required":"infestation pit"
        },
        "infestation pit":{
            "no":11,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildtime":36,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"lair"
        },
		"spire":{
            "no":12,
            "race":"zerg",
            "mineral":200,
            "gas":200,
            "buildtime":71,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"lair"
        },
		"greater spire":{
            "no":13,
            "race":"zerg",
            "mineral":100,
            "gas":150,
            "buildtime":71,
            "supplyoffer":0,
			"buildfrom":"spire",
            "required":"hive"
        },
		"ultralisk cavern":{
            "no":14,
            "race":"zerg",
            "mineral":150,
            "gas":200,
            "buildtime":46,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"hive"
        },
        "nydus network":{
            "no":15,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildtime":36,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"lair"
        },
		"spine crawler":{
            "no":16,
            "race":"zerg",
            "mineral":100,
            "gas":0,
            "buildtime":36,
            "supplyoffer":0,
			"buildfrom":"drone"
        },
		"spore crawler":{
            "no":17,
            "race":"zerg",
            "mineral":75,
            "gas":0,
            "buildtime":21,
            "supplyoffer":0,
			"buildfrom":"drone",
			"required":"spawning pool"
        }
    },
    "protossBW":{
        "nexus":{
            "no":0,
            "race":"protossBW",
            "mineral":400,
            "gas":0,
            "buildtime":75,
            "supplyoffer":9,
        },
        "pylon":{
            "no":1,
            "race":"protossBW",
            "mineral":100,
            "gas":0,
            "buildtime":19,
            "supplyoffer":8
        },
        "assimilator":{
            "no":2,
            "race":"protossBW",
            "mineral":100,
            "gas":0,
            "buildtime":25,
            "supplyoffer":0
        },
        "forge":{
            "no":3,
            "race":"protossBW",
            "mineral":150,
            "gas":0,
            "buildtime":25,
            "supplyoffer":0,
            "required":"pylon"
        },
        "cybernetics core":{
            "no":4,
            "race":"protossBW",
            "mineral":200,
            "gas":0,
            "buildtime":38,
            "supplyoffer":0,
            "required":"gateway"
            },
        "gateway":{
            "no":5,
            "race":"protossBW",
            "mineral":150,
            "gas":0,
            "buildtime":38,
            "supplyoffer":0
        },
        "templar archives":{
            "no":6,
            "race":"protossBW",
            "mineral":150,
            "gas":200,
            "buildtime":38,
            "supplyoffer":0,
            "required":"citadel of adun"
        },
        "citadel of adun":{
            "no":7,
            "race":"protossBW",
            "mineral":150,
            "gas":100,
            "buildtime":38,
            "supplyoffer":0,
            "required":"cybernetics core"
        },
        "observatory":{
            "no":8,
            "race":"protossBW",
            "mineral":50,
            "gas":100,
            "buildtime":19,
            "supplyoffer":0,
            "required":"robotics facility"
        },
        "fleet beacon":{
            "no":9,
            "race":"protossBW",
            "mineral":300,
            "gas":200,
            "buildtime":38,
            "supplyoffer":0,
            "required":"stargate"
        },
        "robotics facility":{
            "no":10,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildtime":50,
            "supplyoffer":0,
            "required":"cybernetics core"
        },
        "robotics support bay":{
            "no":11,
            "race":"protossBW",
            "mineral":150,
            "gas":100,
            "buildtime":19,
            "supplyoffer":0,
            "required":"robotics facility"
        },
        
        "arbiter tribunal":{
            "no":12,
            "race":"protossBW",
            "mineral":200,
            "gas":150,
            "buildtime":38,
            "supplyoffer":0,
            "required":["stargate","templar archives"]
        },
        "stargate":{
            "no":13,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildtime":44,
            "supplyoffer":0,
            "required":"cybernetics core"
        },
        "photon cannon":{
            "no":15,
            "race":"protossBW",
            "mineral":150,
            "gas":0,
            "buildtime":32,
            "supplyoffer":0,
            "required":"forge"
        },
        "shield battery":{
            "no":16,
            "race":"protossBW",
            "mineral":100,
            "gas":0,
            "buildtime":19,
            "supplyoffer":0,
            "required":"gateway"
        }
    },
    "terranBW":{
        "command center":{
            "no":0,
            "race":"terranBW",
            "mineral":400,
            "gas":0,
            "buildtime":75,
            "supplyoffer":10
        },
        "cc with comsat station":{
            "no":1,
            "race":"terranBW",
            "mineral":50,
            "gas":50,
            "buildtime":25,
            "addon":"true",
            "buildfrom":"command center",
            "required":"academy",
            "supplyoffer":0
        },
        "cc with nuclear silo":{
            "no":2,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildtime":50,
            "addon":"true",
            "buildfrom":"command center",
            "required":"science facility with covert ops",
            "supplyoffer":0
        },
        "supply depot":{
            "no":3,
            "race":"terranBW",
            "mineral":100,
            "gas":0,
            "buildtime":25,
            "supplyoffer":8
        },
        "refinery":{
            "no":4,
            "race":"terranBW",
            "mineral":100,
            "gas":0,
            "buildtime":25,
            "supplyoffer":0
        },
        "barracks":{
            "no":5,
            "race":"terranBW",
            "mineral":150,
            "gas":0,
            "buildtime":50,
            "supplyoffer":0
        },
        "factory":{
            "no":6,
            "race":"terranBW",
            "mineral":200,
            "gas":100,
            "buildtime":50,
            "required":"barracks",
            "supplyoffer":0
        },
        "starport":{
            "no":7,
            "race":"terranBW",
            "mineral":150,
            "gas":100,
            "buildtime":44,
            "required":"factory",
            "supplyoffer":0
        },
        "engineering bay":{
            "no":8,
            "race":"terranBW",
            "mineral":125,
            "gas":0,
            "buildtime":38,
            "supplyoffer":0
        },
        "missile turret":{
            "no":9,
            "race":"terranBW",
            "mineral":75,
            "gas":0,
            "buildtime":19,
            "required":"engineering bay",
            "supplyoffer":0
        },
        "academy":{
            "no":10,
            "race":"terranBW",
            "mineral":150,
            "gas":0,
            "buildtime":50,
            "required":"barracks",
            "supplyoffer":0
        },
        "factory with machine shop":{
            "no":11,
            "race":"terranBW",
            "mineral":50,
            "gas":50,
            "buildtime":25,
            "buildfrom":"factory",
            "addon":"true",
            "required":"factory",
            "supplyoffer":0
        },
        "starport with control tower":{
            "no":12,
            "race":"terranBW",
            "mineral":50,
            "gas":50,
            "buildtime":25,
            "buildfrom":"starport",
            "addon":"true",
            "required":"starport",
            "supplyoffer":0
        },
        "armory":{
            "no":13,
            "race":"terranBW",
            "mineral":100,
            "gas":50,
            "buildtime":50,
            "required":["factory","factory with machine shop"],
            "supplyoffer":0
        },
        "bunker":{
            "no":14,
            "race":"terranBW",
            "mineral":100,
            "gas":0,
            "buildtime":19,
            "required":"barracks",
            "supplyoffer":0
        },
        "science facility":{
            "no":15,
            "race":"terranBW",
            "mineral":100,
            "gas":150,
            "buildtime":38,
            "required":"starport",
            "supplyoffer":0
        },
        "science facility with physics lab":{
            "no":16,
            "race":"terranBW",
            "mineral":50,
            "gas":50,
            "buildtime":25,
            "required":"science facility",
            "supplyoffer":0
        },
        "science facility with covert ops":{
            "no":17,
            "race":"terranBW",
            "mineral":50,
            "gas":50,
            "buildtime":25,
            "required":"science facility",
            "supplyoffer":0
        },
        "factory machine shop":{
            "no":18,
            "race":"terranBW",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "starport control tower":{
            "no":19,
            "race":"terranBW",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "science facility physics lab":{
            "no":20,
            "race":"terranBW",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "science facility covert ops":{
            "no":21,
            "race":"terranBW",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "cc comsat station":{
            "no":22,
            "race":"terranBW",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        },
        "cc nuclear silo":{
            "no":23,
            "race":"terranBW",
            "mineral":0,
            "gas":0,
            "buildtime":0,
            "buildfrom":"",
            "addon":"true",
            "required":"",
            "supplyoffer":0
        }
    },
    "zergBW":{
        "hatchery":{
            "no":0,
            "race":"zergBW",
            "mineral":300,
            "gas":0,
            "buildtime":75,
			"buildfrom":"drone",
            "supplyoffer":1
        },
        "overlord":{
            "no":1,
            "race":"zergBW",
            "mineral":100,
            "gas":0,
            "buildtime":25,
			"buildfrom":"larva",
            "supplyoffer":8
        },
        "extractor":{
            "no":2,
            "race":"zergBW",
            "mineral":50,
            "gas":0,
            "buildtime":25,
			"buildfrom":"drone",
            "supplyoffer":0
        },
        "spawning pool":{
            "no":3,
            "race":"zergBW",
            "mineral":200,
            "gas":0,
            "buildtime":50,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"hatchery"
        },
        "evolution chamber":{
            "no":4,
            "race":"zergBW",
            "mineral":75,
            "gas":0,
            "buildtime":25,
            "supplyoffer":0,
			"buildfrom":"drone"
            },
        "lair":{
            "no":5,
            "race":"zergBW",
            "mineral":150,
            "gas":100,
            "buildtime":63,
            "supplyoffer":1,
			"buildfrom":"hatchery",
            "required":"spawning pool"
        },
        "hydralisk den":{
            "no":6,
            "race":"zergBW",
            "mineral":100,
            "gas":50,
            "buildtime":25,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"spawning pool"
        },
        "spire":{
            "no":7,
            "race":"zergBW",
            "mineral":200,
            "gas":150,
            "buildtime":75,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"lair"
        },
        "queens nest":{
            "no":8,
            "race":"zergBW",
            "mineral":150,
            "gas":100,
            "buildtime":38,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"lair"
        },
        "hive":{
            "no":10,
            "race":"zergBW",
            "mineral":200,
            "gas":150,
            "buildtime":75,
            "supplyoffer":1,
			"buildfrom":"lair",
            "required":"queens nest"
        },
        "greater spire":{
            "no":11,
            "race":"zergBW",
            "mineral":100,
            "gas":150,
            "buildtime":75,
            "supplyoffer":0,
			"buildfrom":"spire",
            "required":"hive"
        },
		"ultralisk cavern":{
            "no":12,
            "race":"zergBW",
            "mineral":150,
            "gas":200,
            "buildtime":50,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"hive"
        },
		"defiler mound":{
            "no":13,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildtime":38,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"hive"
        },
		"nydus canal":{
            "no":14,
            "race":"zergBW",
            "mineral":150,
            "gas":0,
            "buildtime":25,
            "supplyoffer":0,
			"buildfrom":"drone",
            "required":"hive"
        },
        "creep colony":{
            "no":15,
            "race":"zergBW",
            "mineral":75,
            "gas":0,
            "buildtime":12,
            "supplyoffer":0,
			"buildfrom":"drone"
        },
		"sunken colony":{
            "no":16,
            "race":"zergBW",
            "mineral":50,
            "gas":0,
            "buildtime":12,
            "supplyoffer":0,
			"buildfrom":"creep colony",
            "required":"spawning pool"
        },
		"spore colony":{
            "no":17,
            "race":"zergBW",
            "mineral":50,
            "gas":0,
            "buildtime":12,
            "supplyoffer":0,
			"buildfrom":"creep colony",
			"required":"evolution chamber"
        }
    }
},
"upgrade":{
    "protoss":{
        "warp gate research":{
            "no":0,
            "race":"protoss",
            "mineral":50,
            "gas":50,
            "buildfrom":"cybernetics core",
            "buildtime":100,
        },
        "charge research":{
            "no":1,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"twilight council",
            "buildtime":100,
        },
        "ground weapons level 1":{
            "no":2,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"forge",
            "buildtime":129,
        },
        "ground weapons level 2":{
            "no":3,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildfrom":"forge",
            "buildtime":154,
            "required":["twilight council","ground weapons level 1"]
        },
        "ground weapons level 3":{
            "no":4,
            "race":"protoss",
            "mineral":200,
            "gas":200,
            "buildfrom":"forge",
            "buildtime":179,
            "required":["twilight council","ground weapons level 2"]
        },
        "blink research":{
            "no":5,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildfrom":"twilight council",
            "buildtime":121
        },
        "resonating glaives research":{
            "no":6,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"twilight council",
            "buildtime":100
        },
        "ground armor level 1":{
            "no":7,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"forge",
            "buildtime":129,
        },
        "ground armor level 2":{
            "no":8,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildfrom":"forge",
            "buildtime":154,
            "required":["twilight council","ground armor level 1"]
        },
        "ground armor level 3":{
            "no":9,
            "race":"protoss",
            "mineral":200,
            "gas":200,
            "buildfrom":"forge",
            "buildtime":179,
            "required":["twilight council","ground armor level 2"]
        },
        "psionic storm research":{
            "no":10,
            "race":"protoss",
            "mineral":200,
            "gas":200,
            "buildfrom":"templar archives",
            "buildtime":79
        },
        "shadow stride research":{
            "no":11,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"dark shrine",
            "buildtime":100
        },
        "shields level 1":{
            "no":12,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildfrom":"forge",
            "buildtime":129,
        },
        "shields level 2":{
            "no":13,
            "race":"protoss",
            "mineral":200,
            "gas":200,
            "buildfrom":"forge",
            "buildtime":154,
            "required":["twilight council","shield level 1"]
        },
        "shields level 3":{
            "no":14,
            "race":"protoss",
            "mineral":250,
            "gas":250,
            "buildfrom":"forge",
            "buildtime":179,
            "required":["twilight council","shield level 2"]
        },
        "gravitic boosters research":{
            "no":15,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"robotics bay",
            "buildtime":57
        },
        "gravitic drive research":{
            "no":16,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"robotics bay",
            "buildtime":57
        },
        "air weapons level 1":{
            "no":17,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"cybernetics core",
            "buildtime":129,
        },
        "air weapons level 2":{
            "no":18,
            "race":"protoss",
            "mineral":175,
            "gas":175,
            "buildfrom":"cybernetics core",
            "buildtime":154,
            "required":["fleet beacon","air weapons level 1"]
        },
        "air weapons level 3":{
            "no":19,
            "race":"protoss",
            "mineral":250,
            "gas":250,
            "buildfrom":"cybernetics core",
            "buildtime":179,
            "required":["fleet beacon","air weapons level 2"]
        },
        "extended thermal lances research":{
            "no":20,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildfrom":"robotics bay",
            "buildtime":100
        },
        "anion pulse-crystals research":{
            "no":21,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildfrom":"fleet beacon",
            "buildtime":64
        },
        "air armor level 1":{
            "no":22,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"cybernetics core",
            "buildtime":129,
        },
        "air armor level 2":{
            "no":23,
            "race":"protoss",
            "mineral":175,
            "gas":175,
            "buildfrom":"cybernetics core",
            "buildtime":154,
            "required":["fleet beacon","air armor level 1"]
        },
        "air armor level 3":{
            "no":24,
            "race":"protoss",
            "mineral":250,
            "gas":250,
            "buildfrom":"cybernetics core",
            "buildtime":179,
            "required":["fleet beacon","air armor level 2"]
        },
        "flux vanes research":{
            "no":25,
            "race":"protoss",
            "mineral":100,
            "gas":100,
            "buildfrom":"fleet beacon",
            "buildtime":57
        },
        "tectonic destabilizers research":{
            "no":26,
            "race":"protoss",
            "mineral":150,
            "gas":150,
            "buildfrom":"fleet beacon",
            "buildtime":100
        }
    },
    "terran":{
        "combat shield research":{
            "no":0,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"barracks tech lab",
            "buildtime":79,
        },
        "stimpack research":{
            "no":1,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"barracks tech lab",
            "buildtime":100,
        },
        "infantry weapons level 1":{
            "no":2,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"engineering bay",
            "buildtime":114,
        },
        "infantry weapons level 2":{
            "no":3,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"engineering bay",
            "buildtime":136,
            "required":["armory","infantry weapons level 1"]
        },
        "infantry weapons level 3":{
            "no":4,
            "race":"terran",
            "mineral":200,
            "gas":200,
            "buildfrom":"engineering bay",
            "buildtime":157,
            "required":["armory","infantry weapons level 2"]
        },
        "concussive shells research":{
            "no":5,
            "race":"terran",
            "mineral":50,
            "gas":50,
            "buildfrom":"barracks tech lab",
            "buildtime":43
        },
        "infernal preigniter research":{
            "no":6,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"factory tech lab",
            "buildtime":79
        },
        "infantry armor level 1":{
            "no":7,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"engineering bay",
            "buildtime":114,
        },
        "infantry armor level 2":{
            "no":8,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"engineering bay",
            "buildtime":136,
            "required":["armory","infantry armor level 1"]
        },
        "infantry armor level 3":{
            "no":9,
            "race":"terran",
            "mineral":200,
            "gas":200,
            "buildfrom":"engineering bay",
            "buildtime":157,
            "required":["armory","infantry armor level 2"]
        },
        "mag field accelerator research":{
            "no":10,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"factory tech lab",
            "buildtime":100
        },
        "drilling claws research":{
            "no":11,
            "race":"terran",
            "mineral":75,
            "gas":75,
            "buildfrom":"factory tech lab",
            "required":"armory",
            "buildtime":79
        },
        "vehicle weapons level 1":{
            "no":12,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"armory",
            "buildtime":114,
        },
        "vehicle weapons level 2":{
            "no":13,
            "race":"terran",
            "mineral":175,
            "gas":175,
            "buildfrom":"armory",
            "buildtime":136,
            "required":"vehicle weapons level 1"
        },
        "vehicle weapons level 3":{
            "no":14,
            "race":"terran",
            "mineral":250,
            "gas":250,
            "buildfrom":"armory",
            "buildtime":157,
            "required":"vehicle weapons level 2"
        },
        "smart servos research":{
            "no":15,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"factory tech lab",
            "buildtime":79,
            "required":"armory"
        },
        "corvid reactor research":{
            "no":16,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"starport tech lab",
            "buildtime":79
        },
        "ship weapons level 1":{
            "no":17,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"armory",
            "buildtime":114,
        },
        "ship weapons level 2":{
            "no":18,
            "race":"terran",
            "mineral":175,
            "gas":175,
            "buildfrom":"armory",
            "buildtime":136,
            "required":"ship weapons level 1"
        },
        "ship weapons level 3":{
            "no":19,
            "race":"terran",
            "mineral":250,
            "gas":250,
            "buildfrom":"armory",
            "buildtime":157,
            "required":"ship weapons level 2"
        },
        "cloaking field research":{
            "no":20,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"starport tech lab",
            "buildtime":79
        },
        "hyperflight rotors research":{
            "no":21,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"starport tech lab",
            "buildtime":121
        },
        "vehicle and ship plating level 1":{
            "no":22,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"armory",
            "buildtime":114,
        },
        "vehicle and ship plating level 2":{
            "no":23,
            "race":"terran",
            "mineral":175,
            "gas":175,
            "buildfrom":"armory",
            "buildtime":136,
            "required":"vehicle and ship plating level 1"
        },
        "vehicle and ship plating level 3":{
            "no":24,
            "race":"terran",
            "mineral":250,
            "gas":250,
            "buildfrom":"armory",
            "buildtime":157,
            "required":"vehicle and ship plating level 2"
        },
        "hisec auto tracking research":{
            "no":25,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"engineering bay",
            "buildtime":57
        },
        "neosteel armor research":{
            "no":26,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"engineering bay",
            "buildtime":100
        },
        "personal cloaking research":{
            "no":27,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"ghost academy",
            "buildtime":86
        },
        "enhanced shockwaves research":{
            "no":28,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"engineering bay",
            "buildtime":79
        },
        "nuke":{
            "no":29,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"engineering bay",
            "buildtime":43
        },
        "weapon refit research":{
            "no":30,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"fusion core",
            "buildtime":100
        },
        "advanced ballistics research":{
            "no":31,
            "race":"terran",
            "mineral":150,
            "gas":150,
            "buildfrom":"fusion core",
            "buildtime":79
        },
        "rapid reignition research":{
            "no":32,
            "race":"terran",
            "mineral":100,
            "gas":100,
            "buildfrom":"fusion core",
            "buildtime":57
        }
    },
    "zerg":{
        "metabolic boost research":{
            "no":0,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"spawning pool",
            "buildtime":79
        },
        "glial reconstitution research":{
            "no":1,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"roach warren",
            "buildtime":79
        },
        "melee attacks level 1":{
            "no":2,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"evolution chamber",
            "buildtime":114
        },
        "melee attacks level 2":{
            "no":3,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildfrom":"evolution chamber",
            "buildtime":136,
            "required":["lair","melee attacks level 1"]
        },
        "melee attacks level 3":{
            "no":4,
            "race":"zerg",
            "mineral":200,
            "gas":200,
            "buildfrom":"evolution chamber",
            "buildtime":157,
            "required":["hive","melee attacks level 2"]
        },
        "adrenal glands research":{
            "no":5,
            "race":"zerg",
            "mineral":200,
            "gas":200,
            "buildfrom":"spawning pool",
            "buildtime":93,
			"required":"hive"
        },
        "tunneling claws research":{
            "no":6,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"roach warren",
            "buildtime":79,
			"required":"lair"
        },
        "missile attacks level 1":{
            "no":7,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"evolution chamber",
            "buildtime":114
        },
        "missile attacks level 2":{
            "no":8,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildfrom":"evolution chamber",
            "buildtime":136,
            "required":["lair","missile attacks level 1"]
        },
        "missile attacks level 3":{
            "no":9,
            "race":"zerg",
            "mineral":200,
            "gas":200,
            "buildfrom":"evolution chamber",
            "buildtime":157,
            "required":["hive","missile attacks level 2"]
        },
        "centrifugal hooks research":{
            "no":10,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"baneling nest",
            "buildtime":71
        },
        "burrow research":{
            "no":11,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"hatchery",
            "buildtime":71
        },
        "ground carapace level 1":{
            "no":12,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildfrom":"evolution chamber",
            "buildtime":114
        },
        "ground carapace level 2":{
            "no":13,
            "race":"zerg",
            "mineral":200,
            "gas":200,
            "buildfrom":"evolution chamber",
            "buildtime":136,
            "required":["lair","ground carapace level 1"]
        },
        "ground carapace level 3":{
            "no":14,
            "race":"zerg",
            "mineral":250,
            "gas":250,
            "buildfrom":"evolution chamber",
            "buildtime":157,
            "required":["hive","ground carapace level 2"]
        },
        "grooved spines research":{
            "no":15,
            "race":"zerg",
            "mineral":75,
            "gas":75,
            "buildfrom":"hydralisk den",
            "buildtime":50
        },
        "muscular augments research":{
            "no":16,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"hydralisk den",
            "buildtime":64
        },
        "flyer attacks level 1":{
            "no":17,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"spire",
            "buildtime":114
        },
        "flyer attacks level 2":{
            "no":18,
            "race":"zerg",
            "mineral":175,
            "gas":175,
            "buildfrom":"spire",
            "buildtime":136,
            "required":"flyer attacks level 1"
        },
        "flyer attacks level 3":{
            "no":19,
            "race":"zerg",
            "mineral":250,
            "gas":250,
            "buildfrom":"spire",
            "buildtime":157,
            "required":"flyer attacks level 2"
        },
        "adaptive talons research":{
            "no":20,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"lurker den",
            "buildtime":57
        },
		"seismic spines research":{
            "no":21,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildfrom":"lurker den",
            "buildtime":57
        },
		"flyer carapace level 1":{
            "no":22,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"spire",
            "buildtime":114
        },
        "flyer carapace level 2":{
            "no":23,
            "race":"zerg",
            "mineral":175,
            "gas":175,
            "buildfrom":"spire",
            "buildtime":136,
            "required":["lair","flyer carapace level 1"]
        },
        "flyer carapace level 3":{
            "no":24,
            "race":"zerg",
            "mineral":250,
            "gas":250,
            "buildfrom":"spire",
            "buildtime":157,
            "required":["hive","flyer carapace level 2"]
        },
		"chitnous plating research":{
            "no":25,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildfrom":"ultralisk cavern",
            "buildtime":79
        },
		"anabolic synthesis research":{
            "no":26,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildfrom":"ultralisk cavern",
            "buildtime":43
        },
		"pneumatized carapace research":{
            "no":27,
            "race":"zerg",
            "mineral":100,
            "gas":100,
            "buildfrom":"hatchery",
            "buildtime":43
        },
		"mutate ventral sacs research":{
            "no":28,
            "race":"zerg",
            "mineral":150,
            "gas":150,
            "buildfrom":"lair",
            "buildtime":43
        }
    },
    "protossBW":{
        "singularity charge research":{
            "no":0,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"cybernetics core",
            "buildtime":105,
        },
        "leg enhancements research":{
            "no":1,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"citadel of adun",
            "buildtime":84,
        },
        "ground weapons level 1":{
            "no":2,
            "race":"protossBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"forge",
            "buildtime":168,
        },
        "ground weapons level 2":{
            "no":3,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"forge",
            "buildtime":180,
            "required":["templar archives","ground weapons level 1"]
        },
        "ground weapons level 3":{
            "no":4,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"forge",
            "buildtime":193,
            "required":["templar archives","ground weapons level 2"]
        },
        "sensor array research":{
            "no":5,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"observatory",
            "buildtime":84
        },
        "gravitic booster research":{
            "no":6,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"observatory",
            "buildtime":84
        },
        "ground armor level 1":{
            "no":7,
            "race":"protossBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"forge",
            "buildtime":168,
        },
        "ground armor level 2":{
            "no":8,
            "race":"protossBW",
            "mineral":175,
            "gas":175,
            "buildfrom":"forge",
            "buildtime":180,
            "required":["templar archives","ground armor level 1"]
        },
        "ground armor level 3":{
            "no":9,
            "race":"protossBW",
            "mineral":250,
            "gas":250,
            "buildfrom":"forge",
            "buildtime":193,
            "required":["templar archives","ground armor level 2"]
        },
        "scarab damage research":{
            "no":10,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"robotic support bay",
            "buildtime":105
        },
        "increased reaver capacity research":{
            "no":11,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"robotic support bay",
            "buildtime":105
        },
        "shields level 1":{
            "no":12,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"forge",
            "buildtime":168,
        },
        "shields level 2":{
            "no":13,
            "race":"protossBW",
            "mineral":300,
            "gas":300,
            "buildfrom":"forge",
            "buildtime":180,
            "required":["templar archives","shield level 1"]
        },
        "shields level 3":{
            "no":14,
            "race":"protossBW",
            "mineral":400,
            "gas":400,
            "buildfrom":"forge",
            "buildtime":193,
            "required":["templar archives","shield level 2"]
        },
        "gravitic drive research":{
            "no":15,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"robotics bay",
            "buildtime":105
        },
        "carrier capacity research":{
            "no":16,
            "race":"protossBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"fleet beacon",
            "buildtime":63
        },
        "air weapons level 1":{
            "no":17,
            "race":"protossBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"cybernetics core",
            "buildtime":168,
        },
        "air weapons level 2":{
            "no":18,
            "race":"protossBW",
            "mineral":175,
            "gas":175,
            "buildfrom":"cybernetics core",
            "buildtime":180,
            "required":["fleet beacon","air weapons level 1"]
        },
        "air weapons level 3":{
            "no":19,
            "race":"protossBW",
            "mineral":250,
            "gas":250,
            "buildfrom":"cybernetics core",
            "buildtime":193,
            "required":["fleet beacon","air weapons level 2"]
        },
        "apial sensors research":{
            "no":20,
            "race":"protossBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"fleet beacon",
            "buildtime":105
        },
        "gravitic thrusters research":{
            "no":21,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"fleet beacon",
            "buildtime":105
        },
        "air armor level 1":{
            "no":22,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"cybernetics core",
            "buildtime":168,
        },
        "air armor level 2":{
            "no":23,
            "race":"protossBW",
            "mineral":225,
            "gas":225,
            "buildfrom":"cybernetics core",
            "buildtime":180,
            "required":["fleet beacon","air armor level 1"]
        },
        "air armor level 3":{
            "no":24,
            "race":"protossBW",
            "mineral":300,
            "gas":300,
            "buildfrom":"cybernetics core",
            "buildtime":1193,
            "required":["fleet beacon","air armor level 2"]
        },
        "disruption web research":{
            "no":25,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"fleet beacon",
            "buildtime":50
        },
        "argus jewel research":{
            "no":26,
            "race":"protossBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"fleet beacon",
            "buildtime":105
        },
        "stasis field research":{
            "no":27,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"arbiter tribunal",
            "buildtime":63
        },
        "recall research":{
            "no":28,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"arbiter tribunal",
            "buildtime":76
        },
        "khaydarin core research":{
            "no":29,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"arbiter tribunal",
            "buildtime":105
        },
        "psionic storm research":{
            "no":30,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"templar archives",
            "buildtime":76
        },
        "hallucination research":{
            "no":31,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"templar archives",
            "buildtime":50
        },
        "khaydarin amulet research":{
            "no":32,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"templar archives",
            "buildtime":105
        },
        "maelstrom research":{
            "no":33,
            "race":"protossBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"templar archives",
            "buildtime":63
        },
        "mind control research":{
            "no":34,
            "race":"protossBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"templar archives",
            "buildtime":76
        },
        "argus talisman research":{
            "no":35,
            "race":"protossBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"templar archives",
            "buildtime":105
        },
    },
    "terranBW":{
        "U-238 shells research":{
            "no":0,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"academy",
            "buildtime":63,
        },
        "stimpack research":{
            "no":1,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"academy",
            "buildtime":51,
        },
        "infantry weapons level 1":{
            "no":2,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"engineering bay",
            "buildtime":168,
        },
        "infantry weapons level 2":{
            "no":3,
            "race":"terranBW",
            "mineral":175,
            "gas":175,
            "buildfrom":"engineering bay",
            "buildtime":180,
            "required":["science facility","infantry weapons level 1"]
        },
        "infantry weapons level 3":{
            "no":4,
            "race":"terranBW",
            "mineral":250,
            "gas":250,
            "buildfrom":"engineering bay",
            "buildtime":193,
            "required":["science facility","infantry weapons level 2"]
        },
        "siege tech research":{
            "no":5,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"factory machine shop",
            "buildtime":50
        },
        "spider mines research":{
            "no":6,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"factory machine shop",
            "buildtime":50
        },
        "infantry armor level 1":{
            "no":7,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"engineering bay",
            "buildtime":168,
        },
        "infantry armor level 2":{
            "no":8,
            "race":"terranBW",
            "mineral":175,
            "gas":175,
            "buildfrom":"engineering bay",
            "buildtime":180,
            "required":["science facility","infantry armor level 1"]
        },
        "infantry armor level 3":{
            "no":9,
            "race":"terranBW",
            "mineral":250,
            "gas":250,
            "buildfrom":"engineering bay",
            "buildtime":193,
            "required":["science facility","infantry armor level 2"]
        },
        "ion thrusters research":{
            "no":10,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"factory machine shop",
            "buildtime":63
        },
        "charon boosters research":{
            "no":11,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"factory machine shop",
            "buildtime":84
        },
        "vehicle weapons level 1":{
            "no":12,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"armory",
            "buildtime":168,
        },
        "vehicle weapons level 2":{
            "no":13,
            "race":"terranBW",
            "mineral":175,
            "gas":175,
            "buildfrom":"armory",
            "buildtime":180,
            "required":["science facility","vehicle weapons level 1"]
        },
        "vehicle weapons level 3":{
            "no":14,
            "race":"terranBW",
            "mineral":250,
            "gas":250,
            "buildfrom":"armory",
            "buildtime":193,
            "required":["science facility","vehicle weapons level 2"]
        },
        "cloaking field research":{
            "no":15,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"starport control tower",
            "buildtime":63
        },
        "apollo reactor research":{
            "no":16,
            "race":"terranBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"starport control tower",
            "buildtime":105
        },
        "vehicle plating level 1":{
            "no":17,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"armory",
            "buildtime":168,
        },
        "vehicle plating level 2":{
            "no":18,
            "race":"terranBW",
            "mineral":175,
            "gas":175,
            "buildfrom":"armory",
            "buildtime":180,
            "required":["science facility","vehicle plating level 1"]
        },
        "vehicle plating level 3":{
            "no":19,
            "race":"terranBW",
            "mineral":250,
            "gas":250,
            "buildfrom":"armory",
            "buildtime":193,
            "required":["science facility","vehicle plating level 2"]
        },
        "emp shockwave research":{
            "no":20,
            "race":"terranBW",
            "mineral":200,
            "gas":200,
            "buildfrom":["science facility","science facility with physics lab","science facility with covert ops"],
            "buildtime":76
        },
        "irradiate research":{
            "no":21,
            "race":"terranBW",
            "mineral":200,
            "gas":200,
            "buildfrom":["science facility","science facility with physics lab","science facility with covert ops"],
            "buildtime":50
        },
        "ship weapons level 1":{
            "no":22,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"armory",
            "buildtime":168,
        },
        "ship weapons level 2":{
            "no":23,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"armory",
            "buildtime":180,
            "required":["science facility","ship weapons level 1"]
        },
        "ship weapons level 3":{
            "no":24,
            "race":"terranBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"armory",
            "buildtime":193,
            "required":["science facility","ship weapons level 2"]
        },
        "titan reactor research":{
            "no":25,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":["science facility","science facility with physics lab","science facility with covert ops"],
            "buildtime":105
        },
        "personnel cloaking research":{
            "no":26,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"science facility covert ops",
            "buildtime":50
        },
        "ship plating level 1":{
            "no":27,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"armory",
            "buildtime":168
        },
        "ship plating level 2":{
            "no":28,
            "race":"terranBW",
            "mineral":225,
            "gas":225,
            "buildfrom":"armory",
            "buildtime":180,
            "required":["science facility","ship plating level 1"]
        },
        "ship plating level 3":{
            "no":29,
            "race":"terranBW",
            "mineral":300,
            "gas":300,
            "buildfrom":"armory",
            "buildtime":193,
            "required":["science facility","ship plating level 2"]
        },
        "lockdown research":{
            "no":30,
            "race":"terranBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"science facility covert ops",
            "buildtime":63
        },
        "ocular implants research":{
            "no":31,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"science facility covert ops",
            "buildtime":105
        },
        "moebius reactor research":{
            "no":32,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"science facility covert ops",
            "buildtime":105
        },
        "restoration research":{
            "no":33,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"academy",
            "buildtime":51
        },
        "optical flare research":{
            "no":34,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"academy",
            "buildtime":76
        },
        "caduceus reactor research":{
            "no":35,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"academy",
            "buildtime":105
        },
        "yamato gun research":{
            "no":36,
            "race":"terranBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"science facility physics lab",
            "buildtime":76
        },
        "colossus reactor research":{
            "no":37,
            "race":"terranBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"science facility physics lab",
            "buildtime":105
        },
    },
    "zergBW":{
        "metabolic boost research":{
            "no":0,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"spawning pool",
            "buildtime":63
        },
        "adrenal glands research":{
            "no":1,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"spawning pool",
            "buildtime":63,
            "requirements":"hive"
        },
        "melee attacks level 1":{
            "no":2,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"evolution chamber",
            "buildtime":168
        },
        "melee attacks level 2":{
            "no":3,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"evolution chamber",
            "buildtime":180,
            "required":["lair","melee attacks level 1"]
        },
        "melee attacks level 3":{
            "no":4,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"evolution chamber",
            "buildtime":193,
            "required":["hive","melee attacks level 2"]
        },
        "burrow research":{
            "no":5,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":["hatchery","lair","hive"],
            "buildtime":50
        },
        "muscular augments research":{
            "no":6,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"hydralisk den",
            "buildtime":63
        },
        "missile attacks level 1":{
            "no":7,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"evolution chamber",
            "buildtime":168
        },
        "missile attacks level 2":{
            "no":8,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"evolution chamber",
            "buildtime":180,
            "required":["lair","missile attacks level 1"]
        },
        "missile attacks level 3":{
            "no":9,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"evolution chamber",
            "buildtime":193,
            "required":["hive","missile attacks level 2"]
        },
        "grooved spines research":{
            "no":10,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"hydralisk den",
            "buildtime":63
        },
        "lurker aspect research":{
            "no":11,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"hydralisk den",
            "buildtime":76
        },
        "ground carapace level 1":{
            "no":12,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"evolution chamber",
            "buildtime":168
        },
        "ground carapace level 2":{
            "no":13,
            "race":"zergBW",
            "mineral":225,
            "gas":225,
            "buildfrom":"evolution chamber",
            "buildtime":180,
            "required":["lair","ground carapace level 1"]
        },
        "ground carapace level 3":{
            "no":14,
            "race":"zergBW",
            "mineral":300,
            "gas":300,
            "buildfrom":"evolution chamber",
            "buildtime":193,
            "required":["hive","ground carapace level 2"]
        },
        "anabolic synthesis research":{
            "no":15,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"ultralisk cavern",
            "buildtime":84
        },
        "chitinous plating research":{
            "no":16,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"ultralisk cavern",
            "buildtime":84
        },
        "flyer attacks level 1":{
            "no":17,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"spire",
            "buildtime":168
        },
        "flyer attacks level 2":{
            "no":18,
            "race":"zergBW",
            "mineral":175,
            "gas":175,
            "buildfrom":"spire",
            "buildtime":180,
            "required":["flyer attacks level 1","lair"]
        },
        "flyer attacks level 3":{
            "no":19,
            "race":"zergBW",
            "mineral":250,
            "gas":250,
            "buildfrom":"spire",
            "buildtime":193,
            "required":["flyer attacks level 2","hive"]
        },
        "consume research":{
            "no":20,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"defiler mound",
            "buildtime":63
        },
		"plague research":{
            "no":21,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "buildfrom":"defiler mound",
            "buildtime":63
        },
		"flyer carapace level 1":{
            "no":22,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"spire",
            "buildtime":168
        },
        "flyer carapace level 2":{
            "no":23,
            "race":"zergBW",
            "mineral":225,
            "gas":225,
            "buildfrom":"spire",
            "buildtime":180,
            "required":["lair","flyer carapace level 1"]
        },
        "flyer carapace level 3":{
            "no":24,
            "race":"zergBW",
            "mineral":300,
            "gas":300,
            "buildfrom":"spire",
            "buildtime":193,
            "required":["hive","flyer carapace level 2"]
        },
		"metasynaptic node research":{
            "no":25,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"defiler mound",
            "buildtime":105
        },
		"ventral sacs research":{
            "no":26,
            "race":"zergBW",
            "mineral":200,
            "gas":200,
            "buildfrom":["lair","hive"],
            "buildtime":101
        },
		"antennae research":{
            "no":27,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":["lair","hive"],
            "buildtime":84
        },
		"pneumatized carapace research":{
            "no":28,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":["lair","hive"],
            "buildtime":84
        },
        "ensnare research":{
            "no":28,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"queens nest",
            "buildtime":50
        },
        "spawn broodling research":{
            "no":28,
            "race":"zergBW",
            "mineral":100,
            "gas":100,
            "buildfrom":"queens nest",
            "buildtime":50
        },
        "gamete meiosis research":{
            "no":28,
            "race":"zergBW",
            "mineral":150,
            "gas":150,
            "buildfrom":"queens nest",
            "buildtime":105
        },
    }
}
}
