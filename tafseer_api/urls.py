from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^quran/', include('quran_text.urls')),
    url(r'^tafseer/', include('quran_tafseer.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    ]

urlpatterns += i18n_patterns(url(r'^', include('docs.urls')))
