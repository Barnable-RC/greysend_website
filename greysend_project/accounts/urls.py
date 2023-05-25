from accounts import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('members', views.list_users, name='list_users'),
    path('signup',views.signup, name='signup'),
    path("<str:user>/", views.profile_view, name='profile_view')
]


# re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
# re_path(r"^bio/(?P<username>\w+)/$", views.bio, name="bio"),
