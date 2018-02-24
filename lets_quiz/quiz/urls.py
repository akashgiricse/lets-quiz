from django.conf.urls import url
from quiz import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^play/$', views.play, name='play'),

]
