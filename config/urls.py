from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

urlpatterns = [
    path('', include('web.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    # path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)