from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.SuraListView.as_view()),
    url(r'^(?P<sura_num>[0-9]+)/$',
        view=views.SuraAyatTextView.as_view()),
    url(r'^(?P<sura_num>[0-9]+)/(?P<ayah_from_num>[0-9]+)/(?P<ayah_to_num>[0-9]+)$',
        view=views.AyahRangeTextView.as_view()),
    url(r'^(?P<sura_num>[0-9]+)/(?P<number>[0-9]+)$',
        view=views.AyahTextView.as_view()),
]
