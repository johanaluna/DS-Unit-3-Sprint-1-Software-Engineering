#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, NAME, NOUN


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5"""
        prod = Product('Test Product Luna')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        """Test stealability"""
        prod = Product('Luna Product', price=10, weight=3, flammability=1.0)
        self.assertEqual(prod.stealability(), 'Very stealable!')

    def test_explode(self):
        """Test explode"""
        prod = Product('Luna Product', price=10, weight=3, flammability=1.0)
        self.assertEqual(prod.explode(), '...fizzle')


class AcmeProductTests_2part(unittest.TestCase):
    def test_default_num_products(self):
        list_products = generate_products()
        self.assertEqual(len(list_products), 30)

    def test_legal_names(self):
        names = generate_products()
        #self.assertIn(names[0], NAME)


if __name__ == '__main__':
    unittest.main()
