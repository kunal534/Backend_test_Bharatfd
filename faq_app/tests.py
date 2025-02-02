from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )

    def test_faq_creation(self):
        """Ensure FAQ is created properly."""
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a Python web framework.")

    def test_translation(self):
        """Ensure translations are generated correctly."""
        self.faq.save()
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)

