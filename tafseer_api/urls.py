from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    url(r'^quran/', include('quran_text.urls')),
    url(r'^tafseer/', include('quran_tafseer.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url('sentry-debug/', trigger_error),
    ]

urlpatterns += i18n_patterns(url(r'^', include('docs.urls')))
