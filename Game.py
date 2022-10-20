import random

import pygame
import pygwidgets
from Box import Start, Box, Reset

N_BOXES = 16
SELECTIVE_ONE = '1'
SELECTIVE_TWO = '2'
MATCHES = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
POINTS = 0
SCORE = 0

# noinspection PyAttributeOutsideInit
class Game:
    def __init__(self, window):
        # AUDIO ASSETS
        self.window = window
        self.switch = True
        self.win = pygame.mixer.Sound('assets/win.mp3')
        self.match = pygame.mixer.Sound('assets/pufferfish.mp3')
        self.wrong = pygame.mixer.Sound('assets/wrong.mp3')
        self.click = pygame.mixer.Sound('assets/click.mp3')
        self.win.play()  # PLAY THE SCREAM ON START
        # AUDIO ASSETS

        # SCORE REPRESENTATION
        self.p = POINTS
        self.s = SCORE
        self.win = window
        # SCORE REPRESENTATION

        # OVERLAY TEXT SETTING / MODDING
        self.oInfoDisplay = pygwidgets.DisplayText(window, (20, 20), fontSize=32)
        self.oInfoDisplay2 = pygwidgets.DisplayText(window, (60, 380), fontSize=25)
        self.oPoints = pygwidgets.DisplayText(window, (20, 40), fontSize=32)
        self.oInfoDisplay.setText('  Very Meme-y Matching Game!')
        self.oPoints.setText('  Points: ' + str(self.p))
        self.oInfoDisplay2.setText('Start Game                                  Reset All')
        # OVERLAY TEXT SETTING / MODDING

        self.reset()  # BECAUSE:

    def reset(self):
        # SHUFFLING
        random.shuffle(MATCHES)
        # SHUFFLING

        # BOX DEFAULTS
        self.x = 20
        self.y = 90  # THIS SETS MY Y TO 90- WILL BE USED AS A DEFAULT COORDINATE
        self.X_INCREMENT = 110
        self.Y_INCREMENT = 50
        self.boxList = []  # All Guessing boxes
        self.startBox = []  # All Start boxes
        self.resetBox = []  # All Reset boxes
        # BOX DEFAULTS

        # BOX LOCATION DEFAULTS
        self.sBox = Start(self.window, 55, 400)  # THIS SETS STARTING WINDOW COORDS
        self.rBox = Reset(self.window, 305, 400)
        self.startBox.append(self.sBox)  # APPENDING THE START BOX
        self.resetBox.append(self.rBox)
        # BOX LOCATION DEFAULTS

        for thisVariableIterates in range(0, N_BOXES):
            if (thisVariableIterates % 4) == 0:  # EVERY 4, SO SOMETHING
                self.x = 20  # SET THE VARIABLE X TO 20
                self.y = self.y + self.Y_INCREMENT  # SET "Y" TO ITSELF + THE ITERATOR TO GO LOWER
            iterator = int(MATCHES[0 + thisVariableIterates])
            oBox = Box(self.window, self.x, self.y, iterator)
            self.boxList.append(oBox)  # APPEND THE BOX TO THE BOX LIST
            self.x = self.x + self.X_INCREMENT

        for thisVariableIterates in self.boxList:
            thisVariableIterates.hide()  # ...HIDE THEM

    def handleEvent(self, e):
        for sBox in self.startBox:  # ITERATE USING THE sBOX VARIABLE (ARBITRARY) THROUGH THE ALL OF THE STARTBOXES
            if sBox.handleEvent(e):
                for thisVariableIterates in self.boxList:
                    thisVariableIterates.show()

        for rBox in self.resetBox:  # ITERATE USING THE rBOX VARIABLE (ARBITRARY) THROUGH THE ALL OF THE RESETBOXES
            if rBox.handleEvent(e):
                self.reset()  # RESET THE GAME

        for oBox in self.boxList:  # ITERATE USING THE oBOX VARIABLE (ARBITRARY) THROUGH THE ALL OF THE BOXES
            if oBox.handleEvent(e):  # HANDLE THE EVENTS IN THIS BOX
                if self.switch:
                    self.fir = oBox.getPoints()  # SAVE DATA OF BOX
                    self.click.play()  # PLAY SOUND
                    self.switch = False  # TOGGLE SWITCH
                elif not self.switch:
                    self.sec = oBox.getPoints()
                    self.click.play()  # PLAY SOUND
                    if self.fir == self.sec:
                        self.p = self.p + 10  # ADD POINTS
                        self.s = self.s + 2  # ADD POINTS
                        self.oPoints.setText('  Points: ' + str(self.p))  # SET POINTS TEXT
                        self.match.play()  # PLAY SOUND
                        for i in self.boxList:
                            j = i.getPoints()
                            if j == self.fir:
                                i.hide()  # HIDE THE BOXES
                        self.switch = True  # TOGGLE SWITCH
                    elif self.fir != self.sec:
                        self.wrong.play()  # PLAY SOUND
                        self.p = self.p - 2  # REMOVE POINTS
                        self.oPoints.setText('  Points: ' + str(self.p))  # SET POINTS TEXT
                        for i in self.boxList:
                            j = i.getPoints()
                            if j == self.sec:
                                i.show()  # RETURN BOXES
                            if j == self.fir:
                                i.show()  # RETURN BOXES
                        self.switch = True  # TOGGLE SWITCH

    # THIS IS WHERE IM DOING MY INITIAL DRAWING
    def draw(self):
        for oBox in self.boxList:  # FOR EVERY BOX IN THE LIST...
            oBox.draw()  # DRAW IT
        self.sBox.draw()  # DRAW BOX
        self.rBox.draw()  # DRAW BOX
        self.oInfoDisplay.draw()  # DRAW TEXT
        self.oInfoDisplay2.draw()  # DRAW TEXT
        self.oPoints.draw()  # DRAW TEXT
