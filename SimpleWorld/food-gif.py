import pygame
import sys
import os
import kivy

pygame.init()
clock = pygame.time.Clock()

WIDTH = 650
HEIGHT = 650
BG = pygame.transform.scale(pygame.image.load(os.path.join("background", "background.png")), (WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ANII")
FPS = 60
FRAMES = 0


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Food, self).__init__()
        self.food_animation = False
        self.food_sprites = []
        self.food_sprites.append(pygame.image.load(os.path.join("Sprites", "Food(1).png")))
        self.food_sprites.append(pygame.image.load(os.path.join("Sprites", "Food(2).png")))
        self.food_sprites.append(pygame.image.load(os.path.join("Sprites", "Food(3).png")))
        self.food_sprites.append(pygame.image.load(os.path.join("Sprites", "Food(4).png")))
        self.food_current_sprite = 0
        self.image = self.food_sprites[self.food_current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def food_move(self):
        self.food_animation = True

    def update(self, speed):
        if self.food_animation:
            self.food_current_sprite += speed
            if int(self.food_current_sprite) >= len(self.food_sprites):
                self.food_current_sprite = 0
                self.food_animation = False

        self.image = self.food_sprites[int(self.food_current_sprite)]


# creating sprites
food_sprites = pygame.sprite.Group()
food = Food(200, 200)
food_sprites.add(food)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                food.food_move()

    WIN.blit(BG, (0, 0))
    food_sprites.draw(WIN)
    food_sprites.update(1)
    pygame.display.flip()
    FRAMES += 1
    clock.tick(10)
