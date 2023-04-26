from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from applications.account.views import RegisterApiView, ChangePasswordApiView, \
    ForgotPasswordApiView, ForgotCompleteAPIView, ProfileAPIView, ActivationApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('profile', ProfileAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_complete/', ForgotCompleteAPIView.as_view()),
    path('activate/', ActivationApiView.as_view()),
    path('verify/', views.verify_sms, name='verify_sms'),
    # path('registerr/', views.register, name='register'),
]
