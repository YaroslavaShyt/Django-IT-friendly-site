from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import models
from django.utils.encoding import smart_str
from .forms import SignUpForm, AuthenticationForm, SignInForm, PaymentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Studying, StudyingDirection, FAQ, StudyingType, User
from django.contrib import messages
from django.core import serializers
from datetime import datetime


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('courses')
        else:
            print(form.errors)
            messages.error(request, form.errors.get('__all__'))
    return redirect('index')


def sign_up(request):
    if request.user.is_anonymous:
        print('user is anonymous')
        if request.method == 'POST':
            print('method is post')
            form = SignUpForm(request.POST)
            if form.is_valid():
                print('form is valid')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    print('user is not none')
                    login(request, new_user)
                    print('after login')
                    return redirect('courses')
            else:
                messages.error(request, form.errors)
                return redirect('index')
    else:
        return redirect('courses')
    return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')


def index(request):
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    return render(request, 'it_friendly/index.html', context={'sign_in_form': sign_in_form,
                                                              'sign_up_form': sign_up_form})


def get_faq_data(request):
    faq = FAQ.objects.all()
    serialized_faq = []
    for item in faq:
        serialized_faq.append({
            'question': item.question,
            'answer': item.answer
        })
    return JsonResponse({'data': serialized_faq})


def get_studying_names(request):
    studying = Course.objects.all()
    studying_names = [study.name for study in studying]
    return JsonResponse(studying_names, safe=False)


def courses(request):
    print('in courses start')
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    payment_form = PaymentForm()
    studying_directions = StudyingDirection.objects.all()
    course_type = request.GET.get('study-type')
    if course_type is not None and 'courses' in course_type:
        studies = Studying.objects.filter(type='Курс')
    else:
        studies = Studying.objects.all()
    print('in courses before render')
    return render(request, 'it_friendly/courses.html',
                  context={'studies': studies,
                           'studying_directions': studying_directions,
                           'sign_in_form': sign_in_form,
                           'sign_up_form': sign_up_form,
                           'payment_form': payment_form
                           })


def get_study(request):
    study_id = request.GET.get('study_id')
    study = Studying.objects.get(id=study_id)
    study_data = {
        'id': study.id,
        'type': study.type.title,
        'title': study.title,
        'price': study.price,
        'image': study.image,
        'level': study.level,
        'details': study.details,
        'participants': study.participants,
        'programs_settings': study.programs_settings,
        'beginning': study.beginning,
        'time': study.time
    }
    return JsonResponse(study_data)


def team(request):
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    context = {'sign_in_form': sign_in_form,
               'sign_up_form': sign_up_form}
    return render(request, 'it_friendly/team.html', context=context)


def set_cookie(request):
    response = redirect('/it_friendly')
    value = smart_str(request.POST.get('name'), encoding='utf-8', strings_only=True)
    response.set_cookie('name', value)
    return response


def save_session(request):
    request.session['name'] = request.POST.get('name')
    return redirect('/it_friendly')


def buy_course(request):
    data = {'success': False}
    if request.method == 'POST':
        print('in form post')
        form = PaymentForm(request.POST)
        if form.is_valid():
            print('is valid')
            if request.POST.get('card_number') != '0000000000000000' \
                    and len(request.POST.get('card_number')) == 16:
                print('inner check')
                data['success'] = True
         #       try:
                payment = StudyingToStudent(username_student=request.user.username, id_course=request.POST.get('courseId'))
                payment.save()
         #       except:
         #           data['errors'] = ['Не вдалось додати користувача.']
         #           return JsonResponse(data)
            else:
                print('inner check else')
                data['errors'] = ['Номер карти має містити 16 цифр.'] if len(request.POST.get('card_number')) != 16 else  ['Карта не доступна.']
        else:
            print('invalid')
            data['errors'] = list(form.errors.values())
    return JsonResponse(data)
