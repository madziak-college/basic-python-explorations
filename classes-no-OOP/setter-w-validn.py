class Colour:
    def __init__(self, r, g, b):
        self.r = r

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, new_r):
        if not isinstance(new_r, int):
            raise TypeError(f"red component must be an integer, not {type(new_r)}")
        if not 0 <= new_r <= 255:
            raise ValueError(f"invalid red component {new_r}, must be 0 <= r <= 255")
        self._r = new_r

c1 = Colour(355, 0, 0)
