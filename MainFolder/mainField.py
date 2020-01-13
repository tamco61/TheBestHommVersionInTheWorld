import pygame
import sqlite3
from MainFolder import dop_func
from MainFolder import database

pygame.init()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_width(), screen.get_height()
FPS = 20


class SpaceShip:
    def __init__(self, size):
        self.size = size
        self.x0, self.y0 = 0, 0
        self.x1, self.y1 = 0, 0
        self.image = pygame.transform.scale(dop_func.load_image('ship.png', (255, 255, 255)), (size, size))

    def return_image(self):
        return self.image

    def move(self, cell):
        self.x1, self.y1 = cell


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.ship = SpaceShip(self.cell_size - 2)

        # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.ship = SpaceShip(self.cell_size - 2)

    def render(self):
        global screen

        for i in range(self.width):
            for r in range(self.height):
                pygame.draw.polygon(screen, (255, 255, 255, 255), [(self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * (r + 1)),
                                                                   (self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * (r + 1))], 1)
                if i == self.ship.x0 and r == self.ship.y0:
                    screen.blit(self.ship.return_image(), (self.left + self.cell_size * i + 1, self.top + self.cell_size * r + 1))
        for i in range(abs(self.ship.x0 - self.ship.x1)):
            if self.ship.x0 > self.ship.x1:
                self.ship.x0 -= 1
            else:
                self.ship.x0 += 1
            screen.blit(self.ship.return_image(),
                        (self.left + self.cell_size * self.ship.x0 + 1, self.top + self.cell_size * self.ship.y0 + 1))
            clock.tick(FPS)
        for i in range(abs(self.ship.y0 - self.ship.y1)):
            if self.ship.y0 > self.ship.y1:
                self.ship.y0 -= 1
            else:
                self.ship.y0 += 1
            screen.blit(self.ship.return_image(),
                        (self.left + self.cell_size * self.ship.x0 + 1, self.top + self.cell_size * self.ship.y0 + 1))
            clock.tick(FPS)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        if x in range(0, self.width * self.cell_size) and y in range(0, self.height * self.cell_size):
            x0 = x // self.cell_size
            y0 = y // self.cell_size
            return x0, y0
        return None

    def on_click(self, cell):
        self.ship.move(cell)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


def draw_level(number, board):
    global screen

    lst = database.take_planet(number)

    for i in lst:
        id, x, y = i
        image = pygame.transform.scale(dop_func.load_image(f'planet/{id}.jpg', (255, 255, 255)), (board.cell_size, board.cell_size))
        screen.blit(image, (board.left + board.cell_size * x + 1, board.top + board.cell_size * y + 1))


def run_cycle(captain_name):
    board = Board(16, 8)
    cell_s = WIDTH // 16 - 1
    board.set_view((WIDTH - cell_s * 16) // 2, (HEIGHT - cell_s * 8) // 2, WIDTH // 16 - 1)
    fon = pygame.transform.scale(dop_func.load_image('Space.jpg'), (screen.get_width(), screen.get_height()))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        draw_level(1, board)
        board.render()

        pygame.display.flip()