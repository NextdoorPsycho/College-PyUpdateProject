import pygwidgets


class Box:

    def __init__(self, window, x, y, iterator):
        self.window = window
        self.iterator = iterator
        self.nPoints = 1
        self.x = x
        self.y = y

        self.button = pygwidgets.TextButton(self.window, (self.x, self.y), "")
        self.Num = pygwidgets.DisplayText(self.window, (self.x, self.y), "  " + str(self.iterator), fontSize=70)

    def handleEvent(self, event):
        if self.button.handleEvent(event):
            f = 1
            if f == 1:
                self.button.disable()
                f = 0
            if f == 0:
                self.button = pygwidgets.TextButton(self.window, (self.x, self.y), "" + str(self.iterator), fontSize=70)
                self.button.disable()
            return True

    def getPoints(self):
        return self.iterator

    def draw(self):
        self.Num.draw()
        self.button.draw()

    def hide(self):  # HIDE
        self.button.disable()
        self.button.hide()

    def show(self):  # SHOW
        self.button = pygwidgets.TextButton(self.window, (self.x, self.y), "UwU")
        self.button.enable()
        self.button.show()


class Start:

    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.button = pygwidgets.TextButton(self.window, (self.x, self.y), "Start", fontSize=50)

    def handleEvent(self, event):
        if self.button.handleEvent(event):
            self.button.disable()
            return True

    def draw(self):
        self.button.draw()

    def hide(self):  # HIDE
        self.button.disable()
        self.button.hide()

    def show(self):  # SHOW
        self.button.enable()
        self.button.show()


class Reset:

    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.button = pygwidgets.TextButton(self.window, (self.x, self.y), "Reset", fontSize=50)

    def handleEvent(self, event):
        if self.button.handleEvent(event):
            return True

    def draw(self):
        self.button.draw()

    def hide(self):  # HIDE
        self.button.disable()
