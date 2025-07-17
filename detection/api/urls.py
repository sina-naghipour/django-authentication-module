from rest_framework_simplejwt.views import(
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView,
)
from api.views import CustomTokenObtainPairView, Register, DetectItemView
from django.urls import path


app_name = 'api'

urlpatterns = [

    path('token/', CustomTokenObtainPairView.as_view(), name='obtain'),
    path('token/verify/', TokenVerifyView.as_view(), name='obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='obtain'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='obtain'),
    path('register/', Register.as_view(), name='register'),
    path('detect-items/', DetectItemView.as_view(), name='detect-item'),
]
