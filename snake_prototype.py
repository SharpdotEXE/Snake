import pygame
import random

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
        self.position = [self.x, self.y]
        self.counter = 0
        self.body = [self.position, [self.x - self.width, self.y], [self.x - self.width * 2, self.y]]


    def render(self):

        for block in self.body:

            pygame.draw.rect(screen, self.color, (block[0], block[1], self.width, self.height))


    def update_hitbox(self):

        self.hitbox = pygame.Rect(self.x + self.speed, self.y, self.width, self.height)


    def increase_counter(self):

        self.counter += 1


    def move(self):

        self.update_hitbox()

        self.increase_counter()

        if self.counter % 10 == 0:
            if self.direction == 'right':
                self.x += self.speed
            if self.direction == 'left':
                self.x -= self.speed
            if self.direction == 'down':
                self.y += self.speed
            if self.direction == 'up':
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

        # work on this later
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


    def check_collision(self):

        if self.x == apple.x:
            if self.y == apple.y:
                pass


    def cheat_mode(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_m]:

            if self.direction == 'right':

                pygame.draw.line(screen, 'white', [self.x + .5 * self.width, self.y + .5 * self.width,],
                                 [right_boundary, self.y + .5 * self.width], 5)

            if self.direction == 'left':

                pygame.draw.line(screen, 'white', [self.x + .5 * self.width, self.y + .5 * self.width,],
                                 [left_boundary, self.y + .5 * self.width], 5)

            if self.direction == 'down':

                pygame.draw.line(screen, 'white', [self.x + .5 * self.width, self.y + .5 * self.width, ],
                                 [self.x + .5 * self.width, bottom_boundary], 5)

            if self.direction == 'up':

                pygame.draw.line(screen, 'white', [self.x + .5 * self.width, self.y + .5 * self.width, ],
                                 [self.x + .5 * self.width, top_boundary], 5)


        #pygame.draw.line(screen, 'cyan', [x_start, y_start], [x_end, y_end], 5)


    def update_body(self):

        self.position = [self.x, self.y]

        if self.direction == 'right':
            self.body = [self.position, [self.x - self.width, self.y], [self.x - self.width * 2, self.y]]

        if self.direction == 'left':
            self.body = [self.position, [self.x + self.width, self.y], [self.x - self.width * 2, self.y]]

        if self.direction == 'down':
            self.body = [self.position, [self.x, self.y - self.width], [self.x, self.y - self.width * 2]]

        if self.direction == 'up':
            self.body = [self.position, [self.x, self.y + self.width], [self.x, self.y + self.width * 2]]


    def update(self):
        self.render()
        self.move()
        self.check_change_direction()
        self.check_collision()
        self.cheat_mode()
        self.check_wall_loss()
        self.update_body()



class Apple:

    def __init__(self):

        self.width = 25
        self.height = 25
        self.x = random.choice(range(0, width, 25))
        self.y = random.choice(range(0, height, 25))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (212, 36, 56)
        self.square = pygame.Surface((self.width, self.height))


    def render(self):


        self.square.fill(self.color)
        pygame.draw.rect(self.square, self.color, (self.x, self.y, self.width, self.height))
        screen.blit(self.square, (self.x, self.y))


    def update_hitbox(self):

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        if pygame.Rect.colliderect(self.hitbox, snake.hitbox):
            self.x = random.choice(range(left_boundary, right_boundary, 25))
            self.y = random.choice(range(top_boundary, bottom_boundary, 25))


    def check_collision(self):

        if self.x == snake.x:
            if self.y == snake.y:
                self.x = random.choice(range(left_boundary, right_boundary, 25))
                self.y = random.choice(range(top_boundary, bottom_boundary, 25))


    def update(self):
        self.render()
        self.check_collision()



game_counter = 0

top_boundary = 0
bottom_boundary = 475
left_boundary = 0
right_boundary = 475

fpsClock = pygame.time.Clock()
fps = 60
color = (0, 0, 0)
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

snake = Snake()
apple = Apple()


def debug():

    print(snake.direction, snake.body)
    # print(snake.body)
    # print(snake.position)
    # print(len(snake.body))
    # print(apple.x, apple.y)
    # print(f'snake hitbox = {snake.hitbox},     apple hitbox = {apple.hitbox}')
    # print(snake.x, snake.y, apple.x, apple.y)
    # print(f'x={snake.x}, y={snake.y}, w={snake.width}, h={snake.height}')
    # print(snake.hitbox)
    # print(snake.direction)
    # print(snake.x, snake.y)



running = True
while running:

    screen.fill(color)


    snake.update()
    apple.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fpsClock.tick(fps)
    pygame.display.flip()

    ### debug tools

    game_counter += 1
    if game_counter % 15 == 0:
        print()
        debug()
