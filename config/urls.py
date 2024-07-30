from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.views.generic import TemplateView

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include(('delivery.urls', 'config'), namespace='delivery')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('users/', include(('users.urls', 'users'))),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('set_language/', set_language, name='set_language'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
