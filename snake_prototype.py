import pygame
import random
import time

pygame.init()




class Snake:

    def __init__(self):

        self.width = 25
        self.height = 25
        self.x = 250
        self.y = 250
        self.size = 1
        self.color = (30, 242, 19)
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.speed = 25
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)



    def load_image(self):

        self.square = pygame.Surface((self.width, self.height))
        self.square.fill(self.color)
        pygame.draw.rect(self.square, self.color, (self.x, self.y, self.width, self.height), 0)
        screen.blit(self.square, (self.x, self.y))


    def move(self):

        if counter % 10 == 0:
            if self.direction == 'right':
                self.x += self.speed
            elif self.direction == 'left':
                self.x -= self.speed
            elif self.direction == 'down':
                self.y += self.speed
            elif self.direction == 'up':
                self.y -= self.speed


        # if self.direction == 'right':
        #     self.x += self.speed
        # elif self.direction == 'left':
        #     self.x -= self.speed
        # elif self.direction == 'down':
        #     self.y += self.speed
        # elif self.direction == 'up':
        #     self.y -= self.speed


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


    def update_hitbox(self):

        if self.direction == 'right':
            self.hitbox = pygame.Rect(self.x + self.speed, self.y, self.width, self.height)

        if self.direction == 'left':
            self.hitbox = pygame.Rect(self.x - self.speed, self.y, self.width, self.height)

        if self.direction == 'up':
            self.hitbox = pygame.Rect(self.x, self.y + self.speed, self.width, self.height)

        if self.direction == 'down':
            self.hitbox = pygame.Rect(self.x, self.y - self.speed, self.width, self.height)


    def loss(self):

        #work on this later
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


class Apple:

    def __init__(self):

        self.width = 25
        self.height = 25
        self.x = random.choice(range(0, width, 25))
        self.y = random.choice(range(0, height, 25))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (212, 36, 56)


    def load_image(self):

        self.square = pygame.Surface((self.width, self.height))
        self.square.fill(self.color)
        pygame.draw.rect(self.square, self.color, (self.x, self.y, self.width, self.height), 0)
        screen.blit(self.square, (self.x, self.y))



    def update_hitbox(self):

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        if pygame.Rect.colliderect(self.hitbox, snake.hitbox):

            # for some reason end boundary - 1 is currently
            # only way to make apple spawn correctly at end boundary
            # will fix later
            self.x = random.choice(range(left_boundary, right_boundary, 25))
            self.y = random.choice(range(top_boundary, bottom_boundary, 25))
            print('apple eaten')


x = 0


top_boundary = 0
bottom_boundary = 475
left_boundary = 0
right_boundary = 475

fpsClock = pygame.time.Clock()
fps = 60
color = (0, 0, 0)
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

counter = 0



snake = Snake()
apple = Apple()


running = True
while running:

    counter += 1

    screen.fill(color)








    apple.load_image()
    apple.update_hitbox()

    snake.load_image()
    snake.move()
    snake.check_change_direction()
    snake.update_hitbox()

    snake.check_wall_loss()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    fpsClock.tick(fps)
    pygame.display.flip()


    ### debug tools

    # x += 1
    # if x % 45 == 0:
    print(apple.x, apple.y)
    #print(snake.x, snake.y)
    #     print(apple.hitbox)
        #print(f'x={snake.x}, y={snake.y}, w={snake.width}, h={snake.height}')
        #print(snake.hitbox)
        #print(snake.direction)
        #print(snake.x, snake.y)

