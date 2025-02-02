from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")  # Show these fields in the list view
    search_fields = ("question", "answer")  # Allow searching
    list_filter = ("created_at",)  # Enable filtering by date

admin.site.site_header = "FAQ Admin Panel"
admin.site.site_title = "FAQ Management"
