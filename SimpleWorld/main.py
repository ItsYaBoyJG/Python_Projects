import pygame
import os
import sys
import random


# setup
pygame.init()
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
BG = pygame.transform.scale(pygame.image.load(os.path.join("background", "background.png")), (WIDTH, HEIGHT))
pygame.display.set_caption("Simple World")
FPS = 20
FRAMES = 0
clock = pygame.time.Clock()


# food and drinking button
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('arial', 25)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


# player pet/character class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.move_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.join("Sprites", "Stand(1).png")))
        self.sprites.append(pygame.image.load(os.path.join("Sprites", "Stand(2).png")))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def move(self):
        self.move_animation = True

    def update(self, speed):
        if self.move_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.move_animation = False

        self.image = self.sprites[int(self.current_sprite)]


# food sprite animation
# drinking sprite animation
# ticking health bar class
class HealthBar:
    def __init__(self):
        self.current_health = 100
        self.target_health = 100
        self.max_health = 100
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 0.75

    def get_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def update(self):
        self.advanced_health()

    def advanced_health(self):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0, 255, 0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255, 255, 0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(300, 10, health_bar_width, 24)
        transition_bar = pygame.Rect(health_bar.right, 10, transition_width, 24)

        pygame.draw.rect(WIN, (160, 0, 0), health_bar)
        pygame.draw.rect(WIN, transition_color, transition_bar)
        pygame.draw.rect(WIN, (255, 255, 255), (299, 10, self.health_bar_length, 25), 4)


# main
def main_function():
    # buttons and char setup
    food_button = Button((0, 0, 0), 10, 10, 105, 35, "Feed")
    drink_button = Button((0, 0, 0), 10, 45, 165, 35, "Give Water")
    idle_character_on_screen = pygame.sprite.Group()
    idle_character = Player(350, 350)
    idle_character_on_screen.add(idle_character)
    # ticking health bar set up
    # ticking_timer sets the event type id for set
    # set_timer(eventID, milliseconds) 2000 = 2 seconds
    # only using 2000 for time as debug purposes. will need to change time for actual game
    health = HealthBar()
    ticking_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ticking_timer, 15000)

    def draw_window():
        WIN.blit(BG, (0, 0))
        food_button.draw(WIN)
        drink_button.draw(WIN)
        idle_character_on_screen.draw(WIN)
        idle_character_on_screen.update(0.25)
        clock.tick(FPS)
        health.update()
        pygame.display.update()

    run = True
    while run:
        draw_window()
        pos = pygame.mouse.get_pos()
        idle_character.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == ticking_timer:
                health.get_damage(10)
            # button keys and click button
            # can't get the key and mouse click if statements to work together
            # want to combine it all, just don't know how exactly
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    food_button.color = (75, 75, 75)
                    health.get_health(25)
                    print("clicked")
                if event.key == pygame.K_d:
                    drink_button.color = (75, 75, 75)
                    health.get_health(15)
                    print('clicked')

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if food_button.is_over(pos):
                        food_button.color = (75, 75, 75)
                        print('clicked')
                    if drink_button.is_over(pos):
                        drink_button.color = (75, 75, 75)
                        print('clicked')

            else:
                food_button.color = (0, 0, 0)
                drink_button.color = (0, 0, 0)


if __name__ == '__main__':
    main_function()
