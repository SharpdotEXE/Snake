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

    def starting_direction(self):
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'up':
            self.y -= self.speed

    def check_change_direction(self):

        keys = pygame.key.get_pressed()

        if self.direction != 'left':
            if keys[pygame.K_d]:
                self.direction = 'right'

        if self.direction != 'right':
            if keys[pygame.K_a]:
                self.direction = 'left'

        if self.direction != 'up':
            if keys[pygame.K_s]:
                self.direction = 'down'

        if self.direction != 'down':
            if keys[pygame.K_w]:
                self.direction = 'up'

    def loss(self):
        print('you suck')
        pygame.quit()

    def check_wall_loss(self):

        if self.y < top_boundary:
            self.loss()
        if self.y > bottom_boundary:
            self.loss()
        if self.x < left_boundary:
            self.loss()
        if self.x > right_boundary:
            self.loss()


top_boundary = 0
bottom_boundary = 750
left_boundary = 0
right_boundary = 750

fpsClock = pygame.time.Clock()
fps = 60
color = (0, 0, 0)
width, height = 750, 750
screen = pygame.display.set_mode((width, height))

player = Snake(25, 25, 375, 375, 1, None, (30, 242, 19), None, 2.5)
# width, height, x, y, size, hitbox, color, direction, speed

player.starting_direction()

running = True
while running:

    screen.fill(color)

    player.load_image()
    player.move()
    player.check_change_direction()

    player.check_wall_loss()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    fpsClock.tick(fps)

# print(player.x, player.y)

pygame.quit()
