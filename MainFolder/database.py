import sqlite3, random

CONNECTION = sqlite3.connect('data/starWars.db')
CURSOR = CONNECTION.cursor()
TAKED_HERO = set()  # список с использоваными героями


def full_hero(name=0):  # эта и следующая функция берут информацию про героя из бд
    if name:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, bonus_hp, bonus_damage, bonus_armour, photo FROM hero WHERE (name = ?)',
                                (name,)).fetchone()
    else:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, bonus_hp, bonus_damage, bonus_armour, photo FROM hero WHERE (id = ?)',
                                (random.randint(1, 29),)).fetchone()
    return person


def take_hero(name=0):
    if name:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, org, photo FROM hero WHERE (name = ?)',
                                (name, )).fetchone()
    else:
        person = CURSOR.execute('SELECT name, hp, dmg, arm, org, photo FROM hero WHERE (id = ?)',
                                (random.randint(1, 29),)).fetchone()
    return person


def take_planet(number):  # берет карту уровней из бд
    return CURSOR.execute(f"""SELECT * FROM level{number}""").fetchall()



