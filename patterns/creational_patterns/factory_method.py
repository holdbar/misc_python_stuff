# -*- coding: utf-8 -*-

class Culture:
    """
    Culture.
    """
    def __repr__(self):
        return self.__str__()

class Democracy(Culture):
    def __str__(self):
        return "Democracy"


class Dictatorship(Culture):
    def __str__(self):
        return "Dictatorship"


class Government:
    culture = ""
    def __str__(self):
        return self.culture.__str__()


    def __repr__(self):
        return self.culture.__repr__()

    def set_culture(self):
        """
        Set culture of the government.

        This is actually fabric method.
        """
        raise AttributeError("Not implemented Culture")


class GovernmentA(Government):
    """
    Government 1.
    """
    def set_culture(self):
        self.culture = Democracy()


class GovernmentB(Government):
    """
    Government 2.
    """
    def set_culture(self):
        self.culture = Dictatorship()


g1 = GovernmentA()
g1.set_culture()
print(str(g1))

g2 = GovernmentB()
g2.set_culture()
print(str(g2))


