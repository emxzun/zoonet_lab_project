from django.urls import path
from applications.stripe.views import ProductPageAPIView, PaymentSuccessfulAPIView, PaymentCancelledAPIView, StripeWebhookAPIView

urlpatterns = [
	path('product_page/', ProductPageAPIView.as_view(), name='product_page'),
	path('payment_successful/', PaymentSuccessfulAPIView.as_view(), name='payment_successful'),
	path('payment_cancelled/', PaymentCancelledAPIView.as_view(), name='payment_cancelled'),
	path('stripe_webhook/', StripeWebhookAPIView.as_view(), name='stripe_webhook'),
]

