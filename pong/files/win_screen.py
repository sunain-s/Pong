import pygame, sys, menu

# draw text function
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# singleplayer, player win screen
def window_s_player():
    # play sound
    pygame.mixer.Sound.play(win_sound)
    # main loop
    while True:
        click = False
        # event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # display win text and image
        draw_text('Player Wins', title_font, text_color, screen, screen_width/2, 50)
        screen.blit(win_image, (386, 120))

        # get mouse position and display button
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(screen_width/2 - 150, 525, 300, 50)
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('Return to Main Menu', button_font, text_color, screen, screen_width/2, 550)

        # detect button click
        if button1.collidepoint(mx, my):
            if click:
                menu.main_menu()

        # rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

# singleplayer, computer win screen
def window_s_computer():
    # play sound
    pygame.mixer.Sound.play(win_sound)
    # main loop
    while True:
        click = False
        # event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # display win text and image
        draw_text('Computer Wins', title_font, text_color, screen, screen_width/2, 50)
        screen.blit(win_image, (386, 120))

        # get mouse position and display button
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(screen_width/2 - 150, 525, 300, 50)
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('Return to Main Menu', button_font, text_color, screen, screen_width/2, 550)

        # detect button click
        if button1.collidepoint(mx, my):
            if click:
                menu.main_menu()

        # rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

#multiplayer, player 1 win screen
def window_m_player1():
    # play sound
    pygame.mixer.Sound.play(win_sound)
    # main loop
    while True:
        click = False
        # event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # display win text and image
        draw_text('Player 1 Wins', title_font, text_color, screen, screen_width/2, 50)
        screen.blit(win_image, (386, 120))

        # get mouse position and display button
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(screen_width/2 - 150, 525, 300, 50)
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('Return to Main Menu', button_font, text_color, screen, screen_width/2, 550)

        # detect button click
        if button1.collidepoint(mx, my):
            if click:
                menu.main_menu()

        # rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

# multiplayer, player 2 win screen
def window_m_player2():
    # play sound
    pygame.mixer.Sound.play(win_sound)
    # main loop
    while True:
        click = False
        # event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # display win text and image
        draw_text('Player 2 Wins', title_font, text_color, screen, screen_width/2, 50)
        screen.blit(win_image, (386, 120))

        # get mouse position and display button
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(screen_width/2 - 150, 525, 300, 50)
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('Return to Main Menu', button_font, text_color, screen, screen_width/2, 550)

        # detect button click
        if button1.collidepoint(mx, my):
            if click:
                menu.main_menu()

        # rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

# general setup and window
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Pong | Sunain Syed')
screen_width = 1270
screen_height = 648
screen = pygame.display.set_mode((screen_width, screen_height))
win_image = pygame.image.load('images\winner_winner.png')
win_sound = pygame.mixer.Sound('sounds\win.ogg')

# colours + fonts
bg_color = pygame.Color('#2F373F')
accent_color = (27,35,43)
text_color = (211, 79, 61)
title_font = pygame.font.Font('freesansbold.ttf', 80)
button_font = pygame.font.Font('freesansbold.ttf', 24)
