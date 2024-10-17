from django.contrib import admin
from upskill_app import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_registered',)


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'price')


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'subject')


@admin.register(models.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('course', 'quiz_name')


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'final_grade')