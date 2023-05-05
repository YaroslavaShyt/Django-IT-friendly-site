from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.utils.encoding import smart_str
from .forms import SignUpForm, AuthenticationForm, SignInForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Studying


def sign_in(request):
    error = ''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('courses')
        else:
            error = 'Неправильні дані для входу'
    return redirect('index')


def sign_up(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login(request, new_user)
                    return redirect('courses')
    else:
        return redirect('courses')
    form = SignUpForm(request.POST)
    context = {'form': form}
    return render(request, 'it_friendly/index.html', context)


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
    print(faq)
    return JsonResponse(faq)


def courses(request):
    course_type = request.GET.get('study-type')
    if course_type is not None and 'courses' in course_type:
        studies = Studying.objects.filter(type='Курс')
    else:
        studies = Studying.objects.all()
    return render(request, 'it_friendly/courses.html', context={'studies': studies})


def team(request):
    return render(request, 'it_friendly/team.html')


def set_cookie(request):
    response = redirect('/it_friendly')
    value = smart_str(request.POST.get('name'), encoding='utf-8', strings_only=True)
    print(value, type(value))
    response.set_cookie('name', value)
    return response


def save_session(request):
    request.session['name'] = request.POST.get('name')
    return redirect('/it_friendly')
