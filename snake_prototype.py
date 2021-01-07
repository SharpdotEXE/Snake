import pygame
import random

pygame.init()


class Snake:

	def __init__(self, width, height, x, y, size, hitbox, color, direction, speed):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.size = size
		self.hitbox = hitbox
		self.color = color
		self.direction = direction
		self.speed = speed

	def load_image(self):
		square = pygame.Surface((self.width, self.height))
		square.fill(self.color)
		pygame.draw.rect(square, self.color, (self.x, self.y, self.width, self.height), 0)
		screen.blit(square, (self.x, self.y))


	def movement(self):
		for event in pygame.event.get():
			if event.type == pygame.K_DOWN:
				self.y += self.speed
			elif event.type == pygame.K_UP:
				self.y -= self.speed
			elif event.type == pygame.K_RIGHT:
				self.x += self.speed
			elif event.type == pygame.K_LEFT:
				self.x -= self.speed





top_boundary = 0
bottom_boundary = 600
left_boundary = 0
right_boundary = 700

fpsClock = pygame.time.Clock()
fps = 60
color = (0, 0, 0)
width, height = 700, 600
screen = pygame.display.set_mode((width, height))

player = Snake(25, 25, 350, 300, 1, None, (30, 242, 19), None, 25)
			  #width, height, x, y, size, hitbox, color, direction, speed





running = True
while running:

	screen.fill(color)


	player.load_image()
	player.movement()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
	fpsClock.tick(fps)

pygame.quit()