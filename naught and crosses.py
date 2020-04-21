import pygame
import random
from solve import isSolved


class Grid:
    # Keeps track of Naughts (0) and Crosses (1)

    matrix = [
        [9, 9, 9],
        [9, 9, 9],
        [9, 9, 9]
    ]

    def change_position(self, pos, value):
        self.matrix[pos[1]][pos[0]] = value

    def reset(self):
        self.matrix = [
            [9, 9, 9],
            [9, 9, 9],
            [9, 9, 9]
        ]


class Cross:
    def __init__(self, pos, window, width, height):
        self.pos = pos
        self.window = window
        self.width = width
        self.height = height

# Draws Cross
    def draw(self):
        wOffset = self.width/16
        hOffset = self.height/16
        pygame.draw.line(self.window, black, (self.pos[0]*self.width/3 + wOffset, self.pos[1]*self.height/3+hOffset),
                         (self.pos[0]*self.width/3 + 100 + wOffset, self.pos[1]*self.height/3 + 100 + hOffset), 10)
        pygame.draw.line(self.window, black, (self.pos[0]*self.width/3 + 100 + wOffset, self.pos[1]*self.height/3 + hOffset),
                         (self.pos[0]*self.width/3 + wOffset, self.pos[1]*self.height/3 + 100 + hOffset), 10)
        Grid().change_position(self.pos, 1)


class Naught:
    def __init__(self, pos, window, width, height):
        self.pos = pos
        self.window = window
        self.width = width
        self.height = height

    # Draws Naught
    def draw(self):
        pygame.draw.circle(
            self.window, black, (int(self.pos[0]*self.width/3 + self.width/6), int(self.pos[1]*self.height/3 + self.height/6)), 60)
        pygame.draw.circle(
            self.window, white, (int(self.pos[0]*self.width/3 + self.width/6), int(self.pos[1]*self.height/3 + self.height/6)), 50)
        Grid().change_position(self.pos, -1)


class Button:
    def __init__(self, colour, pos, window):
        self.colour = colour
        self.position = pos
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, self.colour, self.position)


class Game:
    def __init__(self, backgroundColour, gridHeight, gridWidth, windowHeight, windowWidth, frameRate):
        self.backgroundColour = backgroundColour
        self.gridHeight = gridHeight
        self.gridWidth = gridWidth
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.frameRate = frameRate
        self.

    def create_window(self):
        # setting up environment
        window = pygame.display.set_mode((self.windowHeight, self.windowWidth))
        window.fill(self.backgroundColour)
        pygame.display.set_caption('Naughts and Crosses')
        for i in range(2):
            pygame.draw.line(window, black, (0, (self.gridHeight/3)*(i+1)),
                             (self.gridHeight, (self.gridHeight/3)*(i+1)), 4)
        for i in range(2):
            pygame.draw.line(window, black, ((self.gridHeight/3)*(i+1), 0),
                             ((self.gridHeight/3)*(i+1), self.gridWidth), 4)
        Button(blue, (10, 510, 100, 50), window).draw()
        return window

    def clock(self, window, frameCount, frameRate):
        clock = pygame.time.Clock()
        totalSeconds = frameCount // frameRate
        minutes = totalSeconds // 60
        seconds = totalSeconds % 60
        outputString = "Time: {0:02}:{1:02}".format(minutes, seconds)
        text = font.render(outputString, True, black)
        window.fill(white,  rect=(380, 530, 120, 40))
        window.blit(text, [380, 530])
        frameCount += 1
        clock.tick(frameRate)
        pygame.display.flip()
        return frameCount

    def on_click(self, window, mouse):
        column = int(mouse[0] // (self.gridHeight/3))
        row = int(mouse[1] // (self.gridWidth/3))
        return (column, row)

    def winningScreen(self, window, startPos, endPos, crossWin):
        pygame.draw.line(window, red, startPos, endPos, 3)

    def main(self):
        window = self.create_window()
        running = True
        naughtsTurn = bool(random.randint(0, 1))
        frameCount = 0
        while running:
            mouse = pygame.mouse.get_pos()
            frameCount = self.clock(window, frameCount, self.frameRate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.on_click(window, mouse)
                    if pos[0] <= 2 and pos[1] <= 2 and abs(Grid.matrix[pos[1]][pos[0]]) == 9:
                        if naughtsTurn:
                            Naught(pos, window, self.gridWidth,
                                   self.gridHeight).draw()
                        else:
                            Cross(pos, window, self.gridWidth,
                                  self.gridHeight).draw()
                        naughtsTurn = not naughtsTurn
                    elif 10 < mouse[0] < 110 and 510 < mouse[1] < 560:
                        #window = self.create_window()
                        running = False
                        mygame.main()
                    solution = isSolved(Grid.matrix)
                    if solution[0] == True:
                        self.winningScreen(
                            window, solution[1], solution[2], True)


pygame.init()
font = pygame.font.Font(None, 30)
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
mygame = Game(white, 500, 500, 500, 570, 60)
mygame.main()
pygame.quit()
