from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def test_create_product(self):
        # Тестуємо створення продукту
        product = Product.objects.create(name="Test Product")
        
        # Перевіряємо, що ім'я продукту правильне
        self.assertEqual(product.name, "Test Product")
        
        # Перевіряємо, що продукт є об'єктом моделі Product
        self.assertIsInstance(product, Product)

    def test_product_string_representation(self):
        # Тестуємо рядкове представлення продукту
        product = Product(name="Test Product")
        self.assertEqual(str(product), "Test Product")  # Перевіряємо, що рядкове представлення правильне
