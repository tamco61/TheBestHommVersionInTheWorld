organization_lst = ['Sith', 'Neutral', 'Jedi Order']


# Базовый класс
class DefaultUnit:
    def __init__(self, hp, damage, armour, attack_speed):
        self.hp = hp
        self.dmg = damage
        self.armour = armour
        self.ats = attack_speed

    def take_damage(self, damage):
        self.hp -= int(damage * (self.armour / (self.armour + 10 * damage)))


# Базовый класс командующего
class CommanderUnit(DefaultUnit):
    def __init__(self, hp, damage, armour, attack_speed, organization=organization_lst[1], bonus_hp=0, bonus_damage=0,
                 bonus_armour=0, bonus_attack_speed=0):
        super().__init__(hp, damage, armour, attack_speed)
        self.group = list()
        self.org = organization
        self.bHP = bonus_hp
        self.bDMG = bonus_damage
        self.bARMOUR = bonus_armour
        self.bATS = bonus_attack_speed
        self.org = organization

    def take_damage(self, damage):
        self.hp -= int(damage * (self.armour / (self.armour + 10 * damage)))

    def add_group(self, unit):
        self.group.append(unit)

    def bHP(self):
        return self.bHP

    def bDMG(self):
        return self.bDMG

    def bARMOUR(self):
        return self.bARMOUR

    def bATS(self):
        return self.bATS

    def org(self):
        return self.org


# Базовый класс солдата
class SoldierUnit(DefaultUnit):
    def __init__(self, hp, damage, armour, attack_speed, organization=organization_lst[1], commander=None):
        super().__init__(hp, damage, armour, attack_speed)
        self.org = organization
        self.com = commander

    def take_damage(self, damage):
        if self.com is None:
            self.hp -= int(damage * (self.armour / (self.armour + 10 * damage)))
        else:
            self.hp = self.hp + self.com.bHP() - int(damage * ((self.armour + self.com.bARMOUR()) / ((self.armour + self.com.bARMOUR()) + 10 * damage)))

