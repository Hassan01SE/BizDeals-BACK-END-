from rest_framework import serializers
from .models import Business,Category



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['type']

class BusinessSerializer(serializers.ModelSerializer):

    #category = serializers.StringRelatedField()
    category = CategorySerializer()
    username = serializers.StringRelatedField()

    class Meta:
        model = Business
        fields = ['id','username','title', 'category', 'location', 'price', 'revenue', 'expense', 'profit', 'description', 'seller', 'email', 'number','img1','img2']
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(**category_data)
        validated_data['category'] = category
        return super().create(validated_data)