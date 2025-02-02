from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQAPIView(APIView):
    def get(self, request):
        """Fetch FAQs and support language-based translation."""
        cache.clear()  # ✅ Clear cache before returning data

        lang = request.GET.get("lang", "en")  # Default to English
        faqs = FAQ.objects.all()

        data = []
        for faq in faqs:
            question, answer = faq.get_translation(lang)
            data.append({"question": question, "answer": answer})

        return Response(data)
