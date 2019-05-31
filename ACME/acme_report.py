#!/usr/bin/env python

"""
Part 4: Class Report
- Report functions and inventory
"""

from random import randomint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

result = []

for adjective in ADJECTIVES:
    for noun in NOUNS:
        result.append(adjective + noun)
sample = random.choices(result, k=30)


def generate_products(self=random.sample, 
                      name=random.choice(result), 
                      price=random.randint(5, 100), 
                      weight=random.randint(5, 100), 
                      flammability=random.uniform(0, 2.5)):
    return sample


def inventory_report(self):
    """
    Print out summary of products list
    """
    mean_price = sum(Product.price for Product in sample) / len(sample)
    mean_weight = sum(Product.weight for Product in sample) / len(sample)
    mean_flam = sum(Product.flammability for Product in sample / len(sample))
    return 'Number of Unique Product Names: ', sample.unique, 
    'Average Price: ', mean_price, "Average Weight: ", mean_weight, 
    "Average Flammability: ", mean_flam

if __name__ == '__main__':
    inventory_report(generate_products())

    # Linting Output
    # A few trailing whitespaces that cant 
    # seem to be fixed. and a single blank line 
    # at the end which won't disppear 