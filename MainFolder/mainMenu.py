import pygame
from MainFolder import dop_func

pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
running = True
FPS = 2
clock = pygame.time.Clock()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, text, on_click=lambda x: None,):
        self.state = 'normal'
        self.on_click = on_click
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        pygame.draw.rect(surface,self.back_color, self.bounds)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'


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
        screen.blit(start_game,
                    (screen.get_width() // 2 - start_game.get_width() // 2, screen.get_height() // 4 * 2.5 - 100))
        screen.blit(quit, (screen.get_width() // 2 - quit.get_width() // 2, screen.get_height() // 4 * 2.5))
        pygame.display.flip()
        clock.tick(FPS)