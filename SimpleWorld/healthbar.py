import pygame
import sys
import os


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
        pygame.draw.rect(WIN, (255, 255, 255), (298, 10, self.health_bar_length, 25), 4)


pygame.init()
WIDTH, HEIGHT = 900, 900

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
BG = pygame.transform.scale(pygame.image.load(os.path.join("background", "background.png")), (WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = HealthBar()


def redraw():
    WIN.blit(BG, (0, 0))
    player.update()
    pygame.display.update()
    clock.tick(60)


run = True
while run:
    redraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.get_health(20)
            if event.key == pygame.K_DOWN:
                player.get_damage(20)
