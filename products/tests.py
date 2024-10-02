from django.test import TestCase
from django.urls import reverse

class ProductViewTest(TestCase):
    def test_get_product(self):
        # Тестуємо ендпоінт для productId = 1
        response = self.client.get(reverse('product_detail', args=[1]))
        
        # Перевіряємо, що статус код відповіді 200
        self.assertEqual(response.status_code, 200)

        # Перевіряємо, що відповідь має правильний JSON формат
        expected_data = {
            "id": "1",
            "name": "1 name"
        }
        self.assertJSONEqual(response.content, expected_data)

    def test_get_non_existent_product(self):
        # Тестуємо ендпоінт для productId = 999, який не існує
        response = self.client.get(reverse('product_detail', args=[999]))
        
        # Перевіряємо, що статус код відповіді 404
        self.assertEqual(response.status_code, 404)
