from numpy import arange, array, random
import numpy
import pygame
from pygame.constants import JOYAXISMOTION
from main import solve_game, valid
import time


pygame.font.init()


class GameGrid:
    board = []
    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(0)
        board.append(row)
    solution = []

    for i in range(0, 9):
        row = []
        for j in range(0,9):
            row.append(board[i][j])
        solution.append(row)
    array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    random.shuffle(array)
    c = 0
    for i in range(0, 4):
        solution[i][j] = array[c]
        c += 1
    for i in range(8, 3, -1):
        solution[i][j] = array[c]
        c += 1

    solve_game(solution)

    first_hint = [[4,4],[4,3],[4,2],[4,1],[3,1],[4,5],[4,6],[4,7],[5,7],[3,4],[2,4],[1,4],[1,5],[5,4],[6,4],[7,4],[7,3],[0,0],[0,8],[8,0],[8,8],[2,1],[1,6],[6,7],[7,2]] 
    second_hint = [[4,4],[3,3],[2,2],[1,1],[0,2],[5,5],[6,6],[7,7],[8,6],[3,5],[2,6],[1,7],[2,8],[5,3],[6,2],[7,1],[6,0]]
    rand_num = random.randint(0, 4)
    rand_num = rand_num % 2

    if rand_num == 0:
        for i in range(0, len(first_hint)):
            x = first_hint[i][0]    
            y = second_hint[i][1]
            board[x][y] = solution[x][y]
    else:
        for i in range(0, len(second_hint)):
            x = second_hint[i][0]   
            y = second_hint[i][1]
            board[x][y] = solution[x][y]


    def __init__(self, rows, columns, height, width):
        self.rows = rows
        self.height = height
        self.columns = columns
        self.width = width
        self.squares = [[Squares(self.board[i][j], i , j, width, height) for j in range(columns)] for i in range(rows)]
        self.game_model = None
        self.selected = None

    def check(self, value, r, c):  # row = r, column = c 
        # row = r 
        # column = c
        return self.solution[r][c] == value
    
    def update_game_model(self):
        self.game_model = [[self.cubes[i][j].value for j in range(self.columns)] for i in range(self.rows)]
    
    def set(self, value):
        # row = r 
        # column = c
        r, c = self.selected
        if self.squares[r][c].value == 0:
            self.sqares[r][c].set(value)
            self.update_game_model()

            if self.check(value, r, c):
                return True
            else: 
                self.squares[r][c].set(0)
                self.sqares[r][c].set_temp(0)
                self.update_game_model()
                return False
    
    def create(self, value):
        r, c = self.selected
        self.squares[r][c].set_temp(value)

    def draw_grid_lines(self, window):
        space = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                x = 4
            else:
                x = 1
            pygame.draw.line(window, (0,0,0), (0, i * space), (self.width, i * space), x)
            pygame.draw.line(window, (0,0,0), (i * space, 0), (i* space, self.height), x)
        
        for i in range(self.rows):
            for j in range(self.columns):
                self.squares[i][j].draw(window)

    
    
    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Squares:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_window(win, board, time, strikes):
    win.fill((222,169,181))
    
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw(win)


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main():
    win = pygame.display.set_mode((540,600))    #initialises the playing window
    pygame.display.set_caption("Sudoku Classic")
    board = GameGrid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


main()
pygame.quit()
        
        


    
