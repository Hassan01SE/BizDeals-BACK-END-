from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Business
from .serializers import CategorySerializer, BusinessSerializer

# Create your views here.

@api_view(['GET', 'POST'])
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
    return Response(serializer.data)