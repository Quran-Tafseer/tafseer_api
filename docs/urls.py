from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.IndexView.as_view())
    ]
