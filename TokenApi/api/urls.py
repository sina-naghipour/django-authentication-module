from django.urls import path
from rest_framework_simplejwt.views import(
    TokenBlacklistView,
    TokenRefreshView,
    TokenVerifyView,
)
from api.views import CustomTokenObtainPairView

app_name = 'api'

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='obtain'), # get token.
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'), # refresh token.
    path('token/verify/', TokenVerifyView.as_view(), name='verify'), # verify token.
    path('token/blacklist/', TokenBlacklistView.as_view(), name='blacklist'), # blacklist.
]
