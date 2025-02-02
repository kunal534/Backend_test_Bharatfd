from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    # Translated fields
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Automatically translate the question and answer into other languages and clear cache."""
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text

        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text

        super().save(*args, **kwargs)

        # ✅ Automatically clear cache when FAQ is updated
        cache.clear()

    def delete(self, *args, **kwargs):
        """Clear cache when FAQ is deleted."""
        super().delete(*args, **kwargs)
        cache.clear()

    def get_translation(self, lang):
        """Returns the translated question and answer based on the given language code."""
        translated_question = getattr(self, f'question_{lang}', self.question)
        translated_answer = getattr(self, f'answer_{lang}', self.answer)
        return translated_question, translated_answer

    def __str__(self):
        return self.question
