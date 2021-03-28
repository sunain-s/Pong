import pygame, sys

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def display_image(image, x, y, surface):
    surface.blit(image, (x, y))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        draw_text('Controls', title_font, title_color, screen, screen_width/2, 50)
        draw_text("Press 'ESC' to return to Menu", text_font, text_color, screen, screen_width/2, 110)
        draw_text('Player 2', text_font, text_color, screen, screen_width/6, 200)
        draw_text('Player 1', text_font, text_color, screen, screen_width/6 * 5, 200)
        display_image(p2_img, screen_width/6 - 50, 250, screen)
        display_image(p1_img, screen_width/6 * 5 - 50, 250, screen)

        #rendering 
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

#general setup and window
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Pong | by Asianguy_123')
screen_width = 1270
screen_height = 648
screen = pygame.display.set_mode((screen_width, screen_height))

#colours + fonts
bg_color = pygame.Color('#2F373F')
text_color = (255,255,255)
title_color = (211, 79, 61)
title_font = pygame.font.Font('freesansbold.ttf', 80)
text_font = pygame.font.Font('freesansbold.ttf', 24)

#images
p1_img = pygame.image.load('p1_ctrl.png')
p2_img = pygame.image.load('p2_ctrl.png')