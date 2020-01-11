import pygame, random
from MainFolder import dop_func

pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
running = True
FPS = 10
clock = pygame.time.Clock()


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (150, 150, 150)
        self.active_color = (0, 0, 0)

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))
                if click[0] == 1 and action is not None:
                    action()
            else:
                pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

        print_text(text, x + 10, y + 15)


def print_text(text, x, y, font_size=50):
    font_type = pygame.font.Font("data/cosm.ttf", font_size)
    mes = font_type.render(text, 1, pygame.Color('white'))
    screen.blit(mes, (x, y))


def menu():
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'),
                                 (screen.get_width(), screen.get_height()))
    screen.blit(fon, (0, 0))
    start_game = Button(350, 80)
    quit = Button(225, 80)
    counter_sec = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
        counter_sec += 1
        if counter_sec == 40:
            fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'),
                                         (screen.get_width(), screen.get_height()))
            counter_sec = 0
        screen.blit(fon, (0, 0))
        start_game.draw(screen.get_width() // 2 - start_game.width // 2, screen.get_height() // 4 * 2.5 - 200, 'Новая игра')
        quit.draw(screen.get_width() // 2 - quit.width // 2, screen.get_height() // 4 * 2.5 - 100, 'Выйти')
        pygame.display.flip()
        clock.tick(FPS)


