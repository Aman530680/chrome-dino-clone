import pygame
import random

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Dino Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
dino_frames = [pygame.image.load("dino.png")]
dino_frames = [pygame.transform.scale(img, (200, 200)) for img in dino_frames]
dino_index = 0
cactus_img = pygame.image.load("catch.png")
cactus_img = pygame.transform.scale(cactus_img, (90, 150))
dino_x, dino_y = 100, HEIGHT - 250
dino_vel = 0
gravity = 0.6
jump_force = -24
dino_rect = dino_frames[0].get_rect(topleft=(dino_x, dino_y))
cactus_x = WIDTH
cactus_y = HEIGHT - 250
cactus_speed = 15
cactus_rect = cactus_img.get_rect(topleft=(cactus_x, cactus_y))
score = 0
level = 1
font = pygame.font.Font(None, 50)
running = True
game_over = False
clock = pygame.time.Clock()
frame_counter = 0

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_rect.y == HEIGHT - 250:
                dino_vel = jump_force
            if event.key == pygame.K_r and game_over:
                dino_rect.y = HEIGHT - 250
                cactus_rect.x = WIDTH
                score = 0
                level = 1
                cactus_speed = 5
                game_over = False
            if event.key == pygame.K_ESCAPE:
                running = False

    if not game_over:
        dino_vel += gravity
        dino_rect.y += dino_vel
        if dino_rect.y > HEIGHT - 250:
            dino_rect.y = HEIGHT - 250

        cactus_rect.x -= cactus_speed
        if cactus_rect.x < -50:
            cactus_rect.x = WIDTH + random.randint(100, 300)
            score += 1

        if score % 5 == 0 and score > 0:
            level = score // 5 + 1
            cactus_speed = 5 + level

        if dino_rect.colliderect(cactus_rect):
            game_over = True

        if frame_counter % 5 == 0:
            dino_index = (dino_index + 1) % len(dino_frames)
        frame_counter += 1

        screen.blit(dino_frames[dino_index], dino_rect.topleft)
        screen.blit(cactus_img, cactus_rect.topleft)

        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        screen.blit(score_text, (20, 20))
        screen.blit(level_text, (20, 70))

    else:
        game_over_text = font.render("Game Over! Press R to Restart", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
