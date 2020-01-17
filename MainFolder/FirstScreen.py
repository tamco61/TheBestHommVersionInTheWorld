import pygame, random, time, sys
from MainFolder import dop_func
from MainFolder.mainMenu import menu
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
run = True
FPS = 2
clock = pygame.time.Clock()
start = time.time()
pygame.mixer.music.load('data/mus1.mp3')


def start_screen():  # начальная заставка игры, ждет нажатия клавиш
    counter_sec = 0
    intro_text = ["PRESS ANY KEY"]
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'), (screen.get_width(), screen.get_height()))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font("data/cosm.ttf", 50)
    string_rendered = font.render(intro_text[0], 1, pygame.Color('white'))
    flag_invis = True
    pygame.mixer.music.play(-1)
    # pressed_key = pygame.mixer.Sound('data/click2.wav')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            elif event.type == pygame.KEYDOWN:
                # pygame.mixer.Sound.play(pressed_key)
                pygame.time.delay(500)
                menu()
                return
        counter_sec += 1
        if counter_sec == 8:  # техника, чтобы текст мигал
            fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'),
                                        (screen.get_width(), screen.get_height()))
            counter_sec = 0
        screen.blit(fon, (0, 0))
        if flag_invis:
            screen.blit(string_rendered, (screen.get_width() // 2 - string_rendered.get_width() // 2,
                                          screen.get_height() // 4 * 3))
            flag_invis = False
        else:
            flag_invis = True
        pygame.display.flip()
        clock.tick(FPS)


start_screen()