from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.SuraListView.as_view()),
    url(r'^(?P<sura_num>[0-9]+)/$', view=views.SuraAyatTextView.as_view()),
    ]
