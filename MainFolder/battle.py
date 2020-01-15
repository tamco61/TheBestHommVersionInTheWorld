import random


def battle(group1, group2):
    lst1, lst2 = group1.lst, group2.lst
    lst = list()
    for i in lst1:
        lst.append(i.get_hpDmgArmour())
    lst1 = lst.copy()
    lst.clear()
    for i in lst2:
        lst.append(i.get_hpDmgArmour())
    lst2 = lst.copy()
    while True:
        for i in range(0, len(lst1)):
            hp1, dmg1, armour1 = lst1[i]
            hp2, dmg2, armour2 = lst2[random.randint(0, len(lst2) - 1)]
            if hp1 <= 0:
                continue
            if hp2 <= 0 and random.randint(0, 100) in range(0, 86):
                continue
            hp2 -= int(dmg1 * (armour2 / (armour2 + 10 * dmg1)))
            if hp2 <= 0 and random.randint(0, 100) in range(0, 86):
                continue
            hp1 -= int(dmg2 * (armour1 / (armour1 + 10 * dmg2)))

        for i in lst1:
            if i[0] > 0:
                return True

        for i in lst2:
            if i[0] > 0:
                return False