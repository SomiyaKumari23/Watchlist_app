from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name='movies_list'),  # example route
    path('<int:pk>/', views.movie_detail, name='movie-detail')
]
