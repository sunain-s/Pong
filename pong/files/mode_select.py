import pygame, menu, s_player, m_player

# draw text function
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def ranked():
    running = True
    while running:

        # display main text and get mouse position
        draw_text('Singleplayer: Endless', title_font, text_color, screen, screen_width/2, 50)
        mx, my = pygame.mouse.get_pos()

        # create and display button + button text
        button1 = pygame.Rect(screen_width/2 - 100, 200, 200, 50)
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('Ranked', button_font, text_color, screen, screen_width/2, 225)

        # create and display button + button text
        button2 = pygame.Rect(screen_width/2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, accent_color, button2)
        draw_text('Practice', button_font, text_color, screen, screen_width/2, 325)

        # create and display button + button text
        button3 = pygame.Rect(screen_width/2 - 100, 400, 200, 50)
        pygame.draw.rect(screen, accent_color, button3)
        draw_text('Menu', button_font, text_color, screen, screen_width/2, 425)

        # event detection
        click = False
        for event in pygame.event.get():
            # if quit, return to main menu
            if event.type == pygame.QUIT:
                running = False
            # if esc, return to main menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # if button clicked, go to selected option
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if button1.collidepoint(mx, my):
                if click:
                    ranked.ranked_bool = True
                    s_player.run()
            if button2.collidepoint(mx, my):
                if click:
                    ranked.ranked_bool = False
                    s_player.run()
            if button3.collidepoint(mx, my):
                if click:
                    menu.main_menu()

        #rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

    # loops until instruction given to send elsewhere
    if running == False:
        menu.main_menu()
    elif running == True:
        ranked()

# single player mode select function
def single_player():
    # main loop
    running = True
    while running:

        # display main text and get mouse position
        draw_text('Select Mode: Singleplayer', title_font, text_color, screen, screen_width/2, 50)
        mx, my = pygame.mouse.get_pos()

        # create and display button + button text
        button1 = pygame.Rect(screen_width/2 - 100, 200, 200, 50)
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('Endless', button_font, text_color, screen, screen_width/2, 225)

        # create and display button + button text
        button2 = pygame.Rect(screen_width/2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, accent_color, button2)
        draw_text('First to 5', button_font, text_color, screen, screen_width/2, 325)

        # create and display button + button text
        button3 = pygame.Rect(screen_width/2 - 100, 400, 200, 50)
        pygame.draw.rect(screen, accent_color, button3)
        draw_text('First to 11', button_font, text_color, screen, screen_width/2, 425)

        # create and display button + button text
        button4 = pygame.Rect(screen_width/2 - 100, 500, 200, 50)
        pygame.draw.rect(screen, accent_color, button4)
        draw_text('Menu', button_font, text_color, screen, screen_width/2, 525)

        # event detection
        click = False
        for event in pygame.event.get():
            # if quit, return to main menu
            if event.type == pygame.QUIT:
                running = False
            # if esc, return to main menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # if button clicked, go to selected option
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if button1.collidepoint(mx, my):
                if click:
                    single_player.end_score = 0
                    ranked()
            if button2.collidepoint(mx, my):
                if click:
                    single_player.end_score = 5
                    s_player.run()
            if button3.collidepoint(mx, my):
                if click:
                    single_player.end_score = 11
                    s_player.run()
            if button4.collidepoint(mx, my):
                if click:
                    menu.main_menu()


        #rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

    # loops until instruction given to send elsewhere
    if running == False:
        menu.main_menu()
    elif running == True:
        single_player()

# multiplayer mode select function
def multi_player():
    # main loop
    running = True
    while running:

        # display text and get mouse position
        draw_text('Select Mode: Multiplayer', title_font, text_color, screen, screen_width/2, 50)
        mx, my = pygame.mouse.get_pos()

        # create and display button + button text
        button1 = pygame.Rect(screen_width/2 - 100, 200, 200, 50)
        pygame.draw.rect(screen, accent_color, button1)
        draw_text('Endless', button_font, text_color, screen, screen_width/2, 225)

        # create and display button + button text
        button2 = pygame.Rect(screen_width/2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, accent_color, button2)
        draw_text('First to 5', button_font, text_color, screen, screen_width/2, 325)

        # create and display button + button text
        button3 = pygame.Rect(screen_width/2 - 100, 400, 200, 50)
        pygame.draw.rect(screen, accent_color, button3)
        draw_text('First to 11', button_font, text_color, screen, screen_width/2, 425)

        # create and display button + button text
        button4 = pygame.Rect(screen_width/2 - 100, 500, 200, 50)
        pygame.draw.rect(screen, accent_color, button4)
        draw_text('Menu', button_font, text_color, screen, screen_width/2, 525)

        # event detection
        click = False
        for event in pygame.event.get():
            # if quit, return to main menu
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # if esc, return to main menu
                if event.key == pygame.K_ESCAPE:
                    running = False
            # if button clicked, go to selected option
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if button1.collidepoint(mx, my):
                if click:
                    multi_player.end_score = 0
                    m_player.run()
            if button2.collidepoint(mx, my):
                if click:
                    multi_player.end_score = 5
                    m_player.run()
            if button3.collidepoint(mx, my):
                if click:
                    multi_player.end_score = 11
                    m_player.run()
            if button4.collidepoint(mx, my):
                if click:
                    menu.main_menu()


        # rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)

    if running == False:
        menu.main_menu()
    elif running == True:
        multi_player()

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
button_font = pygame.font.Font('freesansbold.ttf', 24)