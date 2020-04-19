from django.urls import path

from . import views

urlpatterns = [
    path('',
         view=views.TafseerView.as_view(),
         name='tafseer-list'),
    path('<int:tafseer_id>/',
         view=views.TafseerBooksDetailsView.as_view(),
         name='tafseer-book-details'),
    path('<int:tafseer_id>/',
         view=views.TafseerBooksDetailsView.as_view(),),
    path('<int:tafseer_id>/<int:sura_index>/<int:ayah_number>/',
         view=views.AyahTafseerView.as_view(),
         name='ayah-tafseer'),
    path('<int:tafseer_id>/<int:sura_index>/<int:ayah_number>',
        view=views.AyahTafseerView.as_view()),
    path('<int:tafseer_id>/<int:sura_index>/<int:ayah_from>/<int:ayah_to>/',
         view=views.AyahTafseerRangeView.as_view(),
         name='ayah-tafseer-range'),
    path('<int:tafseer_id>/<int:sura_index>/<int:ayah_from>/<int:ayah_to>',
         view=views.AyahTafseerRangeView.as_view()),
]
