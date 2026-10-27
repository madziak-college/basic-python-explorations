from ..core.third import ThirdClass

class SecondClass:
    def __init__(self):
        self.third = ThirdClass()

    def action(self):
        return self.third.action()

