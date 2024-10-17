from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Почтовый адрес', unique=True, )
    password = models.CharField(max_length=50, verbose_name='Пароль')
    date_registered = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    profile_picture = models.ImageField(upload_to='profile_pictures', verbose_name='Фото профиля')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_registered', 'name']

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=50, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    price = models.IntegerField(verbose_name='Стоимость курса', validators=[MinValueValidator(0)])
    course_picture = models.ImageField(upload_to='course_picture', verbose_name='Превью курса', blank=True, null=True)
    users = models.ManyToManyField(
        User,
        verbose_name='Зачисленные пользователи',
        related_name='courses',
        through='Enrollment'
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['course_name']

    def get_discount(self):
        return self.price * 0.9

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    subject = models.CharField(max_length=50, verbose_name='Тема урока')
    content = models.TextField(verbose_name='Содержание урока')

    course = models.ForeignKey(
        Course,
        verbose_name='Курс',
        related_name='lessons',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('course', 'subject')

    def __str__(self):
        return self.subject


class Enrollment(models.Model):
    CHOICES = {
        True:
            'Завершен',
        False:
            'Не завершен'
    }
    date_of_enrollment = models.DateTimeField(auto_now_add=True, verbose_name='Дата зачисления')
    completion_status = models.BooleanField(default=False, verbose_name='Статус завершения',
                                            choices=CHOICES)
    user = models.ForeignKey(
        User,
        related_name='enrollments',
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        Course,
        related_name='enrollments',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Зачисление'
        verbose_name_plural = 'Зачисления'
        ordering = ('-date_of_enrollment', 'user', 'course')

    def __str__(self):
        return self.user.name + self.course.course_name


class Payment(models.Model):
    date_of_payment = models.DateField(verbose_name='Дата платежа')
    amount = models.IntegerField(verbose_name='Сумма платежа')
    payment_type = models.CharField(max_length=50, verbose_name='Тип платежа')
    user = models.ForeignKey(
        User,
        related_name='payments',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        ordering = ('-date_of_payment', 'user', 'amount')

    def __str__(self):
        return self.user.name + self.payment_type + str(self.amount)


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=50, verbose_name='Название теста')
    quiz_description = models.TextField(verbose_name='Описание теста', blank=True)
    max_points = models.IntegerField(verbose_name='Максимальное количество баллов')
    course = models.OneToOneField(
        Course,
        related_name='quizzes',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering=['quiz_name']

    def __str__(self):
        return self.quiz_name


class Result(models.Model):
    final_grade = models.IntegerField(verbose_name='Оценка за тест',
                                      validators=[MaxValueValidator(100), MinValueValidator(0)],
                                      default=0,
                                      )
    quiz = models.ForeignKey(
        Quiz,
        null=False,
        related_name='result',
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        null=False,
        related_name='results',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
        ordering = ['quiz', 'final_grade']

    def __str__(self):
        return self.quiz.quiz_name + str(self.final_grade)
