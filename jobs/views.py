# jobs/views.py
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import F
from .models import Job, Category
from .serializers import JobSerializer, CategorySerializer
from .filters import JobFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrAdmin, IsAdminUser



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

    # Allow everyone to read, only admins can create or modify
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]    # admin-only
        return [IsAuthenticatedOrReadOnly()]  # anyone can read


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.filter(is_active=True).select_related('category', 'posted_by')
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = JobFilter
    ordering_fields = ['posted_at', 'salary_min']
    ordering = ['-posted_at']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
        if q:
            sq = SearchQuery(q)
            qs = qs.annotate(rank=SearchRank(F('search_vector'), sq)).filter(rank__gte=0.01).order_by('-rank')
        return qs

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(posted_by=user)


