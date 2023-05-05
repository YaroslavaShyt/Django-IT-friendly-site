from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('team', views.team, name='team'),
    path('set_cookie', views.set_cookie, name='set_cookie'),
    path('save_session', views.save_session, name='save_session'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('faq', views.get_faq_data, name='get_faq_data')
]
