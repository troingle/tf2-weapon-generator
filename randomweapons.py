import random
count1 = 0
count2 = 0

weapon_types = ["primary", "secondary", "melee",]
classes = ["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy", ]

positive_percentage = ["damage bonus", "clip size", "faster firing speed", "max overheal", "faster move speed on wearer",
                       "damage vs buildings", "damage vs players", "less damage from melee sources", "less damage from ranged sources", "less damage vulnerability"]

negative_percentage = ["damage penalty", "clip size", "slower firing speed", "max overheal", "slower move speed on wearer",
                       "damage vs buildings", "damage vs players", "more damage from melee sources", "more damage from ranged sources", "more damage vulnerability"]

crits_on_players = ["100% critical hits on burning players", "100% critical hits on wet players",]
negative_normal = ["No random critical hits"]

on_kill_effects = ["Gain a temporary speed boost", "Become crit-boosted for " + str(random.randint(1,10)) + " seconds", "Gain " + str(random.randint(1,100)) + "% of health", "Gain mini-crits for " + str(random.randint(1,10)) + " seconds", "Drop a mini-healthpack", "Drop a medium healthpack", "Drop a large healthpack", "Absorbs the health from your victim"]
on_hit_effects = ["Force enemy to laugh", "Slow enemy down", "Gain a temporary speed boost", "Target becomes Marked-for-death"]

print("A new " + random.choice(weapon_types) + " for the " + random.choice(classes))
print("")

positive_num = random.randint(1,2)
negative_num = random.randint(1,2)

while count1 < positive_num:
    rand = random.randint(1,9)
    if rand <= 5:
        print("+" + str(random.randint(1,10) * 10) + "% " + random.choice(positive_percentage))
    elif rand == 6:
        print("On kill: " + random.choice(on_kill_effects))
    elif rand == 7:
        print("On hit: " + random.choice(on_hit_effects))
    else:
        print(random.choice(crits_on_players))
    count1 += 1

while count2 < negative_num:
    rand = random.randint(1, 5)
    if rand <= 5:
        print("-" + str(random.randint(1, 10) * 10) + "% " + random.choice(negative_percentage))
    count2 += 1