import pygame
import random
from solve import isSolved
from Ai import AiTurn


class Grid:
    # Keeps track of Naughts (0) and Crosses (1)
    def __init__(self):
        self.matrix = [
            [9, 9, 9],
            [9, 9, 9],
            [9, 9, 9]
        ]

    def change_position(self, pos, value):
        self.matrix[pos[1]][pos[0]] = value

# GUI
    def winningLine(self, startPos, endPos, window):
        # Draws line for column
        if startPos[0] == endPos[0]:
            X = (startPos[0])*myGame.gridWidth/3 + myGame.gridWidth/6
            startY = (myGame.gridHeight/100) * 5
            endY = myGame.gridHeight - (myGame.gridHeight/100) * 5
            pygame.draw.line(window, red, (X, startY), (X, endY), 4)
            myGame.isSolved = True
            pygame.display.flip()

        # Draws line for row
        elif startPos[1] == endPos[1]:
            Y = (startPos[1])*myGame.gridHeight/3 + myGame.gridHeight/6
            startX = (myGame.gridWidth/100) * 5
            endX = myGame.gridWidth - (myGame.gridWidth/100) * 5
            pygame.draw.line(window, red, (startX, Y), (endX, Y), 4)
            myGame.isSolved = True
            pygame.display.flip()

        # Draws line for diag
        else:
            startY = (myGame.gridHeight/100) * 5
            endY = myGame.gridHeight - (myGame.gridHeight/100) * 5
            startX = (myGame.gridWidth/100) * 5
            endX = myGame.gridWidth - (myGame.gridWidth/100) * 5
            if startPos != (0, 0):
                startY, endY = endX, startX
            pygame.draw.line(window, red, (startX, startY), (endX, endY), 4)
            pygame.display.flip()
            myGame.isSolved = True


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
        myGame.gameGrid.change_position(self.pos, 1)


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
        myGame.gameGrid.change_position(self.pos, -1)


class Button:
    def __init__(self, colour, pos, window):
        self.colour = colour
        self.position = pos
        self.window = window

    def draw(self):
        text = font.render("New Game", True, black)
        text_rect = text.get_rect(center=(60, 535))
        pygame.draw.rect(self.window, self.colour, self.position)
        self.window.blit(text, text_rect)
        pygame.display.flip()


# Main Game loop
class Game:
    def __init__(self, backgroundColour, gridHeight, gridWidth, windowHeight, windowWidth, frameRate):
        self.backgroundColour = backgroundColour
        self.gridHeight = gridHeight
        self.gridWidth = gridWidth
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.frameRate = frameRate
        self.gameGrid = Grid()
        self.isSolved = False

# Setting up environment
    def create_window(self):
        window = pygame.display.set_mode((self.windowHeight, self.windowWidth))
        window.fill(self.backgroundColour)
        pygame.display.set_caption('Naughts and Crosses')
        for i in range(2):
            pygame.draw.line(window, black, (0, (int(self.gridHeight/3)*(i+1))),
                             (self.gridHeight, int((self.gridHeight/3)*(i+1))), 4)
        for i in range(2):
            pygame.draw.line(window, black, (int((self.gridHeight/3)*(i+1)), 0),
                             (int((self.gridHeight/3)*(i+1)), self.gridWidth), 4)
        Button(white, (10, 510, 100, 50), window).draw()
        return window

# Time
    def clock(self, window, frameCount, frameRate):
        if self.isSolved:
            return
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

# On Click
    def on_click(self, window, mouse):
        if not self.isSolved:
            column = int(mouse[0] // (self.gridHeight/3))
            row = int(mouse[1] // (self.gridWidth/3))
            return (column, row)

# Print Winning
    def winningScreen(self, window, crossWin):
        pygame.draw.rect(window, white, (140, 510, 220, 50))
        if crossWin == 'cross':
            text = font.render("AI beat you", True, black)
        elif crossWin == 'naught':
            text = font.render("You win", True, black)
        else:
            text = font.render("Tie", True, black)

        text_rect = text.get_rect(center=(250, 535))
        window.blit(text, text_rect)
        pygame.display.flip()

# Print Turn 
    def playerTurn(self, naughtsTurn, window):
        pygame.draw.rect(window, white, (140, 510, 220, 50))
        if naughtsTurn:
            text = font.render("Naughts turn", True, black)
        else:
            text = font.render("Click for AI turn", True, black)
        text_rect = text.get_rect(center=(250, 535))
        window.blit(text, text_rect)

# Main Loop
    def main(self):
        global myGame
        window = self.create_window()
        running = True
        naughtsTurn = bool(random.randint(0, 1))
        self.playerTurn(naughtsTurn, window)
        frameCount = 0
        while running:
            mouse = pygame.mouse.get_pos()
            frameCount = self.clock(window, frameCount, self.frameRate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = self.on_click(window, mouse)
                    if naughtsTurn:
                        if not pos == None and pos[0] <= 2 and pos[1] <= 2 and abs(self.gameGrid.matrix[pos[1]][pos[0]]) == 9:
                            Naught(pos, window, self.gridWidth,
                                self.gridHeight).draw()
                            naughtsTurn = not naughtsTurn
                            self.playerTurn(naughtsTurn, window)
                    else:
                        pygame.draw.rect(window, white, (140, 510, 220, 50))
                        text = font.render("Finding AI solution", True, black)
                        text_rect = text.get_rect(center=(250, 535))
                        window.blit(text, text_rect)
                        pygame.display.flip()
                        AIpos = AiTurn(self.gameGrid.matrix)
                        Cross(AIpos, window, self.gridWidth,
                                self.gridHeight).draw()
                        naughtsTurn = not naughtsTurn
                        self.playerTurn(naughtsTurn, window)
                    if 10 < mouse[0] < 110 and 510 < mouse[1] < 560:
                        running = False
                        myGame = Game(white, 500, 500, 500, 570, 60)
                        myGame.main()
                    solution = isSolved(self.gameGrid.matrix)
                    if solution != None:
                        if solution[0] != 'tie':
                            self.gameGrid.winningLine(
                            solution[1], solution[2], window)
                            self.winningScreen(window, solution[0])
                        else:
                            self.winningScreen(window, None)
                            self.isSolved = True
                    


pygame.init()
font = pygame.font.Font(None, 25)
black = (0, 0, 0)
blue = (0, 50, 255)
white = (255, 255, 255)
red = (255, 0, 0)
myGame = Game(white, 500, 500, 500, 570, 60)
myGame.main()
