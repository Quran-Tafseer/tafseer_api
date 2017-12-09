

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^quran/', include('quran_text.urls')),
    url(r'^tafseer/', include('quran_tafseer.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
