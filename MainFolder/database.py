import sqlite3, random

CONNECTION = sqlite3.connect('data/starWars.db')
CURSOR = CONNECTION.cursor()
TAKED_HERO = set()


def full_hero(name=0):
    if name:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, bonus_hp, bonus_damage, bonus_armour, photo FROM hero WHERE (name = ?)',
                                (name,)).fetchone()
    else:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, bonus_hp, bonus_damage, bonus_armour, photo FROM hero WHERE (id = ?)',
                                (random.randint(1, 6),)).fetchone()
    return person


def take_hero(name=0):
    if name:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, org, photo FROM hero WHERE (name = ?)',
                                (name, )).fetchone()
    else:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, org, photo FROM hero WHERE (id = ?)',
                                (random.randint(1, 21),)).fetchone()
    return person


def take_planet(number):
    return CURSOR.execute(f"""SELECT * FROM level{number}""").fetchall()
