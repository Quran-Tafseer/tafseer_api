from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.SuraListView.as_view(), name='sura-list'),
    url(r'^(?P<sura_num>[0-9]+)/(?P<number>[0-9]+)$',
        view=views.AyahTextView.as_view(), name='ayah-detail'),

]
