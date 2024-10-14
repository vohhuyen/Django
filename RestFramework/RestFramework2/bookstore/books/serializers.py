from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# class BookSerializer(serializers.ModelSerializer):
#     category = CategorySerializer() 
#     is_expensive = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'published_date', 'price', 'is_expensive','category']

#     def validate_title(self, value):
#         if 'badword' in value.lower():
#             raise serializers.ValidationError("Title contains inappropriate word.")
#         return value
#     def get_is_expensive(self, obj):
#         return obj.price > 500
    
#     def create(self, validated_data):
#         category_data = validated_data.pop('category')
#         category, created = Category.objects.get_or_create(**category_data)
#         book = Book.objects.create(category=category, **validated_data)
#         return book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Book
        fields = ['url', 'title', 'author', 'published_date', 'price', 'category']

