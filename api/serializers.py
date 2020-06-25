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


class TitleSerializer(serializers.ModelSerializer):
    #user = serializers.ReadOnlyField(source='user.username')
    #following = serializers.CharField(source='following.username')

    class Meta:
        fields = ("id", "name", "year", "genre", "category", "rating", "description")
        model = Title
        


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("bio", "role", "username", "email")  
        model = User      
         
        