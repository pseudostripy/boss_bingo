import random

FarmWep = open('ds2_farming_weapons.txt', 'r')
PostWep = open('ds2_postshrine_weapons.txt', 'r')
PreWep = open('ds2_preshrine_weapons.txt', 'r')
TortWep = open('ds2_torture_weapons.txt', 'r')
PostSpell = open('ds2_postshrine_spells.txt', 'r')
PreSpell = open('ds2_preshrine_spells.txt', 'r')
TortSpell = open('ds2_torture_spells.txt', 'r')
PreBoss = open('ds2_preshrine_bosses.txt', 'r')
PostBoss = open('ds2_postshrine_bosses.txt', 'r')
DlcBoss = open('ds2_dlc_bosses.txt', 'r')

IncFarmWep = input("include farming weapons? (y/n))").lower()
IncPostWep = input("include post shrine weapons? (y/n))").lower()
IncTortWep = input("include torture weapons? (y/n))").lower()

IncPreSpell = input("include spells? (y/n))").lower()
IncPostSpell = input("include post shrine spells? (y/n))").lower()
IncTortSpell = input("include torture spells? (y/n))").lower()

IncPostBoss = input("include post shrine bosses? (y/n))").lower()
IncDlcBoss = input("include dlc bosses? (y/n))").lower()

wep = []

for i in PreWep.readlines():
    wep.append(i[:-1])
if IncFarmWep == "y":
    for i in FarmWep.readlines():
        wep.append(i[:-1])
if IncTortWep == "y":
    for i in TortWep.readlines():
        wep.append(i[:-1])
if IncTortWep == "y":
    for i in TortWep.readlines():
        wep.append(i[:-1])
if IncPreSpell == "y":
    for i in PreSpell.readlines():
        wep.append(i[:-1])
if IncPostSpell == "y":
    for i in PostSpell.readlines():
        wep.append(i[:-1])
if IncTortSpell == "y":
    for i in TortSpell.readlines():
        wep.append(i[:-1])

boss = []

for i in PreBoss.readlines():
    boss.append(i[:-1])
if IncPostBoss == "y":
    for i in PostBoss.readlines():
        boss.append(i[:-1])
if IncDlcBoss == "y":
    for i in DlcBoss.readlines():
        boss.append(i[:-1])
to_out = "["
for i in range(24):
    random.shuffle(wep)
    random.shuffle(boss)
    to_out = to_out + '{"name" : "kill "' + boss[0] + ' with ' + wep[0] + '"},'
random.shuffle(wep)
random.shuffle(boss)
to_out = to_out + '{"name" : "kill "' + boss[0] + ' with ' + wep[0] + '"}]'
print(to_out)
