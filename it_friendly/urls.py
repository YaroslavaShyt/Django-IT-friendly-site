from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/courses', views.courses, name='courses'),
    path('/team', views.team, name='team'),
    path('/set_cookie', views.set_cookie, name='set_cookie'),
    path('/save_session', views.save_session, name='save_session')

]
