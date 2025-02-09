from modeltranslation.translator import TranslationOptions, translator
from .models import News, SiteSettings, ContactPerson, Team, LicenseAchievement, Service, Event



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
    

class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('address', 'about_us')
    required_languages = {
        'ru': ('address', 'about_us'), 
        'en': ('address', 'about_us'), 
        'default': ('address', 'about_us')
    }

    fallback_languages = {
        'ru': ('address', 'about_us'), 
        'en': ('address', 'about_us'), 
        'default': ('address', 'about_us')
    }
    

class ContactPersonTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = {
        'ru': ('name',), 
        'en': ('name',), 
        'default': ('name',)
    }
    fallback_languages = {
        'ru': ('name',), 
        'en': ('name',), 
        'default': ('name',)
    }


class TeamTranslationOptions(TranslationOptions):
    fields = ('full_name', 'description', 'position')
    required_languages = {
        'ru': ('full_name', 'description', 'position',), 
        'en': ('full_name', 'description', 'position',), 
        'default': ('full_name', 'description', 'position',)
    }
    fallback_languages = {
        'ru': ('name',), 
        'en': ('name',), 
        'default': ('name',)
    }
    

class LicenseAchievementTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = {
        'ru': ('title',), 
        'en': ('title',), 
        'default': ('title',)
    }
    

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {
        'ru': ('title', 'content',), 
        'en': ('title', 'content',), 
        'default': ('title', 'content',)
    }
    
    
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {
        'ru': ('title', 'content',), 
        'en': ('title', 'content',), 
        'default': ('title', 'content',)
    }

    
translator.register(News, NewsTranslationOptions)
translator.register(SiteSettings, SiteSettingsTranslationOptions)
translator.register(ContactPerson, ContactPersonTranslationOptions)
translator.register(Team, TeamTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(LicenseAchievement, LicenseAchievementTranslationOptions)
translator.register(Service, ServiceTranslationOptions)