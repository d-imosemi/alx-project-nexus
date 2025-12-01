from django.urls import path
from .views import (
    ApplyJobView,
    UserApplicationsView,
    AdminApplicationsView,
    ApplicationDetailView,
)

urlpatterns = [
    path("apply/", ApplyJobView.as_view(), name="apply-job"),
    path("my-applications/", UserApplicationsView.as_view(), name="my-applications"),
    path("admin/applications/", AdminApplicationsView.as_view(), name="admin-applications"),
    path("application/<int:pk>/", ApplicationDetailView.as_view(), name="application-detail"),
]
