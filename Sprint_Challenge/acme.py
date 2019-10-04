import unittest
import random


class Product():
    """
    Class Product:
    name = name of the proctuct
    price = price of the product(default 10)
    weight = weight of the product(default 20)
    flammability = of the product(default 0.5)
    identifier = identifier of the procuct(integer between 1000000 and 9999999)
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        Calculate ratio between price and weight
        """
        # I multiplied the integer by 1.0 to see decimals in my result
        # because the other way 10/20 is 0 and not 0.5
        ratio = (self.price * 1.0/(self.weight * 1.0))
        if ratio < 0.5:
            return ('Not so stealable...')
        elif (ratio >= 0.5 and ratio < 1.0):
            return ('Kinda stealable')
        else:
            return ('Very stealable!')

    def explode(self):
        """
        Calculate rate of a possible explossion
        between flammability and weight
        """
        explosion = (self.flammability * self.weight)
        if explosion < 10:
            return ('...fizzle')
        elif (explosion >= 10 and explosion < 50):
            return('...boom!')
        else:
            return('...BABOOM!!')


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)
        self.name = name
        self.weight = weight

    def explode(self):
        return("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            return ('That tickles.')
        elif (self.weight >= 5 and self.weight < 15):
            return('Hey that hurt!')
        else:
            return('OUCH!')
