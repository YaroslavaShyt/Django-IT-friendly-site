from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('set_cookie', views.set_cookie, name='set_cookie'),
    path('save_session', views.save_session, name='save_session'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('get_faq_data', views.get_faq_data, name='get_faq_data'),
    path('ask_question', views.ask_question, name='ask_question'),
    path('get_studying_names', views.get_studying_names, name='get_studying_names'),
    path('courses/get_study', views.get_study, name='get_study'),
    path('courses/buy_course', views.buy_course, name='buy_course'),
    path('get_study', views.get_study, name='get_study'),
    path('courses/get_user_studies', views.get_user_studies, name='get_user_studies'),
    path('get_user_studies', views.get_user_studies, name='get_user_studies'),
    path('team/get_user_studies', views.get_user_studies, name='get_user_studies')
]

