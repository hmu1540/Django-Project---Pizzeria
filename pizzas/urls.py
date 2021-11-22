from django.urls import path
from . import views
import pizzas

app_name = 'pizzas' 
# The variable app_name helps Django distinguish this urls.py file from files of the same name in other apps within the project


urlpatterns = [
    path('', views.index, name='index'),
    # Django ignores the base URL for the project (http://localhost:8000/), so the empty string ('') matches the base URL. 
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int: pizza_id>/', views.pizza, name='pizza'),
]