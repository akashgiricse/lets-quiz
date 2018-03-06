from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^play/$', views.play, name='play'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^submission-result/(?P<attempted_question_pk>\d+)/', views.submission_result, name='submission_result'),

]
