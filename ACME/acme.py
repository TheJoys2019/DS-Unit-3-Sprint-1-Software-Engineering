"""
Product Classes for ACME Corporation
"""

import random

# Part One: Keeping It Classy


class Product:
    """
    Product Class for ACME:
    - Assigns:
        - name (str): name of product
        - price (int): price of product(default 10)
        - weight (int): weight of product (default 20)
        - flammability (float): flammability of product (default 0.5)
    - Also randomly creates identifier attribute between 10000 - 9999999
    """
    
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)


# Part Two: Objects and Go!

    def stealability(self):
"""Stealability is calculated by:
        - Price divided by Weight
    - 3 conditions:
        - If output is less than 0.5, it will return "Not So Stealable..."
        - If output is greater than or equal to 0.5 but
            less than 1.0 it will return "Kinda stealable."
        - Otherwise returns "Very Stealable!"
"""
    output = (self.price / self.weight)
        if output < 0.5:
            return "Not So Stealable..."
        elif output >= 0.5 and output < 1.0:
            return "Kinda Stealable."
        return "Very Stealable!"

    def explode(self):
    """
    Explode calcuates the flammability times the weight, 
    and then returns a message:
        - If the product is less than 10, return "...fizzle."
        - If it is 10<= x < 50, return "...boom!"
        - Otherwise, return "...BABOOM!!"
    """    
        boom = (self.flammability * self.weight)
    
        if boom < 10:
            return "...fizzle."
        elif boom >= 10 and boom < 50:
            return "...boom!"
        return "...BABOOM!!"

    # Part 3: A Proper Inheritance

class BoxingGlove(Product):
    """
    Boxing Glove product is subclass based on Product class for ACME.
    """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    
    def explode(self):
        """
        Override the 'explode' method to always return '...it's a glove.'
        """

        return "...it's a glove."

    def punch(self):
        """
        Arguments:
            None
        Returns:
            (str)
            - "That tickles"
            - "Hey that hurt!"
            - "OUCH!"
        """

        if self.weight <5:
            return "That tickles"
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        return "OUCH!"