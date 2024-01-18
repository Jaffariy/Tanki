import pygame
import sys
import imageio
from config import load_config, save_config

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)
GREY = (200, 200, 200)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Settings menu")
font = pygame.font.Font(None, 36)
config = load_config()
FALL_SPEED = config["fall_speed"]


class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)

        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )
        screen.blit(text_surface, text_rect)


def edit_profile_name():
    config = load_config()
    name = config["profile_name"]
    typing = True
    typing_box = pygame.Rect(100, HEIGHT // 2 - 25, 600, 50)
    while typing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, typing_box, 2)
        edit_name_text = font.render("Edit Name: " + name, True, WHITE)
        screen.blit(edit_name_text, (typing_box.x + 5, typing_box.y + 5))
        pygame.display.flip()

    config["profile_name"] = name
    save_config(config)


def view_profile_stats():
    config = load_config()
    running_stats = True

    while running_stats:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running_stats = False

        screen.fill(BLACK)
        stats_box = pygame.Rect(100, HEIGHT // 2 - 100, 600, 200)
        pygame.draw.rect(screen, WHITE, stats_box, 2)
        name_text = font.render("Name: " + config["profile_name"], True, WHITE)
        high_score_text = font.render(
            "High Score: " + str(config["high_score"]), True, WHITE
        )
        loss_count = font.render(
            "Loss count: " + str(config["loses_count"]), True, WHITE
        )
        screen.blit(name_text, (100, HEIGHT // 3))
        screen.blit(high_score_text, (100, HEIGHT // 2))
        screen.blit(loss_count, (100, HEIGHT // 2 + 40))
        pygame.display.flip()


class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, init_val, step):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.val = init_val
        self.step = step
        self.active = False

    def draw(self):
        handle_x = ((self.val - self.min_val) / (self.max_val - self.min_val)) * (
            self.rect.width - 20
        ) + self.rect.x
        pygame.draw.rect(screen, GREY, self.rect, 3)
        pygame.draw.rect(screen, WHITE, [handle_x, self.rect.y, 20, self.rect.height])

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.active = False

        elif event.type == pygame.MOUSEMOTION:
            if self.active:
                mouse_x, mouse_y = event.pos
                handle_x = mouse_x - self.rect.x - 10
                if handle_x < 0:
                    handle_x = 0
                if handle_x > self.rect.width - 20:
                    handle_x = self.rect.width - 20
                self.val = (handle_x / (self.rect.width - 20)) * (
                    self.max_val - self.min_val
                ) + self.min_val
                self.val = round(self.val / self.step) * self.step

    def getValue(self):
        return self.val


edit_name_button = Button("Edit Name", WIDTH // 2 - 100, 300)
stats_button = Button("View Stats", WIDTH // 2 - 100, 360)
save_speed = Button("Save speed", WIDTH // 2 - 100, 240)

settings_text = font.render(f"Adjust speed(min: 0.5, max: 2.0)", True, WHITE)
settings_rect = settings_text.get_rect(center=(WIDTH // 2, 150))
slider = Slider(300, 200, 200, 30, 0.1, 1.0, FALL_SPEED, 0.1)

about_text = font.render("About developers:", True, WHITE)
about_rect = about_text.get_rect(center=(WIDTH // 2, 420))

authors_info = "Jove (tg: rremedy, discord: sp1r1tt_)"
authors_text = font.render(authors_info, True, WHITE)
authors_rect = authors_text.get_rect(center=(WIDTH // 2, 450))

video_path = "Game Assets/menu_background.mp4"
video = imageio.get_reader(video_path)
frames = []
for frame in video:
    frames.append(pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB"))
video.close()
back_button = Button("Back", WIDTH // 2 - 100, 500)
running = True
current_frame = 0
total_frames = len(frames)
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                back_button.x < mouse_x < back_button.x + back_button.width
                and back_button.y < mouse_y < back_button.y + back_button.height
            ):
                exec(open("main.py").read())
            if (
                edit_name_button.x
                < mouse_x
                < edit_name_button.x + edit_name_button.width
                and edit_name_button.y
                < mouse_y
                < edit_name_button.y + edit_name_button.height
            ):
                edit_profile_name()
            elif (
                stats_button.x < mouse_x < stats_button.x + stats_button.width
                and stats_button.y < mouse_y < stats_button.y + stats_button.height
            ):
                view_profile_stats()
            elif (
                save_speed.x < mouse_x < save_speed.x + save_speed.width
                and save_speed.y < mouse_y < save_speed.y + save_speed.height
            ):
                FALL_SPEED = slider.getValue()
                config = load_config()
                config["fall_speed"] = FALL_SPEED
                save_config(config)

        slider.update(event)

    screen.fill(BLACK)
    screen.blit(frames[current_frame], (0, 0))
    current_frame = (current_frame + 1) % total_frames
    back_button.draw()
    edit_name_button.draw()
    stats_button.draw()
    save_speed.draw()
    slider.draw()
    screen.blit(about_text, about_rect)
    screen.blit(authors_text, authors_rect)
    screen.blit(settings_text, settings_rect)

    pygame.display.flip()
    clock.tick(30)


pygame.quit()
sys.exit()
