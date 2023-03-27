from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Tinder',
        default_version='v1',
        description='Swagger documentation'
    ),
    public=True,
)

urlpatterns = [
    path('', include('applications.core.urls')),
    path('rooms/', include('applications.chat.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/recommendations/', include('applications.recommendations.urls')),
    path('api/v1/likedislike/', include('applications.likedislike.urls')),
    path('stripe/', include('applications.stripe.urls')),
    path('stripe_auth/', include('applications.app_users.urls')),

]

