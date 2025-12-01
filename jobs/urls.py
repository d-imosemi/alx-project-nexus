# jobs/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('', include(router.urls)),
]
