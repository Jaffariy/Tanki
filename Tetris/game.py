import pygame
import sys
import random
from config import save_config, load_config

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
GRID_SIZE = 25
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 10

tetromino_colors = {
    "S": (0, 255, 0),
    "I": (0, 255, 255),
    "T": (128, 0, 128),
    "R": (255, 0, 0),
    "L": (255, 165, 0),
}

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")
font = pygame.font.Font(None, 36)


class Tetromino:
    def __init__(self, shape):
        self.x = GRID_WIDTH // 2
        self.y = 0
        self.shape = shape
        self.rotation = 0

    def draw(self, surface):
        color = tetromino_colors[self.shape]
        rotated_shape = self.get_rotated_shape()
        cell_size = GRID_SIZE

        for y, row in enumerate(rotated_shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        surface,
                        color,
                        (
                            self.x * cell_size + x * cell_size,
                            self.y * cell_size + y * cell_size,
                            cell_size,
                            cell_size,
                        ),
                    )
                    inner_color = (255 - color[0], 255 - color[1], 255 - color[2])
                    inner_rect = (
                        self.x * cell_size + x * cell_size + 0.2 * cell_size,
                        self.y * cell_size + y * cell_size + 0.2 * cell_size,
                        0.6 * cell_size,
                        0.6 * cell_size,
                    )
                    pygame.draw.rect(surface, inner_color, inner_rect)

    def get_rotated_shape(self):
        shapes = {
            "S": [
                [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
                [[0, 1, 0], [0, 1, 1], [0, 0, 1]],
                [[0, 0, 0], [0, 1, 1], [1, 1, 0]],
                [[1, 0, 0], [1, 1, 0], [0, 1, 0]],
            ],
            "T": [
                [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
                [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
                [[0, 1, 0], [1, 1, 0], [0, 1, 0]],
                [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
            ],
            "L": [
                [[0, 0, 1], [1, 1, 1], [0, 0, 0]],
                [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
                [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
                [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
            ],
            "I": [
                [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                [[1], [1], [1], [1]],
                [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                [[1], [1], [1], [1]],
            ],
            "R": [
                [[1, 1], [1, 1]],
                [[1, 1], [1, 1]],
                [[1, 1], [1, 1]],
                [[1, 1], [1, 1]],
            ],
        }

        return shapes[self.shape][self.rotation]

    def rotate(self, grid):
        new_rotation = (self.rotation + 1) % 4
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
        shape = self.get_rotated_shape()
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_y = self.y + y
                    grid_x = self.x + x
                    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
                        grid[grid_y][grid_x] = {"color": tetromino_colors[self.shape]}

    def can_move(self, grid, dx=0, dy=0, rotation=None):
        if rotation is None:
            rotation = self.rotation
        else:
            self.rotation = rotation
        future_x = self.x + dx
        future_y = self.y + dy
        shape = self.get_rotated_shape()
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if (
                        future_x + x < 0
                        or future_x + x >= GRID_WIDTH
                        or future_y + y >= GRID_HEIGHT
                        or (
                            future_y + y < GRID_HEIGHT
                            and grid[future_y + y][future_x + x]
                        )
                    ):
                        self.rotation = rotation
                        return False
        self.rotation = rotation
        return True


def main():
    profile_data = load_config()
    clock = pygame.time.Clock()
    score = 0
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    current_tetromino = Tetromino(random.choice(list(tetromino_colors.keys())))
    fall_speed = profile_data.get("fall_speed", 1.0) * 1000
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
                score = clear_full_rows(grid, score)
                current_tetromino = Tetromino(
                    random.choice(list(tetromino_colors.keys()))
                )
                if not current_tetromino.can_move(grid):
                    show_game_over(window, score)
                    # profile_data['loses_count'] += 1
                    # save_config(profile_data)
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
                color = cell["color"]
                pygame.draw.rect(
                    surface, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                )


def show_game_over(surface, score):
    game_over_text = font.render("GAME OVER!", True, WHITE)
    score_text = font.render(f"Your Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart", True, WHITE)
    exit_text = font.render("Press Q to Quit", True, WHITE)
    config = load_config()
    config["loses_count"] += 1
    if config["high_score"] < score:
        config["high_score"] = score
    if config["loses_count"] == 1:
        config["achievements"]["Lose 1 game"] = True
    if config["loses_count"] == 10:
        config["achievements"]["Lose 10 games"] = True
    if config["high_score"] >= 1000:
        config["achievements"]["Get 1000 score"] = True
    if config["high_score"] >= 5000:
        config["achievements"]["Get 5000 score"] = True
    save_config(config)
    surface.fill(BLACK)
    surface.blit(
        game_over_text,
        (
            WINDOW_WIDTH // 2 - game_over_text.get_width() // 2,
            WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2 - 30,
        ),
    )
    surface.blit(
        score_text,
        (
            WINDOW_WIDTH // 2 - score_text.get_width() // 2,
            WINDOW_HEIGHT // 2 - score_text.get_height() // 2 + 10,
        ),
    )
    surface.blit(
        restart_text,
        (
            WINDOW_WIDTH // 2 - restart_text.get_width() // 2,
            WINDOW_HEIGHT // 2 - restart_text.get_height() // 2 + 50,
        ),
    )
    surface.blit(
        exit_text,
        (
            WINDOW_WIDTH // 2 - exit_text.get_width() // 2,
            WINDOW_HEIGHT // 2 - exit_text.get_height() // 2 + 70,
        ),
    )
    pygame.display.flip()
    wait_for_player_to_press_r_or_q()


"""
def show_victory(surface, score):
    victory_text = font.render("CONGRATULATIONS!", True, WHITE)
    score_text = font.render(f"Your Score: {score}", True, WHITE)

    surface.fill(BLACK)
    surface.blit(victory_text, (WINDOW_WIDTH // 2 - 
    victory_text.get_width() // 2, WINDOW_HEIGHT // 2 - 
    victory_text.get_height() // 2 - 30))
    surface.blit(score_text, (WINDOW_WIDTH // 2 - 
    score_text.get_width() // 2, WINDOW_HEIGHT // 2 -
     score_text.get_height() // 2 + 10))
    pygame.display.flip()
"""


def wait_for_player_to_press_r_or_q():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    sys.exit()


def draw_score(surface, score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))


if __name__ == "__main__":
    main()
