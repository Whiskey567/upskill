from django.urls import path

from upskill_app import views

urlpatterns = [
   path('courses_list', views.CoursesList.as_view(), name='courses_list'),
   path('courses/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
   path('courses/create', views.CourseCreateView.as_view(), name='course_create'),
   path('courses/<int:pk>/update', views.CourseUpdateView.as_view(), name='course_update'),
   path('courses/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course_delete'),
]