from django.test import TestCase
from django.urls import reverse

class LandingPagetest(TestCase):
    def test_get(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leads/landing.html')
