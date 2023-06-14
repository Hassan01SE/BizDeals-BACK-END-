from rest_framework import serializers
from .models import Business,Category, Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ['id', 'business', 'seller', 'businessprice', 'firstname', 'lastname', 'username', 'email', 'introduction', 'number', 'tokenpaid']



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
        fields = ['id','username','title', 'category', 'location', 'price', 'revenue', 'expense', 'profit','status', 'description', 'seller', 'email', 'number','img1','img2']
    

    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(**category_data)
        validated_data['category'] = category
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.location = validated_data.get('location', instance.location)
        instance.price = validated_data.get('price', instance.price)
        instance.revenue = validated_data.get('revenue', instance.revenue)
        instance.expense = validated_data.get('expense', instance.expense)
        instance.profit = validated_data.get('profit', instance.profit)
        instance.description = validated_data.get('description', instance.description)
        instance.seller = validated_data.get('seller', instance.seller)
        instance.email = validated_data.get('email', instance.email)
        instance.number = validated_data.get('number', instance.number)
        instance.img1 = validated_data.get('img1', instance.img1)
        instance.img2 = validated_data.get('img2', instance.img2)

        category_data = validated_data.get('category')
        if category_data:
            category = Category.objects.get(**category_data)
            instance.category = category

        instance.save()
        return instance
    
    