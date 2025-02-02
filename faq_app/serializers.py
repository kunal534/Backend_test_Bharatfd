from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['question', 'answer']

    def get_question(self, obj):
        """Get the question based on the selected language."""
        lang = self.context.get('request').query_params.get('lang', 'en')
        return getattr(obj, f'question_{lang}', obj.question)

    def get_answer(self, obj):
        """Get the answer based on the selected language."""
        lang = self.context.get('request').query_params.get('lang', 'en')
        return getattr(obj, f'answer_{lang}', obj.answer)
