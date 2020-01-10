import pygame, random, time
import dop_func
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
FPS = 75
clock = pygame.time.Clock()
start = time.time()


def start_screen():
    intro_text = ["PRESS KEY"]
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font("data/cosm.ttf", 50)
    string_rendered = font.render(intro_text[0], 1, pygame.Color('white'))
    text_coord = [270, 250]
    napr = 1

    def move_text():
        global napr
        speed = 0.3
        if text_coord[1] <= 250:
            text_coord[1] += speed
            napr = 1
        elif text_coord[1] >= 300:
            text_coord[1] -= speed
            napr = 2
        elif napr == 1:
            text_coord[1] += speed
        elif napr == 2:
            text_coord[1] -= speed
        screen.blit(string_rendered, (int(text_coord[0]), int(text_coord[1])))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
        screen.blit(fon, (0, 0))
        move_text()
        pygame.display.flip()
        clock.tick(FPS)


start_screen()