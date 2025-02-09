from typing import Any, Iterable
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.utils.safestring import mark_safe
from django.http import HttpRequest
from .models import News, SiteSettings, SiteSocialMedia, ContactPerson, \
        ContactPersonSocialMedia, Team, TeamSocialMedia, LicenseAchievement, Service, Event, \
        EventImage, Partner, Gallery
from modeltranslation.admin import TranslationAdmin
from django import forms
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
class NewsAdmin(TranslationAdmin):

    prepopulated_fields = {
      "slug": ("title_uz",)
    }
    
class SiteSettingsSocialMediaInline(admin.TabularInline):
    model = SiteSocialMedia
    extra = 0
    

class ContactPersonSocialMediaInline(admin.TabularInline):
    model = ContactPersonSocialMedia
    extra = 0


class TeamSocialMediaInline(admin.TabularInline):
    model = TeamSocialMedia
    extra = 0


class TranslationSocialMediaExtra(TranslationAdmin):
    readonly_fields = ('extra_display',)


    def extra_display(self, obj):
        # Compute or format some extra data for display.
        html = (
            "<div style='padding: 10px; background-color: #f0f0f0; border-radius: 5px;'>"
            "Ikonka nomini "
            "<a href='https://fontawesome.com/v6/search?ic=free' target='_blank'>BU YERDAN</a> oling, "
            "misol uchun: <code>fa-brands fa-telegram</code>"
            "</div>"
        )
        return mark_safe(html)

    extra_display.short_description = ""


class SiteSettingsAdmin(TranslationSocialMediaExtra):

    inlines = [SiteSettingsSocialMediaInline]
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


class ContactPersonAdmin(TranslationSocialMediaExtra):
    inlines = [ContactPersonSocialMediaInline]


class TeamAdmin(TranslationSocialMediaExtra):
    inlines = [TeamSocialMediaInline]
    list_display = ('image_tag', 'full_name', 'position',)
    list_display_links = ('full_name',)


class LicenseAchievementAdmin(TranslationAdmin):
    list_display = ('image_tag', 'title', 'achievement_type',)
    list_display_links = ('title',)


class ServiceAdmin(TranslationAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {
      "slug": ("title_uz",)
    }
    

class EventAdmin(TranslationAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {
      "slug": ("title_uz",)
    }


class EventImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)
    list_display_links = ('image_tag',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)
    list_display_links = ('image_tag',)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title',)
    list_display_links = ('title',)



admin.site.register(News, NewsAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(EventImage, EventImageAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(LicenseAchievement, LicenseAchievementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Service, ServiceAdmin)