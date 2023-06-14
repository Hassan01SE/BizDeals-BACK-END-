from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Business, Category
from .serializers import CategorySerializer, BusinessSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, BasePermission

# Create your views here.


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
             return Business.objects.filter(username__user_name__iexact=username).order_by('title')
        
        category = self.request.query_params.get('category')
        if category in ['ecommerce', 'restaurant', 'digital']:
            return Business.objects.filter(category__type=category).order_by('title')
        return Business.objects.filter(status='online').order_by('title')
    
   
    



class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = 'pk'

    



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