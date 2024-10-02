from django.test import TestCase
from django.test import TestCase
from django.urls import reverse

class ProductViewTest(TestCase):
    def test_get_product(self):
        response = self.client.get(reverse('get_product', args=[1]))
        self.assertEqual(response.status_code, 200)
        expected_data = {
            "id": "1",
            "name": "1 name"
        }
        self.assertJSONEqual(response.content, expected_data)
