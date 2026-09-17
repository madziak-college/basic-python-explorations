# The single dot means "from the current directory"
from .third import ThirdClass

class FirstClass:
    def __init__(self):
        self.third = ThirdClass()
