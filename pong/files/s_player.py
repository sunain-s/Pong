import pygame, random, mode_select, win_screen, highscores
from random import randint

# block class
class Block(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))

# player class, inherits block class
class Player(Block):
	# creates base variables
	def __init__(self,path,x_pos,y_pos,speed):
		super().__init__(path,x_pos,y_pos)
		self.speed = speed
		self.movement = 0

	# bounds screen
	def screen_constrain(self):
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= screen_height:
			self.rect.bottom = screen_height

	# player movement
	def update(self,ball_group):
		self.rect.y += self.movement
		self.screen_constrain()

# ball class, inherits block class
class Ball(Block):
	# creates base variables
	def __init__(self,path,x_pos,y_pos,speed_x,speed_y,paddles):
		super().__init__(path,x_pos,y_pos)
		self.speed_x = speed_x * random.choice((-1,1))
		self.speed_y = speed_y * random.choice((-1,1))
		self.paddles = paddles
		self.active = False
		self.score_time = 0

	# ball movement
	def update(self):
		if self.active:
			self.rect.x += self.speed_x
			self.rect.y += self.speed_y
			self.collisions()
		else:
			self.restart_counter()

	# collision detection and actions
	def collisions(self):
		# border collision
		if self.rect.top <= 0 or self.rect.bottom >= screen_height:
			pygame.mixer.Sound.play(plob_sound)
			self.speed_y *= -1

		# paddle collision
		if pygame.sprite.spritecollide(self,self.paddles,False):
			pygame.mixer.Sound.play(plob_sound)
			collision_paddle = pygame.sprite.spritecollide(self,self.paddles,False)[0].rect
			if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
				self.speed_x *= -1
			if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
				self.speed_x *= -1
			if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
				self.rect.top = collision_paddle.bottom
				self.speed_y *= -1
			if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
				self.rect.bottom = collision_paddle.top
				self.speed_y *= -1

	# reset ball position and restart game
	def reset_ball(self):
		self.active = False
		self.speed_x = randint(3, 5) * random.choice((-1,1))
		self.speed_y = randint(3, 5) * random.choice((-1,1))
		self.score_time = pygame.time.get_ticks()
		self.rect.center = (screen_width/2,screen_height/2)
		pygame.mixer.Sound.play(score_sound)

	# round counter, 3 2 1
	def restart_counter(self):
		current_time = pygame.time.get_ticks()
		countdown_number = 3

		if current_time - self.score_time <= 700:
			countdown_number = 3
		if 700 < current_time - self.score_time <= 1400:
			countdown_number = 2
		if 1400 < current_time - self.score_time <= 2100:
			countdown_number = 1
		if current_time - self.score_time >= 2100:
			self.active = True

		# displays counter
		time_counter = basic_font.render(str(countdown_number),True,accent_color)
		time_counter_rect = time_counter.get_rect(center = (screen_width/2,screen_height/2 + 50))
		pygame.draw.rect(screen,bg_color,time_counter_rect)
		screen.blit(time_counter,time_counter_rect)

# opponent class, inherits block class
class Opponent(Block):
	# creates base variables
	def __init__(self,path,x_pos,y_pos,speed):
		super().__init__(path,x_pos,y_pos)
		self.speed = speed

	# opponent movement
	def update(self,ball_group):
		if self.rect.top < ball_group.sprite.rect.y:
			self.rect.y += self.speed
		if self.rect.bottom > ball_group.sprite.rect.y:
			self.rect.y -= self.speed
		self.constrain()

	# bounds to screen
	def constrain(self):
		if self.rect.top <= 0: self.rect.top = 0
		if self.rect.bottom >= screen_height: self.rect.bottom = screen_height

# game manager class
class GameManager:
	# creates base variables
	def __init__(self,ball_group,paddle_group):
		self.player_score = 0
		self.opponent_score = 0
		self.ball_group = ball_group
		self.paddle_group = paddle_group

	# creates paddle and ball
	def run_game(self):
		# Drawing the game objects
		self.paddle_group.draw(screen)
		self.ball_group.draw(screen)

		# Updating the game objects
		self.paddle_group.update(self.ball_group)
		self.ball_group.update()
		self.reset_ball()
		self.draw_score()

	# checks if end score reached, restarts round
	def reset_ball(self):
		if self.ball_group.sprite.rect.right >= screen_width:
			self.opponent_score += 1
			if mode_select.ranked.ranked_bool:
				highscores.enter_score(self.player_score)
			if self.opponent_score == mode_select.single_player.end_score:
				win_screen.window_s_computer()
			self.ball_group.sprite.reset_ball()
		if self.ball_group.sprite.rect.left <= 0:
			self.player_score += 1
			if self.player_score == mode_select.single_player.end_score:
				win_screen.window_s_player()
			self.ball_group.sprite.reset_ball()

	# displays score
	def draw_score(self):
		player_score = basic_font.render(str(self.player_score),True,accent_color)
		opponent_score = basic_font.render(str(self.opponent_score),True,accent_color)

		player_score_rect = player_score.get_rect(midleft = (screen_width / 2 + 40,screen_height/2))
		opponent_score_rect = opponent_score.get_rect(midright = (screen_width / 2 - 40,screen_height/2))

		screen.blit(player_score,player_score_rect)
		screen.blit(opponent_score,opponent_score_rect)

# General setup
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1270
screen_height = 648
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong | by Asianguy_123')

# constants
bg_color = pygame.Color('#2F373F')
accent_color = (27,35,43)
basic_font = pygame.font.Font('freesansbold.ttf', 32)
plob_sound = pygame.mixer.Sound("sounds\pong.ogg")
score_sound = pygame.mixer.Sound("sounds\score.ogg")
middle_strip = pygame.Rect(screen_width/2 - 2,0,4,screen_height)

# Game objects
player = Player('images\Paddle.png',screen_width - 20,screen_height/2,5)
opponent = Opponent('images\Paddle.png',20,screen_width/2,5)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)
ball = Ball('images\Ball.png',screen_width/2,screen_height/2,4,4,paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

# main game function
def run():
	game_manager = GameManager(ball_sprite,paddle_group)
	Ball.reset_ball(ball)
	running = True
	# main loop
	while running:
		# event detection
		for event in pygame.event.get():
			# if quit, return to mode select
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				# if esc, return to mode select
				if event.key == pygame.K_ESCAPE:
					running = False
				# player movement up and down
				if event.key == pygame.K_UP:
					player.movement -= player.speed
				if event.key == pygame.K_DOWN:
					player.movement += player.speed
			# detect key release to stop movement
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					player.movement += player.speed
				if event.key == pygame.K_DOWN:
					player.movement -= player.speed
		
		# Background Stuff
		screen.fill(bg_color)
		pygame.draw.rect(screen,accent_color,middle_strip)
		
		# Run the game
		game_manager.run_game()

		# Rendering
		pygame.display.flip()
		clock.tick(120)

