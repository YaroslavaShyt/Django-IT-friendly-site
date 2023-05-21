from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import models
from django.utils.encoding import smart_str
from .forms import SignUpForm, AuthenticationForm, SignInForm, PaymentForm, QuestionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Studying, StudyingDirection, FAQ, StudyingType, User, StudyingStudent, CourseTimingRange, CourseLevel, CoursePriceRange
from django.contrib import messages
from django.core import serializers
from datetime import datetime
from django.core.mail import send_mail
from .letter_template import get_letter_template, get_ask_question_letter_template


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('courses')
        else:
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
                    return redirect('save_session')
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
    question_form = QuestionForm()
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    return render(request, 'it_friendly/index.html', context={'sign_in_form': sign_in_form,
                                                              'sign_up_form': sign_up_form,
                                                              'question_form': question_form
                                                              })


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
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    payment_form = PaymentForm()
    question_form = QuestionForm()

    level_filter = request.GET.get('level')
    direction_filter = request.GET.get('direction')
    availability_filter = request.GET.get('availability')
    cost_filter = request.GET.get('cost')
    study_type_filter = request.GET.getlist('study-type')

    studying_directions = StudyingDirection.objects.all()
    studies = Studying.objects.all()
    levels = CourseLevel.objects.all()
    prices = CoursePriceRange.objects.all()
    timings = CourseTimingRange.objects.all()

    if level_filter:
        studies = studies.filter(level_id=level_filter)
    if direction_filter:
        studies = studies.filter(studying_direction_id=direction_filter)
    if availability_filter:
        studies = studies.filter(timing_range_id=availability_filter)
    if cost_filter:
        studies = studies.filter(price_range_id=cost_filter)
    if study_type_filter:
        studies = studies.filter(type__in=study_type_filter)

    return render(request, 'it_friendly/courses.html',
                  context={'studies': studies,
                           'studying_directions': studying_directions,
                           'levels': levels,
                           'timings': timings,
                           'prices': prices,
                           'sign_in_form': sign_in_form,
                           'sign_up_form': sign_up_form,
                           'payment_form': payment_form,
                           'question_form': question_form,
                           'selected_level': int(level_filter) if level_filter else level_filter,
                           'selected_direction': int(direction_filter) if direction_filter else direction_filter,
                           'selected_availability': int(availability_filter) if availability_filter else availability_filter,
                           'selected_cost': int(cost_filter) if cost_filter else cost_filter,
                           'selected_study_types': study_type_filter
                           })




def get_study(request):
    study_id = request.GET.get('study_id')
    study_data = fetch_course_data(study_id)
    return JsonResponse(study_data)

def team(request):
    question_form = QuestionForm()
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    context = {'sign_in_form': sign_in_form,
               'sign_up_form': sign_up_form,
               'question_form':  question_form
               }
    return render(request, 'it_friendly/team.html', context=context)


def set_cookie(request):
    response = redirect('/it_friendly')
    value = smart_str(request.POST.get('name'), encoding='utf-8', strings_only=True)
    response.set_cookie('name', value)
    return response


def save_session(request):
    request.session['session'] = request.POST.get('name')
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
                try:
                    payment = StudyingStudent(id_course=request.POST.get('courseId'), username_student=request.user.username)
                    payment.save()
                    course_data = fetch_course_data(request.POST.get('courseId'))
                    letter_content = get_letter_template(course_data=course_data)
                    from_email = 'slavka112015@ukr.net'
                    recipient_list = [request.POST['email']]
                    send_mail(letter_content['subject'], letter_content['message'], from_email, recipient_list)
                    data['success'] = True
                except:
                    data['errors'] = ['Здається, ви вже зареєстровані. '
                                      'Перевірте особистий кабінет. '
                                      'Якщо ні - зверніться за допомогою у підтримку.']
                return JsonResponse(data)
            else:
                print('inner check else')
                data['errors'] = ['Номер карти має містити 16 цифр.'] if len(request.POST.get('card_number')) != 16 else  ['Карта не доступна.']
        else:
            print('invalid')
            data['errors'] = list(form.errors.values())
    return JsonResponse(data)


def fetch_course_data(study_id):
    study = Studying.objects.get(id=study_id)
    study_data = {
        'id': study.id,
        'type': study.type.title,
        'title': study.title,
        'price': study.price,
        'image': study.image,
        'level': study.level.level,
        'details': study.details,
        'participants': study.participants,
        'programs_settings': study.programs_settings,
        'beginning': study.beginning,
        'time': study.time
    }
    return study_data


def get_studying_student_data(student_username):
    data = StudyingStudent.objects.filter(username_student=student_username)
    result = [course.id_course.title for course in data]
    return {'data': result}


def get_user_studies(request):
    user_studies = get_studying_student_data(request.user.username)
    return JsonResponse(user_studies)


def ask_question(request):
    data = {'success': False}
    if request.method == 'POST':
        print('in form post')
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                letter_content = get_ask_question_letter_template(request.POST)
                from_email = 'slavka112015@ukr.net'
                recipient_list = ['yaroslavashyt@gmail.com']
                send_mail(letter_content['subject'], letter_content['message'], from_email, recipient_list)
                data['success'] = True
            except:
                data['errors'] = ['Не вдалося поставити питання. '
                                  'Схоже проблема на нашому боці! '
                                  'Ми працюємо над її усуненням. ']
                return JsonResponse(data)

        else:
            print('invalid')
            data['errors'] = list(form.errors.values())
    return JsonResponse(data)