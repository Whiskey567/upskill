import factory
from factory.django import ImageField

from upskill_app import models

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    date_registered = factory.Faker('date_time')
    profile_picture = ImageField()

    class Meta:
        model = models.User

class CourseFactory(factory.django.DjangoModelFactory):
    course_name = factory.Faker('sentence')
    description = factory.Faker('text')
    price = factory.Faker('random_int', min=0, max=10000)
    course_picture = ImageField()


    class Meta:
        model = models.Course