from django.contrib import admin
from .models import News, Medicine
from modeltranslation.admin import TranslationAdmin


class NewsAdmin(TranslationAdmin):
    prepopulated_fields = {
      "slug": ("title_uz",)
    }
  
admin.site.register(News, NewsAdmin)
admin.site.register([Medicine])