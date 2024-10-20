import django_filters
import upskill_app.models
from django.db.models import Q

class Course(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Стоимость курса от и до')
    # course_name = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    # description = django_filters.CharFilter(lookup_expr='icontains', label='Описание')
    finished = django_filters.BooleanFilter(method='filter_finished', label = 'Завершен')
    term = django_filters.CharFilter(method='filter_term', label='')
    grade = django_filters.Filter(method='filter_grade', label='Набрано баллов больше:')

    class Meta:
        model = upskill_app.models.Course
        fields = ['term', 'price_range', 'finished']

    def filter_finished(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(enrollments__user__name='Руслан').filter(enrollments__completion_status=True)
        if not value:
            return queryset.filter(enrollments__user__name='Руслан').filter(enrollments__completion_status=False)

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(course_name__icontains=term) | Q(description__icontains=term)
        return queryset.filter(criteria).distinct()

    def filter_grade(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(enrollments__user__name='Руслан').filter(quizzes__result__final_grade__gte=value)
