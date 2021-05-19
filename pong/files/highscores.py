import pygame, sys, menu

# draw text function
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# writes to file, gets and displays highscores
def highscore_func(username, player_score):
    # adding player score and username to file
    file = open('files\scores.txt', 'a')
    file.write(username + ';' + str(player_score) + '\n')
    file.close()

    # retrieving scores
    users = []
    scores = []
    display_user = []
    display_score = []
    with open('files\scores.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n').split(';')
            users.append(line[0])
            scores.append(int(line[1]))
            top_ten = sorted(scores, reverse = True)
        
        # creating top_ten list
        if len(scores) < 10:
            for x in range(len(scores)):
                user = users[scores.index(top_ten[x])]
                score = top_ten[x]
                display_user.append(user)
                display_score.append(score)
                del users[scores.index(top_ten[x])]
                scores.remove(top_ten[x])
        else:
            for x in range(10):
                user = users[scores.index(top_ten[x])]
                score = top_ten[x]
                display_user.append(user)
                display_score.append(score)
                del users[scores.index(top_ten[x])]
                scores.remove(top_ten[x])
        file.close()

    # main leaderboard loop
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
        
        # gets mouse position and creates button/box
        mx, my = pygame.mouse.get_pos()
        background_box = pygame.Rect(screen_width/2 - 150, 100, 300, 450)
        button = pygame.Rect(screen_width/2 - 200, 575, 400, 50)

        # displays boxes and button text
        pygame.draw.rect(screen, accent_color, background_box)
        pygame.draw.rect(screen, accent_color, button)
        draw_text('Return to main menu', button_font, text_color, screen, screen_width/2, 600)

        # displays text and leaderboard
        draw_text('Leaderboard', title_font, text_color, screen, screen_width/2, 50)
        for i in range(len(display_user)):
            if i == 0:
                draw_text(f'{i+1} - {display_user[i]}: {display_score[i]}', 
                num_one_font, gold_color, screen, screen_width/2, 130)
            elif i == 1:
                draw_text(f'{i+1} - {display_user[i]}: {display_score[i]}', 
                num_two_font, silver_color, screen, screen_width/2, 180)
            else:
                draw_text(f'{i+1} - {display_user[i]}: {display_score[i]}', 
                leaderboard_font, text_color, screen, screen_width/2, 110 + 40 * (i + 1))

        # if button click detected
        if button.collidepoint(mx, my):
            if click:
                menu.main_menu()
        # rendering
        pygame.display.flip()
        clock.tick(120)
        screen.fill(bg_color)


# enter score to add to highscores
def enter_score(player_score):
    # main loop
    input_active = False
    username = 'Enter your username'
    while True:
        # rendering
        screen.fill(bg_color)
        clock.tick(120)

        # displays title text and gets mouse position
        draw_text('Ranked: register score', title_font, text_color, screen, screen_width/2, 50)
        mx, my = pygame.mouse.get_pos()

        # creates buttons for input and submission
        username_button = pygame.Rect(screen_width/2 - 150, 200, 300, 50)
        score_box = pygame.Rect(screen_width/2 - 150, 300, 300, 50)
        submit_button = pygame.Rect(screen_width/2 - 150, 400, 300, 50)

        # displays buttons and button texts
        pygame.draw.rect(screen, accent_color, username_button)
        draw_text(username, button_font, text_color, screen, screen_width/2, 225)
        pygame.draw.rect(screen, accent_color, score_box)
        draw_text(str(player_score) , button_font, text_color, screen, screen_width/2, 325)
        pygame.draw.rect(screen, accent_color, submit_button)
        draw_text('Submit score', button_font, text_color, screen, screen_width/2, 425)

        # detects events
        for event in pygame.event.get():
            # quit button in top right
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # detects click on username button and defaults username
            if event.type == pygame.MOUSEBUTTONDOWN and username_button.collidepoint(mx, my):
                input_active = True
                user_len = True
                username = ''
            # detects key input and displays to screen
            if input_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                        if len(username) < 13:
                            user_len = True
                    elif len(username) > 12:
                        user_len = False
                    elif user_len:
                        username += event.unicode
            # detects click on submit button and open highscore func
            if submit_button.collidepoint(mx, my) and event.type == pygame.MOUSEBUTTONDOWN:
                highscore_func(username, player_score)
            pygame.display.flip()
        pygame.display.flip()

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
gold_color = (255, 215, 0)
silver_color = (192, 192, 192)
title_font = pygame.font.Font('freesansbold.ttf', 60)
button_font = pygame.font.Font('freesansbold.ttf', 24)
leaderboard_font = pygame.font.Font('freesansbold.ttf', 18)
num_one_font = pygame.font.Font('freesansbold.ttf', 24)
num_two_font = pygame.font.Font('freesansbold.ttf', 21)
