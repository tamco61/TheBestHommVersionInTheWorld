import pygame, random, time
import dop_func
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
run = True
FPS = 2
clock = pygame.time.Clock()


def start_screen():
    intro_text = ["PRESS ANY KEY"]
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'), (screen.get_width(), screen.get_height()))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font("data/cosm.ttf", 50)
    string_rendered = font.render(intro_text[0], 1, pygame.Color('white'))
    change_text = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            elif event.type == pygame.KEYDOWN:
                menu()
                return
        screen.blit(fon, (0, 0))
        if change_text:
            screen.blit(string_rendered, (screen.get_width() // 2 - string_rendered.get_width() // 2, screen.get_height() // 4 * 3))
            change_text = False
        else:
            change_text = True
        pygame.display.flip()
        clock.tick(FPS)


def menu():
    if dop_func.check_save():
        menu_text = ['Продолжить игру', 'Выйти']
    else:
        menu_text = ['Новая игра', 'Выйти']
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'),
                                 (screen.get_width(), screen.get_height()))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font("data/cosm.ttf", 50)
    start_game = font.render(menu_text[0], 1, pygame.Color('white'))
    quit = font.render(menu_text[1], 1, pygame.Color('white'))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            
        screen.blit(fon, (0, 0))
        screen.blit(start_game, (screen.get_width() // 2 - start_game.get_width() // 2, screen.get_height() // 4 * 2.5 - 100))
        screen.blit(quit, (screen.get_width() // 2 - quit.get_width() // 2, screen.get_height() // 4 * 2.5))
        pygame.display.flip()
        clock.tick(FPS)


start_screen()