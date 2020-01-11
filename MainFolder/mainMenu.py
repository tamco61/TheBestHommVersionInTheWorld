import pygame

pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
running = True
font = pygame.font.Font("FirstScreen/data/cosm.ttf", 50)
string_rendered = font.render(intro_text[0], 1, pygame.Color('white'))


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