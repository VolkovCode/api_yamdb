from rest_framework import serializers

from .models import Category, Genre, Title, User


class CategorySerializer(serializers.ModelSerializer):
    #name = serializers.CharField(source='')

    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_field = 'slug'

class GenreSerializer(serializers.ModelSerializer):
    #author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("bio", "role", "username", "email")  
        model = User      
         

class CategoryReprField(serializers.SlugRelatedField):

    def to_representation(self, value):
        return {'name': value.name, 'slug': value.slug}


class GenreReprField(serializers.SlugRelatedField):
   
    def to_representation(self, value):
        return {'name': value.name, 'slug': value.slug}

class TitleSerializer(serializers.ModelSerializer):
    category = CategoryReprField(slug_field='slug', queryset=Category.objects.all())
    genre = GenreReprField(slug_field='slug', queryset=Genre.objects.all(), many=True)

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre', 'category',)
        model = Title           