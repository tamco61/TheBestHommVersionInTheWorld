import pygame, random
from MainFolder import dop_func, database

pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
running = True
FPS = 10
clock = pygame.time.Clock()

pygame.mixer.music.load('data/mus1.mp3')


class Button:
    def __init__(self, width, height, inactive_color=(150, 150, 150), active_color=(0, 0, 0), text_size=50):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text_size = text_size

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        naved = pygame.mixer.Sound('data/naved.wav')
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(naved)
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        else:
                            action()
                            return
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

        print_text(text, x + 10, y + 15, font_size=self.text_size)


def print_text(text, x, y, font_size=50, font_type='cosm.ttf', color='white'):
    font_type = pygame.font.Font(f"data/{font_type}", font_size)
    mes = font_type.render(text, 1, pygame.Color(color))
    screen.blit(mes, (x, y))


def menu():
    fon = pygame.transform.scale(dop_func.load_image(f'fon{str(random.randint(0, 4))}.jpg'),
                                 (screen.get_width(), screen.get_height()))

    start_game = Button(350, 80)
    quit = Button(225, 80)
    counter_sec = 0
    pygame.mixer.music.play(-1)
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
        start_game.draw(screen.get_width() // 2 - start_game.width // 2,
                        screen.get_height() // 4 * 2.5 - 200, 'Новая игра', choose_captain)
        quit.draw(screen.get_width() // 2 - quit.width // 2, screen.get_height() // 4 * 2.5 - 100, 'Выйти', quit)
        pygame.display.flip()
        clock.tick(FPS)


def choose_captain():
    background = pygame.transform.scale(dop_func.load_image(f'board.jpg'),
                                 (screen.get_width(), screen.get_height()))
    heroes = set()
    while len(heroes) != 5:
        heroes.add(database.take_hero())
    c = 0
    FPS = 60
    heroes = list(heroes)
    image0 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[0][-1]),
                                    (screen.get_width() // 6, screen.get_height() // 2))
    image1 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[1][-1]),
                                    (screen.get_width() // 6, screen.get_height() // 2))
    image2 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[2][-1]),
                                    (screen.get_width() // 6, screen.get_height() // 2))
    image3 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[3][-1]),
                                    (screen.get_width() // 6, screen.get_height() // 2))
    image4 = pygame.transform.scale(dop_func.load_image("heroes/" + heroes[4][-1]),
                                    (screen.get_width() // 6, screen.get_height() // 2))
    choose = Button(185, 65, text_size=30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dop_func.terminate()
        screen.fill((255, 255, 255))
        print_text('Выберите капитана', (2 * screen.get_width()) // 6, screen.get_height() // 8, color='black')
        for i in range(0, 5):
            screen.blit(locals()['image%s' % i], (screen.get_width() // 8 + 0.9 * c * screen.get_width() // 6,
                                                  screen.get_height() // 5))
            choose.draw(screen.get_width() // 8 + c * screen.get_width() // 6, 3 * screen.get_height() // 4, "Выбрать")
            c += 1
        c = 0
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    choose_captain()