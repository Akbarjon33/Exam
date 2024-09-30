from django.contrib import admin
from .models import Post, Comment, Favorite, Category, PostImage

# Inline-изображения для публикаций
class PostImageInline(admin.TabularInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Category)
