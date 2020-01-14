class Group:
    def __init__(self, name):
        self.name = name
        self.lst = list()

    def get_bonus(self, hero):
        bHP = 0
        bDMG = 0
        bARMOUR = 0
        for i in self.lst:
            if i.name() == hero.name():
                continue
            bHP += i.bHP()
            bDMG += i.bDMG()
            bARMOUR += i.bARMOUR()
        return bHP, bDMG, bDMG

    def append_hero(self, hero):
        if len(self.lst) < 5:
            self.lst.append(hero)

    def remove_hero(self, index):
        self.lst.remove(index)

    def lst(self):
        return self.lst


# Базовый класс
class DefaultUnit:
    def __init__(self, name, hp, damage, armour):
        self.name = name
        self.hp = hp
        self.dmg = damage
        self.armour = armour

    def name(self):
        return self.name


# Базовый класс героя
class HeroUnit(DefaultUnit):
    def __init__(self, name, hp, damage, armour, group, bonus_hp=0, bonus_damage=0, bonus_armour=0, photo=0):
        super().__init__(name, hp, damage, armour)
        self.group = group
        self.bHP = bonus_hp
        self.bDMG = bonus_damage
        self.bARMOUR = bonus_armour
        self.photo = photo

    def get_hpDmgArmour(self):
        h, d, a = self.group.get_bonus()
        return self.hp + h, self.dmg + d, self.armour + a
        #  self.hp -= h + int(damage * ((self.armour + a) / (self.armour + a + 10 * damage)))

    def bHP(self):
        return self.bHP

    def bDMG(self):
        return self.bDMG

    def bARMOUR(self):
        return self.bARMOUR

    def id(self):
        return self.id