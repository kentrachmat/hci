class ButtonModel :
    idle = 1
    hover = 2
    pressIn = 3
    pressOut = 4
    
    def __init__(self):
        self.state = self.idle

    def enter(self) :
        if self.state == self.idle :
            self.state = self.hover
        if self.state == self.pressOut :
            self.state = self.pressIn

    def leave(self) :
        if self.state == self.hover :
            self.state = self.idle
        if self.state == self.pressIn :
            self.state = self.pressOut

    def press(self) :
        if self.state == self.hover :
            self.state = self.pressIn

    def release(self) :
        if self.state == self.pressIn :
            self.action()
            self.state = self.hover
        if self.state == self.pressOut :
            self.state = self.idle

    def action(self):
        print("action")