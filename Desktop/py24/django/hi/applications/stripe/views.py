from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.stripe.models import UserPayment
import stripe
import time


stripe.api_key = settings.STRIPE_SECRET_KEY_TEST


class ProductPageAPIView(APIView):

    @staticmethod
    def get(request):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': settings.PRODUCT_PRICE,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url=settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        return redirect(checkout_session.url, code=303)


## use Stripe dummy card: 4242 4242 4242 4242

class PaymentSuccessfulAPIView(APIView):
    @staticmethod
    def get(request):
        checkout_session_id = request.GET.get('session_id', None)
        session = stripe.checkout.Session.retrieve(checkout_session_id)
        customer = stripe.Customer.retrieve(session.customer)
        user_id = request.user.user_id
        user_payment = UserPayment.objects.get(app_user=user_id)
        user_payment.stripe_checkout_id = checkout_session_id
        user_payment.save()
        return render(request, 'user_payment/payment_successful.html', {'customer': customer})

class PaymentCancelledAPIView(APIView):
	@staticmethod
	def payment_cancelled(request):
		stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
		return render(request, 'user_payment/payment_cancelled.html')


class StripeWebhookAPIView(APIView):
    @csrf_exempt
    @staticmethod
    def post(request):
        stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
        time.sleep(10)
        payload = request.body
        signature_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None
        try:
            event = stripe.Webhook.construct_event(
                payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
            )
        except ValueError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            session_id = session.get('id', None)
            time.sleep(15)
            user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
            user_payment.payment_bool = True
            user_payment.save()
        return Response(status=status.HTTP_200_OK)