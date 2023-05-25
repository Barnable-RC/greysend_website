from accounts import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('members', views.list_users, name='list_users'),
    path('signup',views.signup, name='signup'),
    path("<username>/", views.profile_view, name='profile_view'),
    path('log_out', views.log_out, name='logout'),
    path('log_in', views.log_in, name="login"),
]
