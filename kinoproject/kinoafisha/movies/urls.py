
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Главная страница приложения
    path('movies/', views.movie_list, name='movie_list'),  # Список фильмов
]

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie_list, name='movie_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('my-tickets/', views.my_tickets, name='my_tickets'),
    path('buy-ticket/<int:movie_id>/', views.buy_ticket, name='buy_ticket'),
]