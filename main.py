import pygame
from pygame.locals import *

pygame.init()

# временно
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# временно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Танчики")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Где-то тут ассеты будем прогружать



LEVELS = [
    # Здесь должны быть данные для каждого уровня - расположение блоков, танков и т.д.
]


# Класс для танка
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Загрузка изображения танка
        self.image = pygame.image.load("путь_к_изображению_танка.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Инициализация начальной позиции
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        # Обновление логики танка
        pass

    def draw(self, screen):
        # Отрисовка танка на экране
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Инициализация танка
tank = Tank()

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Обновление состояния игры
    tank.update()

    # Отрисовка игровых объектов
    screen.fill(BLACK)
    tank.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Выход из игры
pygame.quit()

#логично что мы это еще будем редачить, причем очень сильно
#да и вообще, много кусков кода выносить в отдельные файлы