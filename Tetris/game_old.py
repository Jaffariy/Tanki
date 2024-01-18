import pygame
import sys
import random
import os


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
GRID_SIZE = 25
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 30

tetromino_colors = {
    'S': (0, 255, 0),
    'I': (0, 255, 255),
    'T': (128, 0, 128),
    'R': (255, 0, 0),
    'L': (255, 165, 0)
}

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
        image = self.images[self.shape][self.rotation]
        image_width, image_height = image.get_width(), image.get_height()
        for x in range(0, image_width, GRID_SIZE):
            for y in range(0, image_height, GRID_SIZE):
                if image.get_at((x, y)) != (0, 0, 0, 0):
                    grid_y = self.y + (y // GRID_SIZE)
                    grid_x = self.x + (x // GRID_SIZE)
                    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
                        cell_image = image.subsurface((x, y, GRID_SIZE, GRID_SIZE))
                        grid[grid_y][grid_x] = {'color': tetromino_colors[self.shape], 'image': cell_image}

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
    fall_speed = 2000
    last_fall_time = pygame.time.get_ticks()

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
        current_time = pygame.time.get_ticks()
        if current_time - last_fall_time > fall_speed:
            if not current_tetromino.drop(grid):
                clear_full_rows(grid, score)
                score = clear_full_rows(grid, score)
                current_tetromino = Tetromino(random.choice(list(images.keys())), images)
                if not current_tetromino.can_move(grid):
                    print("Game over!")
                    break
            last_fall_time = current_time

        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 5)
        draw_score(window, score)
        draw_grid(window, grid)
        current_tetromino.draw(window)
        pygame.display.flip()
        clock.tick(FPS)

def clear_full_rows(grid, score):
    full_rows = [i for i, row in enumerate(grid) if all(row)]
    for i in full_rows:
        del grid[i]
        grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        score += 100
    return score

def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                color = cell['color']
                if 'image' in cell and cell['image']:
                    surface.blit(cell['image'], (x * GRID_SIZE, y * GRID_SIZE))
                else:
                    pygame.draw.rect(surface, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw_score(surface, score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))


if __name__ == "__main__":
    main()
