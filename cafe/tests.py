from django.test import TestCase
from .models import Product

class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            category='drink',
            price=2.99,
            cost=1.99,
            name='Coke',
            description='A refreshing drink',
            barcode='1234567890',
            exp_date='2023-12-31',
            size='small',
            create_date='2022-04-16 15:30:00',
        )

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.__str__(), self.product.name)
        self.assertEqual(self.product.category, 'drink')
        self.assertEqual(self.product.price, 2.99)
        self.assertEqual(self.product.cost, 1.99)
        self.assertEqual(self.product.description, 'A refreshing drink')
        self.assertEqual(self.product.barcode, '1234567890')
        self.assertEqual(self.product.exp_date, '2023-12-31')
        self.assertEqual(self.product.size, 'small')
        self.assertEqual(self.product.create_date, '2022-04-16 15:30:00')