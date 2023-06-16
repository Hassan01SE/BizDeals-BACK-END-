from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Business, Category, Purchase
from .serializers import CategorySerializer, BusinessSerializer, PurchaseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, BasePermission
from django.conf import settings
from rest_framework.exceptions import ValidationError

from django.views.decorators.csrf import csrf_exempt
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


class PostUserWritePermission(BasePermission):
    message = 'Updating listing is restricted to the owner of the listing'
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        return obj.username == request.user


class BusinessListView(generics.ListCreateAPIView):
    serializer_class = BusinessSerializer
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        user = self.request.user  # Assuming you want to use the authenticated user
        serializer.save(username=user)

    def get_queryset(self):

        username = self.request.query_params.get('username')
        if username:
             return Business.objects.filter(username__user_name__iexact=username, status = 'online').order_by('title')
        
        category = self.request.query_params.get('category')
        if category in ['ecommerce', 'restaurant', 'digital']:
            return Business.objects.filter(category__type=category, status='online' ).order_by('title')
        return Business.objects.filter(status='online').order_by('title')
    
   
    
class PurchaseListView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def create_checkout_session(self, price, product_name):
        price = price//287;
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': price*100,
                            'product_data': {
                                'name': product_name,
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://localhost:3000/checkout/success',
                cancel_url='http://localhost:3000/checkout/fail',
            )
            return checkout_session
        except Exception as e:
            print(e)
            return None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        

        price = serializer.validated_data['tokenpaid']
        product_name = serializer.validated_data['business']

        checkout_session = self.create_checkout_session(price, product_name)
        if checkout_session:
            serializer.save() 
            return Response({'checkout_url': checkout_session.url}, status=201)
        else:
            return Response({'error': 'Failed to create checkout session'}, status=500)

   

        




class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = 'pk'



@csrf_exempt
@api_view(['POST','GET'])
def create_purchase(request):
    serializer = PurchaseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        # Create a PaymentIntent with the provided amount
        stripe.api_key = 'sk_test_51NIuP9AtptvsQ5QyjUcDooyq7GfSRXNtMJziNRks4na0RhZwvoOlZILlbah0J3XvcBw84QRX9F0sS1dehuxvihuB00pPf2IiJL'

        amount = int(serializer.validated_data['token_paid'])  # Convert to cents
        currency = 'pkr'

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card']
        )

        # Save the purchase with the payment details
        purchase = serializer.save(payment_intent_id=payment_intent.id)

        return Response({'purchase_id': purchase.id})
    except stripe.error.StripeError as e:
        raise ValidationError(str(e))

    



""" @api_view(['GET', 'POST'])
def businessview(request):
    category = request.GET.get('category', None)
    if category in ['ecommerce', 'restaurant', 'digital']:
        businesses = Business.objects.filter(category__type=category).order_by('title')
    else:
        businesses = Business.objects.all().order_by('title')
    serializer = BusinessSerializer(businesses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def businessdetailview(request, pk):
    business = get_object_or_404(Business, pk=pk)
    serializer = BusinessSerializer(business)
    return Response(serializer.data) """