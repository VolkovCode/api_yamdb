from django.contrib import admin

from .models import Title, Category, Genre, User


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'genre', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')    

class UserAdmin(admin.ModelAdmin):
    list_display = ("role",)
        

admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)