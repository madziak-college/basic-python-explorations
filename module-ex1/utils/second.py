# The single dot means "from the current directory"
from .third import ThirdClass

class SecondClass:
    def __init__(self):
        self.third = ThirdClass()

    def action(self):
        return self.third.action()

