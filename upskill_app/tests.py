from pydoc import resolve

from django.urls import reverse
from django.test import TestCase

from upskill_app import models, factories

class UpskillTestCase(TestCase):

    def setUp(self):
        self.course = factories.CourseFactory()
        self.user = factories.UserFactory()


    def test_get_courses_list(self):
        url = reverse('courses_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), models.Course.objects.count())

    def test_get_course_detail(self):
        url = reverse('course_detail', kwargs={'pk': self.course.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['course'], self.course)

    def test_course_update(self):
        url = reverse('course_update', kwargs={'pk': self.course.pk})
        old_course_name = self.course.course_name
        response = self.client.post(url, {'course_name':'new_course_name'})
        self.course.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.course.course_name, old_course_name)

    def test_course_delete(self):
        url = reverse('course_delete', kwargs={'pk': self.course.pk})
        old_courses_count = models.Course.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_courses_count, models.Course.objects.count())

    def test_course_create(self):
        url = reverse('course_create')
        old_courses_count = models.Course.objects.count()
        new_course_data = {
            'course_name': 'Тестовый курс',
            'description': 'Описание тестового курса',
            'price': 1000
        }
        response = self.client.post(url, new_course_data)
        course = models.Course.objects.get(course_name='Тестовый курс')
        self.assertEqual(response.status_code, 302)
        self.assertGreater(models.Course.objects.count(), old_courses_count)
        self.assertEqual(course.description, 'Описание тестового курса')
        self.assertEqual(course.price, 1000)



