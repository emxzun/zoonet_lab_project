from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.account.views import RegisterApiView, ChangePasswordApiView, \
    ActivationApiView, ForgotPasswordApiView, ForgotCompleteAPIView, ProfileAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('profile', ProfileAPIView)
router.register('register', RegisterApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_complete/', ForgotCompleteAPIView.as_view()),
]
