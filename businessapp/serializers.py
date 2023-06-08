from rest_framework import serializers
from .models import Business,Category



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['type']

class BusinessSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:
        model = Business
        fields = ['id','title', 'category', 'location', 'price', 'revenue', 'expense', 'profit', 'description', 'seller', 'email', 'number','img1','img2']
    