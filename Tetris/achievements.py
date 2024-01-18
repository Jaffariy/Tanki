import imageio
import pygame
import sys
from config import load_config

pygame.init()
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris achievements")

achievement_image_gray = pygame.image.load("Game Assets/achievement_gray.png")
achievement_image_gray = pygame.transform.scale(achievement_image_gray, (500, 80))
achievement_image_color = pygame.image.load("Game Assets/achievement.png")
achievement_image_color = pygame.transform.scale(achievement_image_color, (500, 80))
font = pygame.font.Font(None, 36)


class Button:
    def __init__(self, text, x, y, achievement_key):
        self.text = text
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50
        self.achievement_key = achievement_key

    def draw(self, achieved):
        btn_image = achievement_image_color if achieved else achievement_image_gray
        center_x = (WIDTH - btn_image.get_width()) // 2
        screen.blit(btn_image, (center_x, self.y))
        text_surface = font.render(self.text, True, BLACK if achieved else GRAY)
        text_rect = text_surface.get_rect(center=(center_x + btn_image.get_width() // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)



class BackButton:
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


achievements = [
    Button("Lose 1 game", 50, 100, "Lose 1 game"),
    Button("Lose 10 games", 50, 200, "Lose 10 games"),
    Button("Get 1000 score", 50, 300, "Get 1000 score"),
    Button("Get 5000 score", 50, 400, "Get 5000 score")
]


video_path = "Game Assets/menu_background.mp4"
video = imageio.get_reader(video_path)
frames = []
for frame in video:
    frames.append(pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB"))
video.close()
back_button = BackButton("Back", WIDTH // 2 - 100, 500)
config = load_config()

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
            if back_button.x < mouse_x < back_button.x + back_button.width and \
                    back_button.y < mouse_y < back_button.y + back_button.height:
                exec(open("main.py").read())
    screen.fill(WHITE)
    screen.blit(frames[current_frame], (0, 0))
    current_frame = (current_frame + 1) % total_frames
    for button in achievements:
        button.draw(config["achievements"][button.achievement_key])
    mouse_x, mouse_y = pygame.mouse.get_pos()
    back_button.draw()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
