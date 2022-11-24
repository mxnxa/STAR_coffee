from django.contrib import admin
from .models import MainContent

@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    list_display_links = ['id', 'title']
