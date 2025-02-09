import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import News, Service, SiteSettings, Team, LicenseAchievement, Event, EventImage, Partner, Gallery

PAGES_DIR = "pages"


class HomeView(View):
    def get(self, request):
        site_settings = SiteSettings.objects.first()
        return render(request,  
                      os.path.join(PAGES_DIR, "home.html"), 
                      {
                          'news': News.objects.all(), 
                          'settings': site_settings,
                          'teams': Team.objects.all(),
                          'licenses': LicenseAchievement.objects.filter(achievement_type='license'),
                          'achievements': LicenseAchievement.objects.filter(achievement_type='achievement'),
                          'services': Service.objects.all(),
                          'events': Event.objects.all(),
                          'event_images': EventImage.objects.all(),
                          'partners': Partner.objects.all(),
                          'galleries': Gallery.objects.all()
                        })





class ServiceDetail(View):
    def get(self, request, slug):
        site_settings = SiteSettings.objects.first()
        service_obj = Service.objects.get(slug=slug)
        services = Service.objects.all()
        return render(request, os.path.join(PAGES_DIR, "services-single.html"), {'service': service_obj, 'settings': site_settings, 'services': services})


class EventsAll(View):
    def get(self, request):
        return render(request, os.path.join(PAGES_DIR, "events.html"), {'events': Event.objects.all(), 'settings': SiteSettings.objects.first()})


class EventDetail(View):
    def get(self, request, slug):
        event_obj = Event.objects.get(slug=slug)
        return render(request, os.path.join(PAGES_DIR, "event-detail.html"), {'event': event_obj, 'latest_events': Event.objects.order_by('-created_at')[:4], 'settings': SiteSettings.objects.first()})


class NewsAll(View):



    def get(self, request):
        return render(request, os.path.join(PAGES_DIR, "news.html"), {'news': News.objects.all(), 'settings': SiteSettings.objects.first()})
    
    
class NewsDetail(View):
    def get(self, request, slug):
        news_obj = News.objects.get(slug=slug)
        news_obj.views += 1
        news_obj.save()
        return render(request, os.path.join(PAGES_DIR, "news-detail.html"), {'news': news_obj, 'latest_news': News.objects.order_by('-created_at')[:4], 'settings': SiteSettings.objects.first()})