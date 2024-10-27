from django.urls import path
from rest_framework.routers import DefaultRouter


from upskill_app import views




router = DefaultRouter()

router.register('users', views.UserAPI, basename='users')
router.register('courses', views.CourseAPI, basename='courses')
router.register('lessons', views.LessonAPI, basename='lessons')
router.register('enrollments', views.EnrollmentAPI, basename='enrollments')
router.register('payments', views.PaymentAPI, basename='payments')
router.register('quizzes', views.QuizAPI, basename='quizzes')
router.register('results', views.ResultsAPI, basename='results')


urlpatterns = [
   path('courses_list/', views.CoursesList.as_view(), name='courses_list'),
   path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
   path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
   path('courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course_update'),
   path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
] + router.urls