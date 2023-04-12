from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.utils.encoding import smart_str


# Pure Python singleton
class Singleton:
    _instance = None
    name = ""
    age = 0

    def __new__(cls, name="", age=0):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.name = name
            cls.age = age
        return cls._instance


person1 = Singleton("Yaroslava", 19)
print(person1.name)
print(person1.age)
person2 = Singleton("Yasia", 20)
print(person2.name)
print(person2.age)
print(person1 is person2)


# django Singleton
class SingletonModel(models.Model):
    name = models.CharField(default='Mary', max_length=50)
    email = models.EmailField(default='itfriendly_corporative.gmail.com')

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

"""
singleton_instance1 = SingletonModel(name="Singleton 1", email='email_1.com')
singleton_instance1.save()
singleton_instance2 = SingletonModel(name="Singleton 2", email='email_2.com')
singleton_instance2.save()
if singleton_instance1.pk == singleton_instance2.pk:
    result = "The Singleton model provides a true singleton."
else:
    result = "The Singleton model does not provide a true singleton."
print(f'{singleton_instance1.name}\n{singleton_instance1.email}\n{result}')
"""

# OOP
class Animal:
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age

    def __str__(self):
        return f'<p><b>Name:</b> {self.name}</p><p><b>Gender:</b> {self.gender}</p><p><b>Age:</b> {self.age}</p>'

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        if not isinstance(new_gender, str):
            raise TypeError('Incorrect type of animal gender! Only string is required')
        elif not new_gender:
            raise ValueError('Animal gender is a required parameter!')
        elif new_gender not in ['m', 'f', 'male', 'female']:
            raise ValueError('Incorrect value of animal gender!')
        self._gender = new_gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Incorrect type of animal name! Only string is required')
        elif not new_name:
            raise ValueError('Animal name is a required parameter!')
        elif not new_name.isalpha():
            raise ValueError('Incorrect value of animal name!')
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Incorrect type of animal age! Only int is required')
        elif not new_age:
            raise ValueError('Animal age is a required parameter!')
        elif new_age not in range(0, 150):
            raise ValueError('Incorrect value of animal age!')
        self._age = new_age

    def make_sound(self):
        return self.name + ': ' + '......'


class Turtle(Animal):
    def __init__(self, gender, name, age):
        super().__init__(gender, name, age)


class Cat(Animal):
    def __init__(self, gender, name, age, sound):
        super().__init__(gender, name, age)
        self.sound = sound

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, new_sound):
        if not isinstance(new_sound, str):
            raise TypeError('Incorrect type of animal sound! Only string is required')
        elif not new_sound:
            raise ValueError('Animal name is a required parameter!')
        elif not new_sound.isalpha():
            raise ValueError('Incorrect value of animal sound!')
        self._sound = new_sound

    def make_sound(self):
        return f'{self.name}: {self.sound}'


class Dog(Cat):
    def init(self, gender, name, age, sound):
        super().__init__(gender, name, age, sound)


data = [Cat('f', 'Monica', 4, 'meoooooow'), Dog('m', 'Bim', 6, 'woof'), Turtle('f', 'Tatia', 10)]
hash_list = {'fruit': 'apple', 'vegetable': 'cucumber', 'liquid': 'agua'}
cat, dog, turtle = data


def demonstrate_for_cycle():
    res = ''
    for i in cat.name:
        res += i + i.upper()
    return res


print(f"{cat}\n"
      f"{cat.make_sound()}\n"
      f"{dog}\n"
      f"{dog.make_sound()}\n"
      f"{turtle}\n"
      f"{turtle.make_sound()}\n"
      f"{turtle.name.split('a')}\n"
      f"{''.join(turtle.name.split('a'))}\n"
      f"{demonstrate_for_cycle()}\n"
      f"{hash_list['liquid']}, {hash_list}\n"
      f"{hash_list['fruit'] < hash_list['vegetable']}\n"
      f"{int(21.0)}, {float(21)}, {bool(21)}, {str(21)}\n")


def set_cookie(request):
    response = redirect('/it_friendly')
    value = smart_str(request.POST.get('name'), encoding='utf-8', strings_only=True)
    print(value, type(value))
    response.set_cookie('name', value)
    return response


def save_session(request):
    request.session['name'] = request.POST.get('name')
    return redirect('/it_friendly')


def index(request):
    # return render(request, 'it_friendly/index.html', {'name': (request.session.get('name', 'Вхід'))})
   return render(request, 'it_friendly/index.html', {'name': (request.COOKIES.get('name', 'Вхід'))})


def courses(request):
    return render(request, 'it_friendly/courses.html')


def team(request):
    return render(request, 'it_friendly/team.html')
