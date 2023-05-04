from chat import views
from django.urls import path

urlpatterns = [
    #path('', views.landing_page, name='home'),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    
]