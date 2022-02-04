import imageio
import os
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

WIDTH = 650
HEIGHT = 650
BG = pygame.transform.scale(pygame.image.load(os.path.join("background", "background.png")), (WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ANII")
FPS = 60
FRAMES = 0


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


# creating sprites
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if run:
        player.move()

    WIN.blit(BG, (0, 0))
    moving_sprites.draw(WIN)
    moving_sprites.update(0.25)
    pygame.display.flip()
    FRAMES += 1
    clock.tick(10)
