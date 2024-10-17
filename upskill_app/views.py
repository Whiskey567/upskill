from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from upskill_app.models import Course




class CoursesList(ListView):
   model = Course
   context_object_name = 'courses'
   template_name = 'upskill/courses_list.html'

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
   success_url = reverse_lazy('course_list')
