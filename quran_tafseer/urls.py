from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.TafseerView.as_view(), name='tafseer-list'),
    url(r'^(?P<tafseer_id>[0-9]+)/(?P<sura_index>[0-9]+)'
        r'/(?P<ayah_number>[0-9]+)/$',
        view=views.AyahTafseerView.as_view(), name='ayah-tafseer'),
    url(r'^(?P<tafseer_id>[0-9]+)/(?P<sura_index>[0-9]+)/'
        r'(?P<ayah_from>[0-9]+)/(?P<ayah_to>[0-9]+)/$',
        view=views.AyahTafseerRangeView.as_view(), name='ayah-tafseer'),
]
