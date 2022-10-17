import pygame

from Box import *

N_BOXES = 16
SELECTIVE_ONE = '1'
SELECTIVE_TWO = '2'
MATCHES = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
POPPER = 0
POINTS = 0
SCORE = 0


class Game:
    def __init__(self, window):
        random.shuffle(MATCHES)  # Mix
        pygame.mixer.music.load('assets/win.mp3')
        pygame.mixer.music.load('assets/wrong.mp3')
        pygame.mixer.music.load('assets/click.mp3')
        pygame.mixer.music.load('assets/pufferfish.mp3')
        self.win = pygame.mixer.Sound('assets/win.mp3')
        self.match = pygame.mixer.Sound('assets/pufferfish.mp3')
        self.wrong = pygame.mixer.Sound('assets/wrong.mp3')
        self.click = pygame.mixer.Sound('assets/click.mp3')
        self.win.play()

        self.p = POINTS
        self.s = SCORE
        self.win = window
        self.oInfoDisplay = pygwidgets.DisplayText(window, (20, 20), fontSize=32)
        self.oInfoDisplay2 = pygwidgets.DisplayText(window, (60, 380), fontSize=25)
        self.oPoints = pygwidgets.DisplayText(window, (20, 40), fontSize=32)

        self.x = 20
        self.y = 90
        self.X_INCREMENT = 110
        self.Y_INCREMENT = 50

        self.boxList = []  # All Guessing boxes
        self.startBox = []  # All Start boxes
        self.resetBox = []  # All Reset boxes

        self.sBox = Start(window, 55, 400)
        self.rBox = Reset(window, 305, 400)
        self.startBox.append(self.sBox)
        self.resetBox.append(self.rBox)
        for i in range(0, N_BOXES):
            if i == 4:
                self.x = 20
                self.y = self.y + self.Y_INCREMENT
            if i == 8:
                self.x = 20
                self.y = self.y + self.Y_INCREMENT
            if i == 12:
                self.x = 20
                self.y = self.y + self.Y_INCREMENT
            oBox = Box(window, self.x, self.y)
            self.boxList.append(oBox)
            self.x = self.x + self.X_INCREMENT

        for i in self.boxList:
            i.hide()

        self.oInfoDisplay.setText('  Very Meme Generic Matching Game!')
        self.oPoints.setText('  Points: ' + str(self.p))
        self.oInfoDisplay2.setText('Start Game                                  Reset All')
        self.fir = 20000  # unattainable values
        self.sec = 10000  # unattainable values
        self.switch = True

    def handleEvent(self, event):
        for sBox in self.startBox:
            if sBox.handleEvent(event):
                for i in self.boxList:
                    i.show()

        for rBox in self.resetBox:
            if rBox.handleEvent(event):
                for i in self.boxList:  # Restart the game
                    Game.__init__(self, self.win)

        for oBox in self.boxList:
            if oBox.handleEvent(event):
                if self.switch:
                    self.fir = oBox.getPoints()
                    self.click.play()
                    print("LOGGING FIRST POINT", self.fir)
                    self.switch = False
                elif not self.switch:
                    self.sec = oBox.getPoints()
                    self.click.play()
                    print("LOGGING SECOND POINT", self.sec)
                    if self.fir == self.sec:
                        print("MATCHED!!")
                        self.p = self.p + 10
                        self.s = self.s + 2
                        self.oPoints.setText('  Points: ' + str(self.p))
                        self.match.play()
                        for i in self.boxList:
                            j = i.getPoints()
                            if j == self.fir:
                                i.hide()
                        self.switch = True
                    elif self.fir != self.sec:
                        print("UNMATCHED!!!")
                        self.wrong.play()
                        self.p = self.p - 2
                        self.oPoints.setText('  Points: ' + str(self.p))
                        for i in self.boxList:
                            j = i.getPoints()
                            if j == self.sec:
                                i.show()
                            if j == self.fir:
                                i.show()
                        self.fir = 20000
                        self.sec = 10000
                        self.switch = True

    def draw(self):
        random.shuffle(self.boxList)
        for oBox in self.boxList:
            oBox.draw()
        self.sBox.draw()
        self.rBox.draw()
        self.oInfoDisplay.draw()
        self.oInfoDisplay2.draw()
        self.oPoints.draw()
