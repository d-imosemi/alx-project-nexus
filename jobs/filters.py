# jobs/filters.py
import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    min_salary = django_filters.NumberFilter(field_name='salary_min', lookup_expr='gte')
    max_salary = django_filters.NumberFilter(field_name='salary_max', lookup_expr='lte')
    job_type = django_filters.CharFilter(field_name='job_type')
    category = django_filters.NumberFilter(field_name='category_id')
    is_remote = django_filters.BooleanFilter(field_name='is_remote')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['job_type', 'category', 'is_remote', 'city']
