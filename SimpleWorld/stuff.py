import pygame
import os
import sys
'''
#print(pygame.sysfont.get_fonts())

b = 2
c = 3

a = b**2 + c**2

print(a)
'''
pygame.init()
WIDTH, HEIGHT = 900, 900

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
BG = pygame.transform.scale(pygame.image.load(os.path.join("background", "background.png")), (WIDTH, HEIGHT))


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
            font = pygame.font.SysFont('comicsans', 35)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


class Settings:
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
            font = pygame.font.SysFont('comicsans', 35)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


# buttons
food_button = Settings((0, 0, 0), HEIGHT-10, WIDTH-10, 130, 35, "")
drink_button = Button((0, 0, 0), 10, 45, 200, 35, "'d' to Give Water")


def redraw_window():
    WIN.blit(BG, (0, 0))
    food_button.draw(WIN)
    drink_button.draw(WIN)


run = True

while run:
    redraw_window()
    pygame.display.update()
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        # button keys and click button
        # can't get the key and mouse click if statements to work together
        # want to combine it all, just don't know how exactly
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                food_button.color = (75, 75, 75)
                print("clicked")
            if event.key == pygame.K_d:
                drink_button.color = (75, 75, 75)
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

