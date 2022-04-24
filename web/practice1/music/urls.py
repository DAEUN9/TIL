from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('artists/', views.artist_list),
    path('artists/<artist_pk>/', views.artist_detail),
    path('artists/<artist_pk>/music/', views.create_music),
    path('music/', views.music_list),
    path('music/<music_pk>/', views.music_detail)
]
