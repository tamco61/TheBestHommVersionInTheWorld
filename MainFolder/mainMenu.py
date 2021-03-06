import pygame, random
from MainFolder import dop_func, database, mainField
from UnitClasses.defaultUnit import groupMain
from UnitClasses import defaultUnit

pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
running = True
FPS = 10
clock = pygame.time.Clock()
WIDTH, HEIGHT = screen.get_width(), screen.get_height()
pygame.mixer.music.load('data/mus1.mp3')
flag_click = [False, False, None]


class Button:  # класс для создания кнопок
    def __init__(self, width, height, inactive_color=(150, 150, 150), active_color=(0, 0, 0), text_size=50,
                 font_type='cosm.ttf'):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text_size = text_size
        self.font_type = font_type
        self.action = None

    def draw(self, x, y, text, action=None, param_action=None, color='white'):  # рисует кнопку
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        naved = pygame.mixer.Sound('data/naved.wav')
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))
                global flag_click
                if click[0] == 1:
                    pygame.mixer.Sound.play(naved)
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        elif action == 'battle':
                            param_action.next()
                        elif action == 'set_captain':
                            set_captain(param_action[0], param_action[1])
                        elif action == 'return':
                            self.action = True
                            mainField.pause(True)
                        elif action == dop_func.save_game:
                            dop_func.save_game(param_action)
                            self.action = True
                            mainField.pause(True)
                        elif action == 'change_hero':
                            flag_click[0] = True
                            if flag_click[0] and flag_click[1]:
                                mainField.change_hero(param_action, flag_click[2])
                                flag_click = [False, False, None]
                            else:
                                flag_click = [True, False, param_action]
                        elif action == 'change':
                            flag_click[1] = True
                            if flag_click[0] and flag_click[1]:
                                mainField.change_hero(flag_click[2], param_action)
                                flag_click = [False, False, None]
                            else:
                                flag_click = [False, True, param_action]
                        elif action == 'quit':
                            self.action = True
                        else:
                            if param_action:
                                action(param_action)
                                return
                            action()
                            return
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))
        dop_func.print_text(screen, text, x + 10, y + 15, font_size=self.text_size, font_type=self.font_type, color=color)

    def ret(self):  # возвращает результат действия
        return self.action


def set_captain(name, LEVEL=1):
    # переход к основному игровому полю
    if LEVEL > 5:
        database.TAKED_HERO.append(name)
    else:
        name, hp, damage, armour, bonus_hp, bonus_damage, bonus_armour, photo = list(database.full_hero(name))
        hero = defaultUnit.HeroUnit(name, hp, damage, armour, groupMain, bonus_hp, bonus_damage, bonus_armour, photo)
        groupMain.append_hero(hero)

    mainField.run_cycle(groupMain.lst[0].name, LEVEL)
    return


def draw_stat(lst, lst1):  # вывод стат
    dop_func.print_text(screen, lst[0], lst1[1][0] + WIDTH // 20, lst1[1][1] + HEIGHT // 6, font_size=25, color='black',
                        font_type='stat.ttf')
    dop_func.print_text(screen, f'Hit Point {lst[1]}', lst1[1][0] + WIDTH // 20, lst1[1][1] + HEIGHT // 6 + 35,
                        font_size=25, color='black', font_type='stat.ttf')
    dop_func.print_text(screen, f'Damage {lst[2]}', lst1[1][0] + WIDTH // 20, lst1[1][1] + HEIGHT // 6 + 70,
                        font_size=25, color='black', font_type='stat.ttf')
    dop_func.print_text(screen, f'Armour {lst[3]}', lst1[1][0] + WIDTH // 20, lst1[1][1] + HEIGHT // 6 + 105,
                        font_size=25, color='black', font_type='stat.ttf')
    dop_func.print_text(screen, f'{lst[4]}', lst1[1][0] + WIDTH // 20, lst1[1][1] + HEIGHT // 6 + 140,
                        font_size=25, color='black', font_type='stat.ttf')


def menu():  # стартовое меню
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'),
                                 (WIDTH, HEIGHT))
    start_game = Button(350, 80)
    quit_button = Button(225, 80)
    resume_game = Button(350, 80, text_size=45)
    counter_sec = 0
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
        counter_sec += 1
        if counter_sec == 40:  # смена фона
            fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'),
                                         (WIDTH, HEIGHT))
            counter_sec = 0
        screen.blit(fon, (0, 0))
        if dop_func.check_save():  # если есть сейвы то одна кнопка, если нет, то другая
            start_game.draw(WIDTH // 2 - start_game.width // 2,
                            HEIGHT // 4 * 2.5 - 300, 'Новая игра', start)
            resume_game.draw(WIDTH // 2 - start_game.width // 2,
                             HEIGHT // 4 * 2.5 - 200, 'Продолжить', mainField.resume)
        else:
            start_game.draw(WIDTH // 2 - start_game.width // 2,
                            HEIGHT // 4 * 2.5 - 200, 'Новая игра', start)
        quit_button.draw(WIDTH // 2 - quit_button.width // 2, HEIGHT // 4 * 2.5 - 100,
                         'Выйти', quit)
        pygame.display.flip()
        clock.tick(FPS)


def start():
    f = open('save/save1.json', 'w')
    f.write('{}')
    f.close()
    database.TAKED_HERO.clear()
    groupMain.lst.clear()
    choose_captain()


def choose_captain(LEVEL=1):  # выбор капитана, очень много костылей, лучше не смотреть код
    background = pygame.transform.scale(dop_func.load_image(f'board.jpg'),
                                 (WIDTH, HEIGHT))
    heroes = set()
    while len(heroes) != 5:
        hero = database.take_hero()
        if hero[0] in database.TAKED_HERO or hero[0] in list(map(lambda x: x.name, defaultUnit.groupMain.get_lst())):
            continue
        heroes.add(hero)
    heroes = list(heroes)
    image0 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[0][-1]),
                                    (5 * WIDTH // 26, HEIGHT // 2))
    image1 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[1][-1]),
                                    (5 * WIDTH // 26, HEIGHT // 2))
    image2 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[2][-1]),
                                    (5 * WIDTH // 26, HEIGHT // 2))
    image3 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[3][-1]),
                                    (5 * WIDTH // 26, HEIGHT // 2))
    image4 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[4][-1]),
                                    (5 * WIDTH // 26, HEIGHT // 2))
    dct_names = {0: [heroes[0][0]], 1: [heroes[1][0]], 2: [heroes[2][0]], 3: [heroes[3][0]], 4: [heroes[4][0]]}
    choose = Button(185, 65, text_size=30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
        screen.fill((255, 255, 255))
        dop_func.print_text(screen, 'Выберите героя', (2 * WIDTH) // 6, HEIGHT // 8, color='black')
        for i in range(0, 5):
            choose.draw(3 * WIDTH // 30 + i * WIDTH // 6, 3 * HEIGHT // 4, "Выбрать",
                        "set_captain", (dct_names[i][0], LEVEL))
            if len(dct_names[i]) == 1:
                dct_names[i] = [dct_names[i][0], (3 * WIDTH // 50 + 8 * i * image0.get_width() // 9,
                                                  HEIGHT // 5),
                                (3 * WIDTH // 50 + 8 * i * image0.get_width() // 9 + image0.get_width(),
                                 HEIGHT // 5 + HEIGHT // 2), False]
            if dct_names[i][-1] is False:
                dct_names[i] = [dct_names[i][0], (3 * WIDTH // 50 + 8 * i * image0.get_width() // 9,
                                                  HEIGHT // 5),
                                (3 * WIDTH // 50 + 8 * i * image0.get_width() // 9 + image0.get_width(),
                                 HEIGHT // 5 + HEIGHT // 2), False]
                screen.blit(locals()['image%s' % i], (3 * WIDTH // 50 + 8 * i * image0.get_width() // 9, HEIGHT // 5))
            else:
                dct_names[i] = [dct_names[i][0], (3 * WIDTH // 50 + 8 * i * image0.get_width() // 9,
                                                  HEIGHT // 5),
                                (3 * WIDTH // 50 + 8 * i * image0.get_width() // 9 + image0.get_width(),
                                 HEIGHT // 5 + HEIGHT // 2), True]
                draw_stat(heroes[i], dct_names[i])
            if dct_names[i][1][0] <= pygame.mouse.get_pos()[0] <= dct_names[i][2][0] and\
                    dct_names[i][1][1] <= pygame.mouse.get_pos()[1] <= dct_names[i][2][1] and pygame.mouse.get_pressed()[0]:
                dct_names[i][-1] = not dct_names[i][-1]
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    menu()