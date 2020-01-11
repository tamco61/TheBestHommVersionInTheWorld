import pygame
from MainFolder import dop_func

pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_width(), screen.get_height()



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

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

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
            print(cell)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


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
    board.render()
    pygame.display.flip()