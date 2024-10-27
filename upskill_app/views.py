from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from rest_framework import viewsets

from upskill_app.models import Course, User, Lesson, Enrollment, Payment, Quiz, Result
from upskill_app import filters, serializers


class UserAPI(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = serializers.User

class CourseAPI(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = serializers.Course

class LessonAPI(viewsets.ModelViewSet):
   queryset = Lesson.objects.all()
   serializer_class = serializers.Lesson

class EnrollmentAPI(viewsets.ModelViewSet):
   queryset = Enrollment.objects.all()
   serializer_class = serializers.Enrollment

class PaymentAPI(viewsets.ModelViewSet):
   queryset = Payment.objects.all()
   serializer_class = serializers.Payment

class QuizAPI(viewsets.ModelViewSet):
   queryset = Quiz.objects.all()
   serializer_class = serializers.Quiz

class ResultsAPI(viewsets.ModelViewSet):
   queryset = Result.objects.all()
   serializer_class = serializers.Result


class CoursesList(FilterView):
   model = Course
   context_object_name = 'courses'
   template_name = 'upskill/courses_list.html'
   filterset_class = filters.Course

class CourseDetailView(DetailView):
   model = Course
   context_object_name = 'course'
   template_name = 'upskill/course_detail.html'

class CourseCreateView(CreateView):
   model = Course
   context_object_name = 'course'
   template_name = 'upskill/course_create.html'
   fields = ['course_name', 'description', 'price', 'course_picture']
   success_url = reverse_lazy('courses_list')

class CourseUpdateView(UpdateView):
   model = Course
   template_name = 'upskill/course_form.html'
   fields = ['course_name', 'description', 'price', 'course_picture']


   def get_success_url(self):
       return reverse_lazy('course_detail', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
   model = Course
   template_name = 'upskill/course_confirm_delete.html'
   success_url = reverse_lazy('courses_list')
