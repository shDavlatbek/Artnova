from modeltranslation.translator import TranslationOptions, translator
from .models import News, Medicine


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {
        'ru': ('title', 'content',), 
        'en': ('title', 'content',), 
        'default': ('title', 'content',)
    }
    fallback_languages = {
        'ru': ('title', 'content',), 
        'en': ('title', 'content',), 
        'default': ('title', 'content',)
    }
    
    
# class MedicineTranslationOptions(TranslationOptions):
#     fields = ('name')
#     required_languages = {
#         'ru': ('name'), 
#         'en': ('name'), 
#         'default': ('name')
#     }
#     fallback_languages = {
#         'ru': ('name'), 
#         'en': ('name'), 
#         'default': ('name')
#     }
    
translator.register(News, NewsTranslationOptions)
# translator.register(Medicine, MedicineTranslationOptions)
