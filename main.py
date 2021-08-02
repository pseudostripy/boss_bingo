import random
from configparser import ConfigParser


# function for reading the .txt files
def append_to_list(fname, inputlist):
    fh = open(fname, 'r')
    for name in fh.readlines():
        inputlist.append(name[:-1])
    return inputlist


# import user settings
config = ConfigParser()
config.read('bingoconfig.ini')

bPredrang = config.getboolean('Options', 'preshrine board')
bDLCbosses = config.getboolean('Options', 'dlc bosses')
bSpells = config.getboolean('Options', 'spells')
bFarm = config.getboolean('Options', 'farmed weapons')
bTorture = config.getboolean('Options', 'torture')
bUniqueBosses = config.getboolean('Options', 'Unique bosses')

# simple user traps:
if bTorture and bPredrang:
    print('Torture always includes post drangleic! Overriding.')
    bPredrang = False

nBingoSq = 25

# read bosses/weapons based on config
wep = []
boss = []

# preshrine:
wep = append_to_list('ds2_preshrine_weapons.txt', wep)
boss = append_to_list('ds2_preshrine_bosses.txt', boss)
if bDLCbosses:
    boss = append_to_list('ds2_preshrine_dlc_bosses.txt', boss)
if bSpells:
    wep = append_to_list('ds2_preshrine_spells.txt', wep)
# (this will fail if no dlc or post-shrine because the lists are not separated very well)
if bFarm:
    wep = append_to_list('ds2_farming_weapons.txt', wep)

# post-shrine:
if not bPredrang:
    wep = append_to_list('ds2_postshrine_weapons.txt', wep)
    boss = append_to_list('ds2_postshrine_bosses.txt', boss)

    if bDLCbosses:
        boss = append_to_list('ds2_postshrine_dlc_bosses.txt', boss)
    if bSpells:
        wep = append_to_list('ds2_postshrine_spells.txt', wep)
    if bTorture:
        wep = append_to_list('ds2_torture_weapons.txt', wep)
        if bSpells:
            wep = append_to_list('ds2_torture_spells.txt', wep)


# randomise bosses and weapons
if bUniqueBosses:
    randbosses = random.sample(boss, nBingoSq)
else:
    randbosses = random.choices(boss, k=nBingoSq)

# currently always assume unique weapons
randweapons = random.sample(wep, nBingoSq)

# open file for output:
f = open('./bingolist.txt', "w")

# main file print loop
for i in range(nBingoSq):
    if i == 0:
        f.write('[\n{"name" : "kill ' + randbosses[i] + ' with ' + randweapons[i] + '"}')
    else:
        linestr = ',\n{"name" : "kill ' + randbosses[i] + ' with ' + randweapons[i] + '"}'
        f.write(linestr)
# finish and close file
f.write("\n]\n")
f.close()
