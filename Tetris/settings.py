import pygame
import sys
import imageio

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Settings menu")
font = pygame.font.Font(None, 36)

FALL_SPEED = 1.0


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


class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, init_val, step):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.val = init_val
        self.step = step
        self.active = False

    def draw(self):
        handle_x = ((self.val - self.min_val) / (self.max_val - self.min_val)) * (self.rect.width - 20) + self.rect.x
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
                self.val = ((handle_x / (self.rect.width - 20)) * (self.max_val - self.min_val) + self.min_val)
                self.val = round(self.val / self.step) * self.step

    def getValue(self):
        return self.val


settings_text = font.render("Adjust speed(min: 0.5, max: 2.0)", True, WHITE)
settings_rect = settings_text.get_rect(center=(WIDTH // 2, 150))
slider = Slider(300, 200, 200, 30, 0.5, 2.0, FALL_SPEED, 0.1)

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
            if back_button.x < mouse_x < back_button.x + back_button.width and \
                    back_button.y < mouse_y < back_button.y + back_button.height:
                exec(open("main.py").read())

        slider.update(event)

    screen.fill(BLACK)
    screen.blit(frames[current_frame], (0, 0))
    current_frame = (current_frame + 1) % total_frames
    back_button.draw()
    slider.draw()
    screen.blit(about_text, about_rect)
    screen.blit(authors_text, authors_rect)
    screen.blit(settings_text, settings_rect)

    pygame.display.flip()
    clock.tick(30)

FALL_SPEED = slider.getValue()

pygame.quit()
sys.exit()
