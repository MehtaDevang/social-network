from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup', views.signup, name = 'signup'),
    url(r'^adduser', views.adduser, name = 'adduser'),
    url(r'^login', views.login, name = 'login'),
    url(r'^check_login', views.check_login, name = 'check_login'),
    url(r'^home', views.home, name = 'home'),
]