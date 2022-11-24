from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.homepage.urls')),
    path('', include('apps.user.urls')),
    path('', include('apps.ads.urls')),
    path('', include('apps.categories.urls')),
    path('', include('apps.messages_my.urls')),
    path('feedback/', include('apps.feedback.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('favorites/', include('apps.favorites.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
