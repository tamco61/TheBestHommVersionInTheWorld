import pygame, sys, os


def terminate():  # при вызове функции игра завершается
    pygame.quit()
    sys.exit()


def load_level(filename):  # функция для загрузки уровней
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name, colorkey=None):  # функция для загрузки изображений

    image = pygame.image.load('data/' + name).convert()
    if colorkey is not None:  # проверка на прозрачный фон
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
# вернем игрока, а также размер поля в клетках
    return new_player, x, y


def check_save():  # проверяет есть ли сохраненные игры
    pass