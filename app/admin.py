from django.contrib import admin

from app.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'tags', 'created_at', 'updated_at')
# Register your models here.
admin.site.register(Article, ArticleAdmin)
