from django.conf.urls import url
from . import views

app_name = "administration"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
]