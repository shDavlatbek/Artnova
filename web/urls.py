from django.contrib import admin
from django.urls import include, path
from .views import HomeView, NewsAll, NewsDetail, ServiceDetail, EventsAll, EventDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsAll.as_view(), name="news-all"),
    path('news/<slug:slug>/', NewsDetail.as_view(), name="news-detail"),
    path('services/<slug:slug>/', ServiceDetail.as_view(), name="service-detail"),
    path('events/', EventsAll.as_view(), name="events-all"),
    path('events/<slug:slug>/', EventDetail.as_view(), name="event-detail"),
]
