import random


def battle(tuple):  # производит рассчет боя
    lst1, lst2 = tuple[0].get_lst(), tuple[1].get_lst()
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
            index = random.randint(0, len(lst2) - 1)
            hp1, dmg1, armour1 = lst1[i]
            hp2, dmg2, armour2 = lst2[index]
            if hp1 <= 0:
                continue
            if hp2 <= 0:
                continue
            if random.randint(0, 100) in range(0, 90):
                hp2 -= dmg1 - int(dmg1 * (armour2 / (armour2 + 10 * dmg1)))
                lst2[index] = hp2, dmg2, armour2
            if hp2 <= 0:
                continue
            if random.randint(0, 100) in range(0, 90):
                hp1 -= dmg2 - int(dmg2 * (armour1 / (armour1 + 10 * dmg2)))
                lst1[i] = (hp1, dmg1, armour1)
        n2 = 0
        for i in lst2:
            if i[0] < 0:
                n2 += 1
        n1 = 0
        for i in lst1:
            if i[0] < 0:
                n1 += 1
        if n2 == len(lst2):
            return True
        elif n1 == len(lst1):
            return False