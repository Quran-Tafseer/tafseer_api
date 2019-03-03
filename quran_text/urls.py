from django.urls import path

from . import views

urlpatterns = [
    path('',
         view=views.SuraListView.as_view(), name='sura-list'),
    path('<int:sura_num>/<int:number>/',
         view=views.AyahTextView.as_view(), name='ayah-detail'),
    path('<int:sura_num>/<int:number>',
         view=views.AyahTextView.as_view()),
]
