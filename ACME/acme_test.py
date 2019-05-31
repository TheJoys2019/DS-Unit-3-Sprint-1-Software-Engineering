#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class ACMEProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_default_product_flam(self):
        """Test default product price being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


class ACMEReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_num_products(self):
        """Test default product number being 30."""
        num = len(generate_products)
        self.assertEqual(num, 30)

    def test_legal_names(self):
        """Test product names being an adjective with a space and a noun."""
        prod = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)

if __name__ == '__main__':
    unittest.main()