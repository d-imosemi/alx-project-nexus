from django.urls import path
from .views import LogoutView, RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", TokenObtainPairView.as_view(), name="jwt-login"),
    path("refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("logout/", LogoutView.as_view(), name="jwt-logout"),
    path("profile/", UserDetailView.as_view(), name="jwt-profile"),
]
