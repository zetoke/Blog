from django.contrib import admin
from blog.models import Posts, Category

class PostsAdmin(admin.ModelAdmin):
    #exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)