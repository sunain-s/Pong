import pygame, sys, controls, mode_select

# draw text function
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# main menu
def main_menu():
    # main loop
    while True:
        click = False
        # detects events
        for event in pygame.event.get():
            # quit button in top right
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # detects click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # displays text
        draw_text('PONG', title_font, text_color, screen, screen_width/2, 50)
        draw_text('by Asianguy_123', name_font, text_color, screen, screen_width/2, 100)

        # gets mouse position and creates buttons
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(screen_width/2 - 100, 200, 200, 50)   
        button2 = pygame.Rect(screen_width/2 - 100, 300, 200, 50)
        button3 = pygame.Rect(screen_width/2 - 100, 400, 200, 50)

        # displays buttons and button texts
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('vs Computer', button_font, text_color, screen, screen_width/2, 225)
        pygame.draw.rect(screen, accent_color, button2)
        draw_text('2 Player', button_font, text_color, screen, screen_width/2, 325)
        pygame.draw.rect(screen, accent_color, button3)
        draw_text('Controls', button_font, text_color, screen, screen_width/2, 425)

        # checks if button was clicked, sends to appropiate mode
        if button1.collidepoint(mx, my):
            if click:
                mode_select.single_player()
        if button2.collidepoint(mx, my):
            if click:
                mode_select.multi_player()
        if button3.collidepoint(mx, my):
            if click:
                controls.main()

        # rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

# general setup and window
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Pong | by Asianguy_123')
screen_width = 1270
screen_height = 648
screen = pygame.display.set_mode((screen_width, screen_height))

# colours + fonts
bg_color = pygame.Color('#2F373F')
accent_color = (27,35,43)
text_color = (211, 79, 61)
title_font = pygame.font.Font('freesansbold.ttf', 80)
name_font = pygame.font.Font('freesansbold.ttf', 24)
button_font = pygame.font.Font('freesansbold.ttf', 24)

if __name__ == '__main__':
    main_menu()