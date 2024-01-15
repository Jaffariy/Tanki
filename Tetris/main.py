import pygame
import sys
import imageio
from config import load_config, save_config

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris main menu")
font = pygame.font.Font(None, 36)

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
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

def prompt_for_profile_name():
    name = ""
    typing_box = pygame.Rect(100, HEIGHT // 2 - 25, 600, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name.strip()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, typing_box, 2)
        enter_name_text = font.render("Enter your profile name: " + name, True, WHITE)
        screen.blit(enter_name_text, (typing_box.x + 5, typing_box.y + 5))
        pygame.display.flip()

config = load_config()
if config["profile_name"] == "":
    config["profile_name"] = prompt_for_profile_name()
    save_config(config)

start_button = Button("Start game!", WIDTH // 2 - 100, 200)
settings_button = Button("Settings", WIDTH // 2 - 100, 300)
achievements_button = Button("Achievements", WIDTH // 2 - 100, 400)

video_path = "Game Assets/menu_background.mp4"
video = imageio.get_reader(video_path)
frames = []
for frame in video:
    frames.append(pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB"))
video.close()

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
            if achievements_button.x < mouse_x < achievements_button.x + achievements_button.width and \
                    achievements_button.y < mouse_y < achievements_button.y + achievements_button.height:
                exec(open("achievements.py").read())
            elif settings_button.x < mouse_x < settings_button.x + settings_button.width and \
                    settings_button.y < mouse_y < settings_button.y + settings_button.height:
                exec(open("settings.py").read())
            elif start_button.x < mouse_x < start_button.x + start_button.width and \
                    start_button.y < mouse_y < start_button.y + start_button.height:
                exec(open("game.py").read())

    screen.fill(BLACK)
    screen.blit(frames[current_frame], (0, 0))
    current_frame = (current_frame + 1) % total_frames
    start_button.draw()
    settings_button.draw()
    achievements_button.draw()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
