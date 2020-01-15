import pygame, sys


def terminate():  # при вызове функции игра завершается
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):  # функция для загрузки изображений

    image = pygame.image.load('data/' + name).convert()
    if colorkey is not None:  # проверка на прозрачный фон
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def check_save():  # проверяет есть ли сохраненные игры
    pass


def print_text(screen, text, x, y, font_size=50, font_type='cosm.ttf', color='white'):  # функция для вывода текста
    font_type = pygame.font.Font(f"data/{font_type}", font_size)
    mes = font_type.render(text, 1, pygame.Color(color))
    screen.blit(mes, (x, y))