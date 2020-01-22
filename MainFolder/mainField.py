import pygame
from MainFolder import dop_func
from MainFolder import database
from UnitClasses import defaultUnit
from MainFolder.battle import Battle
from MainFolder import mainMenu
from UnitClasses.defaultUnit import groupMain


pygame.init()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_width(), screen.get_height()
FPS = 20
lst_planet = 0


# Интерфейс перед боем
def battleUI(planet=None, flag=False, res=None):
    global screen
    if flag:
        return res
    battle = Battle((groupMain, planet.get_group()))
    fon = pygame.transform.scale(dop_func.load_image('fone.jpg'), (WIDTH, HEIGHT))
    start_but = mainMenu.Button(105, 75, font_type='stat.ttf')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
        screen.blit(fon, (0, 0))
        not_ours_lst = battle.lst2
        our_lst = battle.lst1
        hp, damage, armour = 0, 0, 0
        for i in range(len(our_lst)):
            hpp, dmgg, armrr = our_lst[i][0], our_lst[i][1], our_lst[i][2]
            if hpp < 0:
                hpp = 0
            dop_func.print_text(screen, 'Ваши герои', WIDTH // 15, HEIGHT // 20, font_type='stat.ttf', font_size=60)
            dop_func.print_text(screen, f'{battle.gr1.get_lst()[i].name} HP {hpp} DMG {dmgg} ARM '
                                        f'{armrr}', WIDTH // 15, i * HEIGHT // 10 + HEIGHT // 5,
                                font_type='stat.ttf', font_size=35)
            dop_func.print_text(screen, 'Общие статы', WIDTH // 15, HEIGHT // 2 + HEIGHT // 8, font_type='stat.ttf',
                                font_size=45)
            hp += int(hpp)
            damage += int(dmgg)
            armour += int(armrr)
        dop_func.print_text(screen, f'HP {hp} DMG {damage} ARM {armour}', WIDTH // 15, HEIGHT // 2 + HEIGHT // 6,
                            font_type='stat.ttf',
                            font_size=35)
        hp, damage, armour = 0, 0, 0
        for i in range(len(not_ours_lst)):
            hpp, dmgg, armrr = not_ours_lst[i][0], not_ours_lst[i][1], not_ours_lst[i][2]
            if hpp < 0:
                hpp = 0
            dop_func.print_text(screen, 'Герои противника', WIDTH // 2, HEIGHT // 20, font_type='stat.ttf', font_size=60)
            dop_func.print_text(screen,
                                f'{battle.gr2.get_lst()[i].name} HP {hpp} DMG {dmgg} ARM '
                                f'{armrr}',
                                WIDTH // 2, i * HEIGHT // 10 + HEIGHT // 5, font_type='stat.ttf', font_size=35)
            dop_func.print_text(screen, 'Общие статы', WIDTH // 2, HEIGHT // 2 + HEIGHT // 8, font_type='stat.ttf',
                                font_size=45)
            hp += int(hpp)
            damage += int(dmgg)
            armour += int(armrr)
        dop_func.print_text(screen, f'HP {hp} DMG {damage} ARM {armour}', WIDTH // 2, HEIGHT // 2 + HEIGHT // 6,
                                font_type='stat.ttf',
                                font_size=35)
        start_but.draw(WIDTH // 2 - start_but.width // 2, HEIGHT // 2 + HEIGHT // 3, "Ход", 'battle', battle)
        pygame.display.flip()
        if battle.get_result() is not None:
            return battle.get_result()


class Planet:  # класс для создания планет
    def __init__(self, id, x, y, lvl):
        self.id = id
        self.lvl = lvl
        self.x = x
        self.y = y
        self.status = False
        self.group = self.get_group()

    def set_status(self, status):  # устанавливает, захвачена планета или нет
        self.status = status

    def get_group(self):  # возвращает группу с планеты
        group = defaultUnit.Group('sec')
        for i in range(self.lvl):
            while True:
                person = database.full_hero()
                if person[0] not in database.TAKED_HERO:
                    break
            name, hp, damage, armour, bonus_hp, bonus_damage, bonus_armour, photo = person
            hero = defaultUnit.HeroUnit(name, hp, damage, armour, group, bonus_hp, bonus_damage, bonus_armour, photo)
            group.append_hero(hero)
        self.group = group
        return group

    def get_status(self):  # возвращет статус планеты
        return self.status


class SpaceShip:  # класс корабля
    def __init__(self, size):
        self.size = size
        self.x0, self.y0 = 0, 0
        self.x1, self.y1 = 0, 0
        self.image = pygame.transform.scale(dop_func.load_image('ship.png', (255, 255, 255)), (size, size))
        self.image = pygame.transform.flip(self.image, 1, 0)

    def return_image(self):
        return self.image

    def move(self, cell):  # изменяет координаты коробля
        self.x1, self.y1 = cell


class Board:  # класс для создания игрового поля
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.ship = SpaceShip(self.cell_size - 2)

        # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.ship = SpaceShip(self.cell_size - 2)

    def render(self):  # отображает игровое поле
        global screen

        for i in range(self.width):
            for r in range(self.height):
                pygame.draw.polygon(screen, (255, 255, 255, 255), [(self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * (r + 1)),
                                                                   (self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * (r + 1))], 1)
        screen.blit(self.ship.return_image(),
                    (self.left + self.cell_size * self.ship.x1 + 1, self.top + self.cell_size * self.ship.y1 + 1))
        screen.blit(pygame.transform.scale(dop_func.load_image('next.jpg', (255, 255, 255)), (self.cell_size, self.cell_size)),
                    (self.left + self.cell_size * 15 + 1, self.top + self.cell_size * 7 + 1))
        return

    def get_cell(self, mouse_pos):  # возвращает клетку
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        if x in range(0, self.width * self.cell_size) and y in range(0, self.height * self.cell_size):
            x0 = x // self.cell_size
            y0 = y // self.cell_size
            return x0, y0
        return None

    def on_click(self, cell):  # передвигает корабль
        self.ship.move(cell)

    def get_click(self, mouse_pos):  # производит действие по клику
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


def congratulations(flag):  # выводит результат битвы
    fon = pygame.transform.scale(dop_func.load_image('battle_fon.jpg'), (WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        screen.blit(fon, (0, 0))
        if flag:
            dop_func.print_text(screen, "Вы победили", WIDTH // 2 - WIDTH // 13, HEIGHT // 2 - HEIGHT // 15)
        else:
            dop_func.print_text(screen, "Вы проиграли", WIDTH // 2 - WIDTH // 13, HEIGHT // 2 - HEIGHT // 15)
        pygame.display.flip()


def resume():
    loaded = dop_func.load_game()
    level = int(list(loaded['planets'].keys())[0])
    database.TAKED_HERO.clear()
    groupMain.lst.clear()
    for i in loaded['heroes']:
        database.TAKED_HERO.append(i)
        name, hp, damage, armour, bonus_hp, bonus_damage, bonus_armour, photo = list(database.full_hero(i))
        hero = defaultUnit.HeroUnit(name, hp, damage, armour, groupMain, bonus_hp, bonus_damage, bonus_armour, photo)
        groupMain.append_hero(hero)
    planets = [Planet(i[0], i[1], i[2], level) for i in database.take_planet(level)]
    for i in planets:
        for j in loaded['planets'][str(level)]:
            if int(list(j.keys())[0]) == i.id:
                i.set_status(list(j.values())[0])
    run_cycle(groupMain.lst[0], level, planets)


def change_hero(hero1, hero2):
    index = 0
    for i in groupMain.lst:
        if i.name == hero2:
            index = groupMain.lst.index(i)
            break
    groupMain.lst.pop(index)
    index1 = database.TAKED_HERO.index(hero1)
    name, hp, damage, armour, bonus_hp, bonus_damage, bonus_armour, photo = list(database.full_hero(hero1))
    hero = defaultUnit.HeroUnit(name, hp, damage, armour, groupMain, bonus_hp, bonus_damage, bonus_armour, photo)
    groupMain.lst.insert(index, hero)
    database.TAKED_HERO.insert(index1, hero2)


def change():
    pers = mainMenu.Button(250, 75, text_size=30, inactive_color=(255, 255, 255), active_color=(255, 255, 255),
                           font_type='stat.ttf')
    stock = mainMenu.Button(250, 75, text_size=30, inactive_color=(255, 255, 255), active_color=(255, 255, 255),
                            font_type='stat.ttf')
    quit = mainMenu.Button(225, 75)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x in range(int(WIDTH // 2 - quit.width // 2), int(WIDTH // 2 + quit.width // 2)):
                    if y in range(int(HEIGHT // 2 + HEIGHT // 3),
                                  (HEIGHT // 2 + HEIGHT // 3 + quit.height)):
                        quit.draw(WIDTH // 2 - quit.width // 2, HEIGHT // 2 + HEIGHT // 3, 'Выйти', 'quit')
                        return quit.ret()
        screen.fill((255, 255, 255))
        dop_func.print_text(screen, 'Команда', WIDTH // 15, HEIGHT // 20, font_type='stat.ttf', font_size=60,
                            color='black')
        dop_func.print_text(screen, 'Все герои', WIDTH // 2, HEIGHT // 20, font_type='stat.ttf', font_size=60,
                            color='black')
        taked = groupMain.lst
        lineup = database.TAKED_HERO
        hp = 0
        damage = 0
        armour = 0
        for i in lineup:
            for j in taked:
                if i == j.name:
                    lineup.remove(i)
        for i in range(len(taked)):
            pers.draw(WIDTH // 15, i * HEIGHT // 13 + HEIGHT // 5, f'{taked[i].name}', color='black',
                      action='change', param_action=taked[i].name)
            hp += int(taked[i].hp)
            damage += int(taked[i].dmg)
            armour += int(taked[i].armour)
        for i in range(len(lineup)):
            stock.draw(WIDTH // 2, i * HEIGHT // 15 + HEIGHT // 5, f'{lineup[i]}', color='black', action='change_hero',
                       param_action=lineup[i])
        dop_func.print_text(screen, 'Общие статы', WIDTH // 15, HEIGHT // 2 + HEIGHT // 8, font_type='stat.ttf',
                            font_size=40, color='black')
        dop_func.print_text(screen, f'HP {hp} DMG {damage} ARM {armour}', WIDTH // 15, HEIGHT // 2 + HEIGHT // 6,
                            font_type='stat.ttf',
                            font_size=30,
                            color='black')
        quit.draw(WIDTH // 2 - quit.width // 2, HEIGHT // 2 + HEIGHT // 3, 'Выйти', 'quit')
        pygame.display.flip()


def pause(ret=False):  # создает паузу при нажати esc
    global lst_planet, lvl
    cont = mainMenu.Button(315, 70, text_size=40)
    save_game = mainMenu.Button(280, 70, text_size=40)
    change_team = mainMenu.Button(225, 70, text_size=40)
    exit_game = mainMenu.Button(220, 70, text_size=40)
    fon = pygame.transform.scale(dop_func.load_image('pause.jpg'), (WIDTH, HEIGHT))
    if ret:
        return True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x in range(WIDTH // 2 - cont.width // 2, WIDTH // 2 + cont.width // 2):
                    if y in range(int(HEIGHT // 2.5), int(HEIGHT // 2.5) + cont.height):
                        cont.draw(WIDTH // 2 - cont.width // 2, HEIGHT // 2 + HEIGHT // 3, "Начать игру", 'return')
                        return cont.ret()
                    elif y in range(int(HEIGHT // 2.5 + cont.height + 10), int(HEIGHT // 2.5 + 2 * cont.height + 10)):
                        save_game.draw(WIDTH // 2 - save_game.width // 2, HEIGHT // 2.5 + cont.height + 10, 'Сохранить',
                                       dop_func.save_game, (lst_planet, lvl))
                        return save_game.ret()

        screen.blit(fon, (0, 0))
        cont.draw(WIDTH // 2 - cont.width // 2, HEIGHT // 2.5, 'Продолжить', 'return')
        save_game.draw(WIDTH // 2 - save_game.width // 2, HEIGHT // 2.5 + cont.height + 10, 'Сохранить', dop_func.save_game, (lst_planet, lvl))
        change_team.draw(WIDTH // 2 - change_team.width // 2, HEIGHT // 2.5 + 2 * cont.height + 2 * 10, 'Команда', change)
        exit_game.draw(WIDTH // 2 - exit_game.width // 2, HEIGHT // 2.5 + 3 * cont.height + 3 * 10, ' Выйти',
                       action=mainMenu.menu)
        pygame.display.flip()


def draw_level(number, board):  # рисует уровень
    global screen

    lst_planet = database.take_planet(number)

    for i in lst_planet:
        id, x, y = i
        image = pygame.transform.scale(dop_func.load_image(f'planet/{id}.jpg', (255, 255, 255)), (board.cell_size, board.cell_size))
        screen.blit(image, (board.left + board.cell_size * x + 1, board.top + board.cell_size * y + 1))

    return lst_planet


def run_cycle(captain_name, LEVEL=1, planets=None):  # основной цикл
    if len(groupMain.lst) != LEVEL:
        groupMain.lst.clear()
    if groupMain.lst == list():
        name, hp, damage, armour, bonus_hp, bonus_damage, bonus_armour, photo = list(database.full_hero(captain_name))
        hero = defaultUnit.HeroUnit(name, hp, damage, armour, groupMain, bonus_hp, bonus_damage, bonus_armour, photo)
        groupMain.append_hero(hero)

    board = Board(16, 8)
    global lst_planet, lvl
    if planets:
        lst_planet = planets
    else:
        lst_planet = [Planet(i[0], i[1], i[2], LEVEL) for i in database.take_planet(LEVEL)]
    lvl = LEVEL
    cell_s = WIDTH // 16 - 1
    board.set_view((WIDTH - cell_s * 16) // 2, (HEIGHT - cell_s * 8) // 2, WIDTH // 16 - 1)
    fon = pygame.transform.scale(dop_func.load_image('Space.jpg'), (WIDTH, HEIGHT))
    flag = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = board.get_cell(event.pos)
                if cell is None:
                    break
                x, y = cell

                if x == 15 and y == 7:
                    if LEVEL < 9:
                        stat = True
                        for i in lst_planet:
                            if not i.get_status():
                                stat = False
                        if stat:
                            return mainMenu.choose_captain(LEVEL + 1)
                    break
                flag = True
                for i in range(len(lst_planet)):
                    if lst_planet[i].x == x and lst_planet[i].y == y:
                        if lst_planet[i].get_status() is False:
                            board.get_click(event.pos)
                            if battleUI(lst_planet[i]):
                                lst_planet[i].set_status(True)
                                congratulations(True)
                            else:
                                congratulations(False)
                        else:
                            flag = False
                            break
                if flag:
                    board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and event.key == 27:
                pause()
        screen.blit(fon, (0, 0))
        draw_level(LEVEL, board)
        board.render()
        if flag is False:
            dop_func.print_text(screen, 'Планета уже захвачена', WIDTH // 2 - WIDTH // 5, HEIGHT // 2 - HEIGHT // 20)
        pygame.display.flip()


