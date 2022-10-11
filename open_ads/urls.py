from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('', include('social_django.urls', namespace='social')),
    # re_path(r'^auth/', include('rest_framework_social_oauth2.urls')),
    path('', include('apps.homepage.urls')),
    path('', include('apps.user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
