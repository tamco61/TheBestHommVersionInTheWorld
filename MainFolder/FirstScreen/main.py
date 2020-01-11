import pygame, random, time
import dop_func
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
run = True
FPS = 2
clock = pygame.time.Clock()
start = time.time()


def start_screen():
    intro_text = ["PRESS ANY KEY"]
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'), (screen.get_width(), screen.get_height()))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font("data/cosm.ttf", 50)
    string_rendered = font.render(intro_text[0], 1, pygame.Color('white'))
    t = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
        screen.blit(fon, (0, 0))
        if t:
            screen.blit(string_rendered, (screen.get_width() // 2 - string_rendered.get_width() // 2, screen.get_height() // 4 * 3))
            t = False
        else:
            t = True
        pygame.display.flip()
        clock.tick(FPS)


start_screen()