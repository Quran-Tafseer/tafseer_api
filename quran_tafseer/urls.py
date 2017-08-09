from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.TafseerView.as_view()),
    url(r'^(?P<tafseer_id>[0-9]+)/(?P<sura_id>[0-9]+)/(?P<ayah_numb>[0-9]+)/$',
        view=views.AyahTafseerView.as_view()),
]
