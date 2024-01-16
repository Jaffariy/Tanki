import pygame
import sys
import random
import os


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
GRID_SIZE = 25
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 5


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")
font = pygame.font.Font(None, 36)


def load_tetromino_images():
    tetrominoes = ['S', 'I', 'T', 'R', 'L']
    images = {}
    for tetromino in tetrominoes:
        images[tetromino] = []
        path = os.path.join("Game Assets", tetromino)
        for image_file in sorted(os.listdir(path)):
            if image_file.endswith('.png'):
                image_path = os.path.join(path, image_file)
                original_image = pygame.image.load(image_path).convert_alpha()
                scaled_image = pygame.transform.scale(original_image, (GRID_SIZE * 4, GRID_SIZE * 4))
                images[tetromino].append(scaled_image)
    return images



class Tetromino:
    def __init__(self, shape, images):
        self.x = GRID_WIDTH // 2
        self.y = 0
        self.shape = shape
        self.images = images
        self.rotation = 0

    def image(self):
        return self.images[self.shape][self.rotation]

    def rotate(self, grid):
        new_rotation = (self.rotation + 1) % len(self.images[self.shape])
        if self.can_move(grid, rotation=new_rotation):
            self.rotation = new_rotation

    def drop(self, grid):
        if self.can_move(grid, dy=1):
            self.y += 1
            return True
        else:
            self.add_to_grid(grid)
            return False

    def add_to_grid(self, grid):
        image = self.image()
        image_mask = pygame.mask.from_surface(image)
        for x in range(image_mask.get_size()[0]):
            for y in range(image_mask.get_size()[1]):
                if image_mask.get_at((x, y)):
                    grid[self.y + (y // GRID_SIZE)][self.x + (x // GRID_SIZE)] = 1

    def can_move(self, grid, dx=0, dy=0, rotation=None):
        if rotation is None:
            rotation = self.rotation
        future_x = self.x + dx
        future_y = self.y + dy
        image = self.images[self.shape][rotation]
        image_mask = pygame.mask.from_surface(image)
        image_width, image_height = image.get_width(), image.get_height()
        for x in range(image_width):
            for y in range(image_height):
                if not image_mask.get_at((x, y)):
                    continue
                if future_x + (x // GRID_SIZE) < 0 or future_x + (x // GRID_SIZE) >= GRID_WIDTH \
                        or future_y + (y // GRID_SIZE) >= GRID_HEIGHT:
                    return False
                if grid[future_y + (y // GRID_SIZE)][future_x + (x // GRID_SIZE)] != 0:
                    return False
        return True

    def draw(self, surface):
        image = self.image()
        surface.blit(image, (self.x * GRID_SIZE, self.y * GRID_SIZE))


def main():
    clock = pygame.time.Clock()
    score = 0
    images = load_tetromino_images()
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    current_tetromino = Tetromino(random.choice(list(images.keys())), images)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and current_tetromino.can_move(grid, dx=-1):
            current_tetromino.x -= 1
        if keys[pygame.K_RIGHT] and current_tetromino.can_move(grid, dx=1):
            current_tetromino.x += 1
        if keys[pygame.K_DOWN] and current_tetromino.can_move(grid, dy=1):
            current_tetromino.y += 1
        if keys[pygame.K_UP]:
            current_tetromino.rotate(grid)
        if not current_tetromino.drop(grid):
            current_tetromino = Tetromino(random.choice(list(images.keys())), images)
            if not current_tetromino.can_move(grid):
                print("Game over!")
                break

        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 5)
        draw_score(window, score)
        current_tetromino.draw(window)
        pygame.display.flip()

        current_tetromino.drop(grid)
        clock.tick(FPS)



def draw_score(surface, score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))


if __name__ == "__main__":
    main()
