"""
URL configuration for upskill project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from upskill import settings, views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('courses_list', views.CoursesList.as_view(), name='courses_list'),
   path('courses/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
   path('courses/create', views.CourseCreateView.as_view(), name='course_create'),
   path('courses/<int:pk>/update', views.CourseUpdateView.as_view(), name='course_update'),
   path('courses/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course_delete'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

