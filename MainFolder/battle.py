import random


class Battle:  # Класс боя в котором происходит просчёты и реализация пошагового боя
    def __init__(self, tuple):
        self.lst1, self.lst2 = tuple[0].get_lst(), tuple[1].get_lst()
        self.gr1, self.gr2 = tuple
        lst = list()
        for i in self.lst1:
            lst.append(i.get_hpDmgArmour())
        self.lst1 = lst.copy()
        lst.clear()
        for i in self.lst2:
            lst.append(i.get_hpDmgArmour())
        self.lst2 = lst.copy()
        self.result = None

    def next(self):
        if self.result is None:
            for i in range(0, len(self.lst1)):
                index = random.randint(0, len(self.lst2) - 1)
                hp1, dmg1, armour1 = self.lst1[i]
                hp2, dmg2, armour2 = self.lst2[index]
                if hp1 <= 0:
                    continue
                if hp2 <= 0:
                    continue
                if random.randint(0, 100) in range(0, 90):
                    hp2 -= dmg1 - int(dmg1 * (armour2 / (armour2 + 10 * dmg1)))
                    self.lst2[index] = hp2, dmg2, armour2
                if hp2 <= 0:
                    continue
                if random.randint(0, 100) in range(0, 90):
                    hp1 -= dmg2 - int(dmg2 * (armour1 / (armour1 + 10 * dmg2)))
                    self.lst1[i] = (hp1, dmg1, armour1)
            n = 0
            while True:
                if self.lst1[n][0] <= 0:
                    self.lst1.remove(self.lst1[n])
                    n = -1
                n += 1
                if n == len(self.lst1):
                    break
            n = 0
            while True:
                if self.lst2[n][0] <= 0:
                    self.lst2.remove(self.lst2[n])
                    n = -1
                n += 1
                if n == len(self.lst2):
                    break
            n2 = 0
            for i in self.lst2:
                if i[0] < 0:
                    n2 += 1
            n1 = 0
            for i in self.lst1:
                if i[0] < 0:
                    n1 += 1
            if n2 == len(self.lst2):
                self.result = True
            elif n1 == len(self.lst1):
                self.result = False
        else:
            self.get_result()

    def get_result(self):
        return self.result